# Infinitely Many Rational $D(q)$-Quintuples for Every Rational $q$

## Solutions to Problems 5.7, 5.8, and 5.9

**Publication date:** 2 September 2026  
**Status:** Complete solution  
**Field:** Number theory, rational Diophantine tuples

## Abstract

We construct five distinct nonzero rational functions in $\mathbb{Q}(z)$ whose pairwise products, increased by $z$, are squares in $\mathbb{Q}(z)$. The construction is nondegenerate at every rational specialization outside a finite set. For a fixed $q\ne0$, substituting $z=qu^2$ and dividing every entry by $u$ gives a rational $D(q)$-quintuple for all but finitely many $u\in\mathbb{Q}^{\times}$. One entry is unbounded along positive integral values of $u$, so infinitely many distinct quintuples result. The case $q=0$ is elementary. At $z=1579$ the same family gives an explicit positive rational $D(1579)$-quintuple. Consequently, Problems 5.7, 5.8, and 5.9 all have affirmative answers.

## 1. Introduction

For $q\in\mathbb{Q}$, a rational $D(q)$-$m$-tuple is a set of $m$ distinct nonzero rational numbers

$$
\{x_1,\dots,x_m\}
$$

such that $x_ix_j+q$ is a square in $\mathbb{Q}$ whenever $1\le i<j\le m$.

Problems 5.7, 5.8, and 5.9 in Dujella's list ask, respectively, whether a rational $D(1579)$-quintuple exists, whether a rational $D(q)$-quintuple exists for every rational $q$, and whether infinitely many such quintuples exist for every rational $q$. These questions are naturally treated together. The construction that gives the specialization $q=1579$ has a free parameter $z$, and retaining that parameter produces a generic $D(z)$-quintuple. A square-class scaling argument then yields infinitely many $D(q)$-quintuples for every fixed $q\ne0$.

Earlier work of Dražić established, conditional on the Parity Conjecture for twists of several explicit elliptic curves, the existence of infinitely many rational $D(q)$-quintuples for a density exceeding $99.5\%$ of square classes. The result below is unconditional and covers every rational $q$.

**Theorem 1.** For every rational number $q$, there exist infinitely many rational $D(q)$-quintuples.

The proof is elementary once one has the explicit rational functions. The only lengthy calculation is a polynomial factorization displayed below. An exact verifier using integer polynomial arithmetic accompanies this manuscript.

## 2. Two algebraic construction lemmas

The following identities are valid over any field of characteristic different from $2$.

**Lemma 2.1 (Structured quadruple).** Let $F$ be a field of characteristic different from $2$, let $q,h,p\in F^{\times}$, and define

$$
D=\frac{h^2+3q}{2h},\qquad
w=\frac{h^2-3q}{2h},\qquad
X=w^2-q,
$$

$$
S=\frac{p^2+X}{2p},\qquad
r=\frac{p^2-X}{4p},\qquad
a=\frac{S+D}{2},\qquad b=\frac{S-D}{2},
$$

$$
c=p,\qquad d=\frac{X}{p}.
$$

Then

$$
\begin{aligned}
ab+q&=r^2, & ac+q&=(a+r)^2, & ad+q&=(a-r)^2,\\
bc+q&=(b+r)^2, & bd+q&=(b-r)^2, & cd+q&=w^2.
\end{aligned}
$$

Consequently, if $F=\mathbb{Q}$ and $a,b,c,d$ are nonzero and pairwise distinct, they form a rational $D(q)$-quadruple.

**Proof.** The definitions give

$$
D^2-w^2=3q,\qquad D^2=X+4q,
$$

and

$$
S+2r=p=c,\qquad S-2r=\frac{X}{p}=d,\qquad S^2-4r^2=X.
$$

Hence

$$
ab+q=\frac{S^2-D^2}{4}+q=\frac{S^2-X}{4}=r^2,
\qquad cd+q=X+q=w^2.
$$

