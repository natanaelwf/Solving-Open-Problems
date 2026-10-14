#!/usr/bin/env python3
"""Check every formula and semantic variable against the LaTeX-derived inventory."""
from pathlib import Path
import json,re,tempfile
from github_math_guard_v2 import scan_markdown
BASE=Path(__file__).resolve().parent
EXTRA='ell int ll gg asymp lfloor rfloor lceil rceil nmid bmod pmod'.split()
PAGE=BASE.parent/'dujella-problem-1.7/README.md'

def canonical(s):
    # Equivalent named delimiters and Unicode mathematical alphabet characters.
    for old,new in [(r'\mathbb{Z}','ℤ'),(r'\mathbb{Q}','ℚ'),(r'\mathbb{R}','ℝ'),(r'\mathcal{O}','𝒪')]:
        s=s.replace(old,new)
    s=s.replace(r'\{',r'\lbrace').replace(r'\}',r'\rbrace')
    s=re.sub(r'\\(?:begin|end)\{(?:gathered|aligned|align\*?)\}', '', s)
    s=re.sub(r'\\(?:qquad|quad|enspace|thinspace)\b', '', s)
    s=re.sub(r'\\[!,;:]','',s)
    s=s.replace('\\\\','').replace('&','')
    return re.sub(r'\s+','',s)

rendered=scan_markdown(PAGE,strict=True,extra_allowed_macros=EXTRA)
assert not rendered.findings,[f.format() for f in rendered.findings]
# Single-letter variables need only semantic italic HTML, not a TeX renderer.
# Recover precisely those marked variables for the independent source comparison.
text=PAGE.read_text()
variables=re.findall(r'<var>([A-Za-z])</var>',text)
recovered=re.sub(r'<var>([A-Za-z])</var>',r'$\1$',text)
with tempfile.TemporaryDirectory() as directory:
    copy=Path(directory)/'semantic-source-check.md';copy.write_text(recovered)
    actual=scan_markdown(copy,strict=True,extra_allowed_macros=EXTRA).expressions
expected=json.loads((BASE/'source_math.json').read_text())
assert len(actual)==len(expected),(len(actual),len(expected))
for i,(a,e) in enumerate(zip(actual,expected),1):
    kind='display' if e['kind']=='DisplayMath' else 'inline'
    assert a.kind==kind,(i,a.kind,kind)
    assert canonical(a.tex)==canonical(e['tex']),(i,a.line,a.tex,e['tex'])
# GitHub's renderer counts opening groups plus one per expression. Keeping
# this below 1000 also leaves room for a second page-hydration pass.
budget=sum(e.tex.count('{')+1 for e in rendered.expressions)
assert budget<1000,budget
print(f'PASS: all {len(actual)} mathematical items match the source in content and order.')
print(f'{len(rendered.expressions)} TeX expressions; {len(variables)} semantic single-letter variables; renderer budget {budget}.')
