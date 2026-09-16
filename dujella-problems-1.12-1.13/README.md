# Uniform Bounds for D(1)-Tuples in Rings of Integers

## Affirmative answers to Dujella's Problems 1.12 and 1.13

**Publication date:** 15 September 2026  
**Status:** Complete solution  
**Field:** Number theory, Diophantine tuples, algebraic number theory

## Abstract

For every positive integer $d$, we give an explicit constant $C_d$ such that any set of distinct nonzero algebraic integers in a number field $K$ of degree $d$, whose pairwise products increased by $1$ are squares in $K$, has at most $C_d$ elements. The bound depends only on $d$, not on $K$ or on the heights of the elements. In degree $2$ it gives $C_2\lt 2^{233}$, uniformly for both real and imaginary quadratic fields. This answers Problems 1.12 and 1.13 in Dujella's problem list affirmatively. The proof combines an elementary nonvanishing determinant, a bound in each dyadic interval of logarithmic height, and an explicit specialization of the quantitative Subspace Theorem of Evertse and Ferretti.

## 1. Statement and scope

Let $K$ be a number field and let $\mathcal O_K$ be its ring of integers. A $D(1)$-tuple is a finite set $A\subset\mathcal O_K\setminus\lbrace{}0\rbrace{}$ of distinct elements such that

```math
ab+1\in K^2
\qquad
(a,b\in A,\ a\ne b),
```

where

```math
K^2=\lbrace{}r^2:r\in K\rbrace{}.
```

Requiring the square roots to belong to $\mathcal O_K$ is equivalent: if $r\in K$ and $r^2\in\mathcal O_K$, then $r$ is integral over $\mathcal O_K$, so $r\in\mathcal O_K$ because $\mathcal O_K$ is integrally closed. Zero square roots are allowed. No condition is imposed on $a^2+1$.

**Theorem 1.1.** For every integer $d\ge 1$, put

```math
\begin{aligned}
N_d&=d^2 2^{13d^2+2d},\\
M_d&=(16d+1)^d 2^{6d\,2^d},\\
L_d&=2^{82+75d},\\
C_d&=N_d+2+8M_d+L_d.
\end{aligned}
```

If $[K:\mathbb Q]=d$, every $D(1)$-tuple $A\subset\mathcal O_K\setminus\lbrace{}0\rbrace{}$ satisfies

```math
|A|\le C_d.
```

**Corollary 1.2.** Every $D(1)$-tuple in the ring of integers of a quadratic field has cardinality less than $2^{233}$.

**Proof.** For $d=2$,

```math
\begin{aligned}
N_2&=2^{58},\\
M_2&=33^2 2^{48},\\
L_2&=2^{232}.
\end{aligned}
```

Consequently,

```math
\begin{aligned}
C_2
&=2^{232}+9736\cdot 2^{48}+2\\
&\lt 2^{232}+2^{62}\\
&\lt 2^{233}.
\end{aligned}
```

Problem 1.13 asks for a bound depending only on $[K:\mathbb Q]$, so Theorem 1.1 gives precisely the requested uniformity. Problem 1.12 asks for an absolute bound for real quadratic fields and is a special case of Corollary 1.2. There is no dependence on the discriminant of $K$, and no assumption that the elements are totally positive or that $K$ is totally real.

If a convention permits $0$ as an element of the tuple, one may add $1$ to $C_d$. Infinite sets with the same pairwise property are also impossible: any such set would contain a finite subset with more than $C_d$ nonzero elements.

## 2. Heights and the small-height range

All logarithms are natural. Write $M_K$ for the places of $K$ and $d=[K:\mathbb Q]$. At an archimedean place $v$, represented by an embedding $\sigma_v:K\hookrightarrow\mathbb C$, use

```math
|z|_v=|\sigma_v(z)|^{w_v},
\qquad
w_v=\frac{[K_v:\mathbb R]}{d}.
```

Thus

```math
\sum_{v\mid\infty}w_v=1.
```

At the finite place corresponding to a prime ideal $\mathfrak p$, use

```math
|z|_v=(N\mathfrak p)^{-\mathrm{ord}_{\mathfrak p}(z)/d}.
```

These absolute values satisfy the product formula. For $z\in K$, set