For a mixed product, let $u$ be either $c$ or $d$, and put $\rho=r$ for $u=c$ and $\rho=-r$ for $u=d$. Then $u=S+2\rho$. Since $c+d=2S$ and $cd=X$, one has $u^2-2uS=-X$. If $x=(S+\varepsilon D)/2$, with $\varepsilon\in\{1,-1\}$, then $x$ is $a$ or $b$ and $x+\rho=(u+\varepsilon D)/2$. Therefore

$$
(x+\rho)^2-(xu+q)
=\frac{u^2-2uS+D^2-4q}{4}
=\frac{-X+X}{4}=0.
$$

This proves all six identities.

**Lemma 2.2 (One-element extension).** Let $F$ be a field of characteristic different from $2$, let $x_1,x_2,x_3,x_4\in F$, and let $s_1,s_2,s_3,s_4$ be their elementary symmetric sums. Put

$$
M=\frac{s_1^2-4s_2}{8}.
$$

Suppose $q,t\in F^{\times}$ satisfy

$$
t^2=\frac{4(M^2-s_4)}{q}.
$$

Then $M^2-s_4\ne0$, and with

$$
e=\frac{q(s_1M+s_3)}{M^2-s_4},
$$

one has

$$
q+x_ie=
\left(\frac{2M+x_i(s_1-2x_i)}{t}\right)^2
\qquad (i=1,2,3,4).
$$

Thus a rational $D(q)$-quadruple extends to a rational $D(q)$-quintuple whenever $e$ is nonzero and distinct from its four entries.

**Proof.** Fix $x=x_i$, and let $T,U,V$ denote, respectively, the sum, the sum of pairwise products, and the product of the other three entries. Then

$$
s_1=x+T,\qquad s_2=xT+U,\qquad s_3=xU+V,\qquad s_4=xV,
$$

so

$$
2M=\frac{(x-T)^2}{4}-U.
$$

A direct expansion gives

$$
M^2-s_4+x(s_1M+s_3)
=\left(M+\frac{x(s_1-2x)}{2}\right)^2.
$$

Indeed, after the terms $xV$ cancel, the difference between the two sides is

$$
x^2\left(2M+U-\frac{(x-T)^2}{4}\right)=0.
$$

The square condition implies $M^2-s_4=qt^2/4\ne0$. Multiplying the identity by $q/(M^2-s_4)=4/t^2$ proves the claimed four square identities.

## 3. A generic rational $D(z)$-quintuple

Let $z$ be an indeterminate. Define

$$
\begin{aligned}
K(z)&=z^2-34z+1,\\
A(z)&=9z^4-20z^3-490z^2-20z+9,\\
B(z)&=9z^6-86z^5+2311z^4-372z^3+2311z^2-86z+9,\\
C(z)&=243z^{10}-7758z^9+58679z^8+73560z^7+278742z^6\\
&\quad+1290220z^5+278742z^4+73560z^3+58679z^2-7758z+243.
\end{aligned}
$$

In $\mathbb{Q}(z)$, put

$$
h=\frac{z+1}{2},\qquad
p=\frac{(z-1)K(z)A(z)}{2B(z)},\qquad
t=-\frac{(z-5)(5z-1)(z^2+14z+1)C(z)}{32(z+1)^3A(z)B(z)}.
$$

Apply Lemma 2.1, with $q=z$, to define $D,w,X,S,r,a,b,c,d$. In particular,

$$
X=\frac{(z-1)^2K(z)}{16(z+1)^2}.
$$

Let $s_1,s_2,s_3,s_4$ be the elementary symmetric sums of $a,b,c,d$, and set $M=(s_1^2-4s_2)/8$.

**Proposition 3.1.** The rational function $M^2-s_4$ is nonzero. With $e$ defined by Lemma 2.2, with $q=z$, the five functions

$$
\mathcal{F}(z)=\{a(z),b(z),c(z),d(z),e(z)\}
$$

