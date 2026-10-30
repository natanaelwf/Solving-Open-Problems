#!/usr/bin/env python3
"""Verify the exact finite arithmetic certificates for Dujella Problem 3.10.

Requires Python 3.9 or later and its standard library only.  Run this script in
the directory containing the four accompanying JSON files, or pass --data-dir.
No computer-algebra system, internet connection, PDF, or floating-point
approximation is used.  ``math.inf`` denotes an exact zero's infinite valuation.

The finite certificates establish the source curve's rank lower bound, the
reconstruction identities, the auxiliary 2-Selmer dimension, and its Cassels
pairing.  The auxiliary Mordell-Weil rank-one conclusion also uses the
global mathematical proof in the accompanying manuscript; this finite
arithmetic verifier does not formalize that proof.

All mathematical checks use explicit exceptions, so ``python -O`` cannot
disable certificate verification.  Cached fields are checked against values
recomputed from the primary integer/rational witnesses.
"""

import argparse
from fractions import Fraction
import json
from math import gcd, inf, isqrt, prod
from pathlib import Path
import sys


SOURCE_A = 4728112640493176179
SOURCE_B = -313185162402159696
ALPHA = 2836090012790868622112037290311559991949411485715
BETA = 2097621505422395657915349531407756829023138973264
PRINTED_PAIRING = [
    [int(bit) for bit in row]
    for row in (
        "001101110", "001011011", "110001010", "100011110",
        "010100010", "111100100", "100101000", "111110000",
        "010000000",
    )
]
FILES = (
    "arithmetic_data.json",
    "conic_certificates.json",
    "local_certificates.json",
    "cassels_pairing.json",
)


class VerificationError(Exception):
    """A mathematical or structural certificate check failed."""


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def integer(value, context):
    require(type(value) is int, context + ": expected an integer")
    return value


def rational(value):
    require(type(value) in (int, str), "A rational witness must be integer/string")
    return Fraction(value)


def valuation(value, prime):
    """Exact additive p-adic valuation; valuation(0,p) is infinity."""
    value = Fraction(value)
    if value == 0:
        return inf
    numerator, denominator = value.numerator, value.denominator
    result = 0
    while numerator % prime == 0:
        numerator //= prime
        result += 1
    while denominator % prime == 0:
        denominator //= prime
        result -= 1
    return result


def unit_residue(value, prime, modulus):
    value = Fraction(value)
    exponent = valuation(value, prime)
    require(exponent != inf, "A zero value has no multiplicative squareclass")
    unit = value / Fraction(prime) ** exponent
    require(gcd(unit.denominator, modulus) == 1, "Nonunit residue denominator")
    return unit.numerator * pow(unit.denominator, -1, modulus) % modulus