```math
h(z)=\sum_{v\in M_K}\log\max\lbrace{}1,|z|_v\rbrace{}.
```

For a nonzero vector $\mathbf z=(z_0,\ldots,z_{n-1})\in K^n$, set

```math
\lVert\mathbf z\rVert_v=\max_i|z_i|_v,
\qquad
H(\mathbf z)=\prod_{v\in M_K}\lVert\mathbf z\rVert_v.
```

For algebraic numbers or vectors outside $K$, the same definitions are made in a number field containing all their coordinates, using that field's normalized places. The resulting absolute heights are independent of this choice. In particular,

```math
h(z)=\log H(1,z).
```

We use the elementary height inequalities

```math
\begin{aligned}
h(uv)&\le h(u)+h(v),\\
h(u\pm v)&\le h(u)+h(v)+\log 2,\\
h(u^{-1})&=h(u)\qquad(u\ne0),\\
h(u^2)&=2h(u).
\end{aligned}
```

If $z\in\mathcal O_K$, its finite-place contributions vanish, and hence:

**Equation (1).**

```math
\begin{aligned}
h(z)
&=\sum_{v\mid\infty}w_v\log^+|\sigma_v(z)|\\
&=\frac{1}{d}\sum_{\sigma:K\hookrightarrow\mathbb C}\log^+|\sigma(z)|.
\end{aligned}
```

Complex conjugate embeddings are counted separately in the last sum.

**Lemma 2.1.** The number of algebraic integers in a fixed algebraic closure of $\mathbb Q$ that have degree at most $d$ and height less than $8$ is at most $N_d$.

**Proof.** Let $z$ have degree $e\le d$, and let $f\in\mathbb Z[X]$ be its monic minimal polynomial. Its Mahler measure is

```math
M(f)=\exp(eh(z))\lt\exp(8e).
```

Each coefficient of $f$ has absolute value at most $2^eM(f)$, by the formula for elementary symmetric functions of its roots. Since $\exp(8)\lt2^{12}$, every coefficient has absolute value less than $2^{13e}\le2^{13d}$. For a fixed degree $e$, the number of possible monic polynomials is therefore at most $(2^{13d+1}+1)^e$. There are at most $d$ possible degrees and at most $d$ roots per polynomial. The desired count is at most

```math
d^2(2^{13d+1}+1)^d
\le d^2 2^{13d^2+2d}
=N_d.
```

## 3. A nonvanishing determinant

**Lemma 3.1.** Let $a_1,a_2,a_3$ be distinct nonzero elements of a field of characteristic zero, and let $b_1,b_2,b_3$ be distinct elements. Suppose, in a common extension field, that

```math
r_{ij}^2=a_i b_j+1
\qquad
(1\le i,j\le3).
```

Then $\det(r_{ij})\ne0$, for every choice of the square roots.

**Proof.** No two rows can be proportional. Indeed, proportionality of rows $i$ and $k$ with ratio $\lambda$ would give

```math
(a_i-\lambda^2a_k)b_j+(1-\lambda^2)=0
\qquad
(j=1,2,3).
```

Since the $b_j$ are distinct, both coefficients vanish, giving $\lambda^2=1$ and $a_i=a_k$, a contradiction. This also rules out zero rows.

If the determinant vanished, the third row would therefore be $\lambda$ times the first plus $\mu$ times the second, with $\lambda\mu\ne0$. Squaring this relation gives

```math
\begin{aligned}
2\lambda\mu r_{1j}r_{2j}&=Pb_j+Q,\\
P&=a_3-\lambda^2a_1-\mu^2a_2,\\
Q&=1-\lambda^2-\mu^2.
\end{aligned}
```

Squaring again gives equality at three distinct points between two polynomials of degree at most two. Thus

```math
(PT+Q)^2=4\lambda^2\mu^2(a_1T+1)(a_2T+1)
```

as a polynomial identity. The right-hand side has two distinct simple roots, whereas the left-hand side is a square. This is impossible.

## 4. A uniform bound in a dyadic height interval

**Lemma 4.1.** If $A$ is a $D(1)$-tuple in $\mathcal O_K$, then for every real $T\ge8$,

```math
\#\lbrace{}a\in A:T\le h(a)\le2T\rbrace{}\le M_d.
```

