# Counting Square-Parameter Diophantine Quadruples

## A complete solution to Dujella's Problem 1.7(c), with partial results for 1.7(d)

**Publication date:** 14 October 2026  
**Status:** Complete solution to part (c); partial results for part (d)  
**Field:** Number theory, Diophantine tuples, asymptotic counting

## Abstract

For a fixed nonzero integer
<var>n</var>, let
$D_{4,n}(N)$ count unordered sets of four distinct positive integers at most
<var>N</var> whose pairwise products, increased by
<var>n</var>, are integer squares. For every fixed
$k\ge1$, we prove

```math
\begin{aligned}
D_{4,k^2}(N)&=\frac{2^{4/3}}{3\Gamma(2/3)^3}\,k^{2/3}\Delta(k)N^{1/3}\log N\\
&\quad+O_k(N^{1/3}),
\end{aligned}
```

where
$\Delta$ is a positive rational-valued multiplicative function given by explicit finite local sums. A uniform Pell estimate and a triple invariant isolate the principal family. A primitive rank-one matrix parametrization then reduces its count to a periodic weighted lattice sum. For fixed nonsquare
<var>n</var>, the same separation gives
$D_{4,n}(N)\ll_{n,\varepsilon}N^{1/4+\varepsilon}$. An elementary divisibility identity improves this to
$O_{n,\varepsilon}(N^{1/6+\varepsilon})$ for quadruples whose three smallest elements form an upper-regular triple. An appendix proves a cubic height bound when the three largest elements form an upper-regular triple. These bounds do not settle finiteness for general nonsquare
<var>n</var>.

**Keywords:** Diophantine quadruples; asymptotic counting; Pell equations; local densities.  
**2020 Mathematics Subject Classification:** 11D09, 11D45, 11N45.

## 1. Introduction and main results

A
$D(n)$ quadruple is an unordered set
$\lbrace a,b,c,d\rbrace$ of distinct positive integers such that the product of any two distinct elements, increased by
<var>n</var>, is a square in
$ℤ$. Throughout,

```math
\begin{gathered}
n\inℤ\setminus\lbrace 0\rbrace ,\\
0\lt a\lt b\lt c\lt d,
\end{gathered}
```

and zero is allowed as a square. We write
$D_{4,n}(N)$ for the number with
$d\le N$. All logarithms are natural. Every asymptotic statement fixes
<var>n</var> (or
<var>k</var>) before letting
<var>N</var> tend to infinity; no uniformity in a growing parameter is asserted.

Problem 1.7(c) of Dujella (2026) asks for the asymptotic behaviour of
$D_{4,n}(N)$ when
<var>n</var> is a nonzero square. Part (d) asks whether there are only finitely many quadruples for each fixed nonsquare
<var>n</var>. The preceding questions on triples were solved by Badesa (2025); see also Dražić, Kazalicki and Mrazović (2026). For
$n=1$, Dujella (2008) proved bounds of order
$N^{1/3}\log N$, and Martin and Sitar (2011) obtained the leading constant

**Equation (1.1).**

```math
K=\frac{2^{4/3}}{3\Gamma(2/3)^3}=0.338285\ldots.
```

**Theorem 1.1** (Square parameters).  For every fixed integer
$k\ge1$,

**Equation (1.2).**

```math
D_{4,k^2}(N)=Kk^{2/3}\Delta(k)N^{1/3}\log N+O_k(N^{1/3}).
```

The rational number
$\Delta(k)\gt 0$ is multiplicative and satisfies
$k^{-1}\le\Delta(k)\le1$. Its local factors are given in (7.2)-(7.4).

For example,

```math
\begin{gathered}
\Delta(1)=\Delta(2)=\Delta(4)=1,\\
\Delta(3)=\frac56,\\
\Delta(5)=\frac35,\\
\Delta(7)=\frac{13}{28},\\
\Delta(8)=\frac34.
\end{gathered}
```

This counts all
$D(k^2)$ quadruples, not just multiples of classical quadruples. Scaling a
$D(1)$ quadruple by
<var>k</var> gives only the lower-bound coefficient
$Kk^{-1/3}$, consistent with
$\Delta(k)\ge k^{-1}$. For
$k=1$, (1.2) recovers the leading term of Martin and Sitar (2011, Theorem 1.1) and gives the smaller remainder
$O(N^{1/3})$ in place of

```math
O\!\left(N^{1/3}(\log N)^{2/3+\sqrt2/6}(\log\log N)^{5/12}\right)
```

in that theorem. The lattice argument below avoids an equidistribution estimate for quadratic congruence roots.

An ordered triple
$A\lt B\lt C$ will be called *upper-regular* if

**Equation (1.3).**

```math
C=A+B+2\sqrt{AB+n}.
```

This specifies the upper sign; we do not identify it with every use of "regular" in the literature. Let
$R_n(N)$ count quadruples with an upper-regular smallest triple, and put
$I_n(N)=D_{4,n}(N)-R_n(N)$.

**Theorem 1.2** (Counting bounds).  For every fixed
$n\ne0$ and every
$\varepsilon\gt 0$,

**Equation (1.4).**

```math
I_n(N)\ll_{n,\varepsilon}N^{1/4+\varepsilon}.
```

If
<var>n</var> is nonsquare, then

**Equation (1.5).**

```math
\begin{gathered}
D_{4,n}(N)\ll_{n,\varepsilon}N^{1/4+\varepsilon},\\
R_n(N)\ll_{n,\varepsilon}N^{1/6+\varepsilon}.
\end{gathered}
```

Sections 2-3 isolate the principal family with an
$O_{n,\varepsilon}(N^{1/4+\varepsilon})$ error. Sections 4-7 count that family and prove Theorem 1.1. Section 8 proves the sharper regular-subfamily estimate. Appendix A treats the separate case of an upper-regular largest triple. The nonsquare finiteness question, also discussed by Dujella and Petričević (2019), remains unresolved here: none of the counting bounds is an absolute bound on the height of all quadruples.

## 2. Uniform counting and the triple invariant

### 2.1. A uniform Pell estimate

The coefficients in the following elementary estimate are allowed to vary. This uniformity is needed in the exceptional-family count.

**Lemma 2.1**.  Fix
$C\gt 0$ and
$\varepsilon\gt 0$. Suppose
$X\ge2$,
$A,B$ are positive integers,
$U,V\inℤ$, and

```math
\begin{gathered}
\max\lbrace A,B,\vert U\vert ,\vert V\vert \rbrace \le X^C,\\
BU-AV\ne0.
\end{gathered}
```

There are
$O_{C,\varepsilon}(X^\varepsilon)$ integers
$1\le t\le X^C$ for which both
$At+U$ and
$Bt+V$ are squares.

*Proof.* Write
$y^2=At+U$,
$z^2=Bt+V$, with
$y,z\ge0$. Elimination gives

**Equation (2.1).**

```math
(By)^2-ABz^2=B(BU-AV)=H\ne0.
```

