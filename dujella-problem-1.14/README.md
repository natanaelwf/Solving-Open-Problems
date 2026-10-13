# Degree-Uniform Bounds for Polynomial Diophantine Tuples

## A complete solution to Dujella's Problem 1.14

**Publication date:** 13 October 2026  
**Status:** Complete solution  
**Field:** Number theory, polynomial Diophantine tuples, polynomial rings

## Abstract

Let $n\in\mathbb Z[x]\setminus\lbrace 0\rbrace$ and let $A$ be a finite set of distinct nonzero integer-coefficient polynomials such that $ab+n$ is a square in $\mathbb Z[x]$ whenever $a\ne b$ belong to $A$. We use the standard polynomial convention that there is no nonzero $p\in\mathbb Z[x]$ for which every $a/p$ and $n/p^2$ is an integer. This excludes a common polynomial scaling of a tuple of integer constants.

For $d=\deg n\ge1$, we prove

```math
|A|
\le
\binom{2^d+d+1}{d+1}
+2^{2d+1}
+6d^2+4d+23.
```

The final constant is $21$, rather than $23$, when $n$ is not a square in $\mathbb C[x]$. Pairing complementary factorization families further shows that every $D(n)$-set in $\mathbb Z[x]$ with cubic $n$ has at most $646$ elements, without a separate nondegeneracy assumption. This gives a degree-only bound for the polynomial formulation of Dujella's Problem 1.14. The proof combines an explicit polynomial separator for squares, two finite-dimensional rank arguments, a factorization analysis of the exceptional diagonal, and Dujella's uniform bound for large elements of integer Diophantine tuples. We also identify exactly why admitting polynomial scalings of integer tuples changes the question.

**Keywords:** polynomial Diophantine tuples; degree-uniform bounds; polynomial method; squares in polynomial rings.

## 1. The problem, conventions, and main result

Problem 1.14 asks for an upper bound for the cardinality of polynomial $D(n)$-tuples that depends only on $\deg n$, and singles out cubic $n$. We establish such a bound for every degree. Since the distinction between the standard polynomial problem and the unrestricted ring-theoretic problem is material, we begin with the precise convention.

For a commutative ring $R$, write

```math
\mathrm{Sq}(R)=\lbrace r^2:r\in R\rbrace.
```

Zero is therefore a square. All tuple entries below are nonzero, but a square root of $ab+n$ is allowed to be zero.

**Definition 1.1.** Let $n\in\mathbb Z[x]\setminus\lbrace0\rbrace$. A $D(n)$-set in $\mathbb Z[x]$ is a finite nonempty set $A\subset\mathbb Z[x]\setminus\lbrace0\rbrace$ such that:

**Equation (1.1).**

```math
ab+n\in\mathrm{Sq}(\mathbb Z[x])
\qquad
(a,b\in A,\ a\ne b).
```

It is called a polynomial $D(n)$-tuple if, in addition:

**Condition (ND).**

```math
\nexists\,p\in\mathbb Z[x]\setminus\lbrace0\rbrace
\quad\text{such that}\quad
\frac{a}{p}\in\mathbb Z\ \text{for every }a\in A,
\qquad
\frac{n}{p^2}\in\mathbb Z.
```

Membership in $\mathbb Z$ means that the quotient is a constant integer, not merely a polynomial with integer coefficients.

Condition (ND) is part of the standard definition used by Dujella, Fuchs and Tichy, and it is also explicit in Dujella's formulation for polynomials. We use the term $D(n)$-set when that condition is not imposed. No positivity condition on the entries or their leading coefficients is assumed. Constants are permitted among the entries. An integer $D(N)$-set is defined by the analogous pairwise square condition on distinct nonzero integers. Whenever positivity is required, it will be stated explicitly.

When $\deg n$ is odd, Condition (ND) is automatic. Indeed, an identity $n=Np^2$ with a nonzero constant $N$ would force

```math
\deg n=2\deg p.
```

When $n$ is a nonzero constant, Condition (ND) is equivalent to requiring at least one nonconstant entry.

For $d\ge1$, define

**Equation (1.2).**

```math
\begin{aligned}
B(d)
&=\binom{2^d+d+1}{d+1}
+2^{2d+1}
+6d^2+4d+23,\\
B(0)&=22.
\end{aligned}
```

**Theorem 1.2 (Degree-uniform bound).** Let $n\in\mathbb Z[x]\setminus\lbrace0\rbrace$, let $d=\deg n$, and let $A$ be a polynomial $D(n)$-tuple in the sense of Definition 1.1. Then

```math
|A|\le B(d).
```

For $d\ge1$, the more precise estimate is:

**Equation (1.3).**

```math
|A|
\le
\binom{2^d+d+1}{d+1}
+2^{2d+1}
+6d^2+4d+21+2\delta(n),
```

where

```math
\delta(n)=
\begin{cases}
1,&n\in\mathrm{Sq}(\mathbb C[x]),\\
0,&n\notin\mathrm{Sq}(\mathbb C[x]).
\end{cases}
```

The estimate is independent of the coefficients of $n$ and of both the coefficients and the degrees of the entries of $A$.

**Corollary 1.3 (Cubic case).** Let $n\in\mathbb Z[x]$ have degree three. Every $D(n)$-set $A\subset\mathbb Z[x]\setminus\lbrace0\rbrace$ satisfies

