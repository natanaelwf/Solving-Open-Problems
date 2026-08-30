#!/usr/bin/env python3
"""Exact 2-Selmer upper bounds for Dujella Problem 3.9.

Together with the independent global Kummer classes checked by
verify_problem_3_9.py, this proves

    rank E(Q) = rank E^(-1)(Q) = 4,
    rank E(Q(i)) = 8.

Only Python's standard library and exact arithmetic are used.
"""

from __future__ import annotations

from fractions import Fraction as Q
from typing import Callable, Iterable, Sequence

if not __debug__:
    raise RuntimeError("Run without Python's -O flag.")


def vp_int(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("v_p(0) is not used")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vp(x: Q, p: int) -> int:
    x = Q(x)
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)


def unit_mod(x: Q, p: int, modulus: int | None = None) -> int:
    x = Q(x)
    a = x.numerator // p ** vp_int(x.numerator, p)
    b = x.denominator // p ** vp_int(x.denominator, p)
    m = p if modulus is None else modulus
    return (a % m) * pow(b % m, -1, m) % m


def square_odd(x: Q, p: int) -> bool:
    if x == 0:
        return True
    return vp(x, p) % 2 == 0 and pow(unit_mod(x, p), (p - 1) // 2, p) == 1


def square_2(x: Q) -> bool:
    if x == 0:
        return True
    return vp(x, 2) % 2 == 0 and unit_mod(x, 2, 8) == 1


def sc_odd(x: Q, p: int) -> tuple[int, int]:
    return vp(x, p) & 1, int(pow(unit_mod(x, p), (p - 1) // 2, p) != 1)


def sc_2(x: Q) -> tuple[int, int, int]:
    unit_bits = {1: (0, 0), 3: (1, 1), 5: (0, 1), 7: (1, 0)}
    minus_one, five = unit_bits[unit_mod(x, 2, 8)]
    return minus_one, vp(x, 2) & 1, five


def sc_real(x: Q) -> tuple[int]:
    return (int(x < 0),)


def bits(row: Sequence[int]) -> int:
    return sum((entry & 1) << i for i, entry in enumerate(row))


def rank2(rows: Iterable[Sequence[int]]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        value = bits(row)
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def nullspace(rows: Iterable[Sequence[int]], ncols: int) -> list[tuple[int, ...]]:
    matrix = [bits(row) for row in rows]
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        selected = next((j for j in range(r, len(matrix)) if (matrix[j] >> c) & 1), None)
        if selected is None:
            continue
        matrix[r], matrix[selected] = matrix[selected], matrix[r]
        for j in range(len(matrix)):
            if j != r and ((matrix[j] >> c) & 1):
                matrix[j] ^= matrix[r]
        pivots.append(c)
        r += 1
    row_for_pivot = {p: matrix[i] for i, p in enumerate(pivots)}
    basis: list[tuple[int, ...]] = []
    for free in (c for c in range(ncols) if c not in pivots):
        value = 1 << free
        for pivot in reversed(pivots):
            if (row_for_pivot[pivot] & value).bit_count() & 1:
                value |= 1 << pivot
        basis.append(tuple((value >> c) & 1 for c in range(ncols)))
    return basis


def dot(a: Sequence[int], b: Sequence[int]) -> int:
    return sum(x * y for x, y in zip(a, b)) & 1


def cubic(x: Q, roots: Sequence[int]) -> Q:
    result = Q(1)
    for root in roots:
        result *= x - root
    return result


def ordinary_pair(x: Q, roots: Sequence[int], sc: Callable[[Q], tuple[int, ...]]) -> tuple[int, ...]:
    return sc(x - roots[0]) + sc(x - roots[1])


def torsion_pair(roots: Sequence[int], sc: Callable[[Q], tuple[int, ...]]) -> tuple[int, ...]:
    e0, e1, e2 = map(Q, roots)
    return sc(e1 - e0) + sc((e1 - e0) * (e1 - e2))


ROOTS_E = (1298283376802401, -637703335220400, -660580041582000)
ROOTS_TWIST = (660580041582000, 637703335220400, -1298283376802401)
PRIMES = (2, 3, 5, 7, 13, 41, 47, 61, 73, 103, 113, 149, 233)
GENERATORS = (-1,) + PRIMES
SCALAR_DIM = len(GENERATORS)
AMBIENT_DIM = 2 * SCALAR_DIM

BASES_E: dict[int | str, tuple[str | int, ...]] = {
    2: ("T", 2, 5), 3: ("T", 2), 5: (2, 5), 7: ("T", 4),
    13: (1, 6), 41: (0, 29), 47: ("T", 40), 61: (0, 2),
    73: (4, 11), 103: ("T", 9), 113: (1, 11), 149: (1, 58),
    233: (6, 33), "R": ("T",),
}
BASES_TWIST: dict[int | str, tuple[str | int, ...]] = {
    2: ("T", -8, 0), 3: ("T", 0), 5: (3, 5), 7: ("T", 1),
    13: (1, 20), 41: (0, 12), 47: ("T", 1), 61: (0, 2),
    73: (2, 62), 103: ("T", 11), 113: (6, 102), 149: (1, 91),
    233: (1, 200), "R": ("T",),
}


def strip_supported(n: int) -> int:
    n = abs(n)
    for p in PRIMES:
        while n % p == 0:
            n //= p
    return n


for roots in (ROOTS_E, ROOTS_TWIST):
    for i in range(3):
        for j in range(i + 1, 3):
            assert strip_supported(roots[i] - roots[j]) == 1


def local_sc(place: int | str) -> tuple[Callable[[Q], tuple[int, ...]], int]:
    if place == "R":
        return sc_real, 1
    if place == 2:
        return sc_2, 3
    assert isinstance(place, int) and place % 2 == 1
    return lambda x: sc_odd(x, place), 2


def local_image(roots: Sequence[int], place: int | str, descriptors: Sequence[str | int]) -> tuple[list[tuple[int, ...]], int]:
    sc, scalar_dim = local_sc(place)
    vectors: list[tuple[int, ...]] = []
    for descriptor in descriptors:
        if descriptor == "T":
            vectors.append(torsion_pair(roots, sc))
            continue
        x = Q(descriptor)
        value = cubic(x, roots)
        if place == "R":
            assert value >= 0
        elif place == 2:
            assert square_2(value)
        else:
            assert isinstance(place, int) and square_odd(value, place)
        vectors.append(ordinary_pair(x, roots, sc))
    expected = 1 if place == "R" else 3 if place == 2 else 2
    assert rank2(vectors) == expected
    return vectors, scalar_dim


def global_images(place: int | str) -> list[tuple[int, ...]]:
    sc, _ = local_sc(place)
    return [sc(Q(g)) for g in GENERATORS]


def pullback(local_vectors: Sequence[Sequence[int]], scalar_dim: int, place: int | str) -> list[tuple[int, ...]]:
    equations = nullspace(local_vectors, 2 * scalar_dim)
    images = global_images(place)
    rows: list[tuple[int, ...]] = []
    for equation in equations:
        first, second = equation[:scalar_dim], equation[scalar_dim:]
        row = [0] * AMBIENT_DIM
        for i, image in enumerate(images):
            row[i] = dot(first, image)
            row[SCALAR_DIM + i] = dot(second, image)
        rows.append(tuple(row))
    return rows


def selmer_dimension(roots: Sequence[int], bases: dict[int | str, tuple[str | int, ...]]) -> tuple[int, int]:
    conditions: list[tuple[int, ...]] = []
    for place in PRIMES + ("R",):
        image, scalar_dim = local_image(roots, place, bases[place])
        conditions.extend(pullback(image, scalar_dim, place))
    condition_rank = rank2(conditions)
    return condition_rank, AMBIENT_DIM - condition_rank


def main() -> None:
    results = []
    for name, roots, bases in (
        ("E", ROOTS_E, BASES_E),
        ("E^(-1)", ROOTS_TWIST, BASES_TWIST),
    ):
        condition_rank, selmer_dim = selmer_dimension(roots, bases)
        assert condition_rank == 22 and selmer_dim == 6
        results.append(selmer_dim)
        print(f"{name}:")
        print(f"  rank of local-condition matrix = {condition_rank}")
        print(f"  dim Sel_2 = {selmer_dim}")
        print("  Mordell-Weil rank over Q <= 4")
    assert results == [6, 6]
    print("Combined with verify_problem_3_9.py:")
    print("  rank E(Q) = rank E^(-1)(Q) = 4")
    print("  rank E(Q(i)) = 4 + 4 = 8 exactly")


if __name__ == "__main__":
    main()
