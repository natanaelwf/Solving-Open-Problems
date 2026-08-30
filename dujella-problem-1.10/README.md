# Jordan Diophantine Tuples in 2 × 2 Integer Matrix Rings

## Results for Dujella's Problem 1.10

**Publication date:** 30 August 2026  
**Status:** Complete solution of the stated existence problem under the integral Jordan-product interpretation  
**Field:** Number theory, noncommutative Diophantine tuples, integer matrix rings  

## Abstract

Problem 1.10 in Dujella's list asks for an analogue of a classical $`D(n)`$ tuple of size $`m`$ in a noncommutative ring and for nontrivial existence results, suggesting 2 × 2 integer matrices and the Jordan product as a test case. We formulate an integral Jordan-square condition that does not require division by 2 inside the ring. In commutative rings without additive 2-torsion, it agrees with the classical definition, and the regular-extension identity remains valid without any commutativity assumption.

For the full ring $`M_2(\mathbb{Z})`$, consider the countably infinite family

```math
X_t=
\begin{pmatrix}
1&t\\
0&-1
\end{pmatrix},
\qquad t\in\mathbb{Z}.
```

Its members are pairwise noncommuting involutions. Every pair has Jordan product $`I_2`$, while every scalar integer matrix is a square in $`M_2(\mathbb{Z})`$. Consequently, this same family is a Jordan family with parameter $`nI_2`$ for every integer $`n`$.

We also determine exactly when a scalar parameter admits a quadruple in the upper-triangular ring $`\mathrm{UT}_2(\mathbb{Z})`$. A Jordan quadruple with parameter $`nI_2`$ exists if and only if

```math
n\not\equiv 2\pmod 4,
```

equivalently, if and only if $`nI_2`$ is a difference of two squares in $`\mathrm{UT}_2(\mathbb{Z})`$. Whenever such a quadruple exists, it can be chosen pairwise noncommuting. For every admissible $`n`$ except $`n=1`$ and $`n=4`$, the proof gives a countably infinite family. A separate construction covers those two parameters. A final extension supplies infinite families whenever $`N+a^2I_2`$ is a square for some nonzero integer $`a`$, including cases in which $`N`$ is noncentral.

**Keywords.** Diophantine tuples; Jordan product; noncommutative rings; integer matrices; upper-triangular matrices; involutions.

## 1. Introduction

Let $`R`$ be a commutative ring and let $`n\in R`$. A classical tuple of size $`r`$ with property $`D(n)`$ is a set of distinct nonzero elements

```math
\lbrace a_1,\ldots,a_r\rbrace\subseteq R
```

such that $`a_i a_j+n`$ is a square in $`R`$ whenever $`i<j`$; see [1] for background.

Problem 1.10 in Dujella's list asks for a noncommutative analogue and for nontrivial results concerning the existence of quadruples, naming the ring of 2 × 2 integer matrices as a test case [2]. The problem records the proposal of Dujella and Franušić to use the Jordan product

```math
A\circ B=\frac{AB+BA}{2}.
```

Their motivating paper points more specifically toward upper-triangular integer matrices [3]. Whenever an integer $`n`$ is used below as a matrix parameter, it is identified with the central matrix $`nI_2`$. We distinguish throughout between the full ring $`M_2(\mathbb{Z})`$ and its upper-triangular subring $`\mathrm{UT}_2(\mathbb{Z})`$, because a square root in the full ring need not lie in the upper-triangular subring.

Two issues deserve explicit treatment. First, $`(AB+BA)/2`$ need not have integer entries, so an integral definition should not silently pass to a larger coefficient ring. Second, an existence result is more informative when the displayed matrices genuinely fail to commute rather than merely reproducing a commutative example inside scalar or diagonal matrices.

The first main result concerns the full matrix ring. For every integer $`n`$, one countably infinite family supplies pairwise noncommuting Jordan tuples of every finite size with parameter $`nI_2`$, and every member is an involution in $`\mathrm{GL}_2(\mathbb{Z})`$. The proof rests on the identities

```math
X_s\circ X_t=I_2\quad(s\ne t),
\qquad
\begin{pmatrix}
0&q\\
1&0
\end{pmatrix}^{\!2}
=qI_2\quad(q\in\mathbb{Z}).
```

The second identity is a feature of the full ring and remains valid for negative $`q`$.

