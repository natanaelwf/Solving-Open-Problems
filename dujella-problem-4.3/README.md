# Infinitely Many Pairs of Diophantine Quadruples with the Same Largest Element

## A complete affirmative solution to Dujella's Problem 4.3

**Publication date:** 12 September 2026  
**Status:** Complete solution  
**Field:** Number theory, Diophantine tuples

## Abstract

A Diophantine quadruple is a set of four distinct positive integers such that the product of every two distinct elements, increased by $1$, is a perfect square. Dujella's Problem 4.3 asks whether infinitely many pairs of Diophantine quadruples have the same largest element. We give an explicit affirmative construction. For every integer $n\ge 0$, an odd power of the Pell unit $485+66\sqrt{54}$ produces two distinct Diophantine quadruples

```math
\mathcal Q_n=\{a,p,q,d\},
\qquad
\mathcal R_n=\{b,a,e,d\},
```

with

```math
b<a<p<q<d,
\qquad
b<a<e<d.
```

The equality of the two largest elements follows from a polynomial identity whose second factor is the Pell equation. Finally, $d=d_n\to\infty$, so the construction gives infinitely many distinct pairs.

## 1. The explicit family

For each integer $n\ge 0$, define positive integers $x=x_n$ and $w=w_n$ by

```math
x_n+w_n\sqrt{54}=(485+66\sqrt{54})^{2n+1}.
```

Set

```math
\begin{aligned}
t&=x-6w,                    & \ell&=4t-3w-1,\\
a&=8w,                      & b&=\frac{9w-6t}{4},\\
r&=4w\ell-1,               & p&=\ell(2w\ell-1),\\
q&=(\ell+2)\bigl(2w(\ell+2)-1\bigr),
                              & U&=4t^2-1,\\
V&=t(4t^2-3),               & e&=U\bigl((a+b)U+2V\bigr),\\
d&=4r(a+r)(p+r).
\end{aligned}
```

**Theorem 1.** For every integer $n\ge 0$, the sets

```math
\mathcal Q_n=\{a,p,q,d\},
\qquad
\mathcal R_n=\{b,a,e,d\}
```

are distinct Diophantine quadruples. Their entries satisfy

```math
b<a<p<q<d,
\qquad
b<a<e<d,
```

and $d=d_n\to\infty$ as $n\to\infty$.

## 2. Pell equation, integrality, and positivity

Since

```math
485^2-54\cdot 66^2=1,
```

the defining equation gives

```math
x^2-54w^2=1.
```

Moving from $n$ to $n+1$ amounts to multiplication by

```math
(485+66\sqrt{54})^2=470449+64020\sqrt{54}.
```

Hence the sequence also satisfies the integer recurrence

```math
\begin{aligned}
(x_0,w_0)&=(485,66),\\
x_{n+1}&=470449x_n+3457080w_n,\\
w_{n+1}&=64020x_n+470449w_n.
\end{aligned}
```

All coefficients in this recurrence are positive, so $x_n,w_n>0$ and $w_n\ge 66$. Modulo $4$, the recurrence reduces to

```math
x_{n+1}\equiv x_n\pmod 4,
\qquad
w_{n+1}\equiv w_n\pmod 4.
```

Since $(x_0,w_0)=(485,66)$, it follows that

```math
x_n\equiv 1\pmod 4,
\qquad
w_n\equiv 2\pmod 4.
```

Therefore

```math
t=x-6w\equiv 1\pmod 4
```

and

```math
9w-6t\equiv 9\cdot 2-6\cdot 1\equiv 0\pmod 4.
```

Thus $b$ is an integer, and every quantity in the construction is integral.

Substituting $x=t+6w$ into $x^2-54w^2=1$ gives

```math
t^2+12tw-18w^2=1.
```

Consequently,

```math
\begin{aligned}
ab
&=8w\cdot\frac{9w-6t}{4}\\
&=18w^2-12tw\\
&=t^2-1.
\end{aligned}
```

Hence

```math
ab+1=t^2.
```

The Pell equation also gives useful bounds. Since $w\ge 66$,

```math
49w^2<54w^2+1<\frac{225}{4}w^2.
```

Because $x>0$ and $x^2=54w^2+1$, taking positive square roots yields

```math
7w<x<\frac{15}{2}w.
```

Since $t=x-6w$, we obtain

```math
w<t<\frac{3}{2}w.
```

It follows that

```math
0<b=\frac{9w-6t}{4}<\frac{3}{4}w<a=8w.
```

Moreover,

```math
\ell=4t-3w-1>w-1\ge 65.
```

In particular, $\ell\ge 3$ and $r=4w\ell-1>0$. Also,

