#!/usr/bin/env python3
"""Exact self-contained verifier for a rational D(1579)-quintuple.

The program uses only Python's standard library and exact Fraction arithmetic.
It verifies both the algebraic construction and the complete ten-pair
certificate printed in Appendix A of the manuscript.  All validation remains
active under ``python -O``.

Usage:
    python verify_problem_5_7.py
    python -O verify_problem_5_7.py
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction as F
from itertools import combinations


class VerificationError(RuntimeError):
    """Raised when an exact verification step fails."""


def require(condition: bool, message: str) -> None:
    """Raise VerificationError unless *condition* is true."""
    if not condition:
        raise VerificationError(message)


def elementary_sums4(values: tuple[F, F, F, F]) -> tuple[F, F, F, F]:
    """Return the four elementary symmetric sums of four rational values."""
    s1 = sum(values, F(0))
    s2 = sum(values[i] * values[j] for i, j in combinations(range(4), 2))
    s3 = sum(
        values[i] * values[j] * values[k]
        for i, j, k in combinations(range(4), 3)
    )
    s4 = values[0] * values[1] * values[2] * values[3]
    return s1, s2, s3, s4


# The exact certificate from the manuscript.  Raw numerator-denominator pairs
# are retained so that reducedness and the integer form of every identity can
# be checked directly.
ELEMENT_DATA: tuple[tuple[int, int], ...] = (
    (
        33380942791732288394506781799035854633069,
        75538472952283763411940280933145492800,
    ),
    (
        3316773984203639702940775190709011433149,
        75538472952283763411940280933145492800,
    ),
    (
        1680187362199310518953,
        2166527099963404441,
    ),
    (
        1709389881871126103949,
        8716539127708085200,
    ),
    (
        304098096506285669837521104823424074474316654947563533621646791874211574337084128550071063420421,
        3796585212474857185303945281228856802407726697264409858869913827070599461019450129348655888733,
    ),
)

ROOT_DATA: dict[tuple[int, int], tuple[int, int]] = {
    (1, 2): (
        10941979381013889381829963110539444558091,
        75538472952283763411940280933145492800,
    ),
    (1, 3): (
        4017088434234597978410857,
        6846225635884358033560,
    ),
    (1, 4): (
        5178555904308195200729,
        17433078255416170400,
    ),
    (1, 5): (
        102975335922383217094373213569585155207608837697611616244212832060657,
        535526142577159816889616333805353727615742370117192125029526556680,
    ),
    (2, 3): (
        1292303630315223261480623,
        6846225635884358033560,
    ),
    (2, 4): (
        1759776140565942992831,
        17433078255416170400,
    ),
    (2, 5): (
        38229089721239204948885403783805280683753830498101986082517043918823,
        535526142577159816889616333805353727615742370117192125029526556680,
    ),
    (3, 4): (619363, 1580),
    (3, 5): (
        12249589944850017954842120528750482143693729496197070,
        48535966676397694976072411838960614105778186356711,
    ),
    (4, 5): (
        16249682237233382941655944683967673323522084311163,
        123590917137894461206966714052895819029002712740,
    ),
}


EXPECTED_PARAMETERS: dict[str, F] = {
    "h": F(790),
    "p": F(1680187362199310518953, 2166527099963404441),
    "t": F(
        -43760220723841232738857861440611350563370603,
        59675393632304173095432821937184939312000,
    ),
    "D": F(628837, 1580),
    "w": F(619363, 1580),
    "X": F(379668710169, 2496400),
    "M": F(-1123238868107, 19971200),
}


def verify() -> None:
    q = 1579

    # Confirm that the printed certificate uses reduced fractions.
    for label, (numerator, denominator) in enumerate(ELEMENT_DATA, start=1):
        require(denominator > 0, f"a{label} has a nonpositive denominator")
        require(
            math.gcd(abs(numerator), denominator) == 1,
            f"a{label} is not in lowest terms",
        )
    for pair, (numerator, denominator) in ROOT_DATA.items():
        require(denominator > 0, f"r{pair} has a nonpositive denominator")
        require(
            math.gcd(abs(numerator), denominator) == 1,
            f"r{pair} is not in lowest terms",
        )

    elements = tuple(F(numerator, denominator) for numerator, denominator in ELEMENT_DATA)
    roots = {pair: F(numerator, denominator) for pair, (numerator, denominator) in ROOT_DATA.items()}

    expected_pairs = set(combinations(range(1, 6), 2))
    require(set(roots) == expected_pairs, "the certificate does not contain exactly ten root pairs")

    # Rational specialization used in the construction.
    A = 9 * q**4 - 20 * q**3 - 490 * q**2 - 20 * q + 9
    B = 9 * q**6 - 86 * q**5 + 2311 * q**4 - 372 * q**3 + 2311 * q**2 - 86 * q + 9
    C = (
        243 * q**10
        - 7758 * q**9
        + 58679 * q**8
        + 73560 * q**7
        + 278742 * q**6
        + 1290220 * q**5
        + 278742 * q**4
        + 73560 * q**3
        + 58679 * q**2
        - 7758 * q
        + 243
    )

    h = F(q + 1, 2)
    p = F((q - 1) * (q * q - 34 * q + 1) * A, 2 * B)
    t = F(
        -(q - 5) * (5 * q - 1) * (q * q + 14 * q + 1) * C,
        32 * (q + 1) ** 3 * A * B,
    )
    require(h == EXPECTED_PARAMETERS["h"], "h does not match the printed value")
    require(p == EXPECTED_PARAMETERS["p"], "p does not match the printed value")
    require(t == EXPECTED_PARAMETERS["t"], "t does not match the printed value")

    # Lemma 1: construct a D(q)-quadruple.
    D = (h * h + 3 * q) / (2 * h)
    w = (h * h - 3 * q) / (2 * h)
    X = w * w - q
    S = (p * p + X) / (2 * p)
    r = (p * p - X) / (4 * p)
    a = (S + D) / 2
    b = (S - D) / 2
    c = p
    d = X / p
    base = (a, b, c, d)

    require(D == EXPECTED_PARAMETERS["D"], "D does not match the printed value")
    require(w == EXPECTED_PARAMETERS["w"], "w does not match the printed value")
    require(X == EXPECTED_PARAMETERS["X"], "X does not match the printed value")

    lemma1_roots = {
        (1, 2): r,
        (1, 3): a + r,
        (1, 4): a - r,
        (2, 3): b + r,
        (2, 4): b - r,
        (3, 4): w,
    }
    for (i, j), root in lemma1_roots.items():
        require(
            base[i - 1] * base[j - 1] + q == root * root,
            f"the quadruple identity failed at pair {(i, j)}",
        )
        require(
            root * root == roots[(i, j)] * roots[(i, j)],
            f"the printed root disagrees at pair {(i, j)}",
        )

    # Lemma 2: verify the extension condition and construct the fifth entry.
    s1, s2, s3, s4 = elementary_sums4(base)
    M = (s1 * s1 - 4 * s2) / 8
    require(M == EXPECTED_PARAMETERS["M"], "M does not match the printed value")
    require(M * M - s4 == F(q, 4) * t * t, "the extension square condition failed")

    e = q * (s1 * M + s3) / (M * M - s4)
    constructed = base + (e,)
    require(constructed == elements, "the printed quintuple does not match the construction")

    for i, x in enumerate(base, start=1):
        predicted = (2 * M + x * (s1 - 2 * x)) / t
        require(
            predicted * predicted == roots[(i, 5)] * roots[(i, 5)],
            f"the extension root disagrees at pair {(i, 5)}",
        )

    # Structural conditions in the definition of a rational D(q)-quintuple.
    require(all(value != 0 for value in elements), "the quintuple contains zero")
    require(len(set(elements)) == 5, "the five entries are not pairwise distinct")
    require(all(value > 0 for value in elements), "not all five entries are positive")

    # Direct verification of the complete finite certificate, first with
    # Fractions and then in the equivalent integer form.
    for i, j in combinations(range(1, 6), 2):
        ai = elements[i - 1]
        aj = elements[j - 1]
        rij = roots[(i, j)]
        require(ai * aj + q == rij * rij, f"fraction identity failed at pair {(i, j)}")

        Ni, Di = ELEMENT_DATA[i - 1]
        Nj, Dj = ELEMENT_DATA[j - 1]
        Rij, Sij = ROOT_DATA[(i, j)]
        left = (Ni * Nj + q * Di * Dj) * Sij * Sij
        right = Rij * Rij * Di * Dj
        require(left == right, f"integer identity failed at pair {(i, j)}")
        print(f"({i},{j}): exact identity verified")

    ordered_labels = sorted((value, index) for index, value in enumerate(elements, start=1))
    expected_order = [2, 5, 4, 1, 3]
    require(
        [index for _, index in ordered_labels] == expected_order,
        "the strict order of the entries is not the one stated in the manuscript",
    )
    interval_claims = {
        2: (43, 44),
        5: (80, 81),
        4: (196, 197),
        1: (441, 442),
        3: (775, 776),
    }
    for value, index in ordered_labels:
        lower, upper = interval_claims[index]
        require(F(lower) < value < F(upper), f"the interval bound for a{index} failed")

    print("Strict order: a2 < a5 < a4 < a1 < a3")
    print("PASS: the construction and all ten D(1579) identities are exact.")


def main() -> int:
    try:
        verify()
    except VerificationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