The upper-triangular ring exhibits a sharper arithmetic distinction. Comparing diagonal entries projects every Jordan condition with parameter $`nI_2`$ in $`\mathrm{UT}_2(\mathbb{Z})`$ to necessary ordinary integer-square conditions. A parity argument rules out quadruples when $`n\equiv2\pmod4`$. Conversely, explicit pairwise noncommuting constructions give quadruples for every other residue class, yielding an exact scalar-parameter criterion in the upper-triangular ring. In the excluded congruence class, leaving the upper-triangular ring at the square-root stage is therefore unavoidable, rather than an artifact of the full-ring construction.

The scope of the conclusions is deliberate. This article addresses the full-matrix existence example in Problem 1.10 and gives an exact upper-triangular criterion for scalar parameters $`nI_2`$, equivalently characterizing when $`nI_2`$ is a difference of two squares in $`\mathrm{UT}_2(\mathbb{Z})`$. It does not classify arbitrary matrix parameters $`N`$ in either $`M_2(\mathbb{Z})`$ or $`\mathrm{UT}_2(\mathbb{Z})`$; Section 5 records only a broad sufficient condition and an explicit noncentral example.

## 2. An integral Jordan condition

Throughout this section, $`\mathcal{A}`$ denotes an associative unital ring whose additive group has no 2-torsion, so that $`2x=0`$ implies $`x=0`$. Let $`N\in\mathcal{A}`$ be fixed.

**Definition 2.1 (Integral Jordan condition).** A set of distinct nonzero elements

```math
\lbrace A_1,\ldots,A_r\rbrace\subseteq\mathcal{A}
```

is a Jordan tuple of size $`r`$ with parameter $`N`$, also denoted a $`D^{\circ}(N)`$ tuple, if for every $`i<j`$ there exists $`R_{ij}\in\mathcal{A}`$ such that

```math
A_iA_j+A_jA_i+2N=2R_{ij}^{2}.
\qquad\text{(1)}
```

We write $`A_i\circ A_j+N=R_{ij}^{2}`$ as shorthand for (1); the doubled identity is the definition inside $`\mathcal{A}`$.

**Proposition 2.2 (Compatibility with the classical definition).** If $`\mathcal{A}`$ is commutative, then Definition 2.1 is exactly the classical condition with parameter $`N`$.

*Proof.* In a commutative ring, equation (1) becomes

```math
2(A_iA_j+N)=2R_{ij}^{2}.
```

Multiplication by 2 is injective on the additive group of $`\mathcal{A}`$, so cancellation gives

```math
A_iA_j+N=R_{ij}^{2}.
```

This is the classical condition.

**Remark 2.3 (Interpretation after adjoining one half).** Equation (1) itself gives

```math
A_iA_j+A_jA_i=2\bigl(R_{ij}^{2}-N\bigr).
```

Hence the anticommutator of every admissible pair has a unique half in $`\mathcal{A}`$, namely $`R_{ij}^{2}-N`$. Equivalently, the natural map

```math
\mathcal{A}\longrightarrow
\mathcal{A}\otimes_{\mathbb{Z}}\mathbb{Z}[1/2]
```

is injective under the hypothesis that the additive group has no 2-torsion. In this localization, equation (1) becomes

```math
\frac{A_iA_j+A_jA_i}{2}+N=R_{ij}^{2}.
```

Thus Definition 2.1 is the literal Jordan-square condition with both the Jordan product and its square root represented inside the original ring.

**Definition 2.4 (Pairwise noncommuting families).** A $`D^{\circ}(N)`$ tuple is pairwise noncommuting if

```math
[A_i,A_j]:=A_iA_j-A_jA_i\ne0
```

for every $`i\ne j`$. An infinite $`D^{\circ}(N)`$ family is an infinite set every finite subset of which is a $`D^{\circ}(N)`$ tuple.

The regular extension displayed in Problem 1.10 remains valid with an arbitrary fixed parameter $`N`$.

**Proposition 2.5 (Regular triple).** Suppose $`A,B,R,N\in\mathcal{A}`$ satisfy $`A\circ B+N=R^2`$ in the sense of Definition 2.1. Set

```math
C=A+B+2R.
```

Then

```math
A\circ C+N=(A+R)^2,
\qquad
B\circ C+N=(B+R)^2.
```

Consequently, if $`A`$, $`B`$, and $`C`$ are distinct and nonzero, then they form a $`D^{\circ}(N)`$ triple.

*Proof.* The hypothesis is

```math
AB+BA+2N=2R^2.
```

Using $`C=A+B+2R`$, we obtain