are distinct and nonzero in $\mathbb{Q}(z)$, and $xy+z$ is a square in $\mathbb{Q}(z)$ for every pair of distinct entries $x,y\in\mathcal{F}(z)$.

**Proof.** Lemma 2.1 supplies the six square identities among $a,b,c,d$. The relations

$$
a+b=S,\qquad c+d=2S,\qquad cd=X,\qquad
ab=\frac{S^2-X-4z}{4}
$$

give

$$
s_1=3S,\qquad
s_2=\frac{9S^2+3X-4z}{4},\qquad
s_4=\frac{X(S^2-X-4z)}{4},
$$

and hence

$$
M=\frac{4z-3X}{8}.
$$

Using $S=(p^2+X)/(2p)$, one obtains

$$
\frac{4(M^2-s_4)}{z}
=\frac{p^2(4z+5X)^2-4X(p^2+X)^2}{16zp^2}.
$$

Put

$$
\Delta=p^2(4z+5X)^2-4X(p^2+X)^2.
$$

Substitution and exact factorization give

$$
\Delta=
\frac{z(z-5)^2(z-1)^2(5z-1)^2K(z)^2(z^2+14z+1)^2C(z)^2}
{256(z+1)^6B(z)^4}.
$$

Since

$$
p^2=\frac{(z-1)^2K(z)^2A(z)^2}{4B(z)^2},
$$

it follows that

$$
\frac{4(M^2-s_4)}{z}
=\frac{(z-5)^2(5z-1)^2(z^2+14z+1)^2C(z)^2}
{1024(z+1)^6A(z)^2B(z)^2}
=t^2.
$$

Thus $M^2-s_4=zt^2/4\ne0$ in $\mathbb{Q}(z)$, and Lemma 2.2 supplies the remaining four square identities involving $e$.

It remains to prove nondegeneracy in $\mathbb{Q}(z)$. All displayed expressions are defined at $z=2$, where

$$
t(2)=-\frac{3852651}{3603680}\ne0
$$

and

$$
\begin{aligned}
a(2)&=\frac{6092447}{3603680}, &
b(2)&=-\frac{3817673}{3603680}, &
c(2)&=\frac{1561}{1010},\\
d(2)&=-\frac{505}{1784}, &
e(2)&=-\frac{3576247855663273}{3069853820287070}.
\end{aligned}
$$

Exact cross-multiplication gives

$$
e(2)<b(2)<d(2)<0<c(2)<a(2).
$$

Therefore no entry, and no difference of two entries, is the zero rational function. The five elements of $\mathcal{F}(z)$ are distinct and nonzero in $\mathbb{Q}(z)$.

**Corollary 3.2.** There is a finite set $\mathcal E\subset\mathbb{Q}$ such that, for every $z_0\in\mathbb{Q}\setminus\mathcal E$, the five values in $\mathcal{F}(z_0)$ are defined, nonzero, and pairwise distinct, and form a rational $D(z_0)$-quintuple.

**Proof.** The ten square roots are the six functions from Lemma 2.1 and the four functions from Lemma 2.2. Let $\mathcal E$ contain $0$, all rational poles of the five entries and these ten roots, all rational zeros of the five entries, and all rational zeros of their ten pairwise differences. The entries and their differences are nonzero rational functions, so they have only finitely many zeros and poles. Outside $\mathcal E$, all ten identities specialize and the resulting set is nondegenerate.

## 4. Square-class transfer and infinitude

**Lemma 4.1 (Scaling).** If $\{x_1,\dots,x_m\}$ is a rational $D(z)$-$m$-tuple and $\lambda\in\mathbb{Q}^{\times}$, then $\{\lambda x_1,\dots,\lambda x_m\}$ is a rational $D(\lambda^2z)$-$m$-tuple.

**Proof.** If $x_ix_j+z=r_{ij}^2$, then

$$
(\lambda x_i)(\lambda x_j)+\lambda^2z=(\lambda r_{ij})^2.
$$

Nonzero scaling preserves distinctness and nonvanishing.

