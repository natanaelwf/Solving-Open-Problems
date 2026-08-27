# Two Rational Extensions of a Quadruple in Dujella's Problem 1.2

## A positive answer with the specialization $k=19$

**Publication date:** 27 August 2026  
**Status:** Complete solution  
**Field:** Number theory, rational Diophantine tuples  

The complete solution is presented below in a format designed to remain readable, searchable, and indexable directly on GitHub.

## Abstract

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rational numbers such that the product of every two distinct elements, increased by 1, is a rational square. Dujella's Problem 1.2 asks whether there is a positive integer $k \ge 2$ for which

$$
D_k = \{k-1, k+1, 4k, 16k^3-4k\}
$$

has more than one extension to a rational Diophantine quintuple. We show that $k=19$ works. The quadruple

$$
\left.D_k\right|_{k=19} = \{18,20,76,109{,}668\}
$$

admits at least the two distinct extensions

$$
\frac{132}{1849}
\qquad\text{and}\qquad
\frac{658{,}806{,}825{,}550{,}380}{9{,}003{,}099{,}140{,}750{,}557{,}441}.
$$

All required assertions are certified below by exact square identities. The second number is the specialization at $k=19$ of the regular extension of the family, while the last section records an elliptic-curve calculation that leads to the additional extension $132/1849$.

## 1. The quadruple

Put

$$
a=k-1,\qquad b=k+1,\qquad c=4k,\qquad d=4k(4k^2-1)=16k^3-4k.
$$

For every $k$ one has

$$
\begin{aligned}
ab+1 &= k^2, & ac+1 &= (2k-1)^2, & bc+1 &= (2k+1)^2,\\
ad+1 &= (4k^2-2k-1)^2, & bd+1 &= (4k^2+2k-1)^2, & cd+1 &= (8k^2-1)^2.
\end{aligned}
$$

For $k\ge 2$ the four entries are positive and strictly increasing, so $D_k$ is a Diophantine quadruple. At $k=19$ this gives

$$
(a,b,c,d)=(18,20,76,109{,}668),
$$

with the six square roots

$$
19,\qquad 37,\qquad 39,\qquad 1405,\qquad 1481,\qquad 2887.
$$

## 2. An additional extension at $k=19$

The following identities give an elementary certificate and also explain why the value $k=19$ occurs. Define

$$
q=2k+5,\qquad n=7k-1.
$$

Direct expansion gives

$$
\begin{aligned}
(3k+8)^2-\left(q^2+(k-1)n\right)
  &= -2(k-19)(k+1), && \text{(1)}\\
(3k+10)^2-\left(q^2+(k+1)n\right)
  &= -2(k-19)(k+2), && \text{(2)}\\
(5k+14)^2-\left(q^2+4kn\right)
  &= -(k-19)(7k+9), && \text{(3)}\\
(10k^2+10k+5)^2-\left(q^2+4k(4k^2-1)n\right)
  &= -4k(k-19)(3k^2+3k+1), && \text{(4)}
\end{aligned}
$$

At $k=19$ one has $q=43$ and $n=132$, and all four right-hand sides vanish. Therefore, for

$$
x_{\mathrm{add}}=\frac{n}{q^2}=\frac{132}{1849},
$$

equations (1)-(4) become

$$
\begin{aligned}
18x_{\mathrm{add}}+1 &= \left(\frac{65}{43}\right)^2,
& 20x_{\mathrm{add}}+1 &= \left(\frac{67}{43}\right)^2,\\
76x_{\mathrm{add}}+1 &= \left(\frac{109}{43}\right)^2,
& 109{,}668x_{\mathrm{add}}+1 &= \left(\frac{3805}{43}\right)^2.
\end{aligned}
$$

Thus $x_{\mathrm{add}}$ extends the quadruple $\{18,20,76,109{,}668\}$.

## 3. The regular extension

The regular extension written down by Stoll (2019, Theorem 7.1) is

$$
\begin{aligned}
f(k)
&=
\frac{4k(2k-1)(2k+1)(4k^2-2k-1)(4k^2+2k-1)(8k^2-1)}
{(64k^6-80k^4+16k^2-1)^2},
&& \text{(5)}
\end{aligned}
$$

At $k=19$, write

$$
H=3{,}000{,}516{,}479,\qquad N=658{,}806{,}825{,}550{,}380.
$$

Then $f(19)=N/H^2$, so

$$
x_{\mathrm{reg}}=
\frac{658{,}806{,}825{,}550{,}380}
{9{,}003{,}099{,}140{,}750{,}557{,}441}.
$$

For completeness, its extension property does not need to be taken on citation: the following exact identities verify it directly,

$$
\begin{aligned}
H^2+18N &= 3{,}002{,}491{,}909^2,
& H^2+20N &= 3{,}002{,}711{,}321^2,\\
H^2+76N &= 3{,}008{,}848{,}361^2,
& H^2+109{,}668N &= 9{,}014{,}051{,}591^2.
\end{aligned}
$$

After division by $H^2$, these give

