# Two 63-Digit Integer Certificates for a Binary Parking-Function Polytope

## An exact counterexample to HLTV Conjecture 8.1

**Publication date:** 25 November 2026  
**Status:** Complete counterexample  
**Field:** Enumerative combinatorics, Ehrhart theory, generalized parking-function polytopes

## Abstract

For the 64-dimensional generalized parking-function polytope with alternating binary parameter vector

```math
\mathbf{b}=(1,2,1,2,\ldots,1,2)=(1,2)^{32},
```

we compute the quadratic ordinary Ehrhart coefficient $e_2$ and the quadratic coefficient $\mu_2$ in the magic basis. Both are negative rational numbers whose reduced numerators have 63 decimal digits. The inequality $\mu_2\lt0$ is an explicit counterexample to Conjecture 8.1 of Hill, Luo, Trinh, and Vindas-Meléndez, which proposes magic positivity for every positive parameter vector in every dimension at least three. The inequality $e_2\lt0$ also shows that this polytope is not Ehrhart positive. The calculation follows from their Theorem 5.9 and uses only finite sums and exact rational arithmetic. A standard-library Python verifier reproduces the coefficients by two independently organized computations.

**Keywords:** parking functions; Ehrhart polynomials; magic positivity; generalized permutahedra; exact arithmetic.

## 1. Statement of the counterexample

Let

```math
n=64,
\qquad
\mathbf{b}=(1,2,1,2,\ldots,1,2)=(1,2)^{32}.
```

For a positive integer vector $\mathbf{b}=(b_1,\ldots,b_n)$, a $\mathbf{b}$-parking function is a positive integer vector $\boldsymbol\beta=(\beta_1,\ldots,\beta_n)$ whose nondecreasing rearrangement satisfies

```math
\beta_i'\le b_1+\cdots+b_i
\qquad
(1\le i\le n).
```

The generalized parking-function polytope $\mathfrak{X}_n(\mathbf{b})$ is the convex hull of all such vectors. Write its Ehrhart polynomial and its degree-$n$ magic expansion as

```math
\begin{aligned}
E_{\mathbf{b}}(t)
&=\#\bigl(t\mathfrak{X}_n(\mathbf{b})\cap\mathbb{Z}^n\bigr)\\
&=\sum_{j=0}^{n}e_jt^j\\
&=\sum_{i=0}^{n}\mu_it^i(1+t)^{n-i}.
\end{aligned}
```

Magic positivity means $\mu_i\ge0$ for every $i$. HLTV Conjecture 8.1 asserts this property for every $\mathbf{b}\in\mathbb{Z}_{\gt0}^n$ with $n\ge3$.

Define the exact integers

```text
D    = 6412392523020340906235606732442755625
N_mu = -193646201997247551632920685189022495196874747990425072873781134
N_e  = -193646201997247551631094418128271824711443829132361876404898934
```

**Theorem 1.** For $n=64$ and $\mathbf{b}=(1,2)^{32}$,

```math
\mu_2=\frac{N_\mu}{D}\lt0,
\qquad
e_2=\frac{N_e}{D}\lt0.
```

Both fractions are in lowest terms. Each numerator is a negative integer with 63 decimal digits. These integers are the reduced numerators of rational coefficients, not integer-valued coefficients and not values obtained from an optional rescaling.

The first inequality disproves HLTV Conjecture 8.1. The second independently rules out nonnegative ordinary Ehrhart coefficients. Indeed, every basis polynomial $t^i(1+t)^{n-i}$ has nonnegative ordinary coefficients, so magic positivity would imply $e_2\ge0$.

## 2. The signed simplex formula

Translation by the integer vector $\mathbf 1=(1,\ldots,1)$ preserves the Ehrhart polynomial. Put

```math
P=\mathfrak{X}_n(\mathbf{b})-\mathbf 1.
```

For each nonempty subset $A\subseteq[n]$, let

```math
\Delta_A^0=\operatorname{conv}\bigl(0,e_i:i\in A\bigr),
```

where the $e_i$ are the standard basis vectors. For the present vector, $P$ contains $0,e_1,\ldots,e_{64}$, so its dimension is 64. The degree-64 magic basis therefore has the correct dimension.

The symmetric signed simplex weights are