All quantities are bounded by fixed powers of
<var>X</var>, with exponents depending only on
<var>C</var>. If
$AB$ is a square, factorization of the left side bounds the number of solutions by
$O(\tau(\vert H\vert ))$.

Otherwise write
$AB=h^2D$, where
$D\gt 1$ is squarefree, and work in the full ring of integers
$𝒪$ of
$ℚ(\sqrt D)$. The algebraic integer

```math
\alpha=By+hz\sqrt D
```

has norm
<var>H</var>. There are at most
$\tau(\vert H\vert )$ integral ideals of norm
$\vert H\vert$: a split prime power
$p^e$ has
$e+1$ possible ideal factors, while an inert or ramified prime has at most one. Hence there are at most
$\tau(\vert H\vert )$ possibilities for
$(\alpha)$.

Generators of a fixed principal ideal differ by units. Both real embeddings of
$\alpha$ have absolute value at most
$X^{C_1}$ for some
$C_1=C_1(C)$, and at least
$X^{-C_1}$ because their product is the nonzero integer
<var>H</var>. Modulo sign, the absolute values of units in one real embedding form a geometric progression. Its ratio is at least
$(1+\sqrt5)/2$, uniformly in the field: this follows from the integral trace and norm
$\pm1$ of a unit with absolute value greater than one. Consequently a fixed ideal contributes
$O_C(\log X)$ permitted generators. The standard divisor bound
$\tau(m)\ll_\eta m^\eta$, with a suitably small
$\eta$, proves the estimate. Finally,
$(y,z)$ determines
<var>t</var>. ◻

**Corollary 2.2**.  For fixed
$n\ne0$, uniformly over
$1\le a\lt b\le N$, the number of positive integers
$t\le N$ for which
$at+n$ and
$bt+n$ are squares is
$O_{n,\varepsilon}(N^\varepsilon)$. A bounded collection of first pairs therefore contributes
$O_{n,\varepsilon}(N^\varepsilon)$ quadruples.

*Proof.* Apply Lemma 2.1 to
$(A,B,U,V)=(a,b,n,n)$, for which
$BU-AV=n(b-a)\ne0$. The coefficients fit the hypotheses with a fixed exponent depending on
<var>n</var> (or after increasing
<var>X</var> by a fixed factor). For quadruples choose both remaining entries among these extensions and replace
$\varepsilon$ by a smaller positive number. ◻

### 2.2. The invariant of a triple

The identities below are standard in the study of
$D(n)$ triples; compare Adžaga et al. (2025). We use a self-contained form with explicit hypotheses, including the lower-sign boundary.

**Lemma 2.3**.  Let
$a\lt b\lt c$ be a
$D(n)$ triple, and write

```math
\begin{gathered}
r^2=ab+n,\\
s^2=ac+n,\\
t^2=bc+n,\\
r,s,t\ge0.
\end{gathered}
```

Put

**Equation (2.2).**

```math
e=n(a+b+c)+2abc-2rst.
```

Then

**Equation (2.3).**

```math
\begin{aligned}
ae+n^2&=(at-rs)^2,\\
be+n^2&=(bs-rt)^2,\\
ce+n^2&=(cr-st)^2.
\end{aligned}
```

**Equation (2.4).**

```math
\begin{aligned}
&e\bigl(n(a+b+c)+2abc+2rst\bigr)\\
&=n^2\bigl((c-a-b)^2-4(ab+n)\bigr).
\end{aligned}
```

If
$M=\vert n\vert$,
$ab\ge3M$,
$c\gt M^2$, and the triple is not upper-regular, then

**Equation (2.5).**

```math
\begin{gathered}
1\le e\le\frac{M^2c}{ab},\\
c\ge\frac{ab}{M^2}.
\end{gathered}
```

For fixed
$a,b,e$, at most two values of
<var>c</var> can occur.

*Proof.* Expansion proves the identities. Since
$c\gt M^2$, the last identity in (2.3) gives
$e\gt -1$, hence
$e\ge0$. The second factor on the left of (2.4) is at least

```math
2abc-M(a+b+c)\gt 2abc-3Mc\ge abc.
```

If
$e=0$, then
$c=a+b\pm2r$. The upper sign is excluded. With the lower sign,
$c\gt b$ implies
$a\gt 2r$, and so

```math
3ab\lt 4ab-a^2\lt -4n\le4M,
```

contrary to
$ab\ge3M$. Thus
$e\ge1$. Moreover
$\vert c-a-b\vert \lt c$ and
$ab+n\ge0$, so the right side of (2.4) is at most
$M^2c^2$. This proves (2.5).

Finally, squaring (2.2) gives the necessary equation

**Equation (2.6).**

```math
\begin{aligned}
&\bigl(n(a+b)+(n+2ab)c-e\bigr)^2\\
&=4(ab+n)(ac+n)(bc+n).
\end{aligned}
```

The coefficient of
$c^2$ after subtraction is
$n^2\ne0$. Thus at most two values of
<var>c</var> are possible; possible extraneous roots after squaring do not affect this upper bound. ◻

## 3. Separating the principal family

### 3.1. A root defect for upper-regular triples

**Lemma 3.1**.  Suppose
$A\lt B\lt C=A+B+2R$, where
$R^2=AB+n$,
$R\ge0$, and let
<var>z</var> be a positive extension of this triple. Set

```math
q=\sqrt{Cz+n}-\sqrt{Az+n}-\sqrt{Bz+n}\inℤ.
```

With
$M=\vert n\vert$,

**Equations (3.1), (3.2).**

```math
\begin{aligned}
\vert q\vert &\le5M\sqrt{\frac{z}{ABC}}&& (z\gt C),\\
\vert q\vert &\le\frac{5M}{\sqrt{Az}}&& (z\lt A).
\end{aligned}
```

If
$z\gt C$, then
$q\ne0$. If
$z\lt A$, then
$Az\le25M^2$.

*Proof.* For positive
$v,z$ with
$vz+n\ge0$,

```math
\left\vert \sqrt{vz+n}-\sqrt{vz}\right\vert
=\frac{M}{\sqrt{vz+n}+\sqrt{vz}}\le\frac{M}{\sqrt{vz}}.
```

Also

**Equation (3.3).**

```math
\begin{aligned}
&\left\vert \sqrt C-\sqrt A-\sqrt B\right\vert\\
&=\frac{2M}{(R+\sqrt{AB})(\sqrt C+\sqrt A+\sqrt B)}\\
&\le\frac{2M}{\sqrt{ABC}}.
\end{aligned}
```

For
$z\gt C$, each of the other three errors is at most
$M\sqrt{z/(ABC)}$. For
$z\lt A$, the term from (3.3), multiplied by
$\sqrt z$, is at most
$2M/\sqrt{Az}$, and the other errors total at most
$3M/\sqrt{Az}$. This proves the estimates.

If
$q=0$, squaring the equality of roots twice and using
$n\ne0$ gives

**Equation (3.4).**

```math
z^2-(A+B+R)z-\frac{3n}{4}=0.
```

