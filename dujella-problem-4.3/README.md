# Infinitely Many Pairs of Diophantine Quadruples with the Same Largest Element

## A complete affirmative solution to Dujella's Problem 4.3

**Publication date:** 12 September 2026  
**Status:** Complete solution  
**Field:** Number theory, Diophantine tuples

## Abstract

A Diophantine quadruple is a set of four distinct positive integers such that the product of every two distinct elements, increased by $1$, is a perfect square. Dujella's Problem 4.3 asks whether infinitely many pairs of Diophantine quadruples have the same largest element. We give an explicit affirmative construction. For every $n\ge 0$, an odd power of the Pell unit $485+66\sqrt{54}$ produces two distinct Diophantine quadruples

$$
\mathcal Q_n=\{a,p,q,d\},
\qquad
\mathcal R_n=\{b,a,e,d\},
$$

with

$$
b<a<p<q<d,
\qquad
b<a<e<d.
$$

The equality of the two largest elements follows from a polynomial identity whose second factor is the Pell equation. Finally, $d\to\infty$, so the construction gives infinitely many distinct pairs.

## 1. The explicit family

For each integer $n\ge 0$, define positive integers $x=x_n$ and $w=w_n$ by

$$
\boxed{
 x_n+w_n\sqrt{54}=(485+66\sqrt{54})^{2n+1}.
}
\tag{1}
$$

Set

$$
\begin{aligned}
t&=x-6w,
&\ell&=4t-3w-1,\\
a&=8w,
&b&=\frac{9w-6t}{4},\\
r&=4w\ell-1,
&p&=\ell(2w\ell-1),\\
q&=(\ell+2)\bigl(2w(\ell+2)-1\bigr),
&U&=4t^2-1,\\
V&=t(4t^2-3),
&e&=U\bigl((a+b)U+2V\bigr),\\
d&=4r(a+r)(p+r).
\end{aligned}
\tag{2}
$$

We prove the following statement.

**Theorem 1.** For every $n\ge 0$, the sets

$$
\boxed{
\mathcal Q_n=\{a,p,q,d\},
\qquad
\mathcal R_n=\{b,a,e,d\}
}
\tag{3}
$$

are distinct Diophantine quadruples. Their entries satisfy

$$
b<a<p<q<d,
\qquad
b<a<e<d,
\tag{4}
$$

and $d=d_n\to\infty$ as $n\to\infty$.

## 2. Pell equation, integrality, and positivity

Since

$$
485^2-54\cdot 66^2=1,
$$

equation (1) gives

$$
x^2-54w^2=1.
\tag{5}
$$

Moving from $n$ to $n+1$ amounts to multiplication by

$$
(485+66\sqrt{54})^2=470449+64020\sqrt{54}.
$$

Hence the sequence also satisfies the integer recurrence

$$
\begin{aligned}
(x_0,w_0)&=(485,66),\\
x_{n+1}&=470449x_n+3457080w_n,\\
w_{n+1}&=64020x_n+470449w_n.
\end{aligned}
\tag{6}
$$

The coefficients in (6) are positive, so $x_n,w_n>0$ and $w_n\ge 66$. Modulo $4$, recurrence (6) reduces to

$$
x_{n+1}\equiv x_n\pmod 4,
\qquad
w_{n+1}\equiv w_n\pmod 4.
$$

Therefore

$$
x_n\equiv 1\pmod 4,
\qquad
w_n\equiv 2\pmod 4.
\tag{7}
$$

It follows that

$$
t=x-6w\equiv 1\pmod 4
$$

and

$$
9w-6t\equiv 9\cdot 2-6\cdot 1\equiv 0\pmod 4.
$$

Thus $b$ is an integer, and every quantity in (2) is integral.

Substituting $x=t+6w$ into (5) gives

$$
\boxed{
 t^2+12tw-18w^2=1.
}
\tag{8}
$$

Consequently,

$$
\begin{aligned}
ab
&=8w\cdot\frac{9w-6t}{4}\\
&=18w^2-12tw\\
&=t^2-1,
\end{aligned}
$$

so

$$
\boxed{ab+1=t^2.}
\tag{9}
$$

The Pell equation also gives useful bounds. Since $w\ge 66$,