```math
|A|\le646.
```

This conclusion requires neither Condition (ND) as an additional hypothesis nor any assumption on the roots of $n$.

**Proof.** An odd-degree polynomial is not a square in $\mathbb C[x]$, and Condition (ND) is automatic. Using the sharper exceptional-diagonal bound in Corollary 4.10 in the partition from Section 6.1, together with Proposition 3.4, Corollary 5.2, and Proposition 2.2, gives

```math
\begin{aligned}
|A|
&\le\binom{12}{4}+64+6\cdot3^2+4\cdot3+21\\
&=495+64+66+21\\
&=646.
\end{aligned}
```

Degree-only bounds for linear parameters were established by Dujella, Fuchs and Tichy and sharpened by Dujella, Fuchs and Walsh. Jurasić obtained the bound $98$ for quadratic parameters. The estimate $22$ for constant parameters already follows from Dujella's large-element theorem, as noted in the earlier polynomial work. Our purpose is uniformity in arbitrary degree, not an improvement of sharper bounds available in particular small degrees.

The exclusion in Condition (ND) cannot be silently omitted. If $\lbrace b_1,\ldots,b_m\rbrace$ is an integer $D(N)$-tuple, then:

**Equation (1.4).**

```math
\lbrace b_1x,\ldots,b_mx\rbrace
\quad\text{is a }D(Nx^2)\text{-set in }\mathbb Z[x].
```

Thus the unrestricted degree-two question contains the problem of uniformly bounding integer $D(N)$-tuples independently of $N$. Section 7 makes this relationship exact. Theorem 1.2 answers Problem 1.14 with the standard polynomial convention. It does not assert a bound for the additional scalar-lift class. The cubic conclusion has no such qualification.

### Structure of the proof

Dujella's integer theorem controls entries of degree greater than $3d$. A formal-square-root Gram matrix controls each fixed degree between $d+1$ and $3d$. For degrees at most $d$, a polynomial rank argument controls the entries for which $a^2+n$ is not a square over $\mathbb C$. The remaining entries satisfy a factorization of $n$ and belong to finitely many one-parameter families. We bound the intersection of each nonconstant family with the tuple and handle the only possible scalar family with a rational-function square-shift lemma.

## 2. Entries of sufficiently large degree

We use one arithmetic result concerning integer Diophantine tuples.