**Proof.** Let $\Sigma_K$ be the $d$ embeddings of $K$ into $\mathbb C$, counting complex conjugates separately. Partition the elements in the indicated interval by the vector

```math
k_\sigma(a)
=\left\lfloor\frac{8\log^+|\sigma(a)|}{T}\right\rfloor
\qquad
(\sigma\in\Sigma_K).
```

By Equation (1), each coordinate is in $\lbrace{}0,1,\ldots,16d\rbrace{}$. There are at most $(16d+1)^d$ classes. Fix one class and put $\ell_\sigma=k_\sigma T/8$. If $k_\sigma\gt0$, every element $a$ in the class satisfies:

**Equation (2).**

```math
e^{\ell_\sigma}\le|\sigma(a)|\lt e^{\ell_\sigma+T/8}.
```

For every unordered pair $\lbrace{}a,b\rbrace{}$, choose a single root $r_{ab}=r_{ba}\in\mathcal O_K$ with $r_{ab}^2=ab+1$. These are global roots in $K$, not independent choices at different embeddings. Separately, for every $\sigma$ and every vertex $a$, choose a complex square root $s_\sigma(a)^2=\sigma(a)$.

Suppose $k_\sigma\gt0$. Then $|\sigma(ab)|\ge e^{T/4}\gt2$. Let $w$ be the square root of $1+1/\sigma(ab)$ with positive real part. It exists because $|1/\sigma(ab)|\lt1$. Since $|w+1|\ge1$,

```math
|w-1|
=\frac{|1/\sigma(ab)|}{|w+1|}
\le\frac{1}{|\sigma(ab)|}.
```

For some $\varepsilon_\sigma(a,b)\in\lbrace{}\pm1\rbrace{}$, it follows that:

**Equation (3).**

```math
\begin{aligned}
\sigma(r_{ab})
&=\varepsilon_\sigma(a,b)s_\sigma(a)s_\sigma(b)+E_\sigma(a,b),\\
|E_\sigma(a,b)|&\le e^{-\ell_\sigma}.
\end{aligned}
```

For $k_\sigma=0$, assign the sign $+1$ merely to complete the notation. Color each edge by its vector of $d$ signs, using at most $q=2^d$ colors.

We need the elementary Ramsey estimate $R_q(6)\le q^{6q}$ for $q\ge2$. Here is a precise greedy argument. Starting with $N=q^{6q}$ vertices, select a vertex and retain a largest neighborhood whose edges from that vertex have one color. After $j$ such selections, the number of remaining vertices is at least

```math
\frac{N}{q^j}-\sum_{i=1}^j\frac{1}{q^i}
=\frac{N}{q^j}-\frac{1-q^{-j}}{q-1}.
```

This is positive for $j\le6q-1$, so $6q-1$ selections and their colors can be made. Some color occurs at least six times among these selections. The corresponding six vertices form a monochromatic complete graph, because every later selected vertex lies in every earlier retained neighborhood.

If the fixed height class had at least $q^{6q}$ vertices, choose six monochromatic vertices and label them $a_1,a_2,a_3,b_1,b_2,b_3$. Then

```math
\Delta
=\det(r_{a_i b_j})_{1\le i,j\le3}
\in\mathcal O_K\setminus\lbrace{}0\rbrace{}
```

by Lemma 3.1.

At an embedding with $k_\sigma\gt0$, the main matrix in Equation (3) has entries $\varepsilon_\sigma s_\sigma(a_i)s_\sigma(b_j)$ and rank one. Its entries have modulus at most $\mu=e^{\ell_\sigma+T/8}$, and the error entries have modulus at most $\eta=e^{-\ell_\sigma}$. In the column expansion of the determinant, all terms with at least two main columns vanish. The three terms with one main column and the term with three error columns give

```math
|\sigma(\Delta)|
\le18\mu\eta^2+6\eta^3
\le24e^{-\ell_\sigma+T/8}.
```

If $k_\sigma=0$, then $|\sigma(a)|\lt e^{T/8}$ for all vertices in the class, so

```math
\begin{aligned}
|\sigma(r_{ab})|&\le\sqrt2\,e^{T/8},\\
|\sigma(\Delta)|
&\le6(\sqrt2\,e^{T/8})^3\\
&\lt24e^{3T/8}.
\end{aligned}
```