```math
\begin{aligned}
AC+CA+2N
&=2A^2+(AB+BA)+2(AR+RA)+2N\\
&=2A^2+2R^2+2(AR+RA)\\
&=2(A+R)^2.
\end{aligned}
```

This is the first identity in the sense of Definition 2.1. The second follows by the same calculation with $`A`$ replaced by $`B`$.

## 3. A universal family in the full matrix ring

The decisive feature of $`M_2(\mathbb{Z})`$ is that every scalar integer matrix is a square, regardless of sign.

**Lemma 3.1 (Scalar matrices are squares in the full ring).** For every $`q\in\mathbb{Z}`$, define

```math
Q_q:=
\begin{pmatrix}
0&q\\
1&0
\end{pmatrix}.
```

Then

```math
Q_q^2=qI_2.
```

*Proof.* This follows immediately by direct multiplication.

**Theorem 3.2 (Universal pairwise noncommuting family).** For $`t\in\mathbb{Z}`$, define

```math
X_t:=
\begin{pmatrix}
1&t\\
0&-1
\end{pmatrix}.
\qquad\text{(2)}
```

Then

```math
\mathcal{X}:=\lbrace X_t:t\in\mathbb{Z}\rbrace
```

has the following properties.

1. Every $`X_t`$ is an involution in $`\mathrm{GL}_2(\mathbb{Z})`$.
2. Distinct members of $`\mathcal{X}`$ do not commute.
3. For every integer $`n`$, every finite subset of distinct members of $`\mathcal{X}`$ is a $`D^{\circ}(nI_2)`$ tuple in $`M_2(\mathbb{Z})`$.

Consequently, for every integer $`n`$ and every $`r\ge2`$, there exists a pairwise noncommuting $`D^{\circ}(nI_2)`$ tuple of size $`r`$ consisting entirely of involutions in $`\mathrm{GL}_2(\mathbb{Z})`$.

*Proof.* For every integer $`t`$,

```math
X_t^2=
\begin{pmatrix}
1&t\\
0&-1
\end{pmatrix}^{\!2}
=I_2,
```

so $`X_t^{-1}=X_t`$, proving the first assertion. For integers $`s`$ and $`t`$,

```math
X_sX_t=
\begin{pmatrix}
1&t-s\\
0&1
\end{pmatrix},
\qquad
X_tX_s=
\begin{pmatrix}
1&s-t\\
0&1
\end{pmatrix}.
```

Hence

```math
X_sX_t+X_tX_s=2I_2.
\qquad\text{(3)}
```

and

```math
[X_s,X_t]=2(t-s)E_{12}.
\qquad\text{(4)}
```

Here $`E_{ij}`$ denotes the standard 2 × 2 matrix unit. If $`s\ne t`$, equation (4) is nonzero, proving the second assertion.

Fix an integer $`n`$. For distinct $`s`$ and $`t`$, equation (3) gives $`X_s\circ X_t=I_2`$. By Lemma 3.1,

```math
X_s\circ X_t+nI_2=(n+1)I_2=Q_{n+1}^{2}.
```

Thus every pair satisfies Definition 2.1, with the same square root $`Q_{n+1}`$. This proves the third assertion and the final conclusion.

**Remark 3.3.** There is no hidden divisibility issue: equation (3) shows that

```math
\frac{X_sX_t+X_tX_s}{2}=I_2
```

already belongs to $`M_2(\mathbb{Z})`$. Negative values of $`n+1`$ cause no obstruction because Lemma 3.1 applies to every integer $`q`$.

**Corollary 3.4 (An explicit quadruple for every integer parameter).** For every integer $`n`$, define

```math
\begin{aligned}
X_0&=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
&X_1&=\begin{pmatrix}1&1\\0&-1\end{pmatrix},\\
X_2&=\begin{pmatrix}1&2\\0&-1\end{pmatrix},
&X_3&=\begin{pmatrix}1&3\\0&-1\end{pmatrix}.
\end{aligned}
```

These four matrices form a pairwise noncommuting $`D^{\circ}(nI_2)`$ quadruple in $`M_2(\mathbb{Z})`$. For every pair, one may take

```math
Q_{n+1}=
\begin{pmatrix}
0&n+1\\
1&0
\end{pmatrix}
```

as a square root of the shifted Jordan product.

*Proof.* Take $`t=0,1,2,3`$ in Theorem 3.2.