For
$z\gt C$, the left side is positive. This is immediate when
$n\lt 0$; when
$n\gt 0$, use
$z(z-A-B-R)\gt zR\gt R^2\gt n$. Thus
$q\ne0$. For
$z\lt A$, equation (3.4) is impossible if
$n\gt 0$. If
$n\lt 0$, it implies
$z(A+B+R-z)=3M/4$, hence
$Az\lt 3M/4$. In the remaining case,
$q\ne0$ and integrality together with (3.2) gives
$Az\le25M^2$. ◻

Applying the smaller-extension assertion to
$\lbrace b,c,d\rbrace$ and its extension
<var>a</var> gives

**Equation (3.5).**

```math
ab\le25M^2
```

whenever the largest triple is upper-regular. Corollary 2.2 then gives an
$O_{n,\varepsilon}(N^\varepsilon)$ contribution. Appendix A strengthens this to an absolute height bound.

### 3.2. A non-upper-regular smallest triple

**Proposition 3.2**.  For fixed
$n\ne0$ and every
$\varepsilon\gt 0$,
$I_n(N)\ll_{n,\varepsilon}N^{1/4+\varepsilon}$.

*Proof.* The cases
$ab\lt 3M$ or
$c\le M^2$ involve only boundedly many first pairs and are covered by Corollary 2.2. The same holds when
$\lbrace b,c,d\rbrace$ is upper-regular, by (3.5). In all remaining cases Lemma 2.3 applies to both
$\lbrace a,b,c\rbrace$ and
$\lbrace b,c,d\rbrace$. For the invariant
<var>e</var> of the first triple it gives

```math
\begin{gathered}
e\le\frac{M^2c}{ab},\\
d\ge\frac{bc}{M^2},\\
ae\le\frac{M^4N}{b^2}.
\end{gathered}
```

If
$b\le N^{1/4}$, then
$r^2=ab+n\le N^{1/2}+n$. There are
$O_n(N^{1/4})$ possible
<var>r</var>, and each positive integer
$r^2-n$ has at most
$\tau(r^2-n)$ ordered factor pairs. Corollary 2.2 then controls
$c,d$.

If
$b\gt N^{1/4}$, then
$ae\le M^4N^{1/2}$ and
$ae+n^2=x^2$ for some
$0\le x\ll_n N^{1/4}$. Factoring the positive integer
$x^2-n^2=ae$ gives
$O_{n,\varepsilon}(N^{1/4+\varepsilon})$ possibilities for
$(a,e)$. For each such pair,

**Equation (3.6).**

```math
\begin{gathered}
ab+n=r^2,\\
eb+n^2=y^2.
\end{gathered}
```

Lemma 2.1 gives
$O_{n,\varepsilon}(N^\varepsilon)$ choices for
<var>b</var>, unless
$e=an$. There are then at most two
<var>c</var> by (2.6), and
$O_{n,\varepsilon}(N^\varepsilon)$ choices for
<var>d</var>.

The degenerate case
$e=an$ requires
$n\gt 0$, since
$e\gt 0$. Equation (3.6) yields
$y^2=nr^2$, with
$r\gt 0$, so
$n=k^2$ for an integer
$k\ge1$. The first identity in (2.3) gives
$x^2=k^2(a^2+k^2)$. Thus
$k\mid x$ and
$(x/k)^2-a^2=k^2$. Factoring this difference of squares leaves only finitely many
<var>a</var>, hence
<var>e</var>, in terms of
<var>n</var>. Also
$d\ge bc/M^2\gt b^2/M^2$ gives
$b\ll_n N^{1/2}$, and
$ab+n=r^2$ permits only
$O_n(N^{1/4})$ values of
<var>b</var> for each fixed
<var>a</var>. The preceding bounds on
$c,d$ finish the proof after relabelling
$\varepsilon$. ◻

### 3.3. An upper-regular smallest triple

Write

```math
\begin{gathered}
c=a+b+2r,\\
r^2=ab+n,\\
x^2=ad+n,\\
y^2=bd+n,\\
z^2=cd+n,
\end{gathered}
```

with all roots nonnegative, and put
$q=z-x-y$. Lemma 3.1 gives

**Equation (3.7).**

```math
\begin{gathered}
q\ne0,\\
q^2\le\frac{25M^2d}{abc}.
\end{gathered}
```

**Lemma 3.3**.  In this notation,

**Equation (3.8).**

```math
2\bigl(rx-ay-q(a+r)\bigr)(x+q)=(n-q^2)(a+2r).
```

If
$q^2\ne n$, then, outside boundedly many first pairs,

**Equation (3.9).**

```math
d\gg_n a^2bc^2\ge(ab)^{5/2}.
```

If
$q^2=n$, then
$n=k^2$,
$q=k$, and

**Equation (3.10).**

```math
d=\frac{4r(a+r)(b+r)}{k^2}.
```

*Proof.* The relation
$z=x+y+q$ yields

```math
2xy+2q(x+y)+q^2=2rd-n.
```

Subtracting the right side of (3.8) from its left side gives

```math
\begin{aligned}
&2r(x^2-ad-n)\\
&\quad-a\bigl(2xy+2q(x+y)+q^2-2rd+n\bigr)=0.
\end{aligned}
```

Thus no division by a potentially zero factor is involved.

If
$q^2\ne n$, the first parenthesized factor in (3.8) is a nonzero integer. Since
$x+q=z-y\gt 0$,

**Equation (3.11).**

```math
2(x+q)\le\vert n-q^2\vert (a+2r).
```

For
$ab\ge2M$, one has
$r\asymp\sqrt{ab}$,
$c\asymp b$, and
$a+2r\asymp\sqrt{ab}$. Moreover,

```math
\begin{gathered}
x+q=\frac{(c-b)d}{z+y}\gg\sqrt{ad},\\
\vert n-q^2\vert \le(M+1)q^2\ll_n\frac{d}{abc}.
\end{gathered}
```

Here
$z+y\ll\sqrt{bd}$ because
$c\asymp b$ and
$bd\ge2M$. Substituting into (3.11) gives
$\sqrt{ad}\ll_n d/(\sqrt{ab} c)$. Squaring and cancelling
<var>d</var> proves the first inequality in (3.9); the second follows from
$c\gt b\gt a$. The excluded case
$ab\lt 2M$ has boundedly many first pairs.

If
$q^2=n$, then
$n=k^2\gt 0$. Equation (3.8) and its counterpart with
$a,b$ interchanged give

```math
\begin{gathered}
rx-ay=q(a+r),\\
ry-bx=q(b+r).
\end{gathered}
```

Since
$r^2-ab=k^2$, solving gives

```math
x=\frac{q}{k^2}\bigl(2a(b+r)+k^2\bigr).
```

Positivity of
<var>x</var> forces
$q=k$, and substitution into
$x^2=ad+k^2$ gives (3.10). ◻