```math
\begin{aligned}
y_1&=b_1-1,\\
y_s&=\sum_{j=2}^{s}(-1)^{s-j}
\binom{s-2}{j-2}b_j
\qquad (s\ge2).
\end{aligned}
```

Thus

```math
P=\sum_{\emptyset\ne A\subseteq[n]}
y_{\lvert A\rvert}\Delta_A^0
```

as a signed Minkowski representation. The coefficients need not be nonnegative.

Let $\mathcal{D}(n)$ be the finite set of nonnegative integer vectors $\alpha=(\alpha_A)$, indexed by nonempty subsets of $[n]$, such that

```math
\sum_{A\in\mathcal J}\alpha_A
\le
\left\lvert\bigcup_{A\in\mathcal J}A\right\rvert
```

for every nonempty collection $\mathcal J$ of nonempty subsets.

HLTV Theorem 5.9 gives the following polynomial identity.

**Formula (1).**

```math
E_{\mathbf{b}}(t)
=
\sum_{\alpha\in\mathcal{D}(n)}
\prod_{\emptyset\ne A\subseteq[n]}
\binom{t y_{\lvert A\rvert}+\alpha_A-1}{\alpha_A}.
```

Each binomial expression is interpreted as a polynomial, with value $1$ when $\alpha_A=0$. The theorem applies to the signed weights here: the formula is first established in the nonnegative case and then extended by polynomiality. No positivity assumption is imposed on the alternating weights.

## 3. Extracting only the first two nonconstant coefficients

Write

```math
H_s=\sum_{j=1}^{s}\frac{1}{j},
\qquad
H_0=0.
```

For an integer $a\ge1$,

**Formula (2).**

```math
\binom{ty+a-1}{a}
=
\frac{y}{a} t
+
\frac{y^2H_{a-1}}a t^2
+
O(t^3).
```

Every active subset, meaning a subset with $\alpha_A\gt0$, contributes at least one power of $t$. Therefore the linear coefficient uses only one active subset, while the quadratic coefficient uses at most two.

For one active subset of size $s$, the admissible multiplicity satisfies $1\le a\le s$. There are $\binom{n}{s}$ subsets of size $s$, so

**Formula (3).**

```math
 e_1
 =
 \sum_{s=1}^{n}
 \binom{n}{s} y_sH_s.
```

For two distinct active subsets $A$ and $B$, set

```math
s=\lvert A\rvert,
\qquad
r=\lvert B\rvert,
\qquad
h=\lvert A\cap B\rvert.
```

Their multiplicities satisfy exactly

```math
1\le a\le s,
\qquad
1\le c\le r,
\qquad
a+c\le s+r-h.
```

Define

```math
K(s,r,h)
=
\sum_{\substack{
1\le a\le s,\ 1\le c\le r\\
a+c\le s+r-h
}}
\frac{1}{ac}.
```

The one-subset quadratic contribution is included as the diagonal of an ordered-pair sum because

```math
K(s,s,s)
=
\sum_{a+c\le s}\frac{1}{ac}
=
2\sum_{a=1}^{s}\frac{H_{a-1}}{a}.
```

There are

```math
\binom{n}{s}\binom{s}{h}\binom{n-s}{r-h}
```

ordered pairs with the specified sizes and intersection. Formulas (1) and (2) therefore give the exact finite identity

**Formula (4).**

```math
\begin{aligned}
e_2
={}&\frac{1}{2}
\sum_{s=1}^{n}\sum_{r=1}^{n}
\binom{n}{s} y_sy_r\\
&\quad\cdot
\sum_{h=\max(0,s+r-n)}^{\min(s,r)}
\binom{s}{h}\binom{n-s}{r-h}K(s,r,h).
\end{aligned}
```

This formula uses only subset sizes, intersection sizes, binomial coefficients, and finite reciprocal sums. It does not require constructing the exponentially large family of subsets.

Comparing the first three ordinary coefficients of the magic expansion gives

```math
\mu_0=1,
\qquad
e_1=n+\mu_1,
\qquad
e_2=\binom{n}{2}+(n-1)\mu_1+\mu_2.
```

Consequently,

**Formula (5).**

```math
\mu_2=e_2-(n-1)e_1+\binom{n}{2}.
```

## 4. Specialization to the alternating binary vector

For

```math
b_j=\frac{3+(-1)^j}{2},
```

the finite differences simplify to

**Formula (6).**