**Corollary 3.5 (No finite upper bound).** For every integer $`n`$, the cardinalities of pairwise noncommuting $`D^{\circ}(nI_2)`$ tuples in $`M_2(\mathbb{Z})`$ are unbounded, even when every element is required to be an involution in $`\mathrm{GL}_2(\mathbb{Z})`$.

*Proof.* Choose any prescribed number of distinct integers $`t`$ and apply Theorem 3.2.

## 4. The upper-triangular ring

Let

```math
\mathrm{UT}_2(\mathbb{Z})=
\lbrace
\begin{pmatrix}
a&b\\
0&d
\end{pmatrix}
\mathrel{:}a,b,d\in\mathbb{Z}
\rbrace.
```

Although every $`X_t`$ from Theorem 3.2 belongs to $`\mathrm{UT}_2(\mathbb{Z})`$, the square roots $`Q_{n+1}`$ used there generally do not. The diagonal entries provide an immediate bridge back to ordinary integer-square conditions.

**Lemma 4.1 (Diagonal projection).** Let $`\lbrace A_1,\ldots,A_r\rbrace`$ be a $`D^{\circ}(nI_2)`$ tuple in $`\mathrm{UT}_2(\mathbb{Z})`$, and write

```math
A_i=
\begin{pmatrix}
a_i&b_i\\
0&d_i
\end{pmatrix}.
```

Then, for every $`i<j`$, both $`a_i a_j+n`$ and $`d_i d_j+n`$ are squares in $`\mathbb{Z}`$.

*Proof.* Choose

```math
R_{ij}=
\begin{pmatrix}
x_{ij}&y_{ij}\\
0&z_{ij}
\end{pmatrix}
\in\mathrm{UT}_2(\mathbb{Z})
```

as in Definition 2.1. Comparing the two diagonal entries in

```math
A_iA_j+A_jA_i+2nI_2=2R_{ij}^{2}
```

and cancelling 2 gives

```math
a_i a_j+n=x_{ij}^{2},
\qquad
d_i d_j+n=z_{ij}^{2}.
```

**Proposition 4.2 (A congruence obstruction).** If $`n\equiv2\pmod4`$, then every $`D^{\circ}(nI_2)`$ tuple in $`\mathrm{UT}_2(\mathbb{Z})`$ has at most three elements. In particular, no Jordan quadruple with parameter $`nI_2`$ exists in the upper-triangular ring.

*Proof.* There is nothing to prove when $`r\le3`$, so suppose $`r\ge4`$. Use the integers $`a_i`$ from Lemma 4.1. For every $`i<j`$, the integer $`a_i a_j+n`$ is a square, hence is congruent to 0 or 1 modulo 4.

No $`a_i`$ can be divisible by 4, since then $`a_i a_j+n\equiv2\pmod4`$ for every $`j\ne i`$. Thus every even $`a_i`$ is congruent to 2 modulo 4, and two even entries cannot occur because their product is divisible by 4. Hence at most one $`a_i`$ is even.

For two odd entries, their product must be congruent to 3 modulo 4; otherwise the shifted product is congruent to 3 modulo 4. Therefore any two odd entries must lie in opposite residue classes modulo 4, so there can be at most two of them. Altogether $`r\le3`$.

The converse construction begins with a nontrivial representation of the parameter as a difference of two squares.

**Proposition 4.3 (An infinite family from a difference of squares).** Let $`a,b,n\in\mathbb{Z}`$ satisfy $`a\ne0`$ and

```math
n=b^2-a^2.
```

For $`t\in\mathbb{Z}`$, set

```math
Y_t^{(a)}:=
\begin{pmatrix}
a&t\\
0&-a
\end{pmatrix}.
```

Then

```math
\mathcal{Y}_a:=\lbrace Y_t^{(a)}:t\in\mathbb{Z}\rbrace
```

is a countably infinite pairwise noncommuting $`D^{\circ}(nI_2)`$ family in $`\mathrm{UT}_2(\mathbb{Z})`$.

*Proof.* For integers $`s`$ and $`t`$, direct multiplication gives

```math
Y_s^{(a)}\circ Y_t^{(a)}=a^2I_2,
\qquad
[Y_s^{(a)},Y_t^{(a)}]=2a(t-s)E_{12}.
```

Thus distinct members do not commute because $`a\ne0`$. Moreover,

```math
\begin{aligned}
Y_s^{(a)}\circ Y_t^{(a)}+nI_2
&=(a^2+n)I_2\\
&=b^2I_2\\
&=(bI_2)^2,
\end{aligned}
```