**Theorem 2.1 (Dujella's large-element bound).** Let $N\in\mathbb Z\setminus\lbrace0\rbrace$, and let $T$ be a finite set of distinct positive integers such that $uv+N$ is an integer square for distinct $u,v\in T$. Then

```math
\left|\lbrace u\in T:u\ge|N|^3\rbrace\right|\le21.
```

The constant is uniform in $N$, including negative $N$.

**Proposition 2.2.** Let $n\in\mathbb Z[x]\setminus\lbrace0\rbrace$ have degree $d\ge0$, and let $A$ be any $D(n)$-set in $\mathbb Z[x]$. Then:

**Equation (2.1).**

```math
\left|\lbrace a\in A:\deg a\gt3d\rbrace\right|\le21.
```

**Proof.** Let $H$ be the set on the left. There is nothing to prove if $|H|\le1$. Otherwise, for distinct $a,b\in H$, we have $\deg(ab)\gt d$, so the leading coefficient of the square $ab+n$ is

```math
\mathrm{lc}(a)\mathrm{lc}(b)\gt0.
```

Hence all leading coefficients of elements of $H$ have the same sign. Replacing every member of $H$ by its negative, if necessary, preserves all pairwise products and makes these leading coefficients positive.

For every sufficiently large positive integer $t$, the values $a(t)$, with $a\in H$, are positive and pairwise distinct, and $n(t)\ne0$. Furthermore,

```math
\frac{a(t)}{|n(t)|^3}\longrightarrow+\infty
\qquad
(t\longrightarrow+\infty),
```

because $\deg a\gt3d$. The assertion also holds for $d=0$. Choose one integer $t$ for which all these conditions hold simultaneously. Then

```math
\lbrace a(t):a\in H\rbrace
```

is a positive-integer $D(n(t))$-tuple whose every entry exceeds $|n(t)|^3$. Theorem 2.1 gives $|H|\le21$.

The chosen specialization may depend on the entire tuple. No uniform bound for its size is required because Theorem 2.1 is uniform in the resulting integer $n(t)$.

## 3. Polynomial separators and the nonexceptional diagonal

For a nonnegative integer $r$, let

```math
V_r=\mathbb C[x]_{\le r}
```

denote the vector space of polynomials of degree at most $r$, including zero. We identify it with $\mathbb C^{r+1}$ by its coefficient vector. A polynomial function on $V_r$ means a polynomial in these coefficients. All degree bounds for such functions refer to total degree in the coefficient variables.

**Lemma 3.1 (A separator for squares).** Let $L\ge1$, and let $F_1,\ldots,F_s\in V_{2L}$ be a finite nonempty collection of polynomials that are not squares in $\mathbb C[x]$. There exists a polynomial function $Q$ on $V_{2L}$, of degree at most $2^L$, such that:

**Equation (3.1).**

```math
Q(R^2)=0
\quad(R\in V_L),
\qquad
Q(F_i)\ne0
\quad(1\le i\le s).
```

**Proof.** Choose distinct complex numbers $t_0,\ldots,t_L$ at which none of the $F_i$ vanishes. For a fixed $i$, every choice of square roots of the $L+1$ values

```math
F_i(t_0),\ldots,F_i(t_L)
```

determines a unique interpolation polynomial $R\in V_L$. For every such choice, $R^2-F_i$ is nonzero because $F_i$ is not a square. There are only finitely many of these nonzero polynomials as $i$ and the square-root choices vary. We may therefore choose a further point $t_{L+1}$, distinct from the previous points, at which none of them vanishes.

For these $L+2$ points, define

```math
c_j=
\left(
\prod_{\substack{0\le h\le L+1\\h\ne j}}
(t_j-t_h)
\right)^{-1}
\qquad
(0\le j\le L+1).
```

The coefficient of $x^{L+1}$ in the Lagrange interpolation formula shows that:

**Equation (3.2).**

```math
\sum_{j=0}^{L+1}c_jR(t_j)=0
\qquad
(R\in V_L).
```

Conversely, prescribed values at these $L+2$ points come from an element of $V_L$ if this relation holds. Indeed, the interpolant of degree at most $L+1$ then has vanishing leading coefficient.

Consider the polynomial:

**Equation (3.3).**

```math
\Phi(Y_0,\ldots,Y_{L+1})
=
\prod_{\varepsilon\in\lbrace1,-1\rbrace^{L+1}}
\left(
 c_{L+1}Y_{L+1}
 +\sum_{j=0}^{L}\varepsilon_jc_jY_j
\right).
```

It has $2^{L+1}$ linear factors. Changing the sign of $Y_j$, for $j\le L$, permutes the factors. Changing the sign of $Y_{L+1}$ also permutes them after multiplying each factor by $-1$, and the number of factors is even. Thus $\Phi$ is invariant under each individual sign change. Every exponent in every monomial of $\Phi$ is consequently even, so there is a homogeneous polynomial $\Psi$ of degree $2^L$ such that

```math
\Phi(Y_0,\ldots,Y_{L+1})
=
\Psi(Y_0^2,\ldots,Y_{L+1}^2).
```

Set

```math
Q(F)=\Psi\bigl(F(t_0),\ldots,F(t_{L+1})\bigr).
```

Since evaluations are linear in the coefficients of $F$, this is a polynomial function of degree at most $2^L$.

If $F=R^2$ with $R\in V_L$, substitute $Y_j=R(t_j)$ into Equation (3.3). The factor with every $\varepsilon_j=1$ vanishes by Equation (3.2), so $Q(R^2)=0$.

If $Q(F_i)=0$, choose any square roots $Y_j$ of $F_i(t_j)$. A vanishing factor in Equation (3.3) supplies signs such that the signed first $L+1$ values and the last value satisfy Equation (3.2). They are therefore the values of an element $R\in V_L$. This is one of the interpolation polynomials considered when choosing $t_{L+1}$, but it satisfies

```math
R(t_{L+1})^2=F_i(t_{L+1}),
```

a contradiction. Hence $Q(F_i)\ne0$.

**Remark 3.2.** The separator depends on the prescribed finite collection, but its degree does not. We do not need one fixed equation separating every nonsquare from the square locus. This distinction permits the simultaneous nonvanishing needed in the following rank argument.

**Lemma 3.3 (Coefficient-space rank bound).** Let $P(u,v)$ be a polynomial in two vectors $u,v\in\mathbb C^r$ whose degree in the $u$-variables is at most $E$. Suppose $u_1,\ldots,u_m\in\mathbb C^r$ satisfy

```math
P(u_i,u_j)=0
\quad(i\ne j),
\qquad
P(u_i,u_i)\ne0.
```

Then

```math
m\le\binom{r+E}{r}.
```

**Proof.** Write

```math
P(u,v)=\sum_{|\alpha|\le E}u^\alpha p_\alpha(v).
```

Each summand contributes a matrix of rank at most one to

```math
\bigl(P(u_i,u_j)\bigr)_{i,j}.
```

Its rank is therefore at most the number of monomials in $r$ variables of degree at most $E$, namely $\binom{r+E}{r}$. The same matrix is diagonal with all diagonal entries nonzero, so its rank is $m$.

From now on, until Section 6, assume $d=\deg n\ge1$. For a $D(n)$-set $A$, define its exceptional diagonal set by:

**Equation (3.4).**

```math
S=\lbrace a\in A:a^2+n\in\mathrm{Sq}(\mathbb C[x])\rbrace.
```

The use of $\mathbb C[x]$ is deliberate. Pairwise squares in $\mathbb Z[x]$ remain squares over $\mathbb C$, and our separator detects precisely the complex square locus.

**Proposition 3.4.** For every $D(n)$-set $A$, the set

```math
U=\lbrace a\in A:\deg a\le d,\ a\notin S\rbrace
```

satisfies:

**Equation (3.5).**

```math
|U|\le\binom{2^d+d+1}{d+1}.
```

**Proof.** The assertion is immediate if $U$ is empty. Otherwise apply Lemma 3.1, with $L=d$, to the polynomials $a^2+n$ for $a\in U$. Let $Q$ be the resulting separator. For $u,v\in V_d$, set

```math
P(u,v)=Q(uv+n).
```

The coefficients of $uv+n$ are affine-linear in the coefficients of $u$ when $v$ is fixed. Thus $P$ has degree at most $2^d$ in the $d+1$ coefficient variables of $u$.

For distinct $a,b\in U$, Equation (1.1) gives $P(a,b)=0$. On the diagonal, the construction of $Q$ gives $P(a,a)\ne0$. Lemma 3.3, with $r=d+1$ and $E=2^d$, proves Equation (3.5).

## 4. The exceptional diagonal

We next control the set $S$ in Equation (3.4). The only step in this section requiring Condition (ND) is the treatment of a possible scalar family.

### 4.1. Factorization families

**Lemma 4.1.** Every $a\in S$ has degree at most $d$. Moreover, $S$ is covered by at most $2^d$ families of the form:

**Equation (4.1).**

```math
 a_\lambda
 =\frac{\lambda f-\lambda^{-1}g}{2},
 \qquad
 \lambda\in\mathbb C^*,
 \qquad
 fg=n,
```

where $f$ is a monic divisor of $n$ in $\mathbb C[x]$ and $g=n/f$.

**Proof.** For $a\in S$, choose $r\in\mathbb C[x]$ such that $a^2+n=r^2$. Then:

**Equation (4.2).**

```math
(r+a)(r-a)=n.
```

Both factors are nonzero, even if $r=0$, since $n\ne0$. Their degrees add to $d$. As

```math
2a=(r+a)-(r-a),
```

we have $\deg a\le d$.

Write $r+a=\lambda f$, with $f$ monic and $\lambda\in\mathbb C^*$. Then $f$ divides $n$, we have $r-a=\lambda^{-1}(n/f)$, and Equation (4.1) follows.

If

```math
n=\gamma\prod_{\nu=1}^{q}(x-\xi_\nu)^{e_\nu},
\qquad
\sum_{\nu=1}^{q}e_\nu=d,
```

then the number of monic divisors is:

**Equation (4.3).**

```math
\tau(n)
=\prod_{\nu=1}^{q}(e_\nu+1)
\le\prod_{\nu=1}^{q}2^{e_\nu}
=2^d.
```

No squarefreeness assumption has been used.

These families need not be disjoint, and some parameters may give zero or polynomials outside $\mathbb Z[x]$. We only use them as a covering of $S$. Counting additional parameters or overlapping families can only enlarge an upper bound.

### 4.2. Square specializations and a rigidity lemma

**Lemma 4.2 (Square specializations).** Let $F\in\mathbb C[x,t]\setminus\lbrace0\rbrace$. If $F(x,\lambda)$ is a square in $\mathbb C[x]$ for infinitely many $\lambda\in\mathbb C$, then:

**Equation (4.4).**

```math
F(x,t)=c(t)H(x,t)^2
```

for some nonzero $c\in\mathbb C[t]$ and $H\in\mathbb C[x,t]$.

**Proof.** Use unique factorization in $\mathbb C[x,t]$ to write

```math
F(x,t)=c(t)\prod_{i=1}^{s}P_i(x,t)^{m_i},
```

where the $P_i$ are distinct irreducible factors of positive $x$-degree, and $c$ collects all factors depending only on $t$, including the constant factor. Each $P_i$ is primitive as a polynomial in $x$ over $\mathbb C[t]$, and is irreducible over $\mathbb C(t)$ by Gauss's lemma. In characteristic zero it is therefore separable over $\mathbb C(t)$. Distinct $P_i$ remain coprime over that field.

Exclude the zeros of $c$, the $x$-leading coefficients of the $P_i$, their discriminants, and their pairwise resultants. These are finitely many parameter values because the relevant polynomials are nonzero. For every remaining value $\lambda$, the polynomials $P_i(x,\lambda)$ have positive degree, are squarefree, and are pairwise coprime. If any $m_i$ were odd, $F(x,\lambda)$ would not be a square for any of these values. The assumed infinitude of square specializations forces every $m_i$ to be even. Taking

```math
H=\prod_{i=1}^{s}P_i^{m_i/2}
```

proves Equation (4.4).

**Remark 4.3.** The factor $c(t)$ in Equation (4.4) is necessary. For example, $tH(x)^2$ is a square in $\mathbb C[x]$ after every nonzero complex specialization, although $t$ is not a square in $\mathbb C[t]$.

**Lemma 4.4 (Rigidity of a factorization family).** Let $f,g,b\in\mathbb C[x]\setminus\lbrace0\rbrace$ satisfy

```math
\frac{f}{g}\notin\mathbb C,
\qquad
b^2\ne-fg.
```

Then there exists $\mu\in\mathbb C^*$ for which:

**Equation (4.5).**

```math
F(x,\mu)=bf\mu^2+2fg\mu-bg
```

is not a square in $\mathbb C[x]$.

**Proof.** Suppose instead that $F(x,\lambda)$ is a square for every $\lambda\in\mathbb C^*$. By Lemma 4.2,

```math
F(x,t)=c(t)H(x,t)^2.
```

Since $\deg_tF=2$,

```math
\deg c+2\deg_tH=2.
```

If $\deg_tH=1$, then $c$ is a nonzero constant. Absorb a square root of $c$ into $H$ and write

```math
F=(ut+v)^2,
\qquad
u,v\in\mathbb C[x].
```

Comparison of coefficients gives

```math
u^2=bf,
\qquad
uv=fg,
\qquad
v^2=-bg.
```

Consequently,

```math
(fg)^2=u^2v^2=-b^2fg,
```

which implies $b^2=-fg$, a contradiction.

If $\deg_tH=0$, write $H=H(x)$. The nonzero coefficients of $t^2$ and $1$ show that $bf$ and $-bg$ are nonzero constant multiples of $H(x)^2$. Their ratio is constant, so $f/g$ is constant, another contradiction. These are the only possibilities.

**Proposition 4.5.** Suppose that $b\in S$ satisfies $b^2\ne-n$. Fix a family from Equation (4.1) with $f/g\notin\mathbb C$. Then at most $2^{d+1}$ distinct elements of $S$ belong to that family.

**Proof.** For every $\lambda\in\mathbb C^*$ representing an element $a_\lambda\in S$, the polynomial $ba_\lambda+n$ is a square in $\mathbb C[x]$. If $a_\lambda\ne b$, this follows from the tuple condition. If $a_\lambda=b$, it follows from $b\in S$. Multiplication by a nonzero complex scalar preserves the property of being a square. Hence:

**Equation (4.6).**

```math
F_\lambda
=bf\lambda^2+2fg\lambda-bg
=2\lambda(ba_\lambda+n)
```

is a square for every relevant parameter.

By Lemma 4.1, $\deg b\le d$, and both $f$ and $g$ have degree at most $d$. Thus $F_\lambda\in V_{2d}$ for every $\lambda$. Lemma 4.4 supplies a nonzero $\mu$ for which $F_\mu$ is not a square. Apply Lemma 3.1, with $L=d$, to this single polynomial. The resulting function $Q$ has degree at most $2^d$, vanishes on all squares in $V_{2d}$, and satisfies $Q(F_\mu)\ne0$.

Each coefficient of $F_\lambda$ is a polynomial in $\lambda$ of degree at most two. Therefore

```math
q(\lambda)=Q(F_\lambda)
```

is a nonzero polynomial of degree at most $2^{d+1}$. Every parameter representing an element of $S$ in the chosen family is a root of $q$. There are at most $2^{d+1}$ such parameters, and hence at most that many distinct represented elements.

### 4.3. The scalar family

We record explicitly the passage between complex proportionality and the integral Condition (ND). An integer polynomial is called primitive when the greatest common divisor of its coefficients is one.

**Lemma 4.6 (Integral scalar descent).** Let $n\in\mathbb Z[x]\setminus\lbrace0\rbrace$ and let $A\subset\mathbb Z[x]\setminus\lbrace0\rbrace$ be nonempty. The following are equivalent:

1. There are $h\in\mathbb C[x]\setminus\lbrace0\rbrace$ and $\kappa\in\mathbb C^*$ such that $n=\kappa h^2$ and every member of $A$ is a constant multiple of $h$.
2. There are a primitive $p\in\mathbb Z[x]\setminus\lbrace0\rbrace$, an integer $N\in\mathbb Z\setminus\lbrace0\rbrace$, and nonzero integers $b_a$ for $a\in A$, such that

```math
n=Np^2,
\qquad
a=b_ap
\quad(a\in A).
```

**Proof.** The second assertion immediately implies the first. For the converse, choose $a_*\in A$, divide it by the positive greatest common divisor of its coefficients, and call the resulting primitive polynomial $p$. Then $h$ is proportional to $p$. For each $a\in A$, the constant $a/p$ is rational, as can be seen by comparing a coefficient for which $p$ is nonzero. Likewise, $n/p^2$ is rational.

If a rational multiple of a primitive integer polynomial has integer coefficients, that rational multiple is an integer. In lowest terms, its denominator would otherwise divide every coefficient. The polynomial $p^2$ is primitive by Gauss's lemma. Applying this observation to $p$ and to $p^2$ proves the second assertion.

**Lemma 4.7 (At most two square shifts).** Let $t\in\mathbb C(x)\setminus\mathbb C$. Then

```math
\left|
\lbrace\eta\in\mathbb C:t+\eta\in\mathrm{Sq}(\mathbb C(x))\rbrace
\right|
\le2.
```

**Proof.** Suppose that $t+\eta_i$ is a square for three distinct constants $\eta_1,\eta_2,\eta_3$. Regard $t$ as a morphism

```math
t:\mathbb P^1_{\mathbb C}\longrightarrow\mathbb P^1_{\mathbb C}
```

of degree $q\ge1$. At every point in the fiber above $-\eta_i$, the vanishing order of $t+\eta_i$ is even, so the local degree of the morphism is even. The pole orders of $t$ are also even because any one of the $t+\eta_i$ is a rational-function square. Thus every local degree in each of the four distinct fibers above

```math
-\eta_1,
\qquad
-\eta_2,
\qquad
-\eta_3,
\qquad
\infty
```

is even.

In each fiber the local degrees sum to $q$, so that fiber contains at most $q/2$ points and contributes at least $q/2$ to the total ramification

```math
\sum_P(e_P-1).
```

The four fibers therefore contribute at least $2q$. The Riemann-Hurwitz formula for a map of degree $q$ from $\mathbb P^1$ to itself in characteristic zero gives total ramification $2q-2$, a contradiction.

**Proposition 4.8.** Suppose that $A$ satisfies Condition (ND). Among the families in Lemma 4.1, at most one has $f/g\in\mathbb C$. Such a family exists only if $n\in\mathrm{Sq}(\mathbb C[x])$, and it contributes at most two elements of $S$.

**Proof.** If $f/g$ is constant, then $n=fg$ is a nonzero constant times $f^2$, and hence is a square over $\mathbb C$. Because $f$ is monic, the choice of $f$ is unique if it exists. Every root multiplicity of $n$ must be even, and $f$ has half that multiplicity. Write

```math
n=\kappa h^2,
```

where $h$ is this monic polynomial and $\kappa\in\mathbb C^*$. All elements represented by the scalar family are constant multiples of $h$.

Lemma 4.6 and Condition (ND) guarantee an element $b\in A$ that is not a constant multiple of $h$. Put $t=b/h$, so $t\in\mathbb C(x)\setminus\mathbb C$. If $ch\in A$ with $c\in\mathbb C^*$, the entries $ch$ and $b$ are distinct and

```math
(ch)b+n=h^2(ct+\kappa)
```

is a square. Since every nonzero complex constant has a square root, division by $ch^2$ shows that

```math
t+\frac{\kappa}{c}
```

is a square in $\mathbb C(x)$. Distinct nonzero constants $c$ give distinct shifts $\kappa/c$. Lemma 4.7 bounds their number by two.

### 4.4. The complete exceptional-diagonal bound

**Proposition 4.9.** Let $A$ be a polynomial $D(n)$-tuple satisfying Condition (ND), with $d\ge1$. Its exceptional diagonal set satisfies:

**Equation (4.7).**

```math
|S|\le2^{2d+1}+2\delta(n).
```

**Proof.** If $|S|\le2$, the estimate is immediate. Otherwise choose $b\in S$ with $b^2\ne-n$. Such a choice is possible because the polynomial equation $b^2=-n$ has at most two solutions in $\mathbb C[x]$.

Every family with nonconstant $f/g$ contributes at most $2^{d+1}$ elements by Proposition 4.5. There are at most $2^d$ families by Lemma 4.1. Their total contribution is therefore at most

```math
2^d\cdot2^{d+1}=2^{2d+1}.
```

Proposition 4.8 bounds the possible remaining scalar family by two. It is absent when $\delta(n)=0$. Summing these upper bounds proves Equation (4.7). Overlaps between the families do not affect the conclusion.

**Corollary 4.10 (Cubic exceptional-diagonal bound).** If $d=3$, then $|S|\le64$ for every $D(n)$-set $A$ in $\mathbb Z[x]$.

**Proof.** Let $\gamma$ be the leading coefficient of $n$, and write $n=\gamma fh$, where $f$ and $h$ are complementary monic divisors. The families associated with $f$ and $h$ in Equation (4.1) are identical, since

```math
\frac{\mu h-\gamma\mu^{-1}f}{2}
=\frac{\lambda f-\gamma\lambda^{-1}h}{2},
\qquad
\mu=-\frac{\gamma}{\lambda}.
```

The map $f\mapsto h=n/(\gamma f)$ is an involution on the monic divisors of $n$. It has no fixed point when $d=3$, since $f=h$ would imply $3=2\deg f$. Thus the at most eight divisors in Lemma 4.1 can be paired, and $S$ is covered by at most four families. All have nonconstant $f/g$, since a constant ratio would make $n$ a constant multiple of a square and hence of even degree.

If $|S|\le2$, the desired bound is immediate. Otherwise choose $b\in S$ with $b^2\ne-n$, as in Proposition 4.9. Proposition 4.5 bounds each of the at most four families by $2^{3+1}=16$ elements. Therefore

```math
|S|\le4\cdot16=64.
```

## 5. A rank bound for each degree above $d$

The argument in this section is algebraic and requires neither integrality nor Condition (ND). Formal power series are taken in $\mathbb C[[z]]$. The notation $O(z^r)$ means an element of $z^r\mathbb C[[z]]$, with no analytic convergence assertion.

**Proposition 5.1 (Fixed-degree bound).** Let $n\in\mathbb C[x]\setminus\lbrace0\rbrace$ have degree $d$, and let $A$ be a finite set of distinct nonzero complex polynomials satisfying

```math
ab+n\in\mathrm{Sq}(\mathbb C[x])
\qquad
(a,b\in A,\ a\ne b).
```

For an integer $k\gt d$, put

```math
A_k=\lbrace a\in A:\deg a=k\rbrace.
```

Then:

**Equation (5.1).**

```math
|A_k|\le2k-d+1.
```

**Proof.** Let $n_d\ne0$ be the leading coefficient of $n$, and put

```math
j=2k-d\gt k.
```

For $a\in A_k$, denote its leading coefficient by $\alpha_a$, and form the reciprocal normalization

```math
A_a(z)=\frac{z^ka(z^{-1})}{\alpha_a},
\qquad
A_a(0)=1.
```

There is a unique formal square root with constant coefficient one, which we write as

```math
S_a(z)=\sqrt{A_a(z)}=\sum_{r\ge0}s_r(a)z^r.
```

Existence and uniqueness follow recursively by comparing coefficients in $S_a^2=A_a$, since the coefficient to be determined at each positive degree occurs with factor $2$.

For distinct $a,b\in A_k$, let

```math
\begin{aligned}
D_{a,b}(z)
&=\frac{z^{2k}(ab+n)(z^{-1})}{\alpha_a\alpha_b}\\
&=A_a(z)A_b(z)
+\frac{n_d}{\alpha_a\alpha_b}z^j
+O(z^{j+1}).
\end{aligned}
```

Because $ab+n$ is a polynomial square of degree $2k$, the formal square root of $D_{a,b}$ with constant coefficient one is a polynomial of degree at most $k$. On the other hand, expansion of the square root at the unit $A_aA_b$ gives:

**Equation (5.2).**

```math
\sqrt{D_{a,b}(z)}
=S_a(z)S_b(z)
+\frac{n_d}{2\alpha_a\alpha_b}z^j
+O(z^{j+1}).
```

Indeed, the correction to $A_aA_b$ first occurs at degree $j$, and $S_a(0)S_b(0)=1$.

Since $j\gt k$, the coefficient of $z^j$ on the left of Equation (5.2) is zero. Consequently:

**Equation (5.3).**

```math
\alpha_a\alpha_b
\sum_{r=0}^{j}s_r(a)s_{j-r}(b)
=-\frac{n_d}{2}
\qquad
(a\ne b).
```

On the diagonal, $S_a(z)^2=A_a(z)$ and $\deg A_a\le k\lt j$ give:

**Equation (5.4).**

```math
\alpha_a^2
\sum_{r=0}^{j}s_r(a)s_{j-r}(a)
=0.
```

Associate to $a$ the vector

```math
v(a)=\bigl(\alpha_as_0(a),\ldots,\alpha_as_j(a)\bigr)
\in\mathbb C^{j+1},
```

and use the bilinear form

```math
\langle u,v\rangle
=\sum_{r=0}^{j}u_rv_{j-r}.
```

This form is bilinear, not Hermitian. If $m=|A_k|\ge2$, its Gram matrix on the vectors $v(a)$ is, by Equations (5.3) and (5.4),

```math
G=\frac{n_d}{2}\bigl(I_m-\mathbf{1}\mathbf{1}^{T}\bigr).
```

Its eigenvalues are $n_d/2$ with multiplicity $m-1$ and $(1-m)n_d/2$ with multiplicity one. Thus $G$ is nonsingular. If $V$ is the matrix whose rows are the $v(a)$ and $J$ is the $(j+1)$-dimensional coordinate-reversal matrix, then

```math
G=VJV^T.
```

It follows that

```math
m=\mathrm{rank}\,G\le j+1=2k-d+1.
```

The case $m\le1$ is immediate.

**Corollary 5.2.** For a $D(n)$-set $A$ in $\mathbb Z[x]$ with $d\ge1$:

**Equation (5.5).**

```math
\left|
\lbrace a\in A:d\lt\deg a\le3d\rbrace
\right|
\le6d^2+4d.
```

**Proof.** Apply Proposition 5.1 separately to each possible degree:

```math
\sum_{k=d+1}^{3d}(2k-d+1)=6d^2+4d.
```

## 6. Completion of the proof

### 6.1. Positive degree

Assume $d\ge1$. Lemma 4.1 places every element of $S$ in degree at most $d$. Hence $A$ is the disjoint union of

```math
\begin{aligned}
&U,\\
&S,\\
&\lbrace a\in A:d\lt\deg a\le3d\rbrace,\\
&\lbrace a\in A:\deg a\gt3d\rbrace.
\end{aligned}
```

Using Proposition 3.4, Proposition 4.9, Corollary 5.2, and Proposition 2.2, respectively, we obtain

```math
\begin{aligned}
|A|
&\le
\binom{2^d+d+1}{d+1}
+2^{2d+1}+2\delta(n)\\
&\qquad+6d^2+4d+21.
\end{aligned}
```

This is Equation (1.3). Since $\delta(n)\le1$, it also proves Equation (1.2) for positive degree.

### 6.2. Degree zero

Now let $d=0$, so $n$ is a nonzero integer. Proposition 2.2 bounds the number of nonconstant entries by $21$. Condition (ND) ensures that at least one nonconstant entry $b$ exists.

Suppose that two distinct nonzero constants $c,e$ belong to $A$. Write

```math
bc+n=r^2,
\qquad
be+n=s^2,
```

with $r,s\in\mathbb Z[x]$. Then, in $\mathbb C[x]$,

```math
\begin{aligned}
(\sqrt e\,r-\sqrt c\,s)
(\sqrt e\,r+\sqrt c\,s)
&=er^2-cs^2\\
&=n(e-c)\\
&\ne0.
\end{aligned}
```

A product of two polynomials can be a nonzero constant only if both factors are constants. Adding and subtracting these two factors shows that $r$ and $s$ are constant. The identity $bc+n=r^2$, with $c\ne0$, then makes $b$ constant, a contradiction. Thus at most one entry of $A$ is constant, and

```math
|A|\le21+1=22.
```

This completes the proof of Theorem 1.2.

The proof imposes no irreducibility or squarefreeness condition on $n$. The arguments over $\mathbb C$ are used only to obtain upper bounds from a weaker square condition. They do not infer integrality of a complex square root. Integrality enters essentially in the specialization argument of Section 2 and in the exact interpretation of the scalar exclusion. The bound is explicit and unconditional, although no optimality is asserted.

## 7. The unrestricted interpretation and the excluded class

For completeness, the relationship with the unrestricted ring-theoretic question can be stated as an equivalence. This also specifies the exact scope of the answer to Problem 1.14.

**Proposition 7.1.** Fix an even nonnegative integer $d$. The following assertions are equivalent:

1. There is an absolute constant $M$ such that every finite set of distinct positive integers with property $D(N)$, for any nonzero integer $N$, has at most $M$ elements.
2. There is a constant $C_d$ such that every $D(n)$-set in $\mathbb Z[x]$ with $\deg n=d$, without Condition (ND), has at most $C_d$ elements.

**Proof.** Write $d=2e$. To prove the second assertion implies the first, start with an integer $D(N)$-tuple $\lbrace b_1,\ldots,b_m\rbrace$, put

```math
p=x^e
\qquad
(p=1\text{ if }e=0),
```

and set

```math
n=Np^2,
\qquad
A=\lbrace b_1p,\ldots,b_mp\rbrace.
```

This is a $D(n)$-set with $\deg n=d$ and $|A|=m$. Thus the second assertion gives $m\le C_d$ independently of $N$.

Conversely, assume the first assertion and let $A$ be any $D(n)$-set of the specified degree. If Condition (ND) holds, Theorem 1.2 gives $|A|\le B(d)$. Otherwise, write

```math
n=Np^2,
\qquad
A=\lbrace b_1p,\ldots,b_mp\rbrace,
```

with $N,b_i$ nonzero integers and $p\in\mathbb Z[x]\setminus\lbrace0\rbrace$. For $i\ne j$, a square root $r\in\mathbb Z[x]$ of $p^2(b_ib_j+N)$ satisfies

```math
r^2=(b_ib_j+N)p^2.
```

If $b_ib_j+N=0$, that integer is already a square. Otherwise, over $\mathbb C$ we have $r=\lambda p$ with

```math
\lambda^2=b_ib_j+N.
```

Comparing a nonzero coefficient of $p$ shows that $\lambda\in\mathbb Q$. A rational number whose square is an integer is an integer. Hence $b_ib_j+N$ is an integer square in every case.

The positive $b_i$ form a positive-integer $D(N)$-tuple. The absolute values of the negative $b_i$ form another such tuple. Each has size at most $M$, so $m\le2M$. Therefore the second assertion follows with

```math
C_d=\max\lbrace B(d),2M\rbrace.
```

The scalar exclusion is not interchangeable with the weaker requirement that some entry be nonconstant. When $e\ge1$, all entries in the construction above are nonconstant. Conversely, for odd-degree $n$ no scalar-lift class exists, so Theorem 1.2 already bounds every $D(n)$-set in $\mathbb Z[x]$.

The restriction $n\ne0$ is essential. For $n=0$, the sets

```math
\lbrace x^2,x^4,\ldots,x^{2m}\rbrace
```

have the pairwise square property for every $m$, and the usual degree of the zero polynomial is not a nonnegative integer.

Thus the degree-uniform polynomial problem, with the convention used by Dujella, Fuchs and Tichy and by Dujella's research notes, has the explicit answer in Equation (1.2). Its cubic special case has the unconditional bound $646$ for all $D(n)$-sets. The additional unrestricted even-degree question is not claimed here. Proposition 7.1 identifies precisely the integer uniformity assertion that it would also settle.

## Dependencies and verification scope

The proof uses Dujella's integer large-element theorem, stated as Theorem 2.1, and the classical Riemann-Hurwitz formula in Lemma 4.7. All other quantitative estimates used in Theorem 1.2 are proved here by interpolation, unique factorization, formal power series, and finite-dimensional linear algebra. No conjectural uniformity statement, numerical search, or computer calculation is used as a premise.

## References

A. Dujella. “On the size of Diophantine $m$-tuples.” *Mathematical Proceedings of the Cambridge Philosophical Society* **132** (2002), 23-33. Theorem 1. [Preprint](https://arxiv.org/abs/math/0002088).

A. Dujella. *Open problems on Diophantine m-tuples and elliptic curves*. Problem 1.14, University of Zagreb, consulted 13 October 2026. [Problem list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf#page=3).

A. Dujella. *Diophantine m-tuples: Various generalizations*. Section 7.2, “Polynomials”, University of Zagreb, consulted 13 October 2026. [Research notes](https://web.math.pmf.unizg.hr/~duje/gener.html).

A. Dujella, C. Fuchs and R. F. Tichy. “Diophantine $m$-tuples for linear polynomials.” *Periodica Mathematica Hungarica* **45** (2002), 21-33. Definition 1 and the subsequent degree-uniformity question.

A. Dujella, C. Fuchs and P. G. Walsh. “Diophantine $m$-tuples for linear polynomials. II. Equal degrees.” *Journal of Number Theory* **120** (2006), 213-228.

A. Jurasić. “Diophantine $m$-tuples for quadratic polynomials.” *Glasnik Matematički, Serija III* **46(66)** (2011), 283-309.

The Stacks Project Authors. *The Stacks Project*, Algebraic Curves, Section 53.12, “Riemann-Hurwitz”, Tag 0C1B, consulted 13 October 2026. [Reference](https://stacks.math.columbia.edu/tag/0C1B).