def local_squareclass(value, prime):
    """Encode Q_p^*/Q_p^{*2} by (p,-1,5) at 2, (p,nonresidue) otherwise."""
    exponent = valuation(value, prime)
    require(exponent != inf, "Zero cannot be encoded as a squareclass")
    if prime == 2:
        unit_bits = {1: 0, 7: 2, 5: 4, 3: 6}[unit_residue(value, 2, 8)]
        return exponent % 2 | unit_bits
    unit = unit_residue(value, prime, prime)
    legendre = pow(unit, (prime - 1) // 2, prime)
    require(legendre in (1, prime - 1), "Invalid Legendre symbol")
    return exponent % 2 | (2 if legendre == prime - 1 else 0)


def local_pair(first, second, prime):
    width = 3 if prime == 2 else 2
    return local_squareclass(first, prime) | local_squareclass(second, prime) << width


def parity(number):
    # int.bit_count is available only from Python 3.10; keep Python 3.9 support.
    return bin(number).count("1") & 1


def gf2_basis(vectors):
    """Gaussian elimination over F_2 using exact integer bit vectors."""
    pivots = {}
    for vector in vectors:
        require(type(vector) is int and vector >= 0, "Invalid binary vector")
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                vector ^= pivots[pivot]
            else:
                pivots[pivot] = vector
                break
    return pivots


def in_span(vector, basis):
    for pivot in sorted(basis, reverse=True):
        if vector >> pivot & 1:
            vector ^= basis[pivot]
    return vector == 0


def global_squareclass(value, primes):
    """Exact sign/prime parity encoding, with an exact square residual check."""
    value = Fraction(value)
    require(value != 0, "A global squareclass witness is zero")
    remainder = value.numerator * value.denominator
    bits = int(remainder < 0)
    remainder = abs(remainder)
    for index, prime in enumerate(primes, 1):
        while remainder % prime == 0:
            remainder //= prime
            bits ^= 1 << index
    require(isqrt(remainder) ** 2 == remainder,
            "An unlisted prime has odd valuation in a squareclass witness")
    return bits


def decode_squareclass(bits, primes):
    require(0 <= bits < 1 << (len(primes) + 1), "Squareclass bits out of range")
    result = -1 if bits & 1 else 1
    for index, prime in enumerate(primes, 1):
        if bits >> index & 1:
            result *= prime
    return result


def supported_integer(number, primes):
    """Check prime support, not merely its parity."""
    remainder = abs(number)
    require(remainder != 0, "A supported integer must be nonzero")
    for prime in primes:
        while remainder % prime == 0:
            remainder //= prime
    return remainder == 1


def square_rational(value):
    value = Fraction(value)
    return (value >= 0 and isqrt(value.numerator) ** 2 == value.numerator
            and isqrt(value.denominator) ** 2 == value.denominator)


def on_curve(point, first, second):
    x, y = map(Fraction, point)
    return y * y == x * (x + first) * (x + second)


def double_point(point, first, second):
    x, y = map(Fraction, point)
    require(y != 0, "Cannot use affine duplication at a point of order two")
    slope = (3 * x * x + 2 * (first + second) * x + first * second) / (2 * y)
    next_x = slope * slope - first - second - 2 * x
    return next_x, -y + slope * (x - next_x)


def verify_primes(data):
    """Complete recursive Lucas certificates, with every factor of n-1 proved."""
    certificates = data["prime_certificates"]
    require(type(certificates) is dict, "Prime certificates must form an object")
    proven, visiting = set(), set()

    def prove(number):
        integer(number, "Prime candidate")
        if number in proven:
            return
        require(number >= 2, "Prime candidate below two")
        require(number not in visiting, "Circular primality certificate")
        require(str(number) in certificates, "Missing primality certificate")
        certificate = certificates[str(number)]
        if number == 2:
            require(certificate == {}, "The base certificate must be the prime 2")
            proven.add(2)
            return
        visiting.add(number)
        factors = certificate["factors"]
        require(type(factors) is dict and factors, "Missing factorization of n-1")
        factorization = {}
        for raw_prime, exponent in factors.items():
            prime = int(raw_prime)
            integer(exponent, "Primality factor exponent")
            require(2 <= prime < number and exponent > 0, "Invalid primality factor")
            prove(prime)
            factorization[prime] = exponent
        require(prod(p ** e for p, e in factorization.items()) == number - 1,
                "Incomplete/incorrect factorization of n-1")
        witness = integer(certificate["a"], "Lucas witness")
        require(1 < witness < number, "Lucas witness out of range")
        require(pow(witness, number - 1, number) == 1, "Lucas Fermat identity failed")
        for prime in factorization:
            require(gcd(pow(witness, (number - 1) // prime, number) - 1, number) == 1,
                    "Lucas coprimality condition failed")
        visiting.remove(number)
        proven.add(number)

    for prime in data["source_primes"] + data["S"]:
        prove(prime)
    # Do not silently accept invalid, unused certificates in the delivered file.
    for raw_prime in certificates:
        prove(int(raw_prime))
    for key, expected_length in (("source_primes", 19), ("S", 29)):
        primes = data[key]
        require(primes == sorted(set(primes)) and len(primes) == expected_length,
                "Incorrect or duplicate primes in " + key)
    require(data["S"][0] == 2, "The local support must contain 2")
    print("PASS: {} recursive complete Lucas primality certificates.".format(len(proven)))


def verify_source_and_scaling(data):
    require((data["A"], data["B"], data["alpha"], data["beta"])
            == (SOURCE_A, SOURCE_B, ALPHA, BETA), "Curve coefficients differ from manuscript")
    first, second = data["A"], data["B"]
    require(first * second * (first - second) != 0, "Singular source cubic")
    points = data["points"]
    require(type(points) is list and len(points) == 11, "Expected eleven source points")
    primes, width = data["source_primes"], len(data["source_primes"]) + 1
    vectors = []
    for index, point in enumerate(points):
        require(len(point) == 2 and all(type(z) is int for z in point), "Malformed source point")
        require(on_curve(point, first, second), "Source point {} is off curve".format(index + 1))
        x, y = point
        require(y != 0, "A claimed free source point is 2-torsion")
        vectors.append(sum(global_squareclass(z, primes) << (width * j)
                           for j, z in enumerate((x, x + first, x + second))))
    torsion_triples = (
        (first * second, first, second),
        (-first, first * (first - second), second - first),
    )
    for triple in torsion_triples:
        require(square_rational(prod(triple)), "Invalid source torsion Kummer triple")
        vectors.append(sum(global_squareclass(z, primes) << (width * j)
                           for j, z in enumerate(triple)))
    require(len(gf2_basis(vectors)) == 13, "Source Kummer rank is not thirteen")

    point = (912833416575231921, -1757195268626559090518724150)
    half = (5761058741699892246, -18144092568468363333046645050)
    require(on_curve(point, first, second) and on_curve(half, first, second),
            "The source point/half does not satisfy the cubic")
    require(double_point(half, first, second) == point, "The source half is incorrect")
    x, y = point
    u, v, w = Fraction(x * (x + first), y), Fraction(x * (x + second), y), Fraction(y, x)
    require((u, v, w) == (-2930376694, -Fraction(7337240409411, 23554),
                          -Fraction(4887549804850, 2539)), "Incorrect u,v,w values")
    require((u * v, u * w, v * w, u * (w - v), v * (w - u))
            == (x, x + first, x + second, first, second), "Source identities failed")
    require(all(square_rational(z) and z != 0 for z in (u * v, u * w, v * w)),
            "The three source products are not nonzero rational squares")
    h, j, k = u - v - w, u - v + w, u + v - w
    c, d = w * (u - v) * k * k, v * (u - w) * j * j
    scale = Fraction(105, 59803606)
    require((c, d) == (scale * scale * ALPHA, scale * scale * BETA),
            "Auxiliary scaling failed")
    require(u * v * w * (u - v) * (u - w) * (v - w) * h * j * k * c * d * (c - d) != 0,
            "A reconstruction nondegeneracy condition failed")
    require(all(supported_integer(z, data["S"]) for z in (ALPHA, BETA, ALPHA - BETA)),
            "The support omits a bad prime of the auxiliary")
    # The curve-specific ordinary split-prime check, independent of cached data.
    prime = 19
    require(ALPHA * BETA * (ALPHA - BETA) % prime != 0, "Bad reduction at 19")
    count = 1 + sum(sum(y0 * y0 % prime == x0 * (x0 + ALPHA) * (x0 + BETA) % prime
                        for y0 in range(prime)) for x0 in range(prime))
    require(count == 20, "Incorrect point count at 19")
    print("PASS: eleven exact source points; Kummer rank 13, hence source rank >= 11.")
    print("PASS: source half, auxiliary scaling, nondegeneracy, and a_19 = 0.")


def verify_local_invariants(data):
    require(gcd(ALPHA, BETA) == 1 and ALPHA % 4 == 3 and valuation(BETA, 2) == 4,
            "The local invariants have incorrect initial congruences")
    c4 = 16 * (ALPHA * ALPHA - ALPHA * BETA + BETA * BETA)
    c6 = -64 * (ALPHA + BETA) ** 3 + 288 * (ALPHA + BETA) * ALPHA * BETA
    discriminant = 16 * ALPHA ** 2 * BETA ** 2 * (ALPHA - BETA) ** 2
    require(tuple(valuation(z, 2) for z in (c4, c6, discriminant)) == (4, 6, 12),
            "Incorrect two-adic invariant valuations")
    require((ALPHA + BETA + 1) % 4 == 0 and ALPHA * BETA % 16 == 0,
            "The good minus-one twist model is not integral")
    a2 = -(ALPHA + BETA + 1) // 4
    a4 = ALPHA * BETA // 16
    b2, b4, b8 = 1 + 4 * a2, 2 * a4, -a4 * a4
    new_discriminant = -b2 * b2 * b8 - 8 * b4 ** 3
    require(new_discriminant * 2 ** 12 == discriminant and new_discriminant % 2 == 1,
            "The minus-one twist discriminant is not the stated odd integer")
    require(valuation(c4 ** 3, 13) - valuation(discriminant, 13) == -4,
            "The non-CM j-invariant valuation is incorrect")
    nonsplit = []
    odd_root_product = 1
    for prime in data["S"]:
        if prime == 2:
            continue
        require(c4 % prime != 0 and discriminant % prime == 0,
                "An odd support prime is not multiplicative")
        tangent = BETA if ALPHA % prime == 0 else ALPHA if BETA % prime == 0 else -ALPHA
        residue = pow(tangent % prime, (prime - 1) // 2, prime)
        require(residue in (1, prime - 1), "Invalid tangent squareclass")
        local_root = -1 if residue == 1 else 1
        odd_root_product *= local_root
        if local_root == 1:
            nonsplit.append(prime)
    require(nonsplit == [23, 47, 89, 283, 4943, 8893, 23971, 1073681107, 354212181139],
            "The nonsplit-prime table is incorrect")
    require(odd_root_product == -1, "The product of odd local root numbers is incorrect")
    print("PASS: local invariant valuations, good minus-one twist, non-CM valuation, and odd root numbers.")


class Polynomial:
    """Minimal sparse Z[u,v,w,x] arithmetic for formal identity verification."""

    def __init__(self, terms):
        if type(terms) is int:
            terms = {(0, 0, 0, 0): terms}
        self.terms = {key: value for key, value in terms.items() if value}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Polynomial) else Polynomial(value)

    def __add__(self, other):
        result = self.terms.copy()
        for key, value in self.coerce(other).terms.items():
            result[key] = result.get(key, 0) + value
        return Polynomial(result)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        result = {}
        for left, a in self.terms.items():
            for right, b in self.coerce(other).terms.items():
                key = tuple(i + j for i, j in zip(left, right))
                result[key] = result.get(key, 0) + a * b
        return Polynomial(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        require(type(exponent) is int and exponent >= 0, "Invalid polynomial exponent")
        result, factor = Polynomial(1), self
        while exponent:
            if exponent & 1:
                result = result * factor
            factor = factor * factor
            exponent //= 2
        return result


def verify_reconstruction_polynomials():
    u, v, w, x = [Polynomial({tuple(int(i == j) for i in range(4)): 1}) for j in range(4)]
    h, j, k, capital_v = u - v - w, u - v + w, u + v - w, u * v * w
    c, d = w * (u - v) * k ** 2, v * (u - w) * j ** 2
    t, y_squared = x + v * w * j * k, x * (x + c) * (x + d)
    na = capital_v * ((4 * v * w - h ** 2) * t + 2 * capital_v * h * j * k)
    nb, nc, nd = na - u * t ** 2, na - v * t ** 2, na - w * t ** 2
    pairs_and_right_sides = (
        (na, nb, u ** 2 * v * w * t ** 2 * h ** 2 * x),
        (na, nc, u * v ** 2 * w * t ** 2 * j ** 2 * (x + c)),
        (na, nd, u * v * w ** 2 * t ** 2 * k ** 2 * (x + d)),
        (nb, nc, u * v * t ** 2 * x * (x + c)),
        (nb, nd, u * w * t ** 2 * x * (x + d)),
        (nc, nd, v * w * t ** 2 * (x + c) * (x + d)),
    )
    for index, (left, right, target) in enumerate(pairs_and_right_sides, 1):
        require(not (left * right + 4 * capital_v ** 2 * y_squared - target).terms,
                "Universal polynomial identity {} failed".format(index))
    print("PASS: all six universal reconstruction identities in Z[u,v,w,x].")


def verify_selmer(data):
    primes, witnesses = data["S"], data["local_witnesses"]
    width = len(primes) + 1
    require(width == 30 and len(witnesses) == len(primes), "Invalid Selmer data dimensions")
    rows = []
    for prime, local_witnesses in zip(primes, witnesses):
        vectors = []
        dimension = 3 if prime == 2 else 2
        for witness, cached_vector in local_witnesses:
            if witness == "T0":
                first, second = ALPHA * BETA, ALPHA
            elif witness == "Ta":
                first, second = -ALPHA, ALPHA * (ALPHA - BETA)
            else:
                integer(witness, "Local abscissa")
                require(witness * (witness + ALPHA) * (witness + BETA) != 0,
                        "A non-torsion local witness meets a root")
                require(local_squareclass(witness * (witness + ALPHA) * (witness + BETA), prime) == 0,
                        "Local abscissa does not lift to a Q_p-point at p={}".format(prime))
                first, second = witness, witness + ALPHA
            vector = local_pair(first, second, prime)
            require(vector == cached_vector, "Incorrect cached local Kummer vector")
            vectors.append(vector)
        require(len(vectors) == dimension and len(gf2_basis(vectors)) == dimension,
                "Local Kummer witnesses do not span at p={}".format(prime))
        local_width = 6 if prime == 2 else 4
        annihilator = gf2_basis([
            row for row in range(1, 1 << local_width)
            if all(parity(row & vector) == 0 for vector in vectors)
        ])
        require(len(annihilator) == local_width - dimension, "Incorrect local annihilator")
        generators = [-1] + primes
        images = ([local_pair(z, 1, prime) for z in generators]
                  + [local_pair(1, z, prime) for z in generators])
        for annihilator_row in annihilator.values():
            rows.append(sum(parity(annihilator_row & image) << i for i, image in enumerate(images)))
    # Since alpha > beta > 0, every real point has xi+alpha >= 0.
    # This is precisely the sign equation on the second global squareclass.
    require(ALPHA > BETA > 0, "Real Kummer condition has changed")
    rows.append(1 << width)
    row_basis = gf2_basis(rows)
    require(len(rows) == 60 and len(row_basis) == 51, "Global Selmer constraint rank is not 51")
    cached_rows = data["selmer_rows"]
    require(len(cached_rows) == len(rows), "Incorrect number of cached Selmer equations")
    cached_basis = gf2_basis(cached_rows)
    require(len(cached_basis) == 51 and all(in_span(row, row_basis) for row in cached_rows)
            and all(in_span(row, cached_basis) for row in rows), "Cached Selmer row space differs")
    kernel = data["kernel"]
    require(len(kernel) == 9 and len(gf2_basis(kernel)) == 9, "Invalid nine-vector Selmer basis")
    require(all(0 <= vector < 1 << (2 * width) for vector in kernel), "Selmer vector out of range")
    require(all(parity(row & vector) == 0 for row in rows for vector in kernel),
            "A displayed Selmer vector fails a local condition")
    triples = []
    mask = (1 << width) - 1
    for vector in kernel:
        first, second = vector & mask, vector >> width
        triple = [decode_squareclass(bits, primes) for bits in (first, second, first ^ second)]
        require(square_rational(prod(triple)), "Selmer triple product is not a square")
        triples.append(triple)
    require(triples == data["triples"], "Cached decoded Selmer triples differ")
    print("PASS: all local Kummer witnesses; 60 global equations of rank 51.")
    print("PASS: nine independent kernel vectors; dim_F2 Sel_2(F/Q) = 9.")
    return triples


def verify_conics(records, triples, primes):
    require(type(records) is list and len(records) == 27, "Expected twenty-seven conic certificates")
    tangents, seen = {}, set()
    for record in records:
        basis, conic = record["basis"], record["conic"]
        require(type(basis) is int and 0 <= basis < 9 and type(conic) is int and 0 <= conic < 3,
                "Conic indices out of range")
        require((basis, conic) not in seen, "Duplicate conic certificate")
        seen.add((basis, conic))
        d1, d2, d3 = triples[basis]
        coefficients = ([BETA - ALPHA, 0, d2, -d3],
                        [-BETA, -d1, 0, d3], [ALPHA, d1, -d2, 0])[conic]
        require(record["coeff"] == coefficients, "Incorrect conic coefficients")
        point = record["point"]
        require(len(point) == 4 and all(type(z) is int for z in point), "Invalid integral conic point")
        require(gcd(*point) == 1 and point[conic + 1] == 0, "Conic point is not primitive/normalized")
        require(sum(coefficient * coordinate ** 2 for coefficient, coordinate in zip(coefficients, point)) == 0,
                "A conic point does not satisfy its exact equation")
        raw_tangent = [coefficient * coordinate for coefficient, coordinate in zip(coefficients, point)]
        content = gcd(*raw_tangent)
        require(content > 0, "Zero conic tangent")
        tangent = [coefficient // content for coefficient in raw_tangent]
        require(record["content"] == content and record["tangent"] == tangent,
                "Incorrect primitive tangent normalization")
        require(gcd(*tangent) == 1, "Tangent is not primitive")
        require(supported_integer(content, primes), "Tangent content has an omitted prime factor")
        require(all(supported_integer(z, primes) for z in coefficients if z),
                "Conic coefficient has an omitted prime factor")
        tangents[basis, conic] = tangent
    require(len(seen) == 27, "A covering/conic pair is missing")
    print("PASS: 27 primitive rational conic points and exact normalized tangents.")
    print("PASS: all bad-prime and tangent-content support is contained in S.")
    return tangents


def hilbert_bit(first, second, prime):
    """Additive quadratic Hilbert symbol, computed exactly from rational inputs."""
    require(first != 0 and second != 0, "A Hilbert-symbol argument is zero")
    if prime == "inf":
        return int(first < 0 and second < 0)
    r, s = valuation(first, prime), valuation(second, prime)
    if prime == 2:
        u, v = unit_residue(first, 2, 8), unit_residue(second, 2, 8)
        return (((u - 1) // 2) * ((v - 1) // 2)
                + r * ((v * v - 1) // 8) + s * ((u * u - 1) // 8)) % 2
    u, v = unit_residue(first, prime, prime), unit_residue(second, prime, prime)
    u_bit = int(pow(u, (prime - 1) // 2, prime) == prime - 1)
    v_bit = int(pow(v, (prime - 1) // 2, prime) == prime - 1)
    return (r * s * ((prime - 1) // 2) + r * v_bit + s * u_bit) % 2


def cached_bound(bound):
    # The discovery JSON uses this sentinel solely for an exact zero error.
    return 1000000000 if bound == inf else bound


def finite_local_values(record, triple, forms):
    prime = record["prime"]
    x = rational(record["x"])
    radicands = [z / d for z, d in zip((x, x + ALPHA, x + BETA), triple)]
    require(all(radicands), "A local covering radicand is zero")
    roots = [rational(value) for value in record["roots"]]
    require(len(roots) == 3 and all(roots), "Invalid approximate local roots")
    errors = []
    for root, radicand in zip(roots, radicands):
        residual_order = valuation(root * root - radicand, prime)
        derivative_order = valuation(2 * root, prime)
        require(residual_order > 2 * derivative_order,
                "Hensel inequality failed at p={}".format(prime))
        # For a nonintegral root, scaling the variable to a unit gives exactly
        # the same displayed inequality and the same absolute error estimate.
        errors.append(inf if residual_order == inf else residual_order - derivative_order)
    require(record["root_error_bounds"] == [cached_bound(e) for e in errors],
            "Cached Hensel error estimates differ")
    values = [sum(coefficient * root for coefficient, root in zip(form, [Fraction(1)] + roots))
              for form in forms]
    bounds = [min(valuation(coefficient, prime) + error
                  for coefficient, error in zip(form, [inf] + errors) if coefficient)
              for form in forms]
    require([rational(value) for value in record["tangent_approximations"]] == values,
            "Cached tangent evaluations differ")
    require(record["tangent_error_bounds"] == [cached_bound(e) for e in bounds],
            "Cached tangent error estimates differ")
    for value, bound in zip(values, bounds):
        require(value != 0 and bound > valuation(value, prime) + (2 if prime == 2 else 0),
                "Tangent squareclass precision is insufficient at p={}".format(prime))
    return values


def real_local_values(record, triple, forms):
    x = rational(record["x"])
    radicands = [z / d for z, d in zip((x, x + ALPHA, x + BETA), triple)]
    require(all(value > 0 for value in radicands), "A real covering radicand is not positive")
    intervals = [[rational(value) for value in pair] for pair in record["root_intervals"]]
    require(len(intervals) == 3 and all(len(pair) == 2 for pair in intervals), "Invalid real root intervals")
    for (lower, upper), radicand in zip(intervals, radicands):
        require(lower < upper and (lower > 0 or upper < 0), "A real root interval meets zero")
        lower_square, upper_square = sorted((lower * lower, upper * upper))
        require(lower_square <= radicand <= upper_square,
                "Rational interval does not enclose a square root")
    signs = []
    for form in forms:
        lower, upper = Fraction(0), Fraction(0)
        for coefficient, (left, right) in zip(form, [(Fraction(1), Fraction(1))] + intervals):
            lower += coefficient * (left if coefficient >= 0 else right)
            upper += coefficient * (right if coefficient >= 0 else left)
        require(lower > 0 or upper < 0, "Real tangent interval does not avoid zero")
        signs.append(1 if lower > 0 else -1)
    require(record["tangent_signs"] == signs, "Cached real tangent signs differ")
    return signs


def verify_pairing(records, companion_matrix, data, triples, tangents):
    primes = data["S"]
    expected_keys = {(basis, prime) for basis in range(9) for prime in primes + ["inf"]}
    require(type(records) is list and len(records) == len(expected_keys), "Incorrect local-certificate count")
    matrix, seen, symbol_count = [[0] * 9 for _ in range(9)], set(), 0
    for record in records:
        basis, prime = record["basis"], record["prime"]
        key = basis, prime
        require(key in expected_keys and key not in seen, "Invalid or duplicate local certificate")
        seen.add(key)
        forms = [tangents[basis, index] for index in range(3)]
        values = (real_local_values(record, triples[basis], forms) if prime == "inf"
                  else finite_local_values(record, triples[basis], forms))
        contributions = []
        for target in triples:
            contribution = sum(hilbert_bit(value, coordinate, prime)
                               for value, coordinate in zip(values, target)) % 2
            symbol_count += 3
            contributions.append(contribution)
        require(record["contribution"] == contributions, "Cached local Hilbert-symbol sum differs")
        matrix[basis] = [entry ^ contribution for entry, contribution in zip(matrix[basis], contributions)]
    require(seen == expected_keys, "Missing local certificate")
    require(matrix == companion_matrix == data["displayed_pairing"] == PRINTED_PAIRING,
            "Recomputed global pairing differs from the printed matrix")
    require(all(matrix[i][i] == 0 and matrix[i][j] == matrix[j][i]
                for i in range(9) for j in range(9)), "Pairing is not alternating")
    rows = [sum(bit << j for j, bit in enumerate(row)) for row in matrix]
    require(len(gf2_basis(rows)) == 6, "Recomputed pairing rank is not six")
    indices = [0, 1, 2, 3, 4, 7]
    minor = [sum(matrix[i][j] << k for k, j in enumerate(indices)) for i in indices]
    require(len(gf2_basis(minor)) == 6, "The stated principal minor is singular")
    width = len(primes) + 1
    torsion_vectors = [
        global_squareclass(ALPHA * BETA, primes) | global_squareclass(ALPHA, primes) << width,
        global_squareclass(-ALPHA, primes) | global_squareclass(ALPHA * (ALPHA - BETA), primes) << width,
    ]
    for mask, target in zip((428, 393), torsion_vectors):
        reconstructed = 0
        for index, vector in enumerate(data["kernel"]):
            if mask >> index & 1:
                reconstructed ^= vector
        require(reconstructed == target, "Incorrect rational 2-torsion coordinate mask")
        require(all(parity(mask & row) == 0 for row in rows), "Rational 2-torsion is not in the radical")
    print("PASS: 261 finite local points with exact Hensel and tangent bounds.")
    print("PASS: nine real points with exact rational interval bounds.")
    print("PASS: {} recomputed Hilbert symbols; the printed 9 x 9 pairing has rank 6.".format(symbol_count))
    print("PASS: stated nonzero principal minor and both rational 2-torsion radical masks.")
    for row in matrix:
        print("  " + " ".join(map(str, row)))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent,
                        help="directory containing the four JSON certificates")
    arguments = parser.parse_args()
    try:
        loaded = [json.loads((arguments.data_dir / filename).read_text(encoding="utf-8")) for filename in FILES]
        data, conics, locals_, pairing = loaded
        verify_primes(data)
        verify_source_and_scaling(data)
        verify_local_invariants(data)
        verify_reconstruction_polynomials()
        triples = verify_selmer(data)
        tangents = verify_conics(conics, triples, data["S"])
        verify_pairing(locals_, pairing, data, triples, tangents)
    except (VerificationError, OSError, ValueError, TypeError, KeyError, IndexError, ZeroDivisionError) as error:
        print("FAIL: " + str(error), file=sys.stderr)
        return 1
    print()
    print("ALL FINITE CERTIFICATES VERIFIED.")
    print("Using the classical Kummer and Cassels-Tate theorems, these data give")
    print("rank F(Q) + corank(divisible Sha(F/Q)[2^infinity]) = 1,")
    print("and the finite quotient of Sha(F/Q)[2^infinity] is (Z/2Z)^6.")
    print("The finite arithmetic gives (rank, divisible corank) = (1,0) or (0,1).")
    print("The manuscript's global arithmetic proof excludes the second alternative")
    print("and proves rank F(Q) = 1 and finiteness of Sha(F/Q).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