Let
$E_k(N)$ count positive pairs
$a\lt b$ with
$ab+k^2=r^2$ for which (3.10) is an integer at most
<var>N</var>. Every such pair gives a quadruple. Indeed the three additional roots are

**Equation (3.12).**

```math
\begin{gathered}
\frac{2a(b+r)+k^2}{k},\\
\frac{2b(a+r)+k^2}{k},\\
\frac{2(a+r)(b+r)+k^2}{k}.
\end{gathered}
```

Their squares are
$ad+k^2,bd+k^2,cd+k^2$ by expansion. A rational number whose square is an integer is an integer. Also
$(a+r)(b+r)=rc-k^2$, and

```math
\frac dc=\frac{4r^2}{k^2}-\frac{4r}{c}\gt 2
```

because
$r\gt k$ and
$c\gt 2r$. The roots for
$ac+k^2$ and
$bc+k^2$ are
$a+r$ and
$b+r$. Thus all six conditions and the required ordering hold, and the two smallest elements recover the pair uniquely.

**Corollary 3.4**.  For fixed
$k\ge1$ and every
$\varepsilon\gt 0$,

**Equation (3.13).**

```math
D_{4,k^2}(N)=E_k(N)+O_{k,\varepsilon}(N^{1/4+\varepsilon}).
```

For fixed nonsquare
<var>n</var>,
$D_{4,n}(N)\ll_{n,\varepsilon}N^{1/4+\varepsilon}$.

*Proof.* Proposition 3.2 handles non-upper-regular smallest triples. For an upper-regular smallest triple with
$q^2\ne n$, (3.9) gives
$ab\ll_n N^{2/5}$, hence
$r\ll_n N^{1/5}$. Factoring
$ab=r^2-n$ and applying Corollary 2.2 gives
$O_{n,\varepsilon}(N^{1/5+\varepsilon})$ quadruples. Bounded first pairs are covered by the same corollary. Lemma 3.3 identifies the remaining family, which occurs only for square
<var>n</var>. ◻

## 4. A primitive determinant parametrization

We now count
$E_k(N)$, equivalently the pairs
$a\lt b$ satisfying

**Equation (4.1).**

```math
\begin{gathered}
ab=r^2-k^2,\\
k^2\mid4r(a+r)(b+r),\\
4r(a+r)(b+r)\le k^2N.
\end{gathered}
```

### 4.1. Unique reduced parameters

The positive integral rank-one matrix

```math
\begin{pmatrix}a&r-k\\
r+k&b\end{pmatrix}
```

has the unique factorization

```math
\ell\begin{pmatrix}us&vs\\
ut&vt\end{pmatrix},\qquad
\gcd(u,v)=\gcd(s,t)=1,
```

where
$\ell$ is the greatest common divisor of its four entries. To obtain this, take the primitive direction of the first row and then remove the common factor from the row multipliers. The off-diagonal difference gives
$\ell(ut-vs)=2k$, so
$\ell\mid2k$.

Transposition exchanges
$(u,v)$ and
$(s,t)$, reverses the determinant sign, and leaves
$a,b,r$ unchanged. We therefore permit

**Equation (4.2).**

```math
\begin{gathered}
\ell\mid2k,\qquad \sigma\in\lbrace -1,1\rbrace ,\\
m=\frac{2\sigma k}{\ell},\qquad ut-vs=m,\\
\gcd(u,v)=\gcd(s,t)=1,\\
a=\ell us,\qquad b=\ell vt,\\
r=\ell vs+\sigma k,
\end{gathered}
```

and impose the lexicographic reduction

**Equation (4.3).**

```math
(u,v)\lt (s,t).
```

The vectors differ because
$m\ne0$. Exactly one of the two signed representations satisfies (4.3). This is an exact uniqueness statement, before any asymptotic approximation.

**Lemma 4.1**.  Up to
$O_k(N^{1/3})$ objects, the reduced parametrization may be replaced by

**Equation (4.4).**

```math
\begin{gathered}
u\lt v,\\
s\ge u,
\end{gathered}
```

with (4.2) unchanged. Outside finitely many
$(u,v)$ depending on
<var>k</var>, positivity,
$a\lt b$, and
$r\gt k$ are automatic.

*Proof.* If
$u=v$, primitivity forces
$u=v=1$, and
$t=s+m$. The height is a cubic polynomial in
<var>s</var> with positive leading coefficient, contributing
$O_k(N^{1/3})$ objects. If
$u\gt v$, then
$a\lt b$ gives
$(u^2-v^2)s\lt vm$. Since reduction implies
$s\ge u$, this requires
$m\gt 0$ and
$u^2\lt vm\lt um$. Hence
$u\lt m$, and the same inequality bounds
<var>s</var>, then
<var>t</var>, in terms of
<var>k</var>.

The discrepancy between lexicographic reduction and
$s\ge u$ lies on
$s=u$. Here
$u(t-v)=m$, so
$u\mid m$ and
$a=\ell u^2$ belongs to a bounded set. For valid pairs, (3.10) gives
$d\gt 4ab^2/k^2$, hence
$b\ll_k N^{1/2}$ and
$r\ll_k N^{1/4}$. Thus this boundary contributes
$O_k(N^{1/4})$ valid pairs.

Finally assume
$u\lt v$ and
$s\ge u$. Failure of
$t\gt 0$ or
$r\gt k$ implies
$uv\le\vert m\vert$, leaving finitely many
$(u,v)$. Failure of
$a\lt b$ implies

```math
\begin{gathered}
(v^2-u^2)s\le v\vert m\vert ,\\
u(v-u)\le\vert m\vert ,
\end{gathered}
```

again bounding
$u,v$. For each fixed
$(u,v)$, determinant solutions form a one-parameter arithmetic progression and the height is a cubic with positive leading coefficient. Their positive-height contribution is
$O_k(N^{1/3})$. This also bounds any invalid boundary objects introduced by the relaxation. ◻

### 4.2. The height interval

Fix
$\ell,\sigma,u,v$ with
$u\lt v$ and
$\gcd(u,v)=1$. Choose
$0\le s_0\lt u$ with
$vs_0\equiv-m\pmod u$, and put
$t_0=(vs_0+m)/u$. All determinant solutions are

```math
\begin{gathered}
s=s_0+uj,\\
t=t_0+vj,\\
j\inℤ.
\end{gathered}
```

Set

**Equation (4.5).**

```math
\begin{gathered}
X=\left(\frac{k^2N}{4}\right)^{1/3},\\
X_\ell=\frac X\ell,\\
Z=\frac su=j+\frac{s_0}{u},\\
S(u,v)=uv(u+v).
\end{gathered}
```

Then
$a=\ell u^2Z$,
$b=\ell v^2Z+\ell vm/u$, and
$r=\ell uvZ+\ell m/2$. Consequently

**Equation (4.6).**

```math
d=\frac{4\ell^3}{k^2}S(u,v)^2(Z+\eta_1)(Z+\eta_2)(Z+\eta_3),
```

where

**Equation (4.7).**