$$
49w^2<54w^2+1<\frac{225}{4}w^2.
$$

Because $x>0$, this implies

$$
7w<x<\frac{15}{2}w.
$$

Hence

$$
w<t<\frac32w.
\tag{10}
$$

Using (10),

$$
0<b=\frac{9w-6t}{4}<\frac34w<a=8w.
\tag{11}
$$

Moreover,

$$
\ell=4t-3w-1>w-1\ge 65,
$$

so $\ell\ge 3$, $r>0$, and

$$
p=\ell(2w\ell-1)
\ge 3(6w-1)
>8w=a.
\tag{12}
$$

Two direct calculations give

$$
\begin{aligned}
ap+1
&=8w\ell(2w\ell-1)+1\\
&=(4w\ell-1)^2\\
&=r^2,
\end{aligned}
\tag{13}
$$

and

$$
q-p=8w\ell+8w-2=a+2r.
$$

Thus

$$
\boxed{q=a+p+2r,}
\tag{14}
$$

and therefore $q>p>a$.

Finally, (10) gives $t>0$, so $U>1$ and $V>0$. Therefore

$$
e=(a+b)U^2+2UV>a+b>a.
\tag{15}
$$

## 3. The first Diophantine quadruple

Equations (13) and (14) imply the following six identities:

$$
\begin{aligned}
ap+1&=r^2,\\
aq+1&=(a+r)^2,\\
pq+1&=(p+r)^2,\\
ad+1&=\bigl(2r(a+r)-1\bigr)^2,\\
pd+1&=\bigl(2r(p+r)-1\bigr)^2,\\
qd+1&=\bigl(2(a+r)(p+r)+1\bigr)^2.
\end{aligned}
\tag{16}
$$

For completeness, the first three follow immediately from $q=a+p+2r$ and $ap=r^2-1$. For the last three, one again uses $ap=r^2-1$ together with

$$
(a+r)(p+r)=rq-1.
\tag{17}
$$

Thus $\mathcal Q_n=\{a,p,q,d\}$ is a Diophantine quadruple.

It remains to check that $d$ is its largest element. We already know that $a<p<q$. By (17),

$$
d=4r(rq-1),
$$

and hence

$$
d-q=(4r^2-1)q-4r.
$$

Since $r\ge 2$ and $q\ge 1$,

$$
d-q\ge 4r^2-4r-1>0.
$$

Therefore

$$
\boxed{a<p<q<d.}
\tag{18}
$$

We will use the fourth identity in (16):

$$
\boxed{
 ad+1=\bigl(2r(a+r)-1\bigr)^2.
}
\tag{19}
$$

## 4. The second Diophantine quadruple

The polynomials

$$
U=4t^2-1,
\qquad
V=4t^3-3t
$$

satisfy

$$
\boxed{
 V^2-(t^2-1)U^2=1.
}
\tag{20}
$$

Define

$$
X=V+aU,
\qquad
Y=V+bU.
\tag{21}
$$

Using (9), (20), and the definition of $e$, we obtain

$$
\begin{aligned}
X^2-1
&=V^2-1+2aUV+a^2U^2\\
&=abU^2+2aUV+a^2U^2\\
&=a\bigl((a+b)U^2+2UV\bigr)\\
&=ae,
\end{aligned}
$$

and similarly

$$
Y^2-1=be.
$$

Therefore

$$
\boxed{
ae+1=X^2,
\qquad
be+1=Y^2.
}
\tag{22}
$$

Together with (9), this proves that $\{b,a,e\}$ is a Diophantine triple.

Define

$$
d'=a+b+(2ab+1)e+2tXY.
\tag{23}
$$

The remaining three square conditions follow directly:

$$
\boxed{
\begin{aligned}
ad'+1&=(tX+aY)^2,\\
bd'+1&=(bX+tY)^2,\\
ed'+1&=(te+XY)^2.
\end{aligned}
}
\tag{24}
$$

For example,

$$
\begin{aligned}
(tX+aY)^2
&=t^2X^2+a^2Y^2+2atXY\\
&=(ab+1)(ae+1)+a^2(be+1)+2atXY\\
&=ad'+1.
\end{aligned}
$$

The second identity is symmetric. For the third,

