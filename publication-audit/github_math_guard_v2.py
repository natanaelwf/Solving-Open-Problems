#!/usr/bin/env python3
"""
github_math_guard_v2.py

Static and server-parser validation for mathematical Markdown intended for GitHub.

Usage:
  python github_math_guard_v2.py lint README.md --strict \
      --inventory-out math-inventory.json

  python github_math_guard_v2.py lint README.md article/README.md --strict

  python github_math_guard_v2.py verify-html README.md server-page.html --strict

This tool deliberately uses a conservative policy. Unknown macros are errors unless
explicitly added with --allow-macro.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, asdict
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


SAFE_MACROS = {
    # Structure and environments
    "begin", "end",
    # Fonts and text
    "mathbb", "mathrm", "mathbf", "mathcal", "mathsf", "mathtt", "text",
    # Fractions, roots, combinatorics
    "frac", "dfrac", "tfrac", "sqrt", "binom",
    # Delimiters and sizing
    "left", "right", "lbrace", "rbrace", "lvert", "rvert", "vert", "mid",
    "langle", "rangle", "big", "Big", "bigg", "Bigg",
    "bigl", "bigr", "Bigl", "Bigr", "biggl", "biggr", "Biggl", "Biggr",
    # Relations and set notation
    "lt", "gt", "le", "leq", "ge", "geq", "ne", "neq", "equiv", "sim",
    "simeq", "cong", "approx", "in", "notin", "ni", "subset", "subseteq",
    "supset", "supseteq", "setminus", "cup", "cap", "emptyset", "nexists",
    "exists", "forall",
    # Arithmetic and algebra
    "cdot", "times", "pm", "mp", "div", "circ", "ast", "star", "oplus",
    "otimes", "wedge", "vee", "propto", "mid",
    # Sums, products, limits
    "sum", "prod", "coprod", "lim", "limsup", "liminf", "max", "min",
    "sup", "inf",
    # Standard operators that GitHub/MathJax normally provides directly
    "log", "ln", "exp", "sin", "cos", "tan", "cot", "sec", "csc",
    "det", "gcd", "ker", "dim", "deg", "hom", "arg",
    # Accents and decorations
    "overline", "underline", "widehat", "widetilde", "hat", "tilde", "bar",
    "vec", "dot", "ddot", "prime",
    # Arrows
    "to", "mapsto", "longrightarrow", "longleftarrow", "rightarrow",
    "leftarrow", "Rightarrow", "Leftarrow", "Leftrightarrow", "uparrow",
    "downarrow",
    # Spacing, ellipses and infinity
    "quad", "qquad", "enspace", "thinspace", "ldots", "cdots", "vdots",
    "ddots", "infty",
    # Layout helpers
    "substack", "overset", "underset",
    # Greek lower case
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta",
    "eta", "theta", "vartheta", "iota", "kappa", "lambda", "mu", "nu",
    "xi", "omicron", "pi", "varpi", "rho", "varrho", "sigma", "varsigma",
    "tau", "upsilon", "phi", "varphi", "chi", "psi", "omega",
    # Greek upper case
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon",
    "Phi", "Psi", "Omega",
}

SAFE_ENVIRONMENTS = {
    "aligned", "alignedat", "gathered", "cases",
    "matrix", "pmatrix", "bmatrix", "Bmatrix", "vmatrix", "Vmatrix",
    "smallmatrix",
}

FORBIDDEN_MACROS = {
    "operatorname": "GitHub rejected this macro in the incident; rewrite with \\mathrm{...}.",
    "operatorname*": "GitHub rejected this macro in the incident; rewrite with \\mathrm{...}.",
    "tag": "Keep equation labels in Markdown, outside mathematics.",
    "boxed": "Use semantic Markdown emphasis instead of ornamental boxes.",
    "newcommand": "Custom macro definitions are not permitted in production Markdown.",
    "renewcommand": "Custom macro definitions are not permitted in production Markdown.",
    "DeclareMathOperator": "Custom operator declarations are not permitted.",
    "def": "TeX macro definitions are not permitted.",
    "require": "Runtime extension loading is not permitted.",
}

BRACED_ARGUMENT_MACROS = {
    "mathbb", "mathrm", "mathbf", "mathcal", "mathsf", "mathtt", "text",
}

VISUALLY_CONFUSABLE_WARNINGS = {
    "nu": "Greek \\nu can be confused with the Latin variable u; verify it is intentional.",
    "upsilon": "Greek \\upsilon can be confused with Latin letters; verify it is intentional.",
}


@dataclass
class Finding:
    severity: str
    path: str
    line: int
    code: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.severity} {self.code}: {self.message}"


@dataclass
class MathExpression:
    path: str
    kind: str
    index: int
    line: int
    tex: str
    in_table: bool = False
    context: str = ""

    def to_json(self) -> dict:
        return asdict(self)


@dataclass
class ScanResult:
    path: str
    expressions: list[MathExpression]
    findings: list[Finding]
    display_count: int
    inline_count: int


def is_escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return count % 2 == 1


def mask_code_spans(line: str) -> str:
    """Replace code-span contents with spaces while preserving string length."""
    chars = list(line)
    i = 0
    while i < len(line):
        if line[i] != "`":
            i += 1
            continue
        run = 1
        while i + run < len(line) and line[i + run] == "`":
            run += 1
        closing = line.find("`" * run, i + run)
        if closing == -1:
            i += run
            continue
        for j in range(i, closing + run):
            chars[j] = " "
        i = closing + run
    return "".join(chars)


def unescaped_positions(text: str, char: str) -> list[int]:
    return [i for i, value in enumerate(text) if value == char and not is_escaped(text, i)]


def likely_table_row(line: str) -> bool:
    masked = mask_code_spans(line)
    pipes = unescaped_positions(masked, "|")
    stripped = masked.strip()
    return len(pipes) >= 2 or (stripped.startswith("|") and stripped.endswith("|"))


def is_table_separator(line: str) -> bool:
    masked = mask_code_spans(line).strip()
    if not masked:
        return False
    cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", masked.strip("|"))]
    return len(cells) >= 2 and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def table_column_count(line: str) -> int:
    masked = mask_code_spans(line).strip()
    if masked.startswith("|"):
        masked = masked[1:]
    if masked.endswith("|") and not is_escaped(masked, len(masked) - 1):
        masked = masked[:-1]
    return len(re.split(r"(?<!\\)\|", masked))


def detect_table_structure(lines: Sequence[str], path: str) -> list[Finding]:
    findings: list[Finding] = []
    for i, line in enumerate(lines):
        if not is_table_separator(line):
            continue
        expected = table_column_count(line)
        for neighbor in (i - 1, i + 1):
            if 0 <= neighbor < len(lines) and likely_table_row(lines[neighbor]):
                actual = table_column_count(lines[neighbor])
                if actual != expected:
                    findings.append(Finding(
                        "ERROR", path, neighbor + 1, "TABLE_COLUMNS",
                        f"Markdown table row has {actual} parsed columns; separator declares {expected}. "
                        "A literal vertical bar inside a cell often causes this."
                    ))
        j = i + 1
        while j < len(lines) and likely_table_row(lines[j]) and lines[j].strip():
            actual = table_column_count(lines[j])
            if actual != expected:
                findings.append(Finding(
                    "ERROR", path, j + 1, "TABLE_COLUMNS",
                    f"Markdown table row has {actual} parsed columns; separator declares {expected}."
                ))
            j += 1
    return findings


def extract_inline_expressions(
    line: str,
    line_number: int,
    path: str,
    inline_index_start: int,
) -> tuple[list[MathExpression], list[Finding]]:
    expressions: list[MathExpression] = []
    findings: list[Finding] = []
    masked = mask_code_spans(line)
    dollars = unescaped_positions(masked, "$")
    if len(dollars) % 2:
        findings.append(Finding(
            "ERROR", path, line_number, "INLINE_DOLLAR",
            "Unpaired inline-math dollar delimiter."
        ))
        return expressions, findings

    in_table = likely_table_row(line)
    for pair_index, (start, end) in enumerate(zip(dollars[0::2], dollars[1::2])):
        tex = line[start + 1:end]
        expression = MathExpression(
            path=path,
            kind="inline",
            index=inline_index_start + pair_index,
            line=line_number,
            tex=tex,
            in_table=in_table,
            context=line,
        )
        expressions.append(expression)

        before = line[start - 1] if start > 0 else ""
        after = line[end + 1] if end + 1 < len(line) else ""
        if before == "-" or after == "-":
            findings.append(Finding(
                "ERROR", path, line_number, "INLINE_HYPHEN",
                "Inline mathematics is directly adjacent to a hyphen. Rewrite prose, for example "
                "'a map of degree $q$' instead of 'degree-$q$'."
            ))

        prefix = line[:start]
        suffix = line[end + 1:]
        open_bracket = prefix.rfind("[")
        close_bracket = prefix.rfind("]")
        if open_bracket > close_bracket and re.match(r"[^\]]*\]\(", suffix):
            findings.append(Finding(
                "ERROR", path, line_number, "INLINE_LINK_LABEL",
                "Inline mathematics occurs inside a Markdown link label. Separate the math from the link."
            ))

        # Conservative emphasis heuristic. It intentionally over-reports rather than silently miss.
        for marker in ("*", "_"):
            if prefix.count(marker) % 2 == 1 and suffix.count(marker) % 2 == 1:
                findings.append(Finding(
                    "ERROR", path, line_number, "INLINE_EMPHASIS",
                    "Inline mathematics appears nested inside Markdown emphasis. "
                    "Do not put $...$ inside italic or bold spans."
                ))
                break

        if in_table and "|" in tex:
            findings.append(Finding(
                "ERROR", path, line_number, "TABLE_PIPE_MATH",
                "Literal '|' inside mathematics in a Markdown table cell will be parsed as a column "
                "separator. Use \\lvert...\\rvert or plain prose."
            ))

    return expressions, findings


def balanced_braces(tex: str) -> tuple[bool, int]:
    depth = 0
    for i, char in enumerate(tex):
        if char not in "{}" or is_escaped(tex, i):
            continue
        depth += 1 if char == "{" else -1
        if depth < 0:
            return False, depth
    return depth == 0, depth


def environment_findings(expr: MathExpression) -> list[Finding]:
    findings: list[Finding] = []
    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", expr.tex):
        action, env = match.groups()
        if action == "begin":
            if env not in SAFE_ENVIRONMENTS:
                findings.append(Finding(
                    "ERROR", expr.path, expr.line, "ENV_NOT_ALLOWED",
                    f"Environment '{env}' is outside the production allowlist."
                ))
            stack.append(env)
        else:
            if not stack or stack.pop() != env:
                findings.append(Finding(
                    "ERROR", expr.path, expr.line, "ENV_MISMATCH",
                    f"Mismatched \\end{{{env}}}."
                ))
    if stack:
        findings.append(Finding(
            "ERROR", expr.path, expr.line, "ENV_UNCLOSED",
            f"Unclosed environment(s): {', '.join(stack)}."
        ))
    return findings


def expression_findings(
    expr: MathExpression,
    allowed_macros: set[str],
    strict: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    tex = expr.tex

    if not tex.strip():
        findings.append(Finding("ERROR", expr.path, expr.line, "EMPTY_MATH", "Empty math expression."))

    if "<" in tex or ">" in tex:
        findings.append(Finding(
            "ERROR", expr.path, expr.line, "LITERAL_ANGLE",
            "Literal '<' or '>' found inside mathematics; use \\lt or \\gt."
        ))

    if expr.in_table and "|" in tex:
        findings.append(Finding(
            "ERROR", expr.path, expr.line, "TABLE_PIPE_MATH",
            "Literal vertical bar found inside mathematics in a Markdown table."
        ))

    ok, depth = balanced_braces(tex)
    if not ok:
        findings.append(Finding(
            "ERROR", expr.path, expr.line, "BRACE_BALANCE",
            f"Unbalanced grouping braces; final depth {depth}."
        ))

    findings.extend(environment_findings(expr))

    for macro, reason in FORBIDDEN_MACROS.items():
        pattern = rf"\\{re.escape(macro)}(?![A-Za-z])"
        if re.search(pattern, tex):
            findings.append(Finding(
                "ERROR", expr.path, expr.line, "FORBIDDEN_MACRO",
                f"\\{macro} is forbidden. {reason}"
            ))

    if re.search(r"\\begin\{array\}", tex):
        findings.append(Finding(
            "ERROR", expr.path, expr.line, "ARRAY_ENV",
            "The array environment is prohibited for production proofs; use aligned or a real Markdown table."
        ))

    commands = re.findall(r"\\([A-Za-z]+)", tex)
    for command in sorted(set(commands)):
        if command not in allowed_macros and command not in FORBIDDEN_MACROS:
            findings.append(Finding(
                "ERROR", expr.path, expr.line, "UNKNOWN_MACRO",
                f"Macro \\{command} is outside the conservative allowlist. "
                "Rewrite it or validate it in an isolated GitHub commit and explicitly allow it."
            ))
        if command in VISUALLY_CONFUSABLE_WARNINGS:
            findings.append(Finding(
                "WARNING", expr.path, expr.line, "CONFUSABLE_SYMBOL",
                VISUALLY_CONFUSABLE_WARNINGS[command]
            ))

    for macro in BRACED_ARGUMENT_MACROS:
        for match in re.finditer(rf"\\{macro}(?![A-Za-z])", tex):
            remainder = tex[match.end():]
            if not re.match(r"\s*\{", remainder):
                findings.append(Finding(
                    "ERROR", expr.path, expr.line, "UNBRACED_MACRO",
                    f"Use an explicit braced argument: \\{macro}{{...}}, not shorthand such as \\{macro}1."
                ))

    if expr.kind == "display":
        stripped = re.sub(r"\\[A-Za-z]+", "", tex)
        stripped = re.sub(r"[\s{}()[\].,;:+\-_=^]+", "", stripped)
        if len(stripped) <= 1:
            findings.append(Finding(
                "WARNING", expr.path, expr.line, "SUSPICIOUS_SHORT_BLOCK",
                "Display mathematics contains only one short token; verify that it was not truncated."
            ))

    if re.search(r"\\nu\s*,\s*[A-Za-z]", tex) or re.search(r"\\nu\s*\^", tex):
        findings.append(Finding(
            "WARNING", expr.path, expr.line, "NU_VS_U",
            "The sequence uses Greek \\nu in a context that often indicates a mistyped Latin u."
        ))

    return findings


def scan_markdown(
    path: Path,
    strict: bool = False,
    extra_allowed_macros: Iterable[str] = (),
) -> ScanResult:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[Finding] = []
    expressions: list[MathExpression] = []
    allowed_macros = set(SAFE_MACROS) | set(extra_allowed_macros)

    findings.extend(detect_table_structure(lines, str(path)))

    in_fence = False
    fence_kind = ""
    math_buffer: list[str] = []
    math_start_line = 0
    display_index = 0
    inline_index = 0

    if "$$" in text:
        for line_no, line in enumerate(lines, 1):
            if "$$" in line:
                findings.append(Finding(
                    "ERROR", str(path), line_no, "DOLLAR_BLOCK",
                    "The '$$' delimiter is prohibited; use a fenced math block."
                ))

    for line_no, line in enumerate(lines, 1):
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            info = stripped[3:].strip().lower()
            if not in_fence:
                in_fence = True
                fence_kind = "math" if info == "math" else "other"
                if fence_kind == "math":
                    math_buffer = []
                    math_start_line = line_no
                continue
            else:
                # Close only a bare fence. Nested language markers are treated as content.
                if stripped in ("```", "~~~"):
                    if fence_kind == "math":
                        display_index += 1
                        expr = MathExpression(
                            path=str(path),
                            kind="display",
                            index=display_index,
                            line=math_start_line,
                            tex="\n".join(math_buffer),
                            in_table=False,
                            context="",
                        )
                        expressions.append(expr)
                    in_fence = False
                    fence_kind = ""
                    math_buffer = []
                    continue

        if in_fence:
            if fence_kind == "math":
                math_buffer.append(line)
            continue

        inline, inline_findings = extract_inline_expressions(
            line, line_no, str(path), inline_index + 1
        )
        expressions.extend(inline)
        inline_index += len(inline)
        findings.extend(inline_findings)

    if in_fence:
        findings.append(Finding(
            "ERROR", str(path), len(lines), "UNCLOSED_FENCE",
            f"Unclosed {fence_kind or 'code'} fence at end of file."
        ))

    for expr in expressions:
        findings.extend(expression_findings(expr, allowed_macros, strict))

    # De-duplicate identical findings caused by both context and expression checks.
    unique: dict[tuple, Finding] = {}
    for finding in findings:
        key = (finding.severity, finding.path, finding.line, finding.code)
        unique.setdefault(key, finding)
    findings = list(unique.values())
    findings.sort(key=lambda item: (item.path, item.line, item.severity, item.code))

    return ScanResult(
        path=str(path),
        expressions=expressions,
        findings=findings,
        display_count=display_index,
        inline_count=inline_index,
    )


class MathRendererHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.renderers: list[dict] = []
        self._current: dict | None = None
        self._depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "math-renderer":
            attr_dict = dict(attrs)
            classes = (attr_dict.get("class") or "").split()
            self._current = {"classes": classes, "text": ""}
            self._depth = 1
        elif self._current is not None:
            self._depth += 1

    def handle_endtag(self, tag: str) -> None:
        if self._current is None:
            return
        self._depth -= 1
        if tag == "math-renderer" and self._depth == 0:
            self.renderers.append(self._current)
            self._current = None

    def handle_data(self, data: str) -> None:
        if self._current is not None:
            self._current["text"] += data

    def handle_entityref(self, name: str) -> None:
        if self._current is not None:
            self._current["text"] += f"&{name};"

    def handle_charref(self, name: str) -> None:
        if self._current is not None:
            self._current["text"] += f"&#{name};"


def normalize_tex(value: str, display: bool = False) -> str:
    value = unescape(value.strip())
    if display and value.startswith("$$") and value.endswith("$$"):
        value = value[2:-2]
    elif not display and value.startswith("$") and value.endswith("$"):
        value = value[1:-1]
    value = re.sub(r"\s+", " ", value).strip()
    if display:
        # GitHub may insert one extra slash before a Markdown-origin line break.
        value = re.sub(r"\\\\\\(?=\s|&)", r"\\\\", value)
    return value


def verify_server_html(
    markdown_path: Path,
    html_path: Path,
    strict: bool,
    extra_allowed_macros: Iterable[str] = (),
) -> tuple[list[Finding], dict]:
    result = scan_markdown(markdown_path, strict=strict, extra_allowed_macros=extra_allowed_macros)
    findings = list(result.findings)
    html_text = html_path.read_text(encoding="utf-8")
    parser = MathRendererHTMLParser()
    parser.feed(html_text)

    display_source = [x for x in result.expressions if x.kind == "display"]
    inline_source = [x for x in result.expressions if x.kind == "inline"]
    display_html = [x for x in parser.renderers if "js-display-math" in x["classes"]]
    inline_html = [x for x in parser.renderers if "js-inline-math" in x["classes"]]

    if len(display_source) != len(display_html):
        findings.append(Finding(
            "ERROR", str(markdown_path), 1, "SERVER_DISPLAY_COUNT",
            f"Source has {len(display_source)} display expressions, but GitHub HTML has {len(display_html)}."
        ))
    if len(inline_source) != len(inline_html):
        findings.append(Finding(
            "ERROR", str(markdown_path), 1, "SERVER_INLINE_COUNT",
            f"Source has {len(inline_source)} inline expressions, but GitHub HTML has {len(inline_html)}."
        ))

    for source, rendered in zip(display_source, display_html):
        expected = normalize_tex(source.tex, display=True)
        actual = normalize_tex(rendered["text"], display=True)
        if expected != actual:
            findings.append(Finding(
                "ERROR", str(markdown_path), source.line, "SERVER_DISPLAY_MISMATCH",
                f"Display expression #{source.index} changed in GitHub's Markdown parser. "
                f"Expected {expected!r}; received {actual!r}."
            ))

    for source, rendered in zip(inline_source, inline_html):
        expected = normalize_tex(source.tex, display=False)
        actual = normalize_tex(rendered["text"], display=False)
        if expected != actual:
            findings.append(Finding(
                "ERROR", str(markdown_path), source.line, "SERVER_INLINE_MISMATCH",
                f"Inline expression #{source.index} changed in GitHub's Markdown parser. "
                f"Expected {expected!r}; received {actual!r}."
            ))

    forbidden_messages = (
        "The following macros are not allowed",
        "Missing close brace",
        "Undefined control sequence",
        "Math input error",
        "MathJax error",
        "ParseError",
    )
    lower_html = html_text.lower()
    for message in forbidden_messages:
        if message.lower() in lower_html:
            findings.append(Finding(
                "ERROR", str(html_path), 1, "SERVER_ERROR_MESSAGE",
                f"GitHub HTML contains the error message {message!r}."
            ))

    summary = {
        "source_display": len(display_source),
        "source_inline": len(inline_source),
        "server_display": len(display_html),
        "server_inline": len(inline_html),
        "total_source": len(result.expressions),
        "total_server": len(parser.renderers),
    }
    return findings, summary


def print_findings(findings: Sequence[Finding]) -> None:
    for finding in findings:
        print(finding.format(), file=sys.stderr if finding.severity == "ERROR" else sys.stdout)


def exit_code(findings: Sequence[Finding], strict: bool) -> int:
    if any(item.severity == "ERROR" for item in findings):
        return 1
    if strict and any(item.severity == "WARNING" for item in findings):
        return 2
    return 0


def filter_ignored_warnings(
    findings: Sequence[Finding],
    ignored_codes: Iterable[str],
) -> list[Finding]:
    ignored = set(ignored_codes)
    return [
        finding for finding in findings
        if not (finding.severity == "WARNING" and finding.code in ignored)
    ]


def command_lint(args: argparse.Namespace) -> int:
    all_findings: list[Finding] = []
    inventory: list[dict] = []
    totals = Counter()

    for name in args.files:
        path = Path(name)
        result = scan_markdown(path, strict=args.strict, extra_allowed_macros=args.allow_macro)
        all_findings.extend(filter_ignored_warnings(result.findings, args.ignore_warning))
        totals["display"] += result.display_count
        totals["inline"] += result.inline_count
        inventory.extend(expression.to_json() for expression in result.expressions)
        print(
            f"{path}: {result.display_count} display expressions, "
            f"{result.inline_count} inline expressions"
        )

    if args.inventory_out:
        Path(args.inventory_out).write_text(
            json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote source inventory to {args.inventory_out}")

    print_findings(all_findings)
    print(
        f"TOTAL: {totals['display']} display, {totals['inline']} inline, "
        f"{sum(item.severity == 'ERROR' for item in all_findings)} errors, "
        f"{sum(item.severity == 'WARNING' for item in all_findings)} warnings"
    )
    return exit_code(all_findings, args.strict)


def command_verify_html(args: argparse.Namespace) -> int:
    findings, summary = verify_server_html(
        Path(args.markdown),
        Path(args.html),
        strict=args.strict,
        extra_allowed_macros=args.allow_macro,
    )
    findings = filter_ignored_warnings(findings, args.ignore_warning)
    print(json.dumps(summary, indent=2))
    print_findings(findings)
    return exit_code(findings, args.strict)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Conservative validator for mathematical Markdown rendered by GitHub."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    lint = subparsers.add_parser("lint", help="Lint one or more Markdown files.")
    lint.add_argument("files", nargs="+", help="Markdown files to validate.")
    lint.add_argument("--strict", action="store_true", help="Treat warnings as failure.")
    lint.add_argument(
        "--allow-macro", action="append", default=[],
        help="Explicitly allow an additional macro name, without the leading backslash."
    )
    lint.add_argument(
        "--ignore-warning", action="append", default=[],
        help="Acknowledge and suppress a warning code after manual review."
    )
    lint.add_argument("--inventory-out", help="Write all detected source expressions as JSON.")
    lint.set_defaults(func=command_lint)

    verify = subparsers.add_parser(
        "verify-html",
        help="Compare source expressions with the server-rendered GitHub HTML."
    )
    verify.add_argument("markdown", help="The Markdown source file.")
    verify.add_argument("html", help="HTML fetched from the commit-specific GitHub blob page.")
    verify.add_argument("--strict", action="store_true", help="Treat warnings as failure.")
    verify.add_argument(
        "--allow-macro", action="append", default=[],
        help="Explicitly allow an additional macro name, without the leading backslash."
    )
    verify.add_argument(
        "--ignore-warning", action="append", default=[],
        help="Acknowledge and suppress a warning code after manual review."
    )
    verify.set_defaults(func=command_verify_html)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