```math
\begin{gathered}
\eta_1=\frac{m}{2uv},\\
\eta_2=\frac{m}{2u(u+v)},\\
\eta_3=\frac{m(2v+u)}{2uv(u+v)}.
\end{gathered}
```

Outside finitely many
$(u,v)$, all shifts have absolute value at most
$1/2$. The height is then increasing for
$Z\ge1$. Comparing the product with
$(Z\pm\max_i\vert \eta_i\vert )^3$ shows that the interval of admissible real
<var>j</var>, before imposing periodic conditions, has length

**Equation (4.8).**

```math
\begin{gathered}
\left(\frac{X_\ell}{S(u,v)^{2/3}}-1\right)_++O_k(1),\\
t_+=\max\lbrace t,0\rbrace .
\end{gathered}
```

Actual solutions outside the finite exceptional set require
$S(u,v)\ll_k X^{3/2}$. We use

**Equation (4.9).**

```math
\#\lbrace 1\le u\lt v:S(u,v)\le CX^{3/2}\rbrace =O_C(X).
```

Indeed
$u\ll_C X^{1/2}$ and
$v\ll_C X^{3/4}u^{-1/2}$; summing the latter bound proves the claim. Thus the bounded error per pair in (4.8) is summable over an
$O_k(X)$ support, not an infinite set.

## 5. A periodic weighted lattice sum

**Lemma 5.1**.  Let
$Q\ge1$ be fixed, and let
$\theta:ℤ^2\toℝ$ be bounded and periodic modulo
<var>Q</var> in each coordinate. Suppose
$\theta(u,v)=0$ when
$\gcd(u,v,Q)\gt 1$. Define

**Equation (5.1).**

```math
\begin{gathered}
\mu_\theta=\frac1{Q^2}\sum_{u,v\bmod Q}\theta(u,v),\\
A_\theta=\mu_\theta\prod_{p\nmid Q}(1-p^{-2}),
\end{gathered}
```

and

**Equation (5.2).**

```math
J=\int_1^\infty[t(t+1)]^{-2/3}\,dt
=\frac{\Gamma(1/3)^2}{2\Gamma(2/3)}.
```

For
$Y\ge2$,

**Equation (5.3).**

```math
\begin{aligned}
&\sum_{\substack{1\le u\lt v,\ \gcd(u,v)=1\\
S(u,v)\le Y^{3/2}}}
\frac{\theta(u,v)}{S(u,v)^{2/3}}\\
&=\frac{A_\theta J}{2}\log Y+O_{Q,\vert\vert \theta\vert\vert _\infty}(1).
\end{aligned}
```

*Proof.* First omit coprimality. In a fixed row
<var>u</var>, the summand
$[uv(u+v)]^{-2/3}$ decreases with
$v\gt u$. Partial summation replaces the periodic weight by its row mean

```math
\overline\theta(u)=\frac1Q\sum_{v\bmod Q}\theta(u,v)
```

with error
$O_{Q,\vert\vert \theta\vert\vert _\infty}(u^{-2})$, including the upper cutoff. Replacing the unweighted row sum by its integral has the same error. These errors are summable in
<var>u</var>.

The row integral is

```math
F_Y(u)=\frac1u\int_1^{T_Y(u)}[t(t+1)]^{-2/3}\,dt,
```

with value zero if the interval is empty, where
$u^3T_Y(u)(T_Y(u)+1)=Y^{3/2}$. The function
$F_Y$ is nonnegative and decreasing, and
$F_Y(1)\le J$. Another partial summation replaces
$\overline\theta(u)$ by
$\mu_\theta$ with uniformly bounded error. The sum of
$F_Y(u)$ may likewise be replaced by its integral with bounded error. Changing the order of integration gives

```math
\begin{aligned}
&\int_1^\infty F_Y(u)\,du\\
&=\int_1^\infty[t(t+1)]^{-2/3}
\left(\frac12\log Y-\frac13\log(t(t+1))\right)_+dt\\
&=\frac J2\log Y+O(1).
\end{aligned}
```

The last error is bounded because the same integrand multiplied by
$\log(t(t+1))$ is integrable. This proves the unprimitive version with leading coefficient
$\mu_\theta J/2$.

Use Möbius inversion for coprimality. Since
$\theta$ vanishes off primitive classes modulo
<var>Q</var>, only
<var>h</var> with
$(h,Q)=1$ occur. Substitution
$(u,v)=(hU,hV)$ contributes
$h^{-2}$ and replaces
<var>Y</var> by
$Y/h^2$. The weight
$\theta_h(U,V)=\theta(hU,hV)$ has the same mean and supremum norm, because multiplication by
<var>h</var> permutes the residue classes modulo
<var>Q</var>. Thus the desired sum is

```math
\frac{\mu_\theta J}{2}
\sum_{\substack{h\ll\sqrt Y\\(h,Q)=1}}\frac{\mu(h)}{h^2}\log\frac{Y}{h^2}+O(1).
```

The bounded errors sum against
$h^{-2}$. The series
$\sum h^{-2}\log h$ converges, and the tail when extending the coefficient of
$\log Y$ to infinity is bounded. Finally,

```math
\sum_{(h,Q)=1}\frac{\mu(h)}{h^2}=\prod_{p\nmid Q}(1-p^{-2}),
```

which proves (5.3). The bounded range of
$Y/h^2$ causes no difficulty and can be included with another bounded error.

For (5.2), substitute
$x=1/(1+t)$ and use the symmetry of
$x^{-2/3}(1-x)^{-2/3}$ on
$(0,1)$: the integral is half of
$B(1/3,1/3)$. ◻

## 6. Counting the principal family

### 6.1. Periodic conditions

Set
$Q=2k^2$. Since every common divisor of
$s,t$ divides
$m=ut-vs$, the condition
$\gcd(s,t)=1$ is equivalent to
$\gcd(s,t,m)=1$. This and

```math
k^2\mid4r(a+r)(b+r)
```

are periodic in
<var>j</var> modulo
<var>Q</var>. For a primitive pair
$(u,v)$, let
$\theta_{\ell,\sigma}(u,v)$ be the proportion of the
<var>Q</var> classes of
<var>j</var> satisfying both conditions.

This proportion depends only on
$(u,v)\bmod Q$. Indeed a primitive pair modulo
<var>Q</var> gives a surjective map
$(s,t)\mapsto ut-vs$, whose kernel consists of the
<var>Q</var> multiples of
$(u,v)$. Hence the pairs obtained as
<var>j</var> varies modulo
<var>Q</var> are exactly all solutions of
$ut-vs\equiv m\pmod Q$, independently of a lift or starting solution. Extend the weight by zero on nonprimitive classes modulo
<var>Q</var>.

The two signs have the same weight. The map
$(s,t)\mapsto(-s,-t)$ exchanges
<var>m</var> and
$-m$, and simultaneously changes
$(a,b,r)$ to
$(-a,-b,-r)$. It preserves primitivity and divisibility. This is a statement about residue classes, not positive integer quadruples. Write the common weight as
$\theta_\ell$.