```math
\begin{aligned}
y_1&=0,\\
y_2&=2,\\
y_s&=(-1)^s2^{s-3}
\qquad (3\le s\le64).
\end{aligned}
```

For $s\ge3$, the constant part of $b_j$ has zero finite difference, while the alternating part contributes

```math
\frac{1}{2}(-1)^s
\sum_{j=2}^{s}\binom{s-2}{j-2}
=
(-1)^s2^{s-3}.
```

Substitution into Formulas (3) and (4) gives

```math
 e_1
 =
 \frac{84101268979011751107052465864}
 {18472920064106597929865025}
```

and the value of $e_2$ stated in Theorem 1. Since $n=64$, Formula (5) becomes

```math
\mu_2=e_2-63e_1+2016,
```

which gives the stated value of $\mu_2$.

There is also an independent closed form for the linear coefficient. For even $n$ and the same alternating binary vector,

**Formula (7).**

```math
 e_1
 =
 \frac{n(9n-7)}{8}
 +
 \frac{2H_n-H_{n/2}}{8}.
```

At $n=64$, Formula (7) agrees exactly with the fraction above.

## 5. Integer arithmetic certificate

Set

```math
L=\operatorname{lcm}(1,2,\ldots,64)
=1182266884102822267511361600.
```

Every harmonic number in Formula (3) can be represented with denominator dividing $L$, and every kernel in Formula (4) with denominator dividing $L^2$. Exact integer summation gives

```text
L * e1 = 5382481214656752070851357815296

2 * L^2 * e2 =
-84420890718696909064557085070814931175194060075793190485334389180044538559905792
```

Reducing these fractions and applying Formula (5) gives the coefficients in Theorem 1. The exact coprimality checks are

```math
\gcd(\lvert N_\mu\rvert,D)
=
\gcd(\lvert N_e\rvert,D)
=1.
```

Therefore $D$ is the reduced positive denominator of both coefficients.

The accompanying verifier computes Formula (4) as an ordered-pair sum. It then recomputes the quadratic coefficient by separating the single-subset contribution from the contribution of distinct unordered pairs, with the diagonal handled independently. Both organizations produce the same $e_2$, and the script also verifies the closed form in Formula (7).

## 6. Exact verification

The verifier uses only Python's standard library and exact integers and fractions.

```text
python verify_counterexample.py
```

It checks all of the following:

1. the finite-difference formula for every weight $y_s$;
2. the exact values of $L e_1$ and $2L^2e_2$;
3. agreement between the ordered-pair and unordered-pair computations of $e_2$;
4. the reduced fractions for $e_1$, $e_2$, and $\mu_2$;
5. the independent closed form for $e_1$;
6. the two gcd certificates, negativity, and the 63-digit numerator counts.

A successful run ends with

```text
All exact checks passed.
n = 64
L = 1182266884102822267511361600
e1 = 84101268979011751107052465864/18472920064106597929865025
e2 = -193646201997247551631094418128271824711443829132361876404898934/6412392523020340906235606732442755625
mu2 = -193646201997247551632920685189022495196874747990425072873781134/6412392523020340906235606732442755625
gcd(|numerator(e2)|, D) = 1
gcd(|numerator(mu2)|, D) = 1
```

The complete program is available in [`verify_counterexample.py`](verify_counterexample.py).

## 7. Interpretation and scope

The counterexample uses 64 parameters, each equal to either 1 or 2. The large signed weights in Formula (6) arise from finite differences of this simple vector. The 63-digit numerators appear only after the exact reciprocal sums are reduced.

No claim is made that 64 is the minimum possible dimension for an alternating binary counterexample. The displayed integers are not discriminants and are not integer Ehrhart or magic coefficients. This argument also does not assert failure of real-rootedness of an Ehrhart $h^*$-polynomial. The complete obstruction used here is the negativity of $e_2$ and $\mu_2$.

## Primary reference

Charlie Hill, Ambrose Luo, Vu Trinh, and Andrés R. Vindas-Meléndez, [*Lattice slices, Ehrhart polynomials, and magic positivity of generalized parking-function polytopes*](https://arxiv.org/abs/2607.15503v1), arXiv:2607.15503v1, 16 July 2026. The conjecture refuted here is Conjecture 8.1, and the signed-simplex Ehrhart formula used in Formula (1) is Theorem 5.9.