**Theorem 4.2.** Fix $q\in\mathbb{Q}^{\times}$. For all but finitely many $u\in\mathbb{Q}^{\times}$, the set

$$
\mathcal{F}_q(u)=
\left\{
\frac{a(qu^2)}{u},\frac{b(qu^2)}{u},\frac{c(qu^2)}{u},
\frac{d(qu^2)}{u},\frac{e(qu^2)}{u}
\right\}
$$

is a rational $D(q)$-quintuple. These specializations give infinitely many distinct quintuples.

**Proof.** Let $\mathcal E$ be the finite set in Corollary 3.2. If $qu^2\notin\mathcal E$, then $\mathcal{F}(qu^2)$ is a rational $D(qu^2)$-quintuple. Lemma 4.1, with $\lambda=1/u$, gives the displayed set. For each $\varepsilon\in\mathcal E$, the equation $qu^2=\varepsilon$ has at most two rational solutions $u$. Hence only finitely many $u\in\mathbb{Q}^{\times}$ are excluded.

To prove infinitude, recall that $c(z)=p(z)$. Define

$$
R(z)=781z^5-15137z^4+5442z^3-11906z^2+385z-45.
$$

Exact polynomial division gives

$$
3(z-1)K(z)A(z)=(3z-83)B(z)-16R(z),
$$

and therefore

$$
p(z)=\frac z2-\frac{83}{6}-\frac{8R(z)}{3B(z)}
=\frac z2-\frac{83}{6}+O(z^{-1})
\qquad (|z|\to\infty).
$$

Choose $u=n$ among the positive integers. All but finitely many such $n$ are admissible, and

$$
\frac{c(qn^2)}{n}=\frac q2n-\frac{83}{6n}+O(n^{-3}).
$$

Its absolute value tends to infinity. If only finitely many distinct quintuples occurred, the union of all their entries would be a finite, hence bounded, subset of $\mathbb{Q}$, contradicting the asymptotic. Thus infinitely many distinct rational $D(q)$-quintuples occur.

For $q=0$, each set

$$
\{1,4,9,16,m^2\},\qquad m=5,6,7,\dots,
$$

is a rational $D(0)$-quintuple. Its five entries are distinct nonzero squares, so every pairwise product is a rational square. The sets are distinct as $m$ varies.

This proves Theorem 1 and gives affirmative answers to Problems 5.8 and 5.9.

## 5. The specialization $q=1579$

At $z=1579$, the construction in Proposition 3.1 is defined. In particular,

$$
h=790,\qquad
p=\frac{1680187362199310518953}{2166527099963404441},
$$

and

$$
t=-\frac{43760220723841232738857861440611350563370603}
{59675393632304173095432821937184939312000}\ne0.
$$

Let $a_1=a(1579)$, $a_2=b(1579)$, $a_3=c(1579)$, $a_4=d(1579)$, and $a_5=e(1579)$. Their reduced numerators and denominators are listed in Appendix A. Exact cross-multiplication gives

$$
43<a_2<44<80<a_5<81<196<a_4<197<441<a_1<442<775<a_3<776.
$$

Thus the five entries are positive, nonzero, and pairwise distinct. Proposition 3.1, specialized at $z=1579$, proves that every pairwise product plus $1579$ is a rational square. Appendix A also records a complete ten-pair square certificate.

**Corollary 5.1.** The set $\{a_1,a_2,a_3,a_4,a_5\}$ listed in Appendix A is a positive rational $D(1579)$-quintuple. Hence Problem 5.7 has an affirmative answer.

## 6. Verification files

Two exact Python verifiers accompany this manuscript. [`verify_problems_5_8_5_9.py`](verify_problems_5_8_5_9.py) checks the central factorization by integer polynomial cross-multiplication, verifies the polynomial division used in the infinitude argument, constructs exact specializations on both signs, and checks the square-class transfer. [`verify_problem_5_7.py`](verify_problem_5_7.py) checks the reduced fractions in Appendix A, the construction at $z=1579$, all ten rational square identities, and the strict order of the five entries. Both scripts use only the Python standard library and exact arithmetic.

