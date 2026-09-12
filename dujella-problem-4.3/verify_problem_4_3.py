#!/usr/bin/env python3
"""Exact verification for the family solving Dujella's Problem 4.3."""

from __future__ import annotations

import argparse
from itertools import combinations
from math import isqrt
from typing import Iterator

# A polynomial in t and w, represented by (degree_t, degree_w) -> coefficient.
Poly = dict[tuple[int, int], int]


def constant(value: int) -> Poly:
    return {(0, 0): value} if value else {}


def add(*polynomials: Poly) -> Poly:
    result: Poly = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial: Poly, value: int) -> Poly:
    return {
        monomial: value * coefficient
        for monomial, coefficient in polynomial.items()
        if value * coefficient
    }


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            result[monomial] = result.get(monomial, 0) + a * b
    return {m: c for m, c in result.items() if c}


def power(polynomial: Poly, exponent: int) -> Poly:
    if exponent < 0:
        raise ValueError("Polynomial exponents must be nonnegative.")
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def verify_polynomial_identities() -> None:
    """Verify the two universal polynomial identities coefficient by coefficient."""
    t: Poly = {(1, 0): 1}
    w: Poly = {(0, 1): 1}
    t2 = power(t, 2)
    w2 = power(w, 2)

    a = scale(w, 8)
    ell = add(scale(t, 4), scale(w, -3), constant(-1))
    r = add(scale(multiply(w, ell), 4), constant(-1))

    z = add(
        scale(power(t, 4), 8),
        scale(multiply(a, power(t, 3)), 8),
        scale(t2, -8),
        scale(multiply(a, t), -4),
        constant(1),
    )
    target = add(scale(power(r, 2), 2), scale(multiply(a, r), 2), constant(-1))
    pell_factor = add(t2, scale(multiply(t, w), 12), scale(w2, -18), constant(-1))
    other_factor = add(t2, scale(multiply(t, w), -4), scale(w2, 2))

    remainder = add(z, scale(target, -1), scale(multiply(pell_factor, other_factor), -8))
    if remainder:
        raise ArithmeticError(f"Central polynomial identity failed: {remainder}")

    u = add(scale(t2, 4), constant(-1))
    v = add(scale(power(t, 3), 4), scale(t, -3))
    remainder = add(
        power(v, 2),
        scale(multiply(add(t2, constant(-1)), power(u, 2)), -1),
        constant(-1),
    )
    if remainder:
        raise ArithmeticError(f"Auxiliary polynomial identity failed: {remainder}")


def make_member(x: int, w: int) -> tuple[tuple[int, int, int, int], tuple[int, int, int, int]]:
    if x <= 0 or w <= 0 or x * x - 54 * w * w != 1:
        raise ArithmeticError("Invalid Pell parameters.")

    t = x - 6 * w
    ell = 4 * t - 3 * w - 1
    a = 8 * w

    b, remainder = divmod(9 * w - 6 * t, 4)
    if remainder:
        raise ArithmeticError("The parameter b is not integral.")

    r = 4 * w * ell - 1
    p = ell * (2 * w * ell - 1)
    q = (ell + 2) * (2 * w * (ell + 2) - 1)
    u = 4 * t * t - 1
    v = t * (4 * t * t - 3)
    e = u * ((a + b) * u + 2 * v)
    d = 4 * r * (a + r) * (p + r)

    first = (a, p, q, d)
    second = (b, a, e, d)

    if not (x % 4 == 1 and w % 4 == 2):
        raise ArithmeticError("The Pell congruences failed.")
    if not (0 < b < a < p < q < d and a < e < d):
        raise ArithmeticError("The required ordering failed.")
    if set(first) == set(second):
        raise ArithmeticError("The two quadruples are not distinct.")
    if a * b + 1 != t * t or a * p + 1 != r * r:
        raise ArithmeticError("A basic square identity failed.")

    z = 8 * t**4 + 8 * a * t**3 - 8 * t**2 - 4 * a * t + 1
    if z != 2 * r * (a + r) - 1:
        raise ArithmeticError("The common-largest-element identity failed.")
    if a * d + 1 != z * z:
        raise ArithmeticError("The shared square certificate failed.")

    return first, second


def family() -> Iterator[tuple[tuple[int, int, int, int], tuple[int, int, int, int]]]:
    x, w = 485, 66
    while True:
        yield make_member(x, w)
        x, w = (
            470449 * x + 3457080 * w,
            64020 * x + 470449 * w,
        )


def verify_quadruple(quadruple: tuple[int, int, int, int]) -> None:
    if len(set(quadruple)) != 4 or min(quadruple) <= 0:
        raise ArithmeticError("A quadruple is degenerate or nonpositive.")

    for left, right in combinations(quadruple, 2):
        value = left * right + 1
        root = isqrt(value)
        if root * root != value:
            raise ArithmeticError(f"Not a square: {left} * {right} + 1")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--count",
        type=int,
        default=100,
        help="number of pairs to verify (default: 100)",
    )
    args = parser.parse_args()
    if args.count < 1:
        parser.error("--count must be positive")

    verify_polynomial_identities()

    iterator = family()
    previous_d = 0
    first_pair = None

    for _ in range(args.count):
        first, second = next(iterator)
        verify_quadruple(first)
        verify_quadruple(second)
        if first[-1] != second[-1]:
            raise ArithmeticError("The largest elements are different.")
        if first[-1] <= previous_d:
            raise ArithmeticError("The sampled largest elements did not increase.")
        previous_d = first[-1]
        if first_pair is None:
            first_pair = (first, second)

    print("Polynomial identities: exact coefficient check passed.")
    print(f"Pairs checked exactly: {args.count}.")
    print(f"Pairwise square conditions checked with isqrt: {12 * args.count}.")
    print("Integrality, positivity, ordering, distinctness, and common maximum: passed.")
    print("First pair:")
    assert first_pair is not None
    print(first_pair[0])
    print(first_pair[1])


if __name__ == "__main__":
    main()