For
$\ell\mid2k$, let
$T_{k,\ell}$ count residue quadruples
$(u,v,s,t)\bmod Q$ with

**Equation (6.1).**

```math
\begin{gathered}
\gcd(u,v,Q)=1,\qquad\gcd(s,t,2k/\ell)=1,\\
ut-vs\equiv2k/\ell\pmod Q,\\
4R(A+R)(B+R)\equiv0\pmod{k^2},\\
A=\ell us,\qquad B=\ell vt,\\
R=\ell vs+k.
\end{gathered}
```

The kernel count gives

```math
\begin{gathered}
\frac1{Q^2}\sum_{u,v\bmod Q}\theta_\ell(u,v)=\frac{T_{k,\ell}}{Q^3},\\
A_\ell=\frac{T_{k,\ell}}{Q^3}\prod_{p\nmid Q}(1-p^{-2}).
\end{gathered}
```

### 6.2. Summation and the constant

Counting permitted residue classes in (4.8) costs
$O_k(1)$ per primitive pair. Both the actual support and the model support lie in
$S(u,v)\le C_kX^{3/2}$, apart from the finite set already covered by Lemma 4.1. By (4.9), all these errors total
$O_k(X)$. Removing the
$-1$ from the positive part costs at most one per pair on the model support, again
$O_k(X)$. Therefore

**Equation (6.2).**

```math
\begin{aligned}
E_k(N)&=2\sum_{\ell\mid2k}X_\ell
\sum_{\substack{u\lt v,\ \gcd(u,v)=1\\
S(u,v)\le X_\ell^{3/2}}}
\frac{\theta_\ell(u,v)}{S(u,v)^{2/3}}\\
&\quad+O_k(X).
\end{aligned}
```

The factor two records the determinant signs; uniqueness was already imposed by lexicographic reduction and its boundary has been accounted for. Applying Lemma 5.1 yields

**Equation (6.3).**

```math
E_k(N)=XJ\left(\sum_{\ell\mid2k}\frac{A_\ell}{\ell}\right)\log X+O_k(X).
```

Define the finite-residue density

**Equation (6.4).**

```math
\Delta(k)=\frac1{Q^3}\prod_{p\mid Q}(1-p^{-2})^{-1}
\sum_{\ell\mid2k}\frac{T_{k,\ell}}{\ell}.
```

Then
$\sum_{\ell\mid2k}A_\ell/\ell=\Delta(k)/\zeta(2)$. Since
$X=(k^2N/4)^{1/3}$,

**Equation (6.5).**

```math
\begin{aligned}
E_k(N)&=\frac{J}{3\cdot4^{1/3}\zeta(2)}\,k^{2/3}\Delta(k)N^{1/3}\log N\\
&\quad+O_k(N^{1/3}).
\end{aligned}
```

The identities
$\zeta(2)=\pi^2/6$ and
$\Gamma(1/3)\Gamma(2/3)=2\pi/\sqrt3$ give

```math
\frac{J}{3\cdot4^{1/3}\zeta(2)}=\frac{2^{4/3}}{3\Gamma(2/3)^3}=K.
```

Combining (6.5) with Corollary 3.4, choosing
$0\lt \varepsilon\lt 1/12$, proves the asymptotic in Theorem 1.1. It remains to evaluate the density and establish its stated properties.

## 7. Explicit local factors

For a prime
<var>p</var> and an integer
<var>w</var>, define

**Equation (7.1).**

```math
G_p(w)=\begin{cases}
1,&w\le0,\\
\frac{3p^{1-w}}{p+1},&w\ge1.
\end{cases}
```

For
$w\ge1$, this is the conditional proportion of primitive pairs over
$ℤ_p$ for which at least one of
$u,v,u+v$ is divisible by
$p^w$. The three alternatives are disjoint, each with probability

```math
\frac{p^{-w}(1-p^{-1})}{1-p^{-2}}=\frac{p^{1-w}}{p+1}.
```

All these proportions can equivalently be taken in finite residue rings of sufficiently large prime-power modulus.

For odd
<var>p</var> and
$e\ge0$, put

**Equation (7.2).**

```math
\delta_p(e)=p^{-e}+(1-p^{-1})\sum_{j=0}^{e-1}p^{-j}
G_p\!\left(e-\left\lfloor\frac{3j}{2}\right\rfloor\right),
```

where the sum is empty if
$e=0$. At
$p=2$, put

**Equation (7.3).**

```math
\delta_2(e)=2^{-e-1}+\frac12\sum_{j=0}^{e}2^{-j}
G_2\!\left(e-1-\left\lfloor\frac{3j}{2}\right\rfloor\right).
```

**Proposition 7.1**.  The density in (6.4) is

**Equation (7.4).**

```math
\Delta(k)=\delta_2(\mathrm{v}_2(k))\prod_{\substack{p\mid k\\
p\text{ odd}}}\delta_p(\mathrm{v}_p(k)).
```

It is rational, positive and multiplicative, with
$k^{-1}\le\Delta(k)\le1$.

*Proof.* In (6.1), first condition on
$(u,v)$ being primitive at
<var>p</var>. Fix
$\ell$, and write
$e=\mathrm{v}_p(k)$,
$j=\mathrm{v}_p(\ell)$.

Suppose
<var>p</var> is odd, so
$0\le j\le e$. If
$j=e$, the determinant is a
<var>p</var> adic unit, so
$(s,t)$ is automatically primitive. The divisibility condition is automatic because
$a,b,r$ are divisible by
$p^e$. Including the weight
$p^{-j}$ gives the contribution
$p^{-e}$.

For
$j\lt e$, put
$h=e-j\gt 0$ and
$\rho=k/\ell$, interpreted
<var>p</var> adically. Thus
$\mathrm{v}_p(\rho)=h$ and
$ut-vs=2\rho$. Modulo
<var>p</var>, the second vector is a scalar multiple of the primitive first vector. The second primitivity condition removes the zero scalar, leaving proportion
$1-p^{-1}$. After extracting
$\ell^3$ from the height numerator, the required condition is

**Equation (7.5).**

```math
\mathrm{v}_p\bigl((vs+\rho)(us+vs+\rho)(vt+vs+\rho)\bigr)\ge2e-3j.
```

If
$2e-3j\le0$, there is no further restriction. Otherwise let

```math
w=\left\lceil\frac{2e-3j}{2}\right\rceil=e-\left\lfloor\frac{3j}{2}\right\rfloor\le h.
```

Under both primitivity conditions, (7.5) is equivalent to

**Equation (7.6).**

```math
p^w\mid uv(u+v).
```

To verify this without discarding cancellation cases, at most one of
$u,v,u+v$ is divisible by
<var>p</var>. If none is, all three factors in (7.5) are units. If
$p\mid u$, then
$v,t,s+t$ are units, and two factors are

```math
\begin{gathered}
vs+\rho=ut-\rho,\\
us+vs+\rho=u(s+t)-\rho.
\end{gathered}
```