Run them from this directory with

```text
python3 verify_problems_5_8_5_9.py
python3 verify_problem_5_7.py
```

## References

1. A. Dujella. *Open Problems on Diophantine m-Tuples and Elliptic Curves*. Version of 30 August 2026, Problems 5.7, 5.8, and 5.9.
2. G. Dražić. “Rational $D(q)$-quintuples.” *Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. RACSAM* **116** (2022), Article 9, 18 pp.

## Appendix A. Exact certificate at $q=1579$

Write $a_i=N_i/D_i$ in lowest terms. Spaces in the integer columns are digit separators only.

| Entry | Numerator $N_i$ | Denominator $D_i$ |
|:---:|---|---|
| $a_1$ | `3 33809 42791 73228 83945 06781 79903 58546`<br>`33069` | `755 38472 95228 37634 11940 28093 31454 92800` |
| $a_2$ | `33167 73984 20363 97029 40775 19070 90114 33149` | `755 38472 95228 37634 11940 28093 31454 92800` |
| $a_3$ | `16 80187 36219 93105 18953` | `2166 52709 99634 04441` |
| $a_4$ | `17 09389 88187 11261 03949` | `8716 53912 77080 85200` |
| $a_5$ | `3 04098 09650 62856 69837 52110 48234 24074`<br>`47431 66549 47563 53362 16467 91874 21157 43370`<br>`84128 55007 10634 20421` | `3796 58521 24748 57185 30394 52812 28856 80240`<br>`77266 97264 40985 88699 13827 07059 94610 19450`<br>`12934 86558 88733` |

For each $1\le i<j\le5$, choose the positive rational number $r_{ij}=R_{ij}/S_{ij}$ listed below.

| Root | Numerator $R_{ij}$ | Denominator $S_{ij}$ |
|:---:|---|---|
| $r_{12}$ | `1 09419 79381 01388 93818 29963 11053 94445`<br>`58091` | `755 38472 95228 37634 11940 28093 31454 92800` |
| $r_{13}$ | `40170 88434 23459 79784 10857` | `68 46225 63588 43580 33560` |
| $r_{14}$ | `51 78555 90430 81952 00729` | `17433 07825 54161 70400` |
| $r_{15}$ | `1029 75335 92238 32170 94373 21356 95851 55207`<br>`60883 76976 11616 24421 28320 60657` | `5 35526 14257 71598 16889 61633 38053 53727`<br>`61574 23701 17192 12502 95265 56680` |
| $r_{23}$ | `12923 03630 31522 32614 80623` | `68 46225 63588 43580 33560` |
| $r_{24}$ | `17 59776 14056 59429 92831` | `17433 07825 54161 70400` |
| $r_{25}$ | `382 29089 72123 92049 48885 40378 38052 80683`<br>`75383 04981 01986 08251 70439 18823` | `5 35526 14257 71598 16889 61633 38053 53727`<br>`61574 23701 17192 12502 95265 56680` |
| $r_{34}$ | `6 19363` | `1580` |
| $r_{35}$ | `122 49589 94485 00179 54842 12052 87504 82143`<br>`69372 94961 97070` | `48535 96667 63976 94976 07241 18389 60614 10577`<br>`81863 56711` |
| $r_{45}$ | `16249 68223 72333 82941 65594 46839 67673 32352`<br>`20843 11163` | `123 59091 71378 94461 20696 67140 52895 81902`<br>`90027 12740` |

For each row corresponding to $(i,j)$, the desired relation

$$
a_i a_j+1579=r_{ij}^2
$$

is equivalent to the integer identity

$$
(N_iN_j+1579D_iD_j)S_{ij}^2=R_{ij}^2D_iD_j.
$$

Substitution of the integers in the two tables verifies this identity for all ten pairs. As a comparatively small example,

$$
a_3a_4+1579=\left(\frac{619363}{1580}\right)^2.
$$