with the same upper-triangular square root for every pair.

Two small scalar parameters cannot be reached by Proposition 4.3, because the only representations of 1 or 4 as $`b^2-a^2`$ have $`a=0`$. They are covered by the following general lift.

**Proposition 4.4 (A noncommuting lift of classical tuples).** Let $`\lbrace c_1,\ldots,c_r\rbrace\subset\mathbb{Z}`$ be a classical tuple of size $`r`$ with property $`D(n)`$, and define

```math
A_i:=
\begin{pmatrix}
c_i&c_i^2\\
0&-c_i
\end{pmatrix}.
```

Then $`\lbrace A_1,\ldots,A_r\rbrace`$ is a pairwise noncommuting $`D^{\circ}(nI_2)`$ tuple of size $`r`$ in $`\mathrm{UT}_2(\mathbb{Z})`$.

*Proof.* The matrices are distinct and nonzero because the integers $`c_i`$ are distinct and nonzero. For $`i\ne j`$, direct multiplication gives

```math
A_i\circ A_j=c_i c_jI_2,
\qquad
[A_i,A_j]=2c_i c_j(c_j-c_i)E_{12}\ne0.
```

If $`c_i c_j+n=r_{ij}^{2}`$, then

```math
A_i\circ A_j+nI_2=(r_{ij}I_2)^2
```

inside $`\mathrm{UT}_2(\mathbb{Z})`$.

**Theorem 4.5 (Scalar-parameter classification in the upper-triangular ring).** For $`n\in\mathbb{Z}`$, the following statements are equivalent.

1. A Jordan quadruple with parameter $`nI_2`$ exists in $`\mathrm{UT}_2(\mathbb{Z})`$.
2. The congruence $`n\not\equiv2\pmod4`$ holds.
3. The scalar matrix $`nI_2`$ is a difference of two squares in $`\mathrm{UT}_2(\mathbb{Z})`$.

Whenever these conditions hold, the quadruple can be chosen pairwise noncommuting. Moreover, if $`n\not\equiv2\pmod4`$ and $`n\notin\lbrace1,4\rbrace`$, then $`\mathrm{UT}_2(\mathbb{Z})`$ contains a countably infinite pairwise noncommuting $`D^{\circ}(nI_2)`$ family.

*Proof.* The implication from statement 1 to statement 2 follows from Proposition 4.2. For the converse, first suppose that $`n\not\equiv2\pmod4`$ and $`n\notin\lbrace1,4\rbrace`$. If $`n`$ is odd, take

```math
a=\frac{n-1}{2},
\qquad
b=\frac{n+1}{2}.
```

Then $`n=b^2-a^2`$, and $`a\ne0`$ because $`n\ne1`$. If $`n=4k`$, take

```math
a=k-1,
\qquad
b=k+1.
```

Again $`n=b^2-a^2`$, and $`a\ne0`$ because $`n\ne4`$. In both cases Proposition 4.3 gives the asserted infinite family.

It remains to treat $`n=1`$ and $`n=4`$. Let

```math
F=\lbrace1,3,8,120\rbrace
```

be Fermat's classical quadruple with property $`D(1)`$. Its six shifted pairwise products are

```math
2^2,\quad3^2,\quad5^2,\quad11^2,\quad19^2,\quad31^2.
```

For $`m\in\lbrace1,2\rbrace`$, the scaled set $`mF`$ is a quadruple with property $`D(m^2)`$, since

```math
(mc_i)(mc_j)+m^2=m^2(c_i c_j+1)
```

is a square for every pair. Applying Proposition 4.4 to $`F`$ and $`2F`$ gives pairwise noncommuting quadruples for $`n=1`$ and $`n=4`$, respectively.

It remains to verify the equivalence of statements 2 and 3. If $`n\not\equiv2\pmod4`$, the preceding formulas represent $`n=b^2-a^2`$ for some integers $`a`$ and $`b`$; for $`n=1`$ or $`n=4`$, one may allow $`a=0`$. Hence

```math
nI_2=(bI_2)^2-(aI_2)^2
```

in $`\mathrm{UT}_2(\mathbb{Z})`$. Conversely, suppose that

```math
nI_2=U^2-V^2
```

with $`U,V\in\mathrm{UT}_2(\mathbb{Z})`$. Comparison of either diagonal entry expresses $`n`$ as a difference of two integer squares. Such a difference is never congruent to 2 modulo 4. Thus statements 2 and 3 are equivalent.