If
$\mathrm{v}_p(u)\lt w$, both have valuation exactly
$\mathrm{v}_p(u)$, whereas the third factor is a unit; their total valuation is too small. If
$\mathrm{v}_p(u)\ge w$, both are divisible by
$p^w$, which is enough even if cancellation raises their valuations. The case
$p\mid v$ is analogous. If
$p\mid u+v$, all four coordinates are units; the two relevant factors are

```math
\begin{gathered}
s(u+v)+\rho,\\
\frac{vs(u+v)+\rho(2v+u)}{u}.
\end{gathered}
```

The same argument applies since
$w\le h$. This includes the threshold
$w=h$. Hence the conditional proportion for
$j\lt e$ is
$(1-p^{-1})G_p(e-\lfloor3j/2\rfloor)$, proving (7.2) after weighting by
$p^{-j}$.

At
$p=2$, one has
$0\le j\le e+1$. If
$j=e+1$, the determinant is odd and
$(s,t)$ is automatically primitive. The numbers
$a,b$ are divisible by
$2^{e+1}$, while
$r=\ell vs+k$ has valuation
<var>e</var>. Divisibility is automatic, giving contribution
$2^{-e-1}$. For
$j\le e$, put
$h=e+1-j\gt 0$. The second-vector primitivity proportion is
$1/2$, and
$\mathrm{v}_2(\rho)=h-1$. The factor four in the numerator changes the required valuation to
$L=2e-3j-2$. If
$L\gt 0$,

```math
w=\left\lceil\frac L2\right\rceil=e-1-\left\lfloor\frac{3j}{2}\right\rfloor
=h-2-\left\lfloor\frac j2\right\rfloor\lt h-1.
```

The preceding valuation check therefore applies and gives the additional proportion
$G_2(w)$. If
$L\le0$, that proportion is one. Summing the weighted contributions proves (7.3).

The Chinese remainder theorem separates the finite residue count. The factors
$(1-p^{-2})^{-1}$ in (6.4) remove the density of primitive first vectors, and the sum over
$\ell\mid2k$ factors into independent sums over prime valuations. The criteria no longer involve unit parts of
$k/\ell$, so (7.4) follows.

Since
$0\lt G_p(w)\le1$, the geometric sums give
$\delta_p(e)\le1$. For odd
<var>p</var>, the first term gives
$\delta_p(e)\ge p^{-e}$. At
$p=2$, the first term and the
$j=e$ term give
$\delta_2(e)\ge2^{-e}$. Finally
$\delta_p(0)=1$ for every prime, including
$2$. These observations prove all the assertions. ◻

For an odd prime
<var>p</var>,
$\Delta(p)=(4p-2)/(p(p+1))$. Table 1 contains exact rational evaluations of the finite sums. This completes the proof of Theorem 1.1.

**Table 1. Selected exact local factors.**

| p | e = 0 | e = 1 | e = 2 | e = 3 | e = 4 |
|---|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 3/4 | 1/2 |
| 3 | 1 | 5/6 | 4/9 | 2/9 | 7/54 |
| 5 | 1 | 3/5 | 1/5 | 9/125 | 19/625 |
| 7 | 1 | 13/28 | 11/98 | 23/686 | 109/9604 |

## 8. The nonsquare regular subfamily

The general nonsquare count already follows from Corollary 3.4. The additional result in this section is a stronger height gap for the upper-regular smallest triple.

**Lemma 8.1**.  For any
$D(n)$ quadruple, let
$x^2=ad+n$,
$y^2=bd+n$,
$z^2=cd+n$ and
$q=z-x-y$. Then

**Equation (8.1).**

```math
d\mid(q^2-n)(q^2-9n).
```

If
<var>n</var> is nonsquare, the right side is nonzero, and

**Equation (8.2).**

```math
d\le\left\vert (q^2-n)(q^2-9n)\right\vert .
```

*Proof.* In
$ℤ/dℤ$, put
$\alpha=-x$,
$\beta=-y$,
$\gamma=z$, and
$E=\alpha\beta+\alpha\gamma+\beta\gamma$. Then
$\alpha^2=\beta^2=\gamma^2=n$,
$q=\alpha+\beta+\gamma$, and

```math
\begin{gathered}
q^2=3n+2E,\\
E^2=3n^2+2\alpha\beta\gamma q=3n^2+2nE.
\end{gathered}
```

Therefore
$(q^2-n)(q^2-9n)=4(E^2-2nE-3n^2)=0$ in this ring. No inversion or parity assumption is used. If
$q^2=n$ or
$q^2=9n$ in
$ℤ$, then
<var>n</var> is an integer square; in the latter case
$3\mid q$. For nonsquare
<var>n</var>, a nonzero multiple of
<var>d</var> has absolute value at least
<var>d</var>. ◻

**Proposition 8.2**.  Let
<var>n</var> be nonsquare and
$M=\vert n\vert$. Every quadruple with upper-regular smallest triple satisfies

**Equation (8.3).**

```math
d\ge\frac{(abc)^2}{625M^4(M+1)(9M+1)}.
```

Consequently
$R_n(N)\ll_{n,\varepsilon}N^{1/6+\varepsilon}$.

*Proof.* By (3.7),
$q^2\ge1$ and
$q^2\le25M^2d/(abc)$. Thus

```math
\begin{aligned}
&\left\vert (q^2-n)(q^2-9n)\right\vert\\
&\le(q^2+M)(q^2+9M)\\
&\le(M+1)(9M+1)q^4.
\end{aligned}
```

Combining with (8.2) and cancelling
$d\gt 0$ gives (8.3). Since
$abc\ge(ab)^{3/2}$, the condition
$d\le N$ implies
$ab\ll_n N^{1/3}$ and
$r\ll_n N^{1/6}$. Factor
$ab=r^2-n$ to count first pairs;
$c=a+b+2r$ is determined, and Corollary 2.2 bounds the choices for
<var>d</var>. The divisor bound and a relabelling of
$\varepsilon$ prove the claim. ◻

Together with Proposition 3.2 and Corollary 3.4, this proves Theorem 1.2. Equation (8.3) is a *lower* bound on
<var>d</var>, not a bound depending only on
<var>n</var>. Neither the divisibility relation nor the counting estimates provide a descent preserving all six square conditions.

## 9. Ancillary exact verification

The accompanying script `verify_problem_1_7.py` performs exact symbolic and arithmetic checks for the identities and finite computations used above. The symbolic portion requires SymPy; all remaining checks use only Python's standard library. From this directory, run:

```console
python3 -m pip install sympy
python3 verify_problem_1_7.py --full
```

The complete run checks 21 symbolic identities, enumerates the 613 quadruples described below, verifies the six principal-family counts in Table 2, and compares the global residue formula with the product of local factors for every integer from 1 through 9. Square roots equal to zero are included. The nonsymbolic checks can be run separately with:

```console
python3 verify_problem_1_7.py --graphs --principal --residue-max 9
```

