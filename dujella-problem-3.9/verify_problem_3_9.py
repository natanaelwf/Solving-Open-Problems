#!/usr/bin/env python3
"""Exact-arithmetic verification for the solution of Dujella's Problem 3.9.

The script uses only Python's standard library.  It checks the explicit
Diophantine triple, the Q-isomorphism to the displayed integral curve, the
exact torsion certificate over Q(i), both 2-Kummer rank certificates, and the
numerical pullback that produces the triple from the v = 180/6643 family
member.

The mathematical note is self-contained; this file is ancillary verification.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt
from typing import Callable, Sequence


if not __debug__:
    raise RuntimeError("Run this verification script without Python's -O flag.")


# ---------------------------------------------------------------------------
# Generic exact-arithmetic helpers
# ---------------------------------------------------------------------------

def is_square_integer(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_square_rational(x: Q) -> bool:
    return (
        x >= 0
        and is_square_integer(x.numerator)
        and is_square_integer(x.denominator)
    )


def assert_square_class(x: Q, representative: int) -> None:
    """Check x = representative * square in Q."""
    if representative == 0:
        raise ValueError("a square-class representative must be nonzero")
    quotient = x / Q(representative)
    assert is_square_rational(quotient), (x, representative, quotient)


def valuation_parity_of_squarefree(rep: int, prime: int) -> int:
    """Parity of v_prime(rep), for the supplied squarefree representatives."""
    return int(abs(rep) % prime == 0)


def sign_character(rep: int) -> int:
    return int(rep < 0)


def rank_mod_2(rows: Sequence[Sequence[int]]) -> int:
    """Row rank over F_2."""
    pivots: dict[int, int] = {}
    for row in rows:
        value = sum((entry & 1) << j for j, entry in enumerate(row))
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def count_points_mod_p(
    p: int,
    rhs: Callable[[int], int],
) -> int:
    """Count affine points plus the point at infinity by direct enumeration."""
    total = 1
    for x in range(p):
        value = rhs(x) % p
        total += sum(1 for y in range(p) if (y * y - value) % p == 0)
    return total


def cubic_from_roots(roots: Sequence[Q]) -> tuple[Q, Q, Q, Q]:
    """Coefficients of product (x-r), in descending degree."""
    c3, c2, c1, c0 = Q(1), Q(0), Q(0), Q(0)
    for root in roots:
        c3, c2, c1, c0 = (
            c3,
            c2 - root * c3,
            c1 - root * c2,
            c0 - root * c1,
        )
    return c3, c2, c1, c0


def double_point_short_generalized(
    point: tuple[Q, Q],
    *,
    a2: Q,
    a4: Q,
    a6: Q,
) -> tuple[Q, Q]:
    """Double a point on y^2 = x^3 + a2*x^2 + a4*x + a6."""
    x_coord, y_coord = point
    if y_coord == 0:
        raise ValueError("cannot affinely double a nonzero 2-torsion point")
    slope = (3 * x_coord**2 + 2 * a2 * x_coord + a4) / (2 * y_coord)
    x_double = slope**2 - a2 - 2 * x_coord
    y_double = -y_coord + slope * (x_coord - x_double)
    return x_double, y_double


# ---------------------------------------------------------------------------
# 1. The rational Diophantine triple
# ---------------------------------------------------------------------------
a = Q(338256750896, 519329865153)
b = Q(-519329865153, 338256750896)
c = Q(
    2118453423815502078396715008,
    395270688488063020499821199375,
)

r_ab = Q(0)
r_ac = Q(44175660045337, 44098756684775)
r_bc = Q(8926353364485863, 8963306864035225)

assert len({a, b, c}) == 3
assert all(value != 0 for value in (a, b, c))
assert a * b + 1 == r_ab**2
assert a * c + 1 == r_ac**2
assert b * c + 1 == r_bc**2


# ---------------------------------------------------------------------------
# 2. Target curve and exact Q-isomorphism
# ---------------------------------------------------------------------------
A = 1264285630784571919597349762400
B = 546907189853176652858460972620151389392800000

R0 = 1298283376802401
R1 = -637703335220400
R2 = -660580041582000


def f_E(x: Q) -> Q:
    return x**3 - x**2 - A * x - B


assert R0 + R1 + R2 == 1
assert f_E(Q(R0)) == f_E(Q(R1)) == f_E(Q(R2)) == 0
assert len({R0, R1, R2}) == 3

# C': y^2 = (x+ab)(x+ac)(x+bc), whose roots are rho_j.
rho0 = -a * b
rho1 = -a * c
rho2 = -b * c

s = Q(421275422609655575, 9535001089)
beta = Q(R0) - s**2

assert rho0 == 1
assert s * r_ac == 44259049
assert s * r_bc == 43999849
assert s**2 * rho0 + beta == R0
assert s**2 * rho1 + beta == R2
assert s**2 * rho2 + beta == R1

# Coefficient-level check of f_E(s^2 x + beta)
q = s**2
transformed_coeffs = (
    q**3,
    q**2 * (3 * beta - 1),
    q * (3 * beta**2 - 2 * beta - A),
    beta**3 - beta**2 - A * beta - B,
)
induced_coeffs = tuple(s**6 * coeff for coeff in cubic_from_roots((rho0, rho1, rho2)))
assert transformed_coeffs == induced_coeffs


# ---------------------------------------------------------------------------
# 3. Exact torsion certificate over Q(i)
# ---------------------------------------------------------------------------
assert R0 - R1 == 43999849**2
assert R0 - R2 == 44259049**2
assert R1 - R2 == 4782960**2

# Both rational primes split in Q(i), and the reductions are good.
assert 17 == 4**2 + 1**2
assert 29 == 5**2 + 2**2
for p, expected_roots, expected_order in (
    (17, (4, 6, 8), 16),
    (29, (2, 6, 22), 32),
):
    roots = (R0 % p, R1 % p, R2 % p)
    assert roots == expected_roots
    assert len(set(roots)) == 3
    order = count_points_mod_p(
        p,
        lambda x, modulus=p: x**3 - x**2 - (A % modulus) * x - (B % modulus),
    )
    assert order == expected_order


# ---------------------------------------------------------------------------
# 4. Rank(E(Q)) >= 4 via an exact 2-Kummer certificate
# ---------------------------------------------------------------------------
P = [
    (
        Q(18434717483122731307680720, 784728169),
        Q(79058306885031575731369370665045739520, 21982590198197),
    ),
    (
        Q(205575756477590805858000, 19351201),
        Q(92664057348302315420944897563312000, 85125933199),
    ),
    (
        Q(-1333100296085788798313904, 2019513721),
        Q(13040064683254174542549826666008960, 90754927108019),
    ),
    (
        Q(-307245410407559064903399631, 465158100625),
        Q(16672539824494902460966518939675019528, 317249453578765625),
    ),
]
S = (Q(3245674849686002), Q(171874625371303506531698))
T = (Q(R1), Q(0))

for x_coord, y_coord in P + [S, T]:
    assert y_coord**2 == f_E(x_coord)
assert double_point_short_generalized(
    S,
    a2=Q(-1),
    a4=Q(-A),
    a6=Q(-B),
) == (Q(R0), Q(0))

# Representatives of ([x-R0], [x-R1]) for P1,...,P4,S.
E_squareclasses = [
    (41 * 47 * 113, 5 * 13 * 47),
    (41 * 47 * 233, 2 * 13 * 47 * 73),
    (-41 * 47 * 103 * 113 * 233, -2 * 13 * 47 * 103),
    (-47 * 61 * 113 * 149, -47 * 61 * 73 * 149),
    (47 * 61 * 103 * 113 * 149 * 233, 2 * 47 * 61 * 103 * 149),
]

for (x_coord, _), (d1, d2) in zip(P + [S], E_squareclasses):
    assert_square_class(x_coord - R0, d1)
    assert_square_class(x_coord - R1, d2)

# At T=(R1,0), the projected Kummer class is (-1,-1).
assert_square_class(Q(R1 - R0), -1)
assert_square_class(Q((R1 - R0) * (R1 - R2)), -1)
E_squareclasses.append((-1, -1))


def E_character_vector(pair: tuple[int, int]) -> list[int]:
    d1, d2 = pair
    return [
        valuation_parity_of_squarefree(d2, 5),
        valuation_parity_of_squarefree(d2, 73),
        valuation_parity_of_squarefree(d2, 2),
        valuation_parity_of_squarefree(d1, 103),
        sign_character(d1),
        valuation_parity_of_squarefree(d1, 61),
    ]


E_kummer_matrix = [E_character_vector(pair) for pair in E_squareclasses]
assert rank_mod_2(E_kummer_matrix) == 6


# ---------------------------------------------------------------------------
# 5. Rank of the (-1)-twist over Q
# ---------------------------------------------------------------------------
C4 = 79017851924035744974834360150
C6 = 8545424841455885200913452697189865459262500
assert 16 * C4 == A
assert 64 * C6 == B

# E^-: y^2 + xy = x^3 - C4*x + C6.
def on_Eminus(point: tuple[Q, Q]) -> bool:
    x_coord, y_coord = point
    return y_coord**2 + x_coord * y_coord == x_coord**3 - C4 * x_coord + C6


Qpoints = [
    (Q(469572437338020), Q(8659141260066207245250)),
    (
        Q(7862279875666677393237, 17606416),
        Q(583152676543238826927776148008847, 73876521536),
    ),
    (Q(177864765470100), Q(343279086114405591450)),
    (
        Q(447490645354678560274980, 2884441849),
        Q(22220310008210701689236734902375750, 154914718384243),
    ),
]
assert all(on_Eminus(point) for point in Qpoints)

# U=4x, V=8y+4x gives V^2=(U-F0)(U-F1)(U-F2).
F0 = 660580041582000
F1 = 637703335220400
F2 = -1298283376802401


def to_monic_twist(point: tuple[Q, Q]) -> tuple[Q, Q]:
    x_coord, y_coord = point
    return 4 * x_coord, 8 * y_coord + 4 * x_coord


for point in Qpoints:
    U, V = to_monic_twist(point)
    assert V**2 == (U - F0) * (U - F1) * (U - F2)

Sminus = (Q(872269302587040), Q(10381666643412520725360))
Tminus = (Q(F1), Q(0))
for U, V in (Sminus, Tminus):
    assert V**2 == (U - F0) * (U - F1) * (U - F2)
assert double_point_short_generalized(
    Sminus,
    a2=Q(1),
    a4=Q(-A),
    a6=Q(B),
) == (Q(F0), Q(0))

# First-coordinate Kummer representatives for Q1,...,Q4,S^-,T^-.
twist_squareclasses = [
    2 * 3 * 5 * 41 * 113 * 233,
    3 * 7 * 73 * 113 * 233,
    2 * 3 * 7 * 73,
    -2 * 5 * 73 * 113 * 233,
    5 * 7 * 13 * 73 * 113 * 233,
]
for point, representative in zip(Qpoints, twist_squareclasses[:4]):
    U, _ = to_monic_twist(point)
    assert_square_class(U - F0, representative)
assert_square_class(Sminus[0] - F0, twist_squareclasses[4])
assert_square_class(Q(F1 - F0), -1)
twist_squareclasses.append(-1)


def twist_character_vector(rep: int) -> list[int]:
    return [
        valuation_parity_of_squarefree(rep, 2),
        valuation_parity_of_squarefree(rep, 5),
        valuation_parity_of_squarefree(rep, 41),
        valuation_parity_of_squarefree(rep, 7),
        sign_character(rep),
        valuation_parity_of_squarefree(rep, 13),
    ]


twist_kummer_matrix = [twist_character_vector(rep) for rep in twist_squareclasses]
assert rank_mod_2(twist_kummer_matrix) == 6


# ---------------------------------------------------------------------------
# 6. Exact reconstruction of the displayed triple (ancillary provenance)
# ---------------------------------------------------------------------------
v = Q(180, 6643)
L = 44129449
assert 1 - 4 * v**2 == Q(43999849, L)
assert 1 + 4 * v**2 == Q(44259049, L)

# Move P1 from E to F_v.
x1, y1 = P[0]
X1 = (x1 - R0) / L**2
Y1 = y1 / L**3
assert Y1**2 == X1**3 + 2 * (1 + 16 * v**4) * X1**2 + (1 - 16 * v**4) ** 2 * X1

# Dual 2-isogeny F_v -> D_v.
W = Y1**2 / X1**2
z = Y1 * ((1 - 16 * v**4) ** 2 - X1**2) / X1**2
assert z**2 == W * (W - 4) * (W - 64 * v**4)
assert W == Q(4293625223577600, 318418364406961)
assert z == Q(
    -16346043633252561844056883200,
    393628226387937104654720357,
)

r = (W - 2) / 2
tau = z / (2 * (r**2 - 1))
eta = r * tau**2 - 1
u = (tau**2 + 1 + eta) / (8 * v**2 * tau)

assert tau == Q(-257579450961, 396627408848)
assert eta == Q(
    37798484235380372589723575,
    26585947944961874728120576,
)
assert u == Q(-1229610544128, 1649489479)
assert eta**2 == tau**4 + (2 - 64 * v**4) * tau**2 + 1
assert u * (tau**2 + 1) == 4 * v**2 * tau * (u**2 + 1)

recovered_a = (tau * u + 1) / (tau - u)
recovered_b = -1 / recovered_a
recovered_c = 4 * tau * u / ((tau * u + 1) * (tau - u))
assert (recovered_a, recovered_b, recovered_c) == (a, b, c)


if __name__ == "__main__":
    print("All exact checks passed.")
    print("  triple: verified")
    print("  Q-isomorphism: verified coefficient-by-coefficient")
    print("  torsion: E[4] over Q(i), #E(F_17)=16, #E(F_29)=32")
    print("  Kummer ranks: 6 for E and 6 for its (-1)-twist")
    print("  conclusion: torsion = Z/4Z x Z/4Z and rank over Q(i) >= 8")
    print("  reconstruction of the triple from v=180/6643: verified")
