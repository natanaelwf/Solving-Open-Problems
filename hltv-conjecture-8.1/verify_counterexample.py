#!/usr/bin/env python3
"""Exact verifier for the binary counterexample to HLTV Conjecture 8.1.

The program uses only Python's standard library.  It computes the linear and
quadratic Ehrhart coefficients from the size/intersection formula extracted
from HLTV Theorem 5.9, obtains the second magic coefficient, and checks the
same quadratic coefficient by an independently organized decomposition into
single-subset and distinct unordered-pair contributions.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd, lcm

N = 64

EXPECTED_D = 6412392523020340906235606732442755625
EXPECTED_E1_NUMERATOR = 84101268979011751107052465864
EXPECTED_E1_DENOMINATOR = 18472920064106597929865025
EXPECTED_E2_NUMERATOR = -193646201997247551631094418128271824711443829132361876404898934
EXPECTED_MU2_NUMERATOR = -193646201997247551632920685189022495196874747990425072873781134
EXPECTED_L = 1182266884102822267511361600
EXPECTED_L_E1 = 5382481214656752070851357815296
EXPECTED_2L2_E2 = (
    -84420890718696909064557085070814931175194060075793190485334389180044538559905792
)


def parameter(j: int) -> int:
    """Return b_j for the alternating vector (1, 2)^32, using 1-based j."""
    if not 1 <= j <= N:
        raise ValueError(f"j must lie in [1, {N}]")
    return 1 if j % 2 else 2


def signed_weights() -> list[int]:
    """Compute the symmetric signed simplex weights y_1,...,y_N."""
    y = [0] * (N + 1)
    y[1] = parameter(1) - 1
    for s in range(2, N + 1):
        y[s] = sum(
            (-1) ** (s - j) * comb(s - 2, j - 2) * parameter(j)
            for j in range(2, s + 1)
        )
    return y


def harmonic_scaled(scale: int) -> list[int]:
    """Return scale * H_s as integers for 0 <= s <= N."""
    values = [0] * (N + 1)
    for s in range(1, N + 1):
        values[s] = values[s - 1] + scale // s
    return values


def kernel_scaled(
    s: int,
    r: int,
    h: int,
    scale: int,
    scaled_harmonics: list[int],
) -> int:
    """Return scale^2 K(s,r,h) exactly as an integer.

    K(s,r,h) is the sum of 1/(ac) over
      1 <= a <= s, 1 <= c <= r, a+c <= s+r-h.
    """
    union_size = s + r - h
    total = 0
    for a in range(1, s + 1):
        c_max = min(r, union_size - a)
        if c_max >= 1:
            total += (scale // a) * scaled_harmonics[c_max]
    return total


def kernel_scaled_direct(
    s: int,
    r: int,
    h: int,
    reciprocal_scaled: list[int],
) -> int:
    """Return scale^2 K(s,r,h) by direct summation over multiplicities."""
    union_size = s + r - h
    total = 0
    for a in range(1, s + 1):
        c_max = min(r, union_size - a)
        for c in range(1, c_max + 1):
            total += reciprocal_scaled[a] * reciprocal_scaled[c]
    return total


def ordered_pair_computation(y: list[int], scale: int) -> tuple[int, int]:
    """Return scale*e1 and 2*scale^2*e2 from the ordered-pair identity."""
    h_scaled = harmonic_scaled(scale)

    scale_e1 = sum(comb(N, s) * y[s] * h_scaled[s] for s in range(1, N + 1))

    two_scale2_e2 = 0
    for s in range(1, N + 1):
        choose_a = comb(N, s)
        for r in range(1, N + 1):
            weight = y[s] * y[r]
            if weight == 0:
                continue
            inner = 0
            h_min = max(0, s + r - N)
            h_max = min(s, r)
            for h in range(h_min, h_max + 1):
                pair_count = comb(s, h) * comb(N - s, r - h)
                k_scaled = kernel_scaled(s, r, h, scale, h_scaled)
                inner += pair_count * k_scaled
            two_scale2_e2 += choose_a * weight * inner

    return scale_e1, two_scale2_e2


def unordered_pair_computation(y: list[int], scale: int) -> int:
    """Return scale^2*e2 via single subsets and distinct unordered pairs."""
    h_scaled = harmonic_scaled(scale)
    reciprocal_scaled = [0] + [scale // value for value in range(1, N + 1)]

    # One active subset.  The t^2 coefficient of
    # binom(t*y+a-1, a) is y^2 H_{a-1}/a.
    scale2_e2 = 0
    for s in range(1, N + 1):
        one_subset_kernel = sum(
            reciprocal_scaled[a] * h_scaled[a - 1] for a in range(1, s + 1)
        )
        scale2_e2 += comb(N, s) * y[s] * y[s] * one_subset_kernel

    # Two distinct active subsets.  For s < r, choosing the smaller set first
    # gives each unordered pair exactly once.  When s = r and h < s, divide
    # the ordered count by two.
    for s in range(1, N + 1):
        for r in range(s, N + 1):
            weight = y[s] * y[r]
            if weight == 0:
                continue
            h_min = max(0, s + r - N)
            h_max = min(s, r)
            for h in range(h_min, h_max + 1):
                if s == r and h == s:
                    continue  # A = B, already included above.
                ordered_count = (
                    comb(N, s) * comb(s, h) * comb(N - s, r - h)
                )
                if s == r:
                    assert ordered_count % 2 == 0
                    pair_count = ordered_count // 2
                else:
                    pair_count = ordered_count
                k_scaled = kernel_scaled_direct(
                    s, r, h, reciprocal_scaled
                )
                scale2_e2 += pair_count * weight * k_scaled

    return scale2_e2


def main() -> None:
    scale = lcm(*range(1, N + 1))
    assert scale == EXPECTED_L

    y = signed_weights()
    assert y[1] == 0
    assert y[2] == 2
    for s in range(3, N + 1):
        assert y[s] == (-1) ** s * 2 ** (s - 3)

    scale_e1, two_scale2_e2 = ordered_pair_computation(y, scale)
    assert scale_e1 == EXPECTED_L_E1
    assert two_scale2_e2 == EXPECTED_2L2_E2

    scale2_e2_independent = unordered_pair_computation(y, scale)
    assert 2 * scale2_e2_independent == two_scale2_e2

    e1 = Fraction(scale_e1, scale)
    e2 = Fraction(two_scale2_e2, 2 * scale * scale)
    mu2 = e2 - (N - 1) * e1 + comb(N, 2)

    assert e1 == Fraction(EXPECTED_E1_NUMERATOR, EXPECTED_E1_DENOMINATOR)
    assert e2 == Fraction(EXPECTED_E2_NUMERATOR, EXPECTED_D)
    assert mu2 == Fraction(EXPECTED_MU2_NUMERATOR, EXPECTED_D)

    # Independent closed form for e1 when n is even.
    h_n = Fraction(sum(scale // j for j in range(1, N + 1)), scale)
    h_half = Fraction(sum(scale // j for j in range(1, N // 2 + 1)), scale)
    e1_closed = Fraction(N * (9 * N - 7), 8) + Fraction(2 * h_n - h_half, 8)
    assert e1_closed == e1

    assert e2 < 0
    assert mu2 < 0
    assert e2.denominator == EXPECTED_D
    assert mu2.denominator == EXPECTED_D
    assert gcd(abs(e2.numerator), EXPECTED_D) == 1
    assert gcd(abs(mu2.numerator), EXPECTED_D) == 1
    assert len(str(abs(e2.numerator))) == 63
    assert len(str(abs(mu2.numerator))) == 63

    print("All exact checks passed.")
    print(f"n = {N}")
    print(f"L = {scale}")
    print(f"e1 = {e1}")
    print(f"e2 = {e2}")
    print(f"mu2 = {mu2}")
    print(f"gcd(|numerator(e2)|, D) = {gcd(abs(e2.numerator), EXPECTED_D)}")
    print(f"gcd(|numerator(mu2)|, D) = {gcd(abs(mu2.numerator), EXPECTED_D)}")


if __name__ == "__main__":
    main()