$$
\begin{aligned}
(te+XY)^2
&=t^2e^2+2teXY+X^2Y^2\\
&=(ab+1)e^2+2teXY+(ae+1)(be+1)\\
&=ed'+1.
\end{aligned}
$$

All quantities in (23) are positive, and

$$
d'-e=a+b+2abe+2tXY>0.
$$

Thus $\{b,a,e,d'\}$ is a Diophantine quadruple with

$$
b<a<e<d'.
\tag{25}
$$

## 5. Coincidence of the largest elements

The decisive point is that $d'=d$.

From (21), (9), and the definitions of $U$ and $V$,

$$
\begin{aligned}
Z:=tX+aY
&=(t+a)V+(at+ab)U\\
&=8t^4+8at^3-8t^2-4at+1.
\end{aligned}
\tag{26}
$$

Now substitute

$$
a=8w,
\qquad
r=4w(4t-3w-1)-1.
$$

The following identity holds in the polynomial ring $\mathbb Z[t,w]$:

$$
\boxed{
\begin{aligned}
Z-\bigl(2r(a+r)-1\bigr)
={}&8(t^2-4tw+2w^2)\\
&\cdot(t^2+12tw-18w^2-1).
\end{aligned}
}
\tag{27}
$$

The second factor on the right side vanishes by (8). Hence

$$
\boxed{
 tX+aY=2r(a+r)-1.
}
\tag{28}
$$

Combining (19), (24), and (28),

$$
\begin{aligned}
ad'+1
&=(tX+aY)^2\\
&=\bigl(2r(a+r)-1\bigr)^2\\
&=ad+1.
\end{aligned}
$$

Since $a>0$, it follows that

$$
\boxed{d'=d.}
\tag{29}
$$

Consequently,

$$
\mathcal R_n=\{b,a,e,d\}
$$

is a Diophantine quadruple and

$$
\boxed{b<a<e<d.}
\tag{30}
$$

Both $\mathcal Q_n$ and $\mathcal R_n$ therefore have the same largest element $d$.

## 6. Distinctness and infinitude

By (18), every element of $\mathcal Q_n$ is at least $a$. By (11), $\mathcal R_n$ contains the element $b<a$. Hence

$$
\mathcal Q_n\ne\mathcal R_n
$$

for every $n\ge 0$.

Let

$$
\alpha=485+66\sqrt{54}>1.
$$

Its norm is $1$, so its conjugate is $\alpha^{-1}$. Taking the difference of (1) and its conjugate gives

$$
w_n=
\frac{\alpha^{2n+1}-\alpha^{-(2n+1)}}{2\sqrt{54}}.
$$

Therefore $w_n\to\infty$. From (18),

$$
d_n>a_n=8w_n,
$$

so $d_n\to\infty$. Thus the common largest elements are unbounded, and the construction yields infinitely many distinct pairs of Diophantine quadruples.

This proves Theorem 1 and gives an affirmative answer to Dujella's Problem 4.3.

## 7. Initial example

For $n=0$,

$$
(x,w,t,\ell)=(485,66,89,157),
\qquad
(a,b,r)=(528,15,41447).
$$

The construction gives

$$
\begin{aligned}
\mathcal Q_0
&=\{528,3253511,3336933,22929452257545400\},\\
\mathcal R_0
&=\{15,528,723737525421,22929452257545400\}.
\end{aligned}
$$

This is the third pair recorded by Gibbs and in Dujella's problem list.

## 8. Exact verification

The accompanying program `verify_problem_4_3.py` uses only Python's standard library. It performs two independent kinds of checks:

1. It verifies identities (20) and (27) coefficient by coefficient in $\mathbb Z[t,w]$.
2. It generates any requested number of members of the family and tests all twelve pairwise products for each pair of quadruples with exact integer arithmetic and `math.isqrt`.

For example,

```text
python verify_problem_4_3.py --count 100
```

checks the first $100$ pairs and all $1200$ square conditions. This finite computation is supplementary; the infinitude follows from the proof in Section 6.

## References

1. A. Dujella. *Open problems on Diophantine m-tuples and elliptic curves*. Problem 4.3, 2026.
2. P. Gibbs. *A Generalised Stern-Brocot Tree from Regular Diophantine Quadruples*. arXiv:math/9903035, 1999.