In either case:

**Equation (4).**

```math
\log|\sigma(\Delta)|
\le\log24-\ell_\sigma+\frac{3T}{8}.
```

For any vertex $a$ in the class, the definition of the floors yields

```math
\sum_{\sigma\in\Sigma_K}\ell_\sigma
\ge dh(a)-\frac{dT}{8}
\ge\frac{7dT}{8}.
```

Summing Equation (4) over all embeddings gives

```math
\log|N_{K/\mathbb Q}(\Delta)|
\le d\log24-\frac{dT}{2}
\lt0,
```

because $T\ge8$ and $\log24\lt4$. This contradicts the fact that the norm of a nonzero algebraic integer is a nonzero integer. Each class therefore has fewer than $q^{6q}$ vertices. Multiplication by the number of classes gives

```math
(16d+1)^d q^{6q}
=(16d+1)^d 2^{6d\,2^d}
=M_d
```

as a valid upper bound.

## 5. The quantitative Subspace Theorem used here

For a linear form $L=\sum_{i=0}^3\gamma_iX_i$ with algebraic coefficients, write

```math
\begin{aligned}
H^*(L)&=H(1,\gamma_0,\gamma_1,\gamma_2,\gamma_3),\\
K(L)&=K(\gamma_0,\gamma_1,\gamma_2,\gamma_3).
\end{aligned}
```

For each place of $K$ occurring below, fix an extension of its absolute value to $\overline{\mathbb Q}$. These fixed extensions are used to evaluate the forms.

**Proposition 5.1.** Let $S\subset M_K$ be finite. For each $v\in S$, let $L_{0,v},\ldots,L_{3,v}$ be algebraic linear forms whose coefficient matrix has determinant $1$. Suppose that at most eight distinct forms occur, that

```math
\begin{aligned}
{}[K(L_{i,v}):K]&\le2,\\
H^*(L_{i,v})&\le\mathcal H,\\
\mathcal H&\ge1,
\end{aligned}
```

and that $\beta_{i,v}\ge0$ with

```math
\sum_{v\in S}\sum_{i=0}^3\beta_{i,v}=\frac{17}{4}.
```

The vectors $\mathbf z\in K^4\setminus\lbrace{}0\rbrace{}$ satisfying

```math
\frac{|L_{i,v}(\mathbf z)|_v}{\lVert\mathbf z\rVert_v}
\le H(\mathbf z)^{-\beta_{i,v}}
\qquad
(v\in S,\ 0\le i\le3),
```

and

```math
H(\mathbf z)\gt\max\lbrace{}\mathcal H,4^{16}\rbrace{},
```

lie in the union of at most $2^{80}$ proper $K$-linear subspaces of $K^4$.

**Proof.** Apply Evertse and Ferretti (2013, Theorem 3.1, pp. 523-524) with

```math
\begin{aligned}
n&=4, & \varepsilon&=\frac14, & R&=8,\\
D&=2, & d_{i,v}&=-\beta_{i,v}.&&
\end{aligned}
```

The determinant factors in their inequality are $1$. Their Galois maximum acts on the argument of the form, not on its coefficients; it is redundant for $\mathbf z\in K^4$. Their threshold $\max\lbrace{}\mathcal H^{1/48},4^{16}\rbrace{}$ is no larger than the one imposed here. Their subspace count specializes to

```math
10^9 2^8 4^{14}4^3\log(192)\log(4\log48)
\lt2^{80}.
```

For example, $10^9\lt2^{30}$, $\log192\lt2^3$, and $\log(4\log48)\lt2^2$ already bound this expression by $2^{77}$. Their subspaces are defined over $K$; intersecting with $K^4$ gives the stated conclusion.

## 6. Extensions much higher than a fixed triple

**Lemma 6.1.** Let $a_1,a_2,a_3\in\mathcal O_K$ be distinct and nonzero, and put

```math
A=\max\lbrace{}1,h(a_1),h(a_2),h(a_3)\rbrace{}.
```

There are at most $L_d=2^{82+75d}$ elements $x\in\mathcal O_K$ such that

