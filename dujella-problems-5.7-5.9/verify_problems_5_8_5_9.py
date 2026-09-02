#!/usr/bin/env python3
"""Exact verifier for "Rational D(q)-Quintuples for Every Rational q".

Only Python's standard library is used.  The program performs independent
exact checks of the manuscript's central algebra:

1. Integer polynomial arithmetic verifies the factorization in equation (11)
   after cross-multiplication.  No computer algebra package is used.
2. Exact Fraction arithmetic constructs the five entries and the ten square
   roots at several rational specializations and verifies every D(z) identity.
3. The square-class transfer z = q*u^2 is checked exactly for a user-selected
   rational q and nonzero rational u.
4. The polynomial division used in the infinitude argument is verified as an
   exact polynomial identity.

All validation remains active under ``python -O``.

Examples:
    python verify_problems_5_8_5_9.py
    python verify_problems_5_8_5_9.py --q 2/3 --u 7/5 --show
    python -O verify_problems_5_8_5_9.py --q=-5/11 --u 13/4
    python verify_problems_5_8_5_9.py --q 0
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from typing import Iterable


class VerificationError(RuntimeError):
    """Raised when an exact verification step fails."""


def require(condition: bool, message: str) -> None:
    """Raise VerificationError unless *condition* is true."""
    if not condition:
        raise VerificationError(message)


def parse_fraction(text: str) -> F:
    try:
        return F(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid rational number: {text!r}") from exc


# ---------------------------------------------------------------------------
# Pure integer polynomial arithmetic.
# Coefficients are stored from lowest to highest degree.
# ---------------------------------------------------------------------------

Poly = tuple[int, ...]
RatPoly = tuple[Poly, Poly]


def ptrim(values: Iterable[int]) -> Poly:
    coefficients = list(values)
    if not coefficients:
        return (0,)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def padd(a: Poly, b: Poly) -> Poly:
    result = [0] * max(len(a), len(b))
    for index, value in enumerate(a):
        result[index] += value
    for index, value in enumerate(b):
        result[index] += value
    return ptrim(result)


def pneg(a: Poly) -> Poly:
    return tuple(-value for value in a)


def psub(a: Poly, b: Poly) -> Poly:
    return padd(a, pneg(b))


def pmul(a: Poly, b: Poly) -> Poly:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return ptrim(result)


def pscale(a: Poly, scalar: int) -> Poly:
    return ptrim(scalar * value for value in a)


def ppow(a: Poly, exponent: int) -> Poly:
    if exponent < 0:
        raise ValueError("negative polynomial exponent")
    result: Poly = (1,)
    base = a
    power = exponent
    while power:
        if power & 1:
            result = pmul(result, base)
        base = pmul(base, base)
        power //= 2
    return result


def rpoly(numerator: Poly, denominator: Poly = (1,)) -> RatPoly:
    require(ptrim(denominator) != (0,), "zero polynomial denominator")
    return ptrim(numerator), ptrim(denominator)


def radd(x: RatPoly, y: RatPoly) -> RatPoly:
    return (
        padd(pmul(x[0], y[1]), pmul(y[0], x[1])),
        pmul(x[1], y[1]),
    )


def rsub(x: RatPoly, y: RatPoly) -> RatPoly:
    return (
        psub(pmul(x[0], y[1]), pmul(y[0], x[1])),
        pmul(x[1], y[1]),
    )


def rmul(x: RatPoly, y: RatPoly) -> RatPoly:
    return pmul(x[0], y[0]), pmul(x[1], y[1])


def rscale(x: RatPoly, scalar: int) -> RatPoly:
    return pscale(x[0], scalar), x[1]


def rpow(x: RatPoly, exponent: int) -> RatPoly:
    return ppow(x[0], exponent), ppow(x[1], exponent)


def requal(x: RatPoly, y: RatPoly) -> bool:
    return pmul(x[0], y[1]) == pmul(y[0], x[1])


def manuscript_polynomials() -> tuple[Poly, Poly, Poly, Poly]:
    """Return K, A, B, C as integer coefficient tuples."""
    K = (1, -34, 1)
    A = (9, -20, -490, -20, 9)
    B = (9, -86, 2311, -372, 2311, -86, 9)
    C = (
        243,
        -7758,
        58679,
        73560,
        278742,
        1290220,
        278742,
        73560,
        58679,
        -7758,
        243,
    )
    return K, A, B, C


def verify_delta_factorization() -> None:
    """Verify equation (11) by integer polynomial cross-multiplication."""
    z = (0, 1)
    z_minus_1 = (-1, 1)
    z_plus_1 = (1, 1)
    z_minus_5 = (-5, 1)
    five_z_minus_1 = (-1, 5)
    z_squared_plus_14z_plus_1 = (1, 14, 1)
    K, A, B, C = manuscript_polynomials()

    p = rpoly(
        pmul(pmul(z_minus_1, K), A),
        pscale(B, 2),
    )
    X = rpoly(
        pmul(ppow(z_minus_1, 2), K),
        pscale(ppow(z_plus_1, 2), 16),
    )

    delta = rsub(
        rmul(
            rpow(p, 2),
            rpow(radd(rscale(rpoly(z), 4), rscale(X, 5)), 2),
        ),
        rscale(rmul(X, rpow(radd(rpow(p, 2), X), 2)), 4),
    )

    rhs_numerator = pmul(
        pmul(
            pmul(
                pmul(
                    pmul(
                        pmul(z, ppow(z_minus_5, 2)),
                        ppow(z_minus_1, 2),
                    ),
                    ppow(five_z_minus_1, 2),
                ),
                ppow(K, 2),
            ),
            ppow(z_squared_plus_14z_plus_1, 2),
        ),
        ppow(C, 2),
    )
    rhs_denominator = pscale(
        pmul(ppow(z_plus_1, 6), ppow(B, 4)),
        256,
    )
    rhs = rpoly(rhs_numerator, rhs_denominator)

    require(requal(delta, rhs), "equation (11) factorization failed")


def verify_polynomial_division() -> None:
    """Verify the exact division underlying p(z)=z/2-83/6+O(1/z)."""
    z = (0, 1)
    z_minus_1 = (-1, 1)
    K, A, B, _ = manuscript_polynomials()
    numerator = pmul(pmul(z_minus_1, K), A)

    # R(z) = 781 z^5 - 15137 z^4 + 5442 z^3
    #        - 11906 z^2 + 385 z - 45.
    R = (-45, 385, -11906, 5442, -15137, 781)

    # Equivalent to
    # N/(2B) = (3z-83)/6 - 8R/(3B):
    #        3N = (3z-83)B - 16R.
    right = psub(pmul((-83, 3), B), pscale(R, 16))
    require(pscale(numerator, 3) == right, "polynomial division identity failed")


# ---------------------------------------------------------------------------
# Exact rational construction and ten-pair verification.
# ---------------------------------------------------------------------------


def poly_A(z: F) -> F:
    return 9 * z**4 - 20 * z**3 - 490 * z**2 - 20 * z + 9


def poly_B(z: F) -> F:
    return 9 * z**6 - 86 * z**5 + 2311 * z**4 - 372 * z**3 + 2311 * z**2 - 86 * z + 9


def poly_C(z: F) -> F:
    return (
        243 * z**10
        - 7758 * z**9
        + 58679 * z**8
        + 73560 * z**7
        + 278742 * z**6
        + 1290220 * z**5
        + 278742 * z**4
        + 73560 * z**3
        + 58679 * z**2
        - 7758 * z
        + 243
    )


@dataclass(frozen=True)
class Construction:
    z: F
    h: F
    p: F
    t: F
    D: F
    w: F
    X: F
    S: F
    r: F
    M: F
    entries: tuple[F, F, F, F, F]
    roots: dict[tuple[int, int], F]


def construct(z: F) -> Construction:
    """Construct and verify one nonexceptional exact specialization."""
    require(z != 0, "the generic extension requires z != 0")

    A = poly_A(z)
    B = poly_B(z)
    C = poly_C(z)
    K = z * z - 34 * z + 1

    require(z + 1 != 0, "z = -1 is a pole of the displayed formulas")
    require(A != 0 and B != 0, "A(z) or B(z) vanishes")

    h = (z + 1) / 2
    p = (z - 1) * K * A / (2 * B)
    require(h != 0 and p != 0, "h or p vanishes")

    t = -(
        (z - 5)
        * (5 * z - 1)
        * (z * z + 14 * z + 1)
        * C
        / (32 * (z + 1) ** 3 * A * B)
    )
    require(t != 0, "t vanishes")

    D = (h * h + 3 * z) / (2 * h)
    w = (h * h - 3 * z) / (2 * h)
    X = w * w - z
    S = (p * p + X) / (2 * p)
    r = (p * p - X) / (4 * p)

    a = (S + D) / 2
    b = (S - D) / 2
    c = p
    d = X / p
    base = (a, b, c, d)

    s1 = sum(base, F(0))
    s2 = sum(base[i] * base[j] for i, j in combinations(range(4), 2))
    s3 = sum(base[i] * base[j] * base[k] for i, j, k in combinations(range(4), 3))
    s4 = a * b * c * d
    M = (s1 * s1 - 4 * s2) / 8

    require(X == (z - 1) ** 2 * K / (16 * (z + 1) ** 2), "equation (7) failed")
    require(M == (4 * z - 3 * X) / 8, "equation (9) failed")
    require(t * t == 4 * (M * M - s4) / z, "extension square condition failed")
    require(M * M - s4 != 0, "extension denominator vanishes")

    e = z * (s1 * M + s3) / (M * M - s4)
    entries = base + (e,)
    require(all(value != 0 for value in entries), "an entry is zero")
    require(len(set(entries)) == 5, "the specialization is degenerate")

    roots: dict[tuple[int, int], F] = {
        (1, 2): r,
        (1, 3): a + r,
        (1, 4): a - r,
        (2, 3): b + r,
        (2, 4): b - r,
        (3, 4): w,
    }
    for index, value in enumerate(base, start=1):
        roots[(index, 5)] = (2 * M + value * (s1 - 2 * value)) / t

    expected_pairs = set(combinations(range(1, 6), 2))
    require(set(roots) == expected_pairs, "the construction did not produce ten roots")
    for i, j in combinations(range(1, 6), 2):
        require(
            entries[i - 1] * entries[j - 1] + z == roots[(i, j)] ** 2,
            f"D(z) identity failed for pair {(i, j)}",
        )

    return Construction(z, h, p, t, D, w, X, S, r, M, entries, roots)


def verify_z2_specialization() -> None:
    data = construct(F(2))
    expected_entries = (
        F(6092447, 3603680),
        F(-3817673, 3603680),
        F(1561, 1010),
        F(-505, 1784),
        F(-3576247855663273, 3069853820287070),
    )
    require(data.t == F(-3852651, 3603680), "the stated value t(2) is incorrect")
    require(data.entries == expected_entries, "the stated z=2 specialization is incorrect")
    a, b, c, d, e = data.entries
    require(e < b < d < 0 < c < a, "the stated strict order at z=2 is incorrect")


def verify_scaled(q: F, u: F) -> tuple[tuple[F, ...], dict[tuple[int, int], F]]:
    """Verify one exact instance of the square-class transfer."""
    require(u != 0, "u must be nonzero")

    if q == 0:
        entries = (F(1), F(4), F(9), F(16), F(25))
        square_bases = (F(1), F(2), F(3), F(4), F(5))
        roots: dict[tuple[int, int], F] = {}
        for i, j in combinations(range(5), 2):
            roots[(i + 1, j + 1)] = square_bases[i] * square_bases[j]
            require(
                entries[i] * entries[j] == roots[(i + 1, j + 1)] ** 2,
                "D(0) identity failed",
            )
        return entries, roots

    generic = construct(q * u * u)
    entries = tuple(value / u for value in generic.entries)
    roots = {pair: value / u for pair, value in generic.roots.items()}

    require(all(value != 0 for value in entries), "a scaled entry is zero")
    require(len(set(entries)) == 5, "the scaled quintuple is degenerate")
    for i, j in combinations(range(1, 6), 2):
        require(
            entries[i - 1] * entries[j - 1] + q == roots[(i, j)] ** 2,
            f"D(q) identity failed after scaling for pair {(i, j)}",
        )
    return entries, roots


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--q",
        type=parse_fraction,
        default=F(2, 3),
        help="target q, as an integer or fraction (default: 2/3)",
    )
    parser.add_argument(
        "--u",
        type=parse_fraction,
        default=F(7, 5),
        help="nonzero scaling parameter u (default: 7/5)",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="print the resulting five entries and ten roots",
    )
    args = parser.parse_args(argv)

    try:
        verify_delta_factorization()
        verify_polynomial_division()
        verify_z2_specialization()

        # Exact specializations on both signs, including nonintegral values and
        # the specialization used in the companion Problem 5.7 manuscript.
        for test_z in (
            F(2, 3),
            F(-7, 5),
            F(11, 13),
            F(-19, 7),
            F(123, 17),
            F(1579),
        ):
            construct(test_z)

        entries, roots = verify_scaled(args.q, args.u)
    except (VerificationError, ZeroDivisionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("PASS: equation (11) holds by exact integer polynomial arithmetic.")
    print("PASS: the polynomial division used for infinitude is exact.")
    print("PASS: all ten D(z) identities hold at exact rational specializations.")
    print(f"PASS: square-class transfer produced a D({args.q})-quintuple for u={args.u}.")

    if args.show:
        print("Entries:")
        for index, value in enumerate(entries, start=1):
            print(f"  a{index} = {value}")
        print("Roots:")
        for pair in sorted(roots):
            print(f"  r{pair[0]}{pair[1]} = {roots[pair]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