For the 200 nonzero integers
$n\in[-100,100]$, exhaustive enumeration with
$d\le500$ found 613 quadruples. Every applicable invariant, divisibility identity and explicit height inequality proved above was verified for each quadruple. For square parameters, the principal construction agreed exactly with the corresponding subfamily in the graph enumeration. Independently, the global residue count (6.4), computed without the local valuation criteria, agreed with (7.4) for every
$1\le k\le9$.

**Table 2. Exact principal-family counts at N = 10⁹.** These are counts of the principal family, not counts of all quadruples.

| k | Density factor | Principal-family count |
|---|---|---|
| 1 | 1 | 3620 |
| 2 | 1 | 6178 |
| 3 | 5/6 | 6368 |
| 4 | 1 | 10652 |
| 5 | 3/5 | 6140 |
| 8 | 3/4 | 12448 |

Every object in Table 2 was checked for all six square conditions, the exact height formula and the reduced parametrization. These computations are supplementary to the proofs; the asymptotic formula and the uniform Pell estimate are established in the preceding sections.

## A. An upper-regular largest triple

This appendix concerns a different subfamily from Section 8. Its conclusion applies to square and nonsquare parameters alike.

**Theorem A.1**.  Let
$M=\vert n\vert$. If
$0\lt a\lt b\lt c\lt d$ is a
$D(n)$ quadruple and

```math
\begin{gathered}
d=b+c+2t,\\
t^2=bc+n,\\
t\ge0,
\end{gathered}
```

then
$d\lt 10^4M^3$. In particular, for each fixed
<var>n</var> there are only finitely many such quadruples.

*Proof.* By (3.5),
$ab\le25M^2$, hence
$a,b\le25M^2$. Put

```math
\begin{gathered}
v=\sqrt{ac+n},\\
w=\sqrt{ad+n},\\
h=w-v\gt 0,\\
\eta=h^2-ab.
\end{gathered}
```

Subtracting the square equations gives
$2hv+h^2=a(b+2t)$, hence
$\eta+2hv=2at$. It follows that

**Equation (A.1).**

```math
\eta(4ac+4hv+\eta)=4n(a^2-h^2).
```

For verification, replace
$\eta(\eta+4hv)$ by
$(\eta+2hv)^2-4h^2v^2$ and use
$v^2=ac+n$,
$t^2=bc+n$, and
$\eta=h^2-ab$.

If
$\eta=0$, (A.1) and
$n\ne0$ force
$a^2=h^2=ab$, contrary to
$a\lt b$. Thus
$\vert \eta\vert \ge1$. Also
$4ac+4hv+\eta\ge4ac-ab\gt 3ac$, giving

**Equation (A.2).**

```math
3ac\lt 4M(a^2+h^2).
```

If
$ac\le2M$, then
$c\le2M$ and
$d\le4c+2\sqrt M\le8M+2\sqrt M\lt 10^4M^3$. Otherwise
$v\gt \sqrt{ac/2}$. Since
$t\le\sqrt{bc}+\sqrt M$,

```math
\begin{aligned}
h&=\frac{a(b+2t)}{w+v}\\
&\le\sqrt{\frac{2a}{c}}\,(b+2\sqrt{bc}+2\sqrt M)\\
&\le\sqrt{2a}\,(3\sqrt b+2\sqrt M).
\end{aligned}
```

Using
$(x+y)^2\le2x^2+2y^2$ gives
$h^2\le36ab+16aM$. Substitution into (A.2) and cancellation of
<var>a</var> yield

```math
\begin{aligned}
c&\lt \frac{4M}{3}(a+36b+16M)\\
&\le\frac{4M}{3}(925M^2+16M)\\
&\lt 1255M^3.
\end{aligned}
```

Finally
$d\le4c+2\sqrt M\lt 10^4M^3$. ◻

**Remark A.2** (Sharpness of the cubic exponent).  A family of Dujella and Petričević (2019, Section 2) shows that the exponent three cannot be replaced by a smaller exponent in a bound uniform over
<var>n</var> for this subfamily. With an integer parameter
<var>h</var> tending to
$+\infty$, their family has
$a=1$ and

```math
\begin{aligned}
n&=-64h^2+16h+16,\\
b&=256h^4-128h^3-48h^2+16h,\\
c&=4096h^6-4096h^5-512h^4\\
&\quad+1152h^3+16h^2-88h-7,\\
d&=4096h^6-2048h^5-1792h^4\\
&\quad+640h^3+288h^2-48h-15.
\end{aligned}
```

For sufficiently large
<var>h</var>, these entries satisfy
$0\lt a\lt b\lt c\lt d$ and
$n\lt 0$. Direct substitution gives

```math
\begin{aligned}
&\frac{d-b-c}{2}\\
&=4(4h^2-h-1)(64h^3-32h^2-4h+1)\\
&=t\gt 0,
\end{aligned}
```

and
$t^2=bc+n$. Thus their largest triple is upper-regular. Since
$d/\vert n\vert ^3\to1/64$, no uniform bound
$d\le C\vert n\vert ^\alpha$ with
$\alpha\lt 3$ can hold for this subfamily. Here
<var>n</var> varies with
<var>h</var>; this comparison makes no claim of infinitude at a fixed nonsquare parameter.

## References

N. Adžaga, G. Dražić, A. Dujella and A. Pethő (2025). Asymptotics of D(q)-pairs and triples via L-functions of Dirichlet characters. *The Ramanujan Journal* **66**, Article 11. DOI: 10.1007/s11139-024-00979-3. Preprint: arXiv:2304.01775v2.

J. Badesa (2025). On the asymptotics of D(n)-pairs and triples. *The Ramanujan Journal* **67**, Article 101. DOI: 10.1007/s11139-025-01149-9.

G. Dražić, M. Kazalicki and R. Mrazović (2026). Equidistribution of Diophantine pairs among the equivalence classes of quadratic forms. *Research in Number Theory* **12**, Article 85. DOI: 10.1007/s40993-026-00776-5. Preprint: arXiv:2512.22902.

A. Dujella (2008). On the number of Diophantine m-tuples. *The Ramanujan Journal* **15**, 37-46. DOI: 10.1007/s11139-007-9066-0.

A. Dujella (2026). *Open problems on Diophantine m-tuples and elliptic curves*. University of Zagreb, [online problem list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf), Problem 1.7; consulted 14 October 2026. Companion to *Diophantine m-tuples and Elliptic Curves*, Springer, 2024.

A. Dujella and V. Petričević (2019). On the largest element in D(n)-quadruples. *Indagationes Mathematicae* **30**, 1079-1086. DOI: 10.1016/j.indag.2019.08.003. Preprint: arXiv:1904.06532.

G. Martin and S. Sitar (2011). Erdős-Turán with a moving target, equidistribution of roots of reducible quadratics, and Diophantine quadruples. *Mathematika* **57**, 1-29. DOI: 10.1112/S0025579310001580. Preprint: arXiv:0903.1834.