```math
\begin{aligned}
a_i x+1&\in K^2 &&(i=1,2,3),\\
h(x)&\gt256A.
\end{aligned}
```

The three $a_i$ need not themselves form a $D(1)$-triple.

**Proof.** For each such $x$, choose $r_i\in\mathcal O_K$ with $r_i^2=a_i x+1$, and set

```math
\begin{aligned}
\mathbf p&=(1,r_1,r_2,r_3),\\
G&=H(\mathbf p),\\
t&=\log G.
\end{aligned}
```

### Height comparison

Since $x=(r_1^2-1)/a_1$ and $h(r_1)\le t$,

```math
h(x)\le2t+A+\log2.
```

At each archimedean place, in ordinary complex moduli,

```math
\begin{aligned}
\max\lbrace{}1,|r_1|,|r_2|,|r_3|\rbrace{}^2
&\le2\max\lbrace{}1,|a_1|,|a_2|,|a_3|\rbrace{}\\
&\qquad\cdot\max\lbrace{}1,|x|\rbrace{}.
\end{aligned}
```

All the $r_i$ and $x$ are integral, so summation of the weighted logarithms gives $2t\le h(x)+3A+\log2$. Thus:

**Equation (5).**

```math
\frac{h(x)-A-\log2}{2}
\le t
\le\frac{h(x)+3A+\log2}{2}.
```

In particular:

**Equation (6).**

```math
t\gt127A,
```

since $h(x)\gt256A$ and $A\ge1$.

### Control of the fixed coefficients

For $v\mid\infty$, put

```math
B_v
=\max\lbrace{}1,|\sigma_v(a_i)|,|\sigma_v(a_i)|^{-1}:1\le i\le3\rbrace{}.
```

For each nonzero algebraic integer $a_i$,

```math
\sum_{v\mid\infty}w_v\log|\sigma_v(a_i)|
=\frac{1}{d}\log|N_{K/\mathbb Q}(a_i)|
\ge0.
```

Consequently,

```math
\sum_{v\mid\infty}w_v\bigl|\log|\sigma_v(a_i)|\bigr|
\le2h(a_i),
```

and hence:

**Equation (7).**

```math
\sum_{v\mid\infty}w_v\log B_v\le6A.
```

Fix global algebraic numbers $\alpha_i\in\overline{\mathbb Q}$ with $\alpha_i^2=a_i/a_1$ for $i=2,3$. Then:

**Equation (8).**

```math
[K(\alpha_i):K]\le2,
\qquad
h(\alpha_i)=\frac12h(a_i/a_1)\le A.
```

At every archimedean place, use a fixed extension of the embedding to $\overline{\mathbb Q}$, consistent with the fixed absolute value in Proposition 5.1.

### Local bases of forms

Fix $v\mid\infty$ and abbreviate $B=B_v$, $\xi=|\sigma_v(x)|$. Within this local calculation we suppress the embedding from the notation and use ordinary complex moduli, before raising to $w_v$.

If $\xi\lt4B^3$, choose the coordinate forms $X_0,X_1,X_2,X_3$. Then $|r_i|^2\le B\xi+1\le5B^4$ and $\max\lbrace{}1,\xi\rbrace{}^{1/2}\le2B^{3/2}$. Therefore:

**Equation (9).**

```math
\prod_{i=0}^3|X_i(\mathbf p)|
=|r_1r_2r_3|
\le32B^8\max\lbrace{}1,\xi\rbrace{}^{-1/2},
```

using $2\cdot5^{3/2}\lt32$ and $B\ge1$.

If $\xi\ge4B^3$, choose $\varepsilon_i\in\lbrace{}\pm1\rbrace{}$ so that

```math
|r_i+\varepsilon_i\alpha_i r_1|\ge|r_i|
\qquad
(i=2,3).
```

Such a sign exists since $\max\lbrace{}|u+v|,|u-v|\rbrace{}\ge|u|$. Choose the ordered basis

```math
\begin{aligned}
&X_0,\\
&X_1,\\
&X_2-\varepsilon_2\alpha_2X_1,\\
&X_3-\varepsilon_3\alpha_3X_1.
\end{aligned}
```

The identity

```math
(r_i-\varepsilon_i\alpha_i r_1)(r_i+\varepsilon_i\alpha_i r_1)
=1-\frac{a_i}{a_1}
```