```math
\begin{aligned}
p
&=\ell(2w\ell-1)\\
&\ge 3(6w-1)\\
&>8w=a.
\end{aligned}
```

Two direct calculations now give

```math
\begin{aligned}
ap+1
&=8w\ell(2w\ell-1)+1\\
&=(4w\ell-1)^2\\
&=r^2
\end{aligned}
```

and

```math
\begin{aligned}
q-p
&=(\ell+2)\bigl(2w(\ell+2)-1\bigr)-\ell(2w\ell-1)\\
&=8w\ell+8w-2\\
&=a+2r.
\end{aligned}
```

Thus

```math
q=a+p+2r,
```

so $q>p>a$.

Finally, $t>w\ge 66$, so $U=4t^2-1>1$ and $V=t(4t^2-3)>0$. Therefore

```math
\begin{aligned}
e
&=U\bigl((a+b)U+2V\bigr)\\
&=(a+b)U^2+2UV\\
&>a+b>a.
\end{aligned}
```

## 3. The first Diophantine quadruple

We have already proved

```math
ap+1=r^2
```

and

```math
q=a+p+2r.
```

These identities imply

```math
\begin{aligned}
aq+1
&=a(a+p+2r)+1\\
&=a^2+r^2+2ar\\
&=(a+r)^2,
\end{aligned}
```

and similarly

```math
pq+1=(p+r)^2.
```

A further identity that will be used repeatedly is

```math
\begin{aligned}
(a+r)(p+r)
&=ap+r(a+p)+r^2\\
&=(r^2-1)+r(a+p)+r^2\\
&=r(a+p+2r)-1\\
&=rq-1.
\end{aligned}
```

Recall that

```math
d=4r(a+r)(p+r).
```

Using $ap=r^2-1$, we obtain

```math
\begin{aligned}
ad+1
&=4ar(a+r)(p+r)+1\\
&=4r(a+r)\bigl(r(a+r)-1\bigr)+1\\
&=\bigl(2r(a+r)-1\bigr)^2.
\end{aligned}
```

The same calculation with $a$ and $p$ interchanged gives

```math
pd+1=\bigl(2r(p+r)-1\bigr)^2.
```

Finally, since $(a+r)(p+r)=rq-1$,

```math
\begin{aligned}
qd+1
&=4qr(a+r)(p+r)+1\\
&=4(a+r)(p+r)\bigl((a+r)(p+r)+1\bigr)+1\\
&=\bigl(2(a+r)(p+r)+1\bigr)^2.
\end{aligned}
```

Thus all six products of two distinct elements of

```math
\mathcal Q_n=\{a,p,q,d\}
```

become perfect squares after adding $1$. Hence $\mathcal Q_n$ is a Diophantine quadruple.

It remains to show that $d$ is its largest element. We already know that $a<p<q$. Since $(a+r)(p+r)=rq-1$,

```math
d=4r(rq-1),
```

and therefore

```math
\begin{aligned}
d-q
&=(4r^2-1)q-4r\\
&\ge 4r^2-4r-1\\
&>0.
\end{aligned}
```

Here $r\ge 2$, which is immediate from $w\ge 66$ and $\ell\ge 65$. Consequently,

```math
a<p<q<d.
```

We will later use the square certificate

```math
ad+1=\bigl(2r(a+r)-1\bigr)^2.
```

## 4. The second Diophantine quadruple

The polynomials

```math
U=4t^2-1,
\qquad
V=4t^3-3t
```

satisfy the identity

```math
V^2-(t^2-1)U^2=1.
```

Define

```math
X=V+aU,
\qquad
Y=V+bU.
```

Since $a,b,U,V>0$, both $X$ and $Y$ are positive. Using $ab=t^2-1$ and the identity above, we find

```math
\begin{aligned}
X^2-1
&=V^2-1+2aUV+a^2U^2\\
&=abU^2+2aUV+a^2U^2\\
&=a\bigl((a+b)U^2+2UV\bigr)\\
&=ae.
\end{aligned}
```

Similarly,

```math
Y^2-1=be.
```

Therefore

```math
ab+1=t^2,
\qquad
ae+1=X^2,
\qquad
be+1=Y^2,
```

so $\{b,a,e\}$ is a Diophantine triple.

Define

```math
d'=a+b+(2ab+1)e+2tXY.
```

The three remaining square conditions follow directly. First,

```math
\begin{aligned}
(tX+aY)^2
&=t^2X^2+a^2Y^2+2atXY\\
&=(ab+1)(ae+1)+a^2(be+1)+2atXY\\
&=ad'+1.
\end{aligned}
```

By symmetry,

```math
(bX+tY)^2=bd'+1.
```

For the third condition,