$$
\begin{aligned}
18x_{\mathrm{reg}}+1
&=\left(\frac{3{,}002{,}491{,}909}{3{,}000{,}516{,}479}\right)^2,
&
20x_{\mathrm{reg}}+1
&=\left(\frac{3{,}002{,}711{,}321}{3{,}000{,}516{,}479}\right)^2,\\
76x_{\mathrm{reg}}+1
&=\left(\frac{3{,}008{,}848{,}361}{3{,}000{,}516{,}479}\right)^2,
&
109{,}668x_{\mathrm{reg}}+1
&=\left(\frac{9{,}014{,}051{,}591}{3{,}000{,}516{,}479}\right)^2.
\end{aligned}
$$

Thus $x_{\mathrm{reg}}$ is a second extension of the same quadruple.

## 4. Distinctness and conclusion

Both extensions are positive. Moreover,

$$
1000N=658{,}806{,}825{,}550{,}380{,}000
<9{,}003{,}099{,}140{,}750{,}557{,}441=H^2,
$$

so $x_{\mathrm{reg}}<1/1000$. On the other hand,

$$
1849<20\cdot132
\qquad\text{and}\qquad
132<1849,
$$

so $1/20<x_{\mathrm{add}}<1$. Consequently

$$
0<x_{\mathrm{reg}}<\frac{1}{1000}<\frac{1}{20}<x_{\mathrm{add}}<1.
$$

The two extensions are therefore distinct, and neither is one of the four positive integer entries of the quadruple.

**Theorem 1.** *Problem 1.2 has an affirmative answer. One may take* $k=19$. *The Diophantine quadruple*

$$
\{18,20,76,109{,}668\}
$$

*has at least the two distinct rational extensions*

$$
\frac{132}{1849}
\qquad\text{and}\qquad
\frac{658{,}806{,}825{,}550{,}380}
{9{,}003{,}099{,}140{,}750{,}557{,}441}.
$$

**Remark 1.** *The argument establishes the existence of at least two extensions; it does not attempt to determine all rational extensions of the quadruple at* $k=19$.

## 5. How the additional extension was located

This section is not needed for the proof above. It records a short elliptic-curve calculation that produces the candidate $132/1849$.

For a rational Diophantine triple $\{a,b,c\}$, consider

$$
E_{a,b,c}:\qquad Y^2=(X+ab)(X+ac)(X+bc)
$$

and the point $P=(0,abc)$. If $z$ extends the triple and

$$
az+1=u^2,\qquad bz+1=v^2,\qquad cz+1=w^2,
$$

with $uvw\ne0$, then

$$
R_z=(abcz,abcuvw)\in E_{a,b,c}(\mathbb{Q}).
$$

For a curve with full rational 2-torsion, the usual Kummer map is an injection

$$
E_{a,b,c}(\mathbb{Q})/2E_{a,b,c}(\mathbb{Q})
\hookrightarrow
\left(\mathbb{Q}^{\times}/\mathbb{Q}^{\times 2}\right)^3.
$$

Away from the 2-torsion points, it is represented by

$$
\delta(X,Y)=(X+ab,X+ac,X+bc)
\qquad\text{modulo rational squares}.
$$

Since

$$
\begin{aligned}
X(R_z)+ab &= ab(cz+1),\\
X(R_z)+ac &= ac(bz+1),\\
X(R_z)+bc &= bc(az+1),
\end{aligned}
$$

one has $\delta(R_z)=\delta(P)$. Thus every such extension is represented by a point in the coset

$$
P+2E_{a,b,c}(\mathbb{Q}).
$$

The candidate used below satisfies the nonvanishing condition.

For the triple $\{k-1,k+1,4k\}$, the curve is

$$
E_k:\qquad
Y^2=(X+k^2-1)(X+4k(k-1))(X+4k(k+1)),
$$

with

$$
P_k=(0,4k(k^2-1)).
$$

Whenever $s^2=3k+7$, the point

$$
Q_k=(8-4k(k+1),8(k-1)s)
$$

lies on $E_k$. Indeed, at its $X$-coordinate the three factors are

$$
-(k-1)s^2,\qquad -8(k-1),\qquad 8,
$$

whose product is $[8(k-1)s]^2$.

Taking $s=8$ gives $k=19$. Hence

$$
E_{19}:\qquad Y^2=(X+360)(X+1368)(X+1520),
$$

with

$$
P=(0,27{,}360),\qquad Q=(-1512,1152).
$$

A direct application of the elliptic-curve group law gives

$$
2Q=\left(\frac{17{,}329}{4},-\frac{3{,}165{,}111}{8}\right)
$$

and

$$
P+2Q=\left(\frac{3{,}611{,}520}{1849},\frac{12{,}987{,}655{,}200}{79{,}507}\right).
$$

Since $abc=18\cdot20\cdot76=27{,}360$, the associated value is

$$
z=\frac{X(P+2Q)}{abc}
=\frac{3{,}611{,}520/1849}{27{,}360}
=\frac{132}{1849}.
$$

The remaining condition against the fourth element is exactly

$$
109{,}668z+1=\left(\frac{3805}{43}\right)^2,
$$

as already verified in Section 2.

## References

1. A. Dujella. *Open problems on Diophantine m-tuples and elliptic curves*. Problem 1.2, 2026.
2. M. Stoll. “Diagonal genus 5 curves, elliptic curves over $\mathbb{Q}(t)$, and rational Diophantine quintuples.” *Acta Arith.* **190** (2019), no. 3, 239-261.