and the bounds

```math
\left|1-\frac{a_i}{a_1}\right|\le2B^2,
\qquad
|r_i|^2
\ge\frac{\xi}{B}-1
\ge\frac{\xi}{2B}
\ge2B^2
```

imply:

**Equation (10).**

```math
\begin{aligned}
|r_i-\varepsilon_i\alpha_i r_1|
&\le2\sqrt2\,B^{5/2}\xi^{-1/2},\\
|r_i-\varepsilon_i\alpha_i r_1|&\le|r_i|.
\end{aligned}
```

Also $|r_1|\le\sqrt{2}B^{1/2}\xi^{1/2}$. Thus:

**Equation (11).**

```math
\begin{aligned}
|r_1|\prod_{i=2}^3|r_i-\varepsilon_i\alpha_i r_1|
&\le8\sqrt2\,B^{11/2}\xi^{-1/2}\\
&\le32B^8\max\lbrace{}1,\xi\rbrace{}^{-1/2}.
\end{aligned}
```

In either case, the selected basis has determinant $1$, each selected value has modulus at most $\max_j|p_j|$, and:

**Equation (12).**

```math
\prod_{i=0}^3|L_{i,v}(\mathbf p)|
\le32B_v^8\max\lbrace{}1,|\sigma_v(x)|\rbrace{}^{-1/2}.
```

There are five possible ordered bases per place and at most eight distinct global forms, namely the four coordinates and $X_i\pm\alpha_iX_1$ for $i=2,3$. By Equation (8), each form has $H^*$ at most $e^A$ and coefficient field of degree at most $2$ over $K$.

### The global inequality

Raise Equation (12) to $w_v$ and multiply over the archimedean places. Equations (1) and (7) give

```math
\prod_{v\mid\infty}\prod_{i=0}^3|L_{i,v}(\mathbf p)|_v
\le32e^{48A-h(x)/2}.
```

By the upper bound for $t$ in Equation (5),

```math
\begin{aligned}
32e^{48A-h(x)/2}
&\le\exp\left(\frac{99}{2}A+\log32+\frac12\log2\right)G^{-1}\\
&\le e^{54A}G^{-1}.
\end{aligned}
```

The last inequality uses $A\ge1$ and

```math
\log32+\frac12\log2
=\frac{11}{2}\log2
\lt\frac92.
```

By Equation (6), $54A\lt t/2$, so the last expression is at most $G^{-1/2}$.

Since $\mathbf p$ is integral and its first coordinate is $1$, $\lVert\mathbf p\rVert_v=1$ at every finite place. Therefore:

**Equation (13).**

```math
\prod_{v\mid\infty}\prod_{i=0}^3
\frac{|L_{i,v}(\mathbf p)|_v}{\lVert\mathbf p\rVert_v}
\le G^{-9/2}.
```

Every individual factor on the left is at most $1$ by the local construction. Every factor is also positive. Indeed, $r_i=0$ would force $x=-1/a_i$, with $h(x)=h(a_i)\le A$, and $r_i\pm\alpha_i r_1=0$ would force $a_i=a_1$.

### Discretization and the subspace count

Let $s$ be the number of archimedean places, so $s\le d$, and put $m=4s$. Fix one of the at most $5^s$ patterns of local bases. Denote the $m$ factors in Equation (13) by $\rho_j$, and write

```math
\rho_j=G^{-u_j},
\qquad
u_j\ge0.
```

Then $\sum_j u_j\ge9/2$, whence

```math
\sum_{j=1}^m\lfloor4mu_j\rfloor\ge17m.
```

Choose nonnegative integers $k_j\le\lfloor4mu_j\rfloor$ with $\sum_jk_j=17m$. For these integers,

```math
\rho_j\le G^{-k_j/(4m)},
\qquad
\sum_j\frac{k_j}{4m}=\frac{17}{4}.
```

The number of possible integer vectors is at most

```math
\binom{18m-1}{m-1}
\le2^{18m}
=2^{72s}.
```

For each fixed basis pattern and exponent vector, Proposition 5.1 applies with $\mathcal H=e^A$. Its threshold holds because $\log G=t\gt127A\gt A$ and $127A\gt16\log4$. Thus all the chosen points $\mathbf p$ lie in a union of at most:

**Equation (14).**

```math
5^s2^{72s}2^{80}
\le2^{80+75d}
```

proper $K$-linear subspaces of $K^4$.

### At most four extension values in each hyperplane

Every proper $K$-linear subspace is contained in a hyperplane

```math
\begin{aligned}
c_0X_0+c_1X_1+c_2X_2+c_3X_3&=0,\\
(c_0,c_1,c_2,c_3)&\in K^4\setminus\lbrace{}0\rbrace{}.
\end{aligned}
```

Put $F=K(T)$ and adjoin $u_i$ satisfying $u_i^2=a_iT+1$ for $i=1,2,3$. The three square classes of $a_iT+1$ in $F^{\ast}/F^{\ast2}$ are independent: every nonempty product has a simple zero at each selected point $T=-1/a_i$, and no other selected factor vanishes there. Such a product cannot be a square in $F$. Consequently, by the elementary theory of multiquadratic extensions,

```math
[F(u_1,u_2,u_3):F]=8,
```

and the signs of the $u_i$ can be changed independently. In particular,

```math
c_0+c_1u_1+c_2u_2+c_3u_3\ne0.
```

Changing just the sign of $u_i$ in a putative zero relation would give $2c_i u_i=0$ for every $i$, followed by $c_0=0$.

Its field norm is the nonzero element

```math
P(T)
=\prod_{\varepsilon\in\lbrace{}\pm1\rbrace{}^3}
\left(c_0+\sum_{i=1}^3c_i\varepsilon_i u_i\right).
```

To see directly that $P\in K[T]$ and $\deg P\le4$, form the same product in formal variables $U_1,U_2,U_3$. It is invariant under changing the sign of any $U_i$, so every occurring exponent is even. Its total degree in the $U_i$ is at most $8$. Substituting $U_i^2=a_iT+1$ therefore yields a polynomial of degree at most $4$, which is precisely $P(T)$.

If $\mathbf p=(1,r_1,r_2,r_3)$ lies in the hyperplane, the polynomial identity just constructed gives $P(x)=0$: in its product expression the factor with all signs positive is zero. This specialization argument also permits zero roots and requires no choice of a branch. Since $P$ is nonzero, there are at most four distinct possible values of $x$. Multiplying this by Equation (14) proves that the number of admissible values is at most

```math
4\cdot2^{80+75d}=L_d.
```

## 7. Proof of the uniform bound

**Proof of Theorem 1.1.** The assertion is immediate if $|A|\le2$. Otherwise order the elements by nondecreasing height, and let $a_1,a_2,a_3$ be the first three. Put

```math
\begin{aligned}
T_0&=\max\lbrace{}8,h(a_3)\rbrace{},\\
A&=\max\lbrace{}1,h(a_1),h(a_2),h(a_3)\rbrace{}\le T_0.
\end{aligned}
```

By Lemma 2.1, at most $N_d$ elements have height less than $8$. Outside that range, at most two elements have height less than $T_0$: if $T_0\gt8$, this follows from the choice of the third element, and if $T_0=8$ there are none.

The closed interval $[T_0,256T_0]$ is covered by the eight intervals

```math
[2^jT_0,2^{j+1}T_0]
\qquad
(j=0,1,\ldots,7).
```

Lemma 4.1 bounds their contribution by $8M_d$. Overlap at endpoints only increases this upper estimate.

Finally, every $x\in A$ with $h(x)\gt256T_0$ is distinct from $a_1,a_2,a_3$ and satisfies $a_i x+1\in K^2$ for $i=1,2,3$. It also satisfies $h(x)\gt256A$. Lemma 6.1 bounds the number of such elements by $L_d$. Hence

```math
|A|\le N_d+2+8M_d+L_d=C_d,
```

as required.

## References

Dujella, A. *Open problems on Diophantine m-tuples and elliptic curves.* Online problem list, Problems 1.12 and 1.13, consulted 15 September 2026.

Evertse, J.-H. and Ferretti, R. G. *A further improvement of the Quantitative Subspace Theorem.* Annals of Mathematics (2) **177** (2013), 513-590. Theorem 3.1 and its hypotheses appear on pp. 523-524.