**Remark 4.6 (The distinction between the two ambient rings).** For $`n\equiv2\pmod4`$, Theorem 3.2 gives a countably infinite pairwise noncommuting $`D^{\circ}(nI_2)`$ family in the full ring $`M_2(\mathbb{Z})`$, whereas Proposition 4.2 rules out even a quadruple in $`\mathrm{UT}_2(\mathbb{Z})`$. Thus the non-upper-triangular square roots in the full-ring construction are essential in this congruence class.

## 5. A sufficient condition for matrix parameters

The construction behind Proposition 4.3 also applies to matrix parameters that need not be central.

**Proposition 5.1.** Let $`a\in\mathbb{Z}\setminus\lbrace0\rbrace`$ and $`N\in M_2(\mathbb{Z})`$. If

```math
N+a^2I_2=S^2
```

for some $`S\in M_2(\mathbb{Z})`$, then

```math
\mathcal{Y}_a=\lbrace Y_t^{(a)}:t\in\mathbb{Z}\rbrace
```

is a countably infinite pairwise noncommuting $`D^{\circ}(N)`$ family in $`M_2(\mathbb{Z})`$. If $`N,S\in\mathrm{UT}_2(\mathbb{Z})`$, the same conclusion holds inside $`\mathrm{UT}_2(\mathbb{Z})`$.

*Proof.* For distinct integers $`s`$ and $`t`$,

```math
Y_s^{(a)}\circ Y_t^{(a)}+N=a^2I_2+N=S^2.
```

Pairwise noncommutativity follows from the commutator identity in Proposition 4.3. The final assertion is immediate because all tuple elements already lie in $`\mathrm{UT}_2(\mathbb{Z})`$.

**Remark 5.2 (An explicit noncentral example).** Take $`a=1`$ and

```math
S=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix},
\qquad
N=S^2-I_2=
\begin{pmatrix}
0&3\\
0&3
\end{pmatrix}.
```

Then $`N`$ is noncentral; for example,

```math
[N,E_{11}]=
\begin{pmatrix}
0&-3\\
0&0
\end{pmatrix}
\ne0.
```

Since $`S,N\in\mathrm{UT}_2(\mathbb{Z})`$, Proposition 5.1 supplies a countably infinite pairwise noncommuting $`D^{\circ}(N)`$ family entirely inside $`\mathrm{UT}_2(\mathbb{Z})`$.

## 6. Conclusion and scope

The doubled identity in Definition 2.1 is an integral form of the Jordan-square condition. It agrees with the classical condition in commutative rings without additive 2-torsion, and the regular-extension calculation requires no commutativity.

For the full ring $`M_2(\mathbb{Z})`$, Theorem 3.2 gives substantially more than one quadruple: for every integer $`n`$ and every $`r\ge2`$, there is a pairwise noncommuting $`D^{\circ}(nI_2)`$ tuple of size $`r`$ consisting of integral involutions, always selected from the same countably infinite family.

For the upper-triangular ring, Theorem 4.5 gives an exact answer for scalar parameters. A Jordan quadruple with parameter $`nI_2`$ exists precisely when $`n\not\equiv2\pmod4`$, equivalently precisely when $`nI_2`$ is a difference of two squares in $`\mathrm{UT}_2(\mathbb{Z})`$, and it may always be chosen pairwise noncommuting. The proof supplies infinite families for every admissible $`n`$ except 1 and 4, for which explicit pairwise noncommuting quadruples are obtained by lifting Fermat's classical example.

These results provide explicit nontrivial existence theorems for the matrix settings highlighted in Problem 1.10, while also identifying a sharp obstruction in the upper-triangular ring. They therefore address the existence part of the problem under the stated Jordan-product interpretation. No classification of arbitrary matrix parameters $`N`$ is claimed; Proposition 5.1 records the sufficient condition

```math
N+a^2I_2=S^2,
\qquad a\ne0,
```

and an explicit noncentral example.

## References

1. A. Dujella. *Diophantine m-Tuples and Elliptic Curves*. Developments in Mathematics, vol. 79, Springer, Cham, 2024.
2. A. Dujella. *Open Problems on Diophantine m-Tuples and Elliptic Curves*. Manuscript, version dated 30 August 2026.
3. A. Dujella and Z. Franušić. “Differences of Two Squares of Upper-Triangular 2 × 2 Integer Matrices.” arXiv:2604.23404v2 [math.NT], 8 May 2026.