```math
\begin{aligned}
(te+XY)^2
&=t^2e^2+2teXY+X^2Y^2\\
&=(ab+1)e^2+2teXY+(ae+1)(be+1)\\
&=ed'+1.
\end{aligned}
```

Thus $\{b,a,e,d'\}$ is a Diophantine quadruple. Moreover, all terms in the definition of $d'$ are positive, and

```math
\begin{aligned}
d'-e
&=a+b+2abe+2tXY\\
&>0.
\end{aligned}
```

Together with $b<a<e$, this gives

```math
b<a<e<d'.
```

## 5. Coincidence of the largest elements

The decisive point is that $d'=d$. From the definitions of $X$ and $Y$,

```math
\begin{aligned}
Z:=tX+aY
&=t(V+aU)+a(V+bU)\\
&=(t+a)V+(at+ab)U.
\end{aligned}
```

Using $ab=t^2-1$, $U=4t^2-1$, and $V=4t^3-3t$, this becomes

```math
Z=8t^4+8at^3-8t^2-4at+1.
```

Now substitute

```math
a=8w,
\qquad
r=4w(4t-3w-1)-1.
```

A direct polynomial expansion in $\mathbb Z[t,w]$ gives

```math
\begin{aligned}
Z-\bigl(2r(a+r)-1\bigr)
&=8(t^2-4tw+2w^2)\\
&\quad\cdot(t^2+12tw-18w^2-1).
\end{aligned}
```

The second factor vanishes because

```math
t^2+12tw-18w^2=1.
```

Hence

```math
tX+aY=2r(a+r)-1.
```

The first extension identity gives

```math
ad'+1=(tX+aY)^2,
```

whereas the first quadruple gives

```math
ad+1=\bigl(2r(a+r)-1\bigr)^2.
```

Therefore

```math
ad'+1=ad+1.
```

Since $a>0$, it follows that

```math
d'=d.
```

Consequently,

```math
\mathcal R_n=\{b,a,e,d\}
```

is a Diophantine quadruple with

```math
b<a<e<d.
```

Thus $\mathcal Q_n$ and $\mathcal R_n$ have the same largest element $d$.

## 6. Distinctness and infinitude

Every element of $\mathcal Q_n$ is at least $a$, whereas $\mathcal R_n$ contains the element $b<a$. Therefore

```math
\mathcal Q_n\ne\mathcal R_n
```

for every integer $n\ge 0$.

Let

```math
\alpha=485+66\sqrt{54}>1.
```

Its norm is $1$, so its conjugate is $\alpha^{-1}$. Taking the difference between the defining equation and its conjugate gives

```math
w_n=
\frac{\alpha^{2n+1}-\alpha^{-(2n+1)}}{2\sqrt{54}}.
```

Hence $w_n\to\infty$. Since

```math
d_n>a_n=8w_n,
```

we also have $d_n\to\infty$. The common largest elements are therefore unbounded, so the construction yields infinitely many distinct pairs of Diophantine quadruples.

This proves Theorem 1 and gives an affirmative answer to Dujella's Problem 4.3.

## 7. Initial example

For $n=0$,

```math
(x,w,t,\ell)=(485,66,89,157),
\qquad
(a,b,r)=(528,15,41447).
```

The construction gives

```math
\begin{aligned}
\mathcal Q_0
&=\{528,3253511,3336933,22929452257545400\},\\
\mathcal R_0
&=\{15,528,723737525421,22929452257545400\}.
\end{aligned}
```

This is the third pair recorded by Gibbs and in Dujella's problem list.

## 8. Exact verification

The accompanying program `verify_problem_4_3.py` uses only Python's standard library. It performs two independent kinds of checks. First, it verifies the identities

```math
V^2-(t^2-1)U^2=1
```

and

```math
\begin{aligned}
Z-\bigl(2r(a+r)-1\bigr)
&=8(t^2-4tw+2w^2)\\
&\quad\cdot(t^2+12tw-18w^2-1)
\end{aligned}
```

coefficient by coefficient in $\mathbb Z[t,w]$. Second, it generates any requested number of members of the family and tests all twelve pairwise products for each pair of quadruples with exact integer arithmetic and `math.isqrt`.

For example,

```text
python verify_problem_4_3.py --count 100
```

checks the first $100$ pairs and all $1200$ square conditions. This finite computation is supplementary; the infinitude follows from the proof in Section 6.

## References

1. A. Dujella. *Open problems on Diophantine m-tuples and elliptic curves*. Problem 4.3, 2026.
2. P. Gibbs. *A Generalised Stern-Brocot Tree from Regular Diophantine Quadruples*. arXiv:math/9903035, 1999.
