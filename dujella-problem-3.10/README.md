# Elliptic Curves of Rank at Least Eleven Induced by Rational Diophantine Quadruples

## An affirmative answer to Dujella's Problem 3.10

**Author:** Natanael Wildner Fraga  
**Date:** 30 October 2026  
**Status:** Complete affirmative solution  
**Field:** Number theory, rational Diophantine quadruples, elliptic curves

## Abstract

We prove that infinitely many rational Diophantine quadruples induce elliptic curves over $\mathbb{Q}$ of rank at least eleven, answering Dujella's Problem 3.10. Starting from a curve of Dujella and Peral, an explicit genus-one construction reduces the question to positive rank of one auxiliary elliptic curve $F$. Complete local $2$‑descent and a Cassels-pairing calculation give $\dim_{\mathbb{F}_2}\mathrm{Sel}_2(F/\mathbb{Q})=9$, infinite-Selmer corank one, and finite two-primary Shafarevich-Tate quotient $(\mathbb{Z}/2\mathbb{Z})^6$. A specialized proof using the cyclotomic, ring-class, and coefficient constructions of OpenAI (2026) gives analytic rank and Mordell-Weil rank one for $F$ and finiteness of its Shafarevich-Tate group. The local comparisons, integral descent, determinant estimates, and finite graph arguments are supplied in the appendices. Given any nontorsion rational point on $F$, one of its first eight positive even multiples yields a valid quadruple. Every curve produced by this construction is $\mathbb{Q}$‑isomorphic to the source curve. The finite arithmetic certificates use exact integer and rational computations.

**Keywords:** Diophantine quadruples; elliptic curves; $2$‑descent; Cassels pairing.  
**2020 Mathematics Subject Classification:** 11D09, 11G05, 11Y50.

## 1. The problem and the precise conclusion

A rational Diophantine quadruple is a set of four distinct nonzero rational numbers $\{a,b,c,d\}$ such that

```math
ab+1,\quad ac+1,\quad ad+1,\quad bc+1,\quad bd+1,\quad cd+1
```

are squares in $\mathbb{Q}$. Negative entries and the square $0=0^2$ are allowed.

Following Dujella and Soydan (2022), the induced elliptic curve is

**Equation (1.1).**

```math
E_{a,b,c,d}:\quad
 y^2=x\bigl(x+(b-a)(d-c)\bigr)\bigl(x+(c-a)(d-b)\bigr).
```

This convention agrees with the genus-one curve

```math
W^2=(aZ+1)(bZ+1)(cZ+1)(dZ+1).
```

Indeed, the rational substitution

```math
\begin{aligned}
x&=\frac{(aZ+1)(d-b)(d-c)}{dZ+1},\\
y&=\frac{W(d-a)(d-b)(d-c)}{(dZ+1)^2}
\end{aligned}
```

gives (1.1). The distinctness assumptions make both curves nonsingular. The two nonzero coefficients satisfy

```math
(c-a)(d-b)-(b-a)(d-c)=(c-b)(d-a)\ne0.
```

Problem 3.10 in Dujella's list asks whether a curve of this kind can have rank greater than ten over $\mathbb{Q}$. The problem is an existence question about a curve; it does not require infinitely many isomorphism classes.

Set

**Equation (1.2).**

```math
\begin{aligned}
E_0 &: Y^2=X(X+A)(X+B),\\
A&=4728112640493176179,\\
B&=-313185162402159696,
\end{aligned}
```

and

**Equation (1.3).**

```math
\begin{aligned}
F &: \eta^2=\xi(\xi+\alpha)(\xi+\beta),\\
\alpha&=2836090012790868622112037290311559991949411485715,\\
\beta&=2097621505422395657915349531407756829023138973264.
\end{aligned}
```

Write

```math
s_2(F)=\mathrm{corank}_{\mathbb{Z}_2}\mathrm{Sel}_{2^\infty}(F/\mathbb{Q}).
```

The Selmer groups in this article use the usual local Kummer conditions at every place.

**Theorem 1.1.** The curves (1.2) and (1.3) satisfy the following statements.

1. $\mathrm{rank}E_0(\mathbb{Q})\ge11$.
2. $\dim_{\mathbb{F}_2}\mathrm{Sel}_2(F/\mathbb{Q})=9$ and $s_2(F)=1$.
3. $\mathrm{ord}_{s=1}L(F,s)=\mathrm{rank}F(\mathbb{Q})=1$, the group $\mathrm{Sha}(F/\mathbb{Q})$ is finite, and $\mathrm{Sha}(F/\mathbb{Q})[2^\infty]\cong(\mathbb{Z}/2\mathbb{Z})^6$.
4. Infinitely many distinct rational Diophantine quadruples induce curves $\mathbb{Q}$‑isomorphic to $E_0$. For any given nontorsion rational point on $F$, the construction in Section 3 produces an admissible quadruple from at least one of its first eight positive even multiples.

**Corollary 1.2.** There is an elliptic curve over $\mathbb{Q}$ induced by a rational Diophantine quadruple with rank greater than ten. Thus Dujella's Problem 3.10 has an affirmative answer.

Sections 2 and 3 prove the source rank bound and the reconstruction. Sections 4 and 5 establish the finite Selmer and Cassels-pairing calculations. Section 6 applies the specialized positive-rank theorem proved in the appendices. The determinant and coefficient constructions used there are those of OpenAI (2026); their required local and integral comparisons are proved with the hypotheses of the auxiliary curve. The source curve and its eleven points are due to Dujella and Peral. The conclusion concerns infinitely many quadruples in one $\mathbb{Q}$‑isomorphism class of induced curves.

## 2. A curve of rank at least eleven

The curve (1.2) and the following points come from Dujella and Peral's 2017 entry in Dujella's table. The coordinate translation from that entry is $X=x-1471642492697005494$, $Y=y$.

| $i$ | $X_i$ | $Y_i$ |
|---:|---:|---:|
| 1 | $-2455690635183512034$ | $3930819100635430521717292170$ |
| 2 | $-1251776678706189504$ | $2609613406782334033646479200$ |
| 3 | $-1272661460204312304$ | $2640823754547721254370236000$ |
| 4 | $-1994688924155600904$ | $3547293495901125966835824600$ |
| 5 | $440641873774783296$ | $538787101369161261182781600$ |
| 6 | $-127433871797554344$ | $508258934492965396363625640$ |
| 7 | $-1352464454208354354$ | $2757613161989370207496135050$ |
| 8 | $-2756837135466868104$ | $4084604229675007831346026200$ |
| 9 | $-1057278032568400104$ | $2306272930055777531757724200$ |
| 10 | $-913127974330002354$ | $2066868814798457862205063050$ |
| 11 | $1640792454010339014$ | $3724723407453925712515593606$ |

**Proposition 2.1.** The curve $E_0$ has rank at least eleven over $\mathbb{Q}$.

*Proof.* Integer substitution verifies that all eleven points lie on $E_0$. For a split cubic, the Kummer map (Silverman, 2009) injects $E_0(\mathbb{Q})/2E_0(\mathbb{Q})$ into $(\mathbb{Q}^\times/\mathbb{Q}^{\times2})^3$. Away from the two-torsion points it is

```math
\kappa(X,Y)=([X],[X+A],[X+B]).
```

At $(0,0)$ and $(-A,0)$ the values are, respectively,

```math
([AB],[A],[B]),\qquad
([-A],[A(A-B)],[B-A]).
```

Use the sign and the valuation parities at

```math
\begin{gathered}
2,3,5,7,11,31,43,67,73,89,173,181,\\
421,461,599,4943,7643,8893,111121
\end{gathered}
```

to encode a squareclass by twenty bits, with the sign in bit zero. Every remaining positive factor is an integer square. Concatenate the three coordinates, with the first coordinate in the least significant block.

For the eleven points followed by the two torsion points, the resulting hexadecimal integers are

| Point | Encoded Kummer class | Point | Encoded Kummer class |
|---:|:---|---:|:---|
| 1 | `819eb9459815c73` | 8 | `883439830010043` |
| 2 | `13e15078051461` | 9 | `11a33019031033` |
| 3 | `96000860001` | 10 | `1075050050407` |
| 4 | `39c34019043853` | 11 | `23623031032072` |
| 5 | `21a04019042030` | 12 | `28457441076c55` |
| 6 | `214f3050832447` | 13 | `88209fc61874411` |
| 7 | `80433c01034053` |  |  |

Binary elimination, using the largest set bit as pivot and numbering bits from zero, gives the thirteen distinct pivot positions

```math
37,42,43,45,46,47,48,49,51,52,53,55,59.
```

Thus the Kummer image has dimension at least thirteen. Since $E_0(\mathbb{Q})[2]\cong(\mathbb{Z}/2\mathbb{Z})^2$, the Mordell-Weil theorem gives

```math
\dim_{\mathbb{F}_2}E_0(\mathbb{Q})/2E_0(\mathbb{Q})
=\mathrm{rank}E_0(\mathbb{Q})+2.
```

Therefore $\mathrm{rank}E_0(\mathbb{Q})\ge11$. This argument requires neither saturation nor finiteness of $\mathrm{Sha}$. □

## 3. The auxiliary curve and the reconstruction

### 3.1. A source double and its auxiliary

Choose

```math
P=(X_0,Y_0)=(912833416575231921,-1757195268626559090518724150).
```

This point is a double on $E_0$. An exact certificate is

```math
H=(5761058741699892246,-18144092568468363333046645050),\qquad 2H=P.
```

Both the curve equation for $H$ and the duplication identity hold over $\mathbb{Q}$. One can also check

```math
\begin{aligned}
X_0&=955423161^2,\\
X_0+A&=2375067590^2,\\
X_0+B&=774369585^2.
\end{aligned}
```

Define

**Equation (3.1).**

```math
u=\frac{X_0(X_0+A)}{Y_0},\qquad
v=\frac{X_0(X_0+B)}{Y_0},\qquad
w=\frac{Y_0}{X_0}.
```

Their values are

```math
u=-2930376694,\qquad
v=-\frac{7337240409411}{23554},\qquad
w=-\frac{4887549804850}{2539}.
```

The curve equation gives

**Equation (3.2).**

```math
\begin{gathered}
uv=X_0,\qquad uw=X_0+A,\qquad vw=X_0+B,\\
u(w-v)=A,\qquad v(w-u)=B.
\end{gathered}
```

In particular, $uv,uw,vw$ are nonzero rational squares. Set

**Equation (3.3).**

```math
\begin{gathered}
h=u-v-w,\qquad j=u-v+w,\qquad k=u+v-w,\qquad V=uvw,\\
C=w(u-v)k^2,\qquad D=v(u-w)j^2,
\end{gathered}
```

and put

```math
F_P:\quad y^2=x(x+C)(x+D).
```

For $\tau=105/59803606$ one has $C=\tau^2\alpha$ and $D=\tau^2\beta$. Thus

**Equation (3.4).**

```math
\psi:F\longrightarrow F_P,\qquad
(\xi,\eta)\longmapsto(\tau^2\xi,\tau^3\eta)
```

is a $\mathbb{Q}$‑isomorphism preserving the origin and doubles. Direct rational arithmetic verifies

**Equation (3.5).**

```math
uvw(u-v)(u-w)(v-w)hjkCD(C-D)\ne0.
```

### 3.2. Universal identities

**Lemma 3.1.** Let $Q=(x,y)\in F_P(\mathbb{Q})$ with $y\ne0$. Define

**Equation (3.6).**

```math
\begin{gathered}
c_0=vw-\frac{h^2}{4},\qquad K=Vhjk,\qquad T=x+vwjk,\\
a=\frac{2c_0T+K}{y},\qquad
\lambda=-\frac{T^2}{2Vy},\\
(b,c,d)=(a+\lambda u,a+\lambda v,a+\lambda w).
\end{gathered}
```

Then

**Equation (3.7).**

```math
\begin{aligned}
ab+1&=\frac{T^2h^2x}{4vwy^2},&
ac+1&=\frac{T^2j^2(x+C)}{4uwy^2},\\
ad+1&=\frac{T^2k^2(x+D)}{4uvy^2},&
bc+1&=\frac{T^2x(x+C)}{4uvw^2y^2},\\
bd+1&=\frac{T^2x(x+D)}{4uv^2wy^2},&
cd+1&=\frac{T^2(x+C)(x+D)}{4u^2vwy^2}.
\end{aligned}
```

If $Q\in2F_P(\mathbb{Q})$, all six quantities are rational squares.

*Proof.* Work first in $\mathbb{Z}[u,v,w,x]$, with the definitions (3.3), $T=x+vwjk$ and $Y_2=x(x+C)(x+D)$. Put

```math
\begin{aligned}
N_a&=V\bigl((4vw-h^2)T+2Vhjk\bigr),\\
N_b&=N_a-uT^2,\quad N_c=N_a-vT^2,\quad N_d=N_a-wT^2.
\end{aligned}
```

Expansion gives

**Equation (3.8).**

```math
\begin{aligned}
N_aN_b+4V^2Y_2&=u^2vwT^2h^2x,\\
N_aN_c+4V^2Y_2&=uv^2wT^2j^2(x+C),\\
N_aN_d+4V^2Y_2&=uvw^2T^2k^2(x+D),\\
N_bN_c+4V^2Y_2&=uvT^2x(x+C),\\
N_bN_d+4V^2Y_2&=uwT^2x(x+D),\\
N_cN_d+4V^2Y_2&=vwT^2(x+C)(x+D).
\end{aligned}
```

These are polynomial identities before specialization. On $F_P$ one has $Y_2=y^2$ and $(a,b,c,d)=(N_a,N_b,N_c,N_d)/(2Vy)$. Division by $4V^2y^2$ proves (3.7).

If $Q$ is a double, the split-cubic Kummer criterion gives $x,x+C,x+D\in\mathbb{Q}^{\times2}$. By (3.2), all the remaining factors in the denominators of (3.7) are rational squares. This proves the last assertion. □

### 3.3. Admissibility and infinitude

**Lemma 3.2.** For every nontorsion $R\in F(\mathbb{Q})$, at least one of

```math
Q_n=\psi(2nR),\qquad 1\le n\le8,
```

produces four distinct nonzero rational numbers through (3.6).

*Proof.* Each $Q_n$ is affine and has $y\ne0$. Their abscissas are distinct, since equal abscissas would give $2mR=\pm2nR$ and contradict nontorsion.

The factor $\lambda$ cannot vanish at any rational affine point with $y\ne0$. Otherwise $T=0$ and $b=a$, while the first identity in (3.7) would give $a^2+1=0$.

The numerator $N(x)=2c_0(x+vwjk)+K$ of $a$ is a nonzero polynomial of degree at most one: if $c_0=0$, its constant term is $K\ne0$. The numerators of $b,c,d$ are

```math
N(x)-\frac{u}{2V}(x+vwjk)^2,\quad
N(x)-\frac{v}{2V}(x+vwjk)^2,\quad
N(x)-\frac{w}{2V}(x+vwjk)^2.
```

They are genuine quadratics. Thus at most seven abscissas can give a zero entry. At least one of the eight abscissas is good. Every pairwise difference of the entries is $\lambda$ times one of $u,v,w,v-u,w-u,w-v$, all nonzero by (3.5). All six squares in (3.7) are nonzero, since $x(x+C)(x+D)=y^2\ne0$, $T\ne0$, and (3.5) holds. □

**Proposition 3.3.** If $\mathrm{rank}F(\mathbb{Q})\gt 0$, infinitely many distinct rational Diophantine quadruples induce curves $\mathbb{Q}$‑isomorphic to $E_0$.

*Proof.* Lemmas 3.1 and 3.2 produce an admissible quadruple from a double. Its induced coefficients satisfy

```math
\begin{aligned}
(b-a)(d-c)&=\lambda^2u(w-v)=\lambda^2A,\\
(c-a)(d-b)&=\lambda^2v(w-u)=\lambda^2B.
\end{aligned}
```

The map $(X,Y)\mapsto(\lambda^2X,\lambda^3Y)$ is therefore a $\mathbb{Q}$‑isomorphism from $E_0$ to (1.1). Proposition 2.1 transfers the rank lower bound.

For infinitude, take all $Q_n=\psi(2nR)$ with $n\ge1$. Only finitely many have a bad abscissa. As a rational function on the smooth projective curve $F_P$,

```math
\lambda=-\frac{(x+vwjk)^2}{2Vy}
```

has a simple pole at the origin, since $\mathrm{ord}_O(x)=-2$ and $\mathrm{ord}_O(y)=-3$. Hence it is nonconstant and has finite fibers. Infinitely many good $Q_n$ give infinitely many values of $\lambda$. The ordered quadruple determines $\lambda=(b-a)/u$, and an unordered set has at most twenty-four orderings. This proves the assertion for distinct sets. □

## 4. Complete local 2-descent

### 4.1. The global squareclass space

The following factorizations are exact:

**Equation (4.1).**

```math
\begin{aligned}
\alpha={}&5\cdot43^2\cdot67^2\cdot73\cdot283^2\cdot599\\
 &\cdot23971^2\cdot111121\cdot552823181^2,\\
\beta={}&2^4\cdot3^5\cdot11^2\cdot23^2\cdot31\cdot173\cdot181^2\\
 &\cdot421\cdot953^2\cdot354212181139^2,\\
\alpha-\beta={}&7\cdot13^2\cdot47^2\cdot89\cdot461\cdot4217^2\\
 &\cdot4943\cdot7643\cdot8893\cdot1073681107^2.
\end{aligned}
```

All displayed factors are prime. The accompanying data include recursive Lucas certificates: for each $n\gt 2$, a complete factorization of $n-1$ and an integer $a$ satisfying

```math
a^{n-1}\equiv1\pmod n,\qquad
\gcd\bigl(a^{(n-1)/q}-1,n\bigr)=1
\quad(q\mid n-1, q\text{ prime}).
```

If $p\mid n$ is prime, these conditions force the order of $a$ modulo $p$ to be divisible by $n-1$. Hence $p\ge n$, proving primality. Recursion terminates at 2.

Let $S$ be the ordered list of primes dividing $2\alpha\beta(\alpha-\beta)$:

**Equation (4.2).**

```math
\begin{gathered}
2,3,5,7,11,13,23,31,43,47,67,73,89,173,181,283,\\
421,461,599,953,4217,4943,7643,8893,23971,111121,\\
552823181,1073681107,354212181139.
\end{gathered}
```

Use the first two Kummer coordinates $([\xi],[\xi+\alpha])$; the third is their product. Each global coordinate is supported on $(-1,p:p\in S)$, so the ambient binary space has dimension sixty.

### 4.2. Exact local images

For odd $p$, write $z=p^v u$ with $u\in\mathbb{Z}_p^\times$ and encode its squareclass by

```math
(v\bmod2,\epsilon_p(u)),\qquad
\epsilon_p(u)=\begin{cases}0,&u\text{ square modulo }p,\\1,&u\text{ nonsquare modulo }p.\end{cases}
```

At 2, use the squareclass basis $(2,-1,5)$; the odd unit modulo eight specifies its last two bits. Concatenate the first and second Kummer coordinates with the first in the least significant bits.

The torsion witnesses $T_0,T_\alpha$ have Kummer pairs

```math
T_0:(\alpha\beta,\alpha),\qquad
T_\alpha:(-\alpha,\alpha(\alpha-\beta)).
```

An integer witness $n$ below means a local point of abscissa $\xi=n$. Direct valuation and unit tests show that $n(n+\alpha)(n+\beta)$ is a nonzero square in $\mathbb{Q}_p$. Each pair in the table records a witness followed by its encoded vector in decimal.

| $p$ | First witness (vector) | Second witness (vector) | Third witness (vector) |
|---:|:---:|:---:|:---:|
| $2$ | $T_0\;(50)$ | $T_\alpha\;(4)$ | $-2\;(3)$ |
| $3$ | $T_0\;(3)$ | $T_\alpha\;(2)$ |  |
| $5$ | $T_0\;(15)$ | $2\;(10)$ |  |
| $7$ | $T_0\;(8)$ | $T_\alpha\;(12)$ |  |
| $11$ | $T_0\;(2)$ | $11\;(1)$ |  |
| $13$ | $T_\alpha\;(8)$ | $-1\;(12)$ |  |
| $23$ | $T_0\;(8)$ | $-2\;(2)$ |  |
| $31$ | $T_0\;(3)$ | $T_\alpha\;(2)$ |  |
| $43$ | $T_\alpha\;(10)$ | $43\;(5)$ |  |
| $47$ | $T_\alpha\;(10)$ | $1\;(8)$ |  |
| $67$ | $T_\alpha\;(10)$ | $67\;(5)$ |  |
| $73$ | $T_0\;(15)$ | $-5\;(10)$ |  |
| $89$ | $T_0\;(8)$ | $T_\alpha\;(6)$ |  |
| $173$ | $T_0\;(1)$ | $-2\;(2)$ |  |
| $181$ | $-2\;(2)$ | $181\;(1)$ |  |
| $283$ | $T_0\;(2)$ | $-6\;(10)$ |  |
| $421$ | $T_0\;(3)$ | $2\;(2)$ |  |
| $461$ | $T_\alpha\;(4)$ | $-4\;(8)$ |  |
| $599$ | $T_0\;(15)$ | $T_\alpha\;(5)$ |  |
| $953$ | $T_0\;(2)$ | $953\;(1)$ |  |
| $4217$ | $-8\;(8)$ | $-1193\;(4)$ |  |
| $4943$ | $T_\alpha\;(6)$ | $4\;(8)$ |  |
| $7643$ | $T_0\;(8)$ | $T_\alpha\;(4)$ |  |
| $8893$ | $T_0\;(8)$ | $T_\alpha\;(6)$ |  |
| $23971$ | $T_0\;(2)$ | $-1\;(10)$ |  |
| $111121$ | $T_0\;(15)$ | $7\;(10)$ |  |
| $552823181$ | $T_0\;(10)$ | $552823181\;(5)$ |  |
| $1073681107$ | $T_\alpha\;(10)$ | $1\;(8)$ |  |
| $354212181139$ | $T_0\;(8)$ | $-1\;(2)$ |  |

The displayed vectors are independent. They form complete local bases because

```math
\#\bigl(F(\mathbb{Q}_p)/2F(\mathbb{Q}_p)\bigr)
=\frac{\#F(\mathbb{Q}_p)[2]}{\vert 2\vert _p}
=\begin{cases}4,&p\ne2,\\8,&p=2.\end{cases}
```

At the real place, $\alpha\gt \beta\gt 0$, so the possible abscissas lie in $[-\alpha,-\beta]\cup[0,\infty)$. The local sign pairs are $(0,0)$ and $(1,0)$; the global sign bit of the second coordinate must therefore vanish.

For $p\notin S$, the curve has good reduction and $p$ is odd. The Kummer image is the unramified subgroup, of size four. Both global coordinates already have even valuation there. Thus no further local condition is required.

### 4.3. The global matrix

For each $p\in S$, take the annihilator of the displayed local span under the ordinary binary dot product and compose it with the localization of the sixty global squareclass coordinates. Append the real sign condition. Call the resulting matrix $M$.

Order the global coordinates as thirty exponents for the first Kummer coordinate followed by thirty for the second. For a reproducible row basis, scan local annihilators in increasing encoded order and retain independent vectors by largest-set-bit elimination. The resulting matrix has sixty rows, and its pivot positions are

```math
\begin{gathered}
4,6,7,9,10,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,\\
30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,\\
47,48,49,50,51,52,53,54,55,56,57,58,59.
\end{gathered}
```

Nine independent kernel vectors, in hexadecimal, are

```math
\begin{matrix}
\mathtt{161000004000001}&\mathtt{20080000020002}&\mathtt{50080000004004}\\
\mathtt{40080200024008}&\mathtt{71080400020020}&\mathtt{140000404020100}\\
\mathtt{1600a0404024800}&\mathtt{600c0400025000}&\mathtt{32080000080000}.
\end{matrix}
```

Their scalar products with every row vanish. By the local characterization of the Selmer group, $\ker M=\mathrm{Sel}_2(F/\mathbb{Q})$. Hence

**Equation (4.3).**

```math
\dim_{\mathbb{F}_2}\mathrm{Sel}_2(F/\mathbb{Q})=60-51=9.
```

## 5. The Cassels pairing and the infinite Selmer corank

### 5.1. Coverings and tangent forms

Decode the nine kernel vectors in Section 4.3 as squarefree triples $(d_1,d_2,d_3)$, in coordinate order $\xi,\xi+\alpha,\xi+\beta$. The third coordinate is the squarefree representative of the product of the first two.

| Basis index | $d_1$ | $d_2$ | $d_3$ |
|---:|---:|---:|---:|
| 1 | $-111121$ | $3481843271918419$ | $-31333800739$ |
| 2 | $842$ | $680227$ | $572751134$ |
| 3 | $519$ | $3912270811$ | $2030468550909$ |
| 4 | $364165$ | $3957385$ | $57645644341$ |
| 5 | $4631$ | $96492094703942371$ | $446854890573957120101$ |
| 6 | $1450240171$ | $6917393371$ | $812437801$ |
| 7 | $542249478131$ | $315261648618539539$ | $3084099617887841$ |
| 8 | $5316809$ | $3091171201321$ | $3084099617887841$ |
| 9 | $599$ | $2014054874539$ | $3362362061$ |

For a triple $d$, the associated covering has projective coordinates $(t_0,t_1,t_2,t_3)$ and equations

**Equation (5.1).**

```math
\begin{aligned}
H_1&=(\beta-\alpha)t_0^2+d_2t_2^2-d_3t_3^2=0,\\
H_2&=-\beta t_0^2+d_3t_3^2-d_1t_1^2=0,\\
H_3&=\alpha t_0^2+d_1t_1^2-d_2t_2^2=0.
\end{aligned}
```

They sum to zero; any two define the covering. An affine local point is specified by $t_0=1$ and

```math
t_1^2=\xi/d_1,\qquad t_2^2=(\xi+\alpha)/d_2,\qquad t_3^2=(\xi+\beta)/d_3.
```

View $H_i$ as a conic in its three occurring variables. Choose a primitive integral point $Q_i$ and let $L_i$ be its primitive tangent form. The supplied certificate contains all twenty-seven such conic points. The tangent coefficients are the coordinatewise products of the conic coefficients and $Q_i$, divided by their common content. Exact substitution verifies the conic equations and primitivity.

Cassels's formula, in this split-cubic convention, is

**Equation (5.2).**

```math
\langle d,d'\rangle=\sum_v\sum_{i=1}^3[L_i(P_v),d'_i]_v\in\mathbb{F}_2,
```

where $P_v$ is a local covering point avoiding the tangent zeros and $[\ ,\ ]_v$ is the additive quadratic Hilbert symbol. Here $H_i$ omits $t_i$, and $L_i$ pairs with $d'_i$. The formula and its identification with Cassels-Tate are given by Fisher, Schaefer and Stoll (2010, Section 3 and Theorem 5.2); see also Wang and Zhang (2022, Section 2.3). The common denominator in the tangent functions cancels because $d'_1d'_2d'_3$ is a square. Rational rescaling of any tangent does not change the global sum, by Hilbert reciprocity.

### 5.2. Exact local certificates

For each of the nine coverings and every $p\in S$, the data specify a rational abscissa $\xi$ and rational approximations $u_i$ to the three square roots. Put

```math
r_1=\xi/d_1,\qquad r_2=(\xi+\alpha)/d_2,\qquad r_3=(\xi+\beta)/d_3.
```

Each of these 261 certificates satisfies

**Equation (5.3).**

```math
v_p(u_i^2-r_i)\gt 2v_p(2u_i).
```

For a nonintegral approximation, use $t_i=u_i z$: the normalized polynomial $z^2-r_i/u_i^2$ has unit constant term and satisfies $v_p(1-r_i/u_i^2)\gt 2v_p(2)$. Thus the integral form of Hensel's lemma applies as well. It supplies an actual root $s_i^2=r_i$ with

```math
v_p(s_i-u_i)\ge e_i:=v_p(u_i^2-r_i)-v_p(2u_i).
```

An exact rational root is assigned error bound $+\infty$. Thus $(1,s_1,s_2,s_3)$ is a genuine local point. For $L_j=\sum_{i=0}^3ℓ_{ji}t_i$, set $u_0=1$, $e_0=+\infty$ and

```math
a_j=\sum_iℓ_{ji}u_i,\qquad
E_j=\min_{ℓ_{ji}\ne0}\bigl(v_p(ℓ_{ji})+e_i\bigr).
```

Then $v_p(L_j(P_p)-a_j)\ge E_j$. The certificates verify

**Equation (5.4).**

```math
E_j\gt v_p(a_j)\quad(p\ne2),\qquad
E_j\gt v_2(a_j)+2\quad(p=2).
```

Consequently the true tangent value is nonzero and has the same squareclass as $a_j$.

For odd $p$, write $a=p^r u$, $b=p^s w$ with $p$‑adic units $u,w$. The symbol is

```math
[a,b]_p=rs\frac{p-1}{2}+r\epsilon_p(w)+s\epsilon_p(u)\pmod2.
```

At 2, the unit residues modulo eight give

```math
[a,b]_2=\frac{u-1}{2}\frac{w-1}{2}
+r\frac{w^2-1}{8}+s\frac{u^2-1}{8}\pmod2.
```

At the real place choose $\xi=1$ for $d_1\gt 0$ and $\xi=-(\alpha+\beta)/2$ for the sole triple with $d_1\lt 0$. All three $r_i$ are positive. Rational intervals with denominator $2^{320}$ enclose their square roots. Propagating the signed intervals through the tangents gives intervals avoiding zero. The resulting signs determine $[a,b]_\infty$, which equals one precisely when $a\lt 0$ and $b\lt 0$.

### 5.3. Vanishing outside the support

For $p\notin S$, the diagonal conic coefficients and every $d'_i$ are units. Primitive conic points reduce to nonzero smooth points. The contents removed from the tangent forms have support in $S$, as the certificate verifies.

The covering has good reduction outside $S$. Choose a primitive integral local point avoiding the tangent zeros. Each conic projection is primitive: otherwise another equation in (5.1), with unit coefficients, would force all four projective coordinates to vanish modulo $p$.

On a smooth conic over $\mathbb{Z}_p$, a tangent at an integral smooth point cuts out twice that point. Its nonzero evaluation on a primitive integral point therefore has even valuation: away from the tangent point it is a unit, and near that point it is a unit times the square of a local parameter. Since $d'_i$ is a unit and $p$ is odd, the Hilbert symbol is zero. A projective rescaling contributes a common factor to all three tangents, which cancels because $d'_1d'_2d'_3$ is a square. Thus all places outside $S\cup\{\infty\}$ contribute zero.

### 5.4. The pairing matrix

The exact sum (5.2), in the ordered basis of Section 5.1, is

**Equation (5.5).**

```math
\mathcal{C}=
\begin{pmatrix}
0&0&1&1&0&1&1&1&0\\
0&0&1&0&1&1&0&1&1\\
1&1&0&0&0&1&0&1&0\\
1&0&0&0&1&1&1&1&0\\
0&1&0&1&0&0&0&1&0\\
1&1&1&1&0&0&1&0&0\\
1&0&0&1&0&1&0&0&0\\
1&1&1&1&1&0&0&0&0\\
0&1&0&0&0&0&0&0&0
\end{pmatrix}.
```

It is alternating and has rank six. Its principal minor on one-based indices $\{1,2,3,4,5,8\}$ has determinant one over $\mathbb{F}_2$. The two rational two-torsion classes have coordinate masks 428 and 393, with the least significant bit first. Both lie in the radical.

The exact certificate checks the arithmetic construction of every matrix entry, including the conic tangents, (5.3), (5.4), the real intervals and all local symbols. These checks determine the arithmetic Cassels pairing (5.5).

### 5.5. The finite quotient and the corank

**Proposition 5.1.** Put $r=\mathrm{rank}F(\mathbb{Q})$ and let $\delta$ be the corank of the maximal divisible subgroup of $\mathrm{Sha}(F/\mathbb{Q})[2^\infty]$. Then

**Equation (5.6).**

```math
r+\delta=1,\qquad
\mathrm{Sha}(F/\mathbb{Q})[2^\infty]
\cong(\mathbb{Q}_2/\mathbb{Z}_2)^\delta\oplus(\mathbb{Z}/2\mathbb{Z})^6.
```

In particular, $s_2(F)=1$.

*Proof.* Since the two-primary group is cofinitely generated, it has an abstract decomposition

```math
\mathrm{Sha}(F/\mathbb{Q})[2^\infty]
\cong(\mathbb{Q}_2/\mathbb{Z}_2)^\delta\oplus T,
```

with $T$ finite. No assumption that $\delta=0$ is made. The finite Kummer exact sequence and (4.3) imply

**Equation (5.7).**

```math
r+\delta+t=7,\qquad t=\dim_{\mathbb{F}_2}T[2].
```

The Cassels-Tate pairing is nondegenerate modulo the maximal divisible subgroup. For an elliptic curve it is alternating, including on the two-primary part: its principal polarization is induced by the rational divisor of the origin, as in Poonen and Stoll (1999). Thus $T$ has a perfect alternating pairing into $\mathbb{Q}/\mathbb{Z}$.

For completeness, this implies an orthogonal decomposition into blocks $(\mathbb{Z}/2^{e_i}\mathbb{Z})^2$. Choose an element of maximal order $2^{e_i}$. Nondegeneracy supplies a partner whose pairing with it has that exact order. They generate a perfect block, which splits off orthogonally; induction finishes the decomposition. Hence $t$ is even.

The pairing on $\mathrm{Sel}_2$ is the pullback of the restriction of Cassels-Tate to $\mathrm{Sha}(F)[2]$. Its rank six gives $t\ge6$. Equation (5.7) gives $t\le7$, so evenness forces $t=6$ and $r+\delta=1$.

In a block $(\mathbb{Z}/2^e\mathbb{Z})^2$ with $e\ge2$, the restriction of the pairing to the subgroup killed by two vanishes: its basic pairing is multiplied by $2^{2e-2}$, which makes it integral. The rank-six restriction on the six-dimensional finite two-torsion therefore forces every $e_i=1$. This proves (5.6). Finally, the infinite Kummer exact sequence identifies $s_2(F)$ with $r+\delta$. □

The finite arithmetic calculation therefore leaves the following two alternatives:

**Equation (5.8).**

```math
\begin{matrix}
\mathrm{rank}F(\mathbb{Q})&\mathrm{Sha}(F/\mathbb{Q})[2^\infty]\\ 
1&(\mathbb{Z}/2\mathbb{Z})^6\\
0&\mathbb{Q}_2/\mathbb{Z}_2\oplus(\mathbb{Z}/2\mathbb{Z})^6.
\end{matrix}
```

This proves the Selmer-corank assertion and the two-primary finite quotient in Theorem 1.1.

## 6. Positive rank of the auxiliary and the answer

**Theorem 6.1.** The auxiliary curve satisfies

```math
\mathrm{ord}_{s=1}L(F,s)=\mathrm{rank}F(\mathbb{Q})=1,
\qquad
\mathrm{Sha}(F/\mathbb{Q})[2^\infty]\cong(\mathbb{Z}/2\mathbb{Z})^6.
```

Its full Shafarevich-Tate group is finite.

*Proof.* Proposition 5.1 gives $s_2(F)=1$ with the usual local Kummer conditions. Lemma A.1 verifies full rational two-torsion, the non-CM hypothesis, the local reduction types, functional sign $-1$, and $a_{19}(F)=0$. Theorem H.5, proved in the appendices for precisely this curve and its indicated twisting classes, gives analytic order one. The forward Gross-Zagier-Kolyvagin theorem gives Mordell-Weil rank one and finiteness of $\mathrm{Sha}$. Thus $\delta=0$ in (5.6), proving the displayed two-primary group. □

For clarity, the dependency order of the positive-rank proof is as follows. Classical nonvanishing supplies seeds with prescribed local classes. Cyclotomic determinants yield a uniform lower bound for normalized central values and a transfer statement for a binary family with one untested vertex. Even half-integral-weight coefficients and finite graph identities then bound suitable nonvanishing companions. The ring-class lower bound and an exact comparison of unaveraged Heegner sums give the lower bound required for the odd coefficient system. A fixed companion and simultaneous addressing produce arbitrarily large binary families with one uniform index bound. The ring-class transfer theorem makes the base Heegner point nontorsion. Each implication, including the treatment of a possibly divisible Shafarevich-Tate group at the base, is proved in the appendices.

*Proof of Theorem 1.1 and Corollary 1.2.* Proposition 2.1 proves the first statement, and Proposition 5.1 proves the second. Theorem 6.1 proves the third. Choose a nontorsion point on $F$, whose existence follows from its rank one. Proposition 3.3 and the explicit exclusions in Lemma 3.2 give the fourth statement. Every curve produced by this construction is $\mathbb{Q}$‑isomorphic to $E_0$, so its rank is at least eleven. This proves the corollary. □

The problem asks for existence of an induced curve. The positive-rank proof supplies the required existence of a nontorsion auxiliary point; the rational formulas in Section 3 construct the quadruple from any such point. No explicit generator or saturation assertion is required.

## 7. Exact arithmetic certificates

The accompanying `verify_certificates.py` uses only Python's standard library and exact integer or rational arithmetic. With the four JSON files in the same directory, run

```text
python3 verify_certificates.py
```

The data are organized as follows.

| File | Mathematical contents |
|:---|:---|
| `arithmetic_data.json` | Curve coefficients, source points, recursive primality certificates, local Kummer witnesses, global Selmer matrix and basis |
| `conic_certificates.json` | Twenty-seven primitive conic points and primitive tangent forms |
| `local_certificates.json` | Two hundred sixty-one finite-place certificates and nine real-place certificates |
| `cassels_pairing.json` | The matrix (5.5) |

The verifier recomputes the derived data. It checks all eleven source points, the thirteen independent Kummer classes, the source double, the auxiliary scaling, the nondegeneracy conditions, and the six polynomial identities (3.8). It reconstructs the local Selmer images and the global matrix of rank 51. It checks the conic equations, primitivity, tangent contents, exact Hensel inequalities, tangent precision bounds and real intervals, and recomputes all 7,290 local Hilbert symbols contributing to (5.5). It also verifies the rank-six matrix, its indicated principal minor and the two torsion classes in its radical. The local-invariant checks verify the good model of the $(-1)$‑twist at two, the valuation proving that $F$ is non-CM, and all odd split and nonsplit reduction types.

These finite checks establish the arithmetic inputs of Theorem 1.1. Proposition 5.1 additionally uses the classical Kummer sequences and Cassels-Tate duality. The positive-rank implication is proved in the mathematical appendices.

## Appendix A. Local invariants and conventions

In the remaining sections write $E=F$ for the auxiliary curve in (1.3), and let $N$ be its conductor. The cyclotomic and ring-class constructions use separate copies of

```math
\Lambda=\mathbb{Z}_2[[t]],\qquad
 \mathcal{O}=\widehat{\Lambda_{(2)}},\qquad
 \Omega=\mathbb{F}_2((t)).
```

The completion is at the height-one prime $(2)$. In particular $t$ is a unit in $\mathcal{O}$. Specialization at $t=0$ is performed over $\Lambda[1/2]$ or $\Lambda_{(t)}$, never by an evaluation map on $\mathcal{O}$.

Parameters indexing the cyclotomic and ring-class families are odd fundamental discriminants, coprime to the fixed support and unit squares at all primes dividing $2N$. We allow $h=1$ as the parameter of the original curve. A local filter fixes the sign and the unit squareclasses at a finite set containing $2N$. Write

```math
s_2(E)=\mathrm{corank}_{\mathbb{Z}_2}
                  \mathrm{Sel}_{2^\infty}(E/\mathbb{Q}),
 \qquad w(h)=\omega(\vert h\vert ).
```

Define the normalized central value for every allowed $h$, and define $s(h)$ when the indicated group is finite:

```math
s(h)=\mathrm{length}_{\mathbb{Z}_2}
                 \mathrm{Sha}(E^{(h)}/\mathbb{Q})[2^\infty],
 \qquad
 L_*(h)=\frac{\sqrt{\vert h\vert }\,L(E^{(h)},1)}
                    {\Omega_E^{\mathrm{sgn}(h)}}.
```

Nonzero periods in the two sign lines are fixed throughout. All valuations above $2$ are normalized by $v(2)=1$.

We use the modularity theorem of Breuil, Conrad, Diamond and Taylor (2001), local Tate and global Poitou–Tate duality as in Milne (2006), the non-CM open-image theorem of Serre (1972), and the forward rank and finiteness theorems of Gross and Zagier (1986) and Kolyvagin (1990). Thus analytic order zero or one gives the corresponding Mordell–Weil rank and a finite Tate–Shafarevich group. The Kummer exact sequence always gives

```math
s_2(E)=\mathrm{rank}E(\mathbb{Q})
       +\mathrm{corank}_{\mathbb{Z}_2}
                       \mathrm{Sha}(E/\mathbb{Q})[2^\infty].
```

Restriction and the projections $1+c,1-c$ for a quadratic extension $K=\mathbb{Q}(\sqrt{k})$ have composites equal to multiplication by two. They preserve the local Kummer conditions. Rationalizing therefore gives

**Equation (A.1).**

```math
s_2(E/K)=s_2(E/\mathbb{Q})+s_2(E^{(k)}/\mathbb{Q}).
```

No integral direct-sum decomposition is needed.

**Lemma A.1.** The curve $E$ is non-CM, has full rational two-torsion and has potentially good reduction at $2$. Its conductor and root number satisfy

```math
N=2^4\prod_{p\in S\setminus\{2\}}p,\qquad
 \varepsilon(E)=-1,
```

where $S$ is the list (4.2). Every odd bad prime is multiplicative. Moreover $E$ has good reduction at $19$ and $a_{19}(E)=0$.

*Proof.* The factorizations (4.1) give

```math
\gcd(\alpha,\beta)=1,\qquad \alpha\equiv3\pmod4,
 \qquad v_2(\beta)=4.
```

The roots $0,-\alpha,-\beta$ are distinct and rational. The invariants are

```math
\begin{aligned}
 c_4&=16(\alpha^2-\alpha\beta+\beta^2),\\
 c_6&=-64(\alpha+\beta)^3+288(\alpha+\beta)\alpha\beta,\\
 \Delta&=16\alpha^2\beta^2(\alpha-\beta)^2,
\end{aligned}
```

and their two-adic valuations are $(4,6,12)$. For the twist by $-1$, substitute $x_-=4X$ and $y_-=8Y+4X$. This gives the integral model

**Equation (A.2).**

```math
Y^2+XY=X^3-\frac{\alpha+\beta+1}{4}X^2
                     +\frac{\alpha\beta}{16}X.
```

Its discriminant is $\Delta/2^{12}$, which is odd. The twist therefore has good reduction at $2$.

Fix an auxiliary coefficient prime $ℓ\ne2$. The quadratic character $\chi$ of $\mathbb{Q}_2(i)$ has conductor exponent two; on odd units it is $\chi(u)=(-1)^{(u-1)/2}$. Twisting the two-dimensional unramified $ℓ$‑adic representation of (A.2) by this character gives conductor exponent four. Its two unramified unitary eigencharacters have product one. The unramified factors in their epsilon constants cancel, leaving the square of the normalized quadratic Gauss factor $W(\chi)$. The identity $W(\chi)^2=\chi(-1)=-1$ therefore gives $\varepsilon_2(E)=-1$. These are the conductor and epsilon-factor identities of Rohrlich (1994), valid also in residue characteristic two. The displayed model is minimal: a smaller integral discriminant would have valuation zero, contradicting the ramified quadratic inertia just exhibited.

At every odd $p\in S$, coprimality gives $v_p(c_4)=0$ and $v_p(\Delta)\gt 0$. The reduction is multiplicative, with conductor exponent one. The node has split tangent directions according as

```math
\beta\ (p\mid\alpha),\qquad
 \alpha\ (p\mid\beta),\qquad
 -\alpha\ (p\mid\alpha-\beta)
```

is a square modulo $p$. The nonsplit primes are exactly

```math
23,47,89,283,4943,8893,23971,1073681107,354212181139.
```

The remaining nineteen odd bad primes are split. Their local root numbers therefore have product $-1$. Together with the real root number $-1$ and the root number at $2$, this gives $\varepsilon(E)=-1$.

At $13$, $v_{13}(\alpha-\beta)=2$ and $v_{13}(\alpha\beta)=0$. Consequently $v_{13}(j(E))=-4$. A CM $j$‑invariant is an algebraic integer, so $E$ is non-CM.

Modulo $19$ the equation is $y^2=x(x+2)(x+4)$. Its three points of ordinate zero have abscissas $0,15,17$. Each of $5,6,7,11,12,13,14,18$ gives two further affine points, and the remaining abscissas give none. Hence $\#E(\mathbb{F}_{19})=20$ and $a_{19}(E)=0$.

□

The local condition at a fixed nonarchimedean place is the derived Kummer condition. If $B/L$ is an elliptic curve, it is represented by $B(L)^\wedge_2[-1]\to R\Gamma(L,T_2B)$, using a free resolution before coefficient reduction. This retains both $B(L)[2^n]$ in degree zero and $B(L)/2^nB(L)$ in degree one. Over an imaginary quadratic field the Selmer complex is the cone

```math
\mathrm{Cone}\left(
 R\Gamma(G_{K,S},M)\oplus\bigoplus_{v\in S}U_v
       \longrightarrow\bigoplus_{v\in S}R\Gamma(K_v,M)
                 \right)[-1].
```

The positive real cone used over $\mathbb{Q}$ is specified separately in the cyclotomic argument.

## Appendix B. Classical nonvanishing with prescribed local classes

We use the following form of Hoffstein–Luo (1997, pp. 435–436). For an elliptic curve $A/\mathbb{Q}$ and an arbitrary finite set $S$ of rational primes, there are infinitely many odd fundamental discriminants $v$ with at most four prime factors such that $L(A^{(v)},1)\ne0$ and $\chi_v(p)=1$ at every $p\in S$. The bound on the number of prime factors is absolute.

**Proposition B.1.** Fix a nonempty filter of odd fundamental discriminants, given by a real sign and unit squareclasses at a finite set containing $2N_A$, and having root number $+1$ for the corresponding twists of $A$. For every finite exclusion set and every real bound $B$, the filter contains a discriminant $d$ such that

```math
L(A^{(d)},1)\ne0,\qquad \omega(\vert d\vert )\le5,
```

and every prime factor of $d$ exceeds $B$ and avoids the exclusions.

*Proof.* The prescribed unit class at two is $1$ or $5$ modulo eight, since an odd fundamental discriminant is $1$ modulo four. Choose a nonzero residue representative at every odd support prime. The Chinese remainder theorem and Dirichlet’s theorem give a positive prime $u\gt B$ in these classes, avoiding the exclusions. In particular $u$ is an odd fundamental discriminant. Apply Hoffstein–Luo to $A^{(u)}$ with a split set containing the original support, the primes of $2N_{A^{(u)}}$, $u$, the exclusions and every prime at most $B$.

The resulting $v$ is a local unit square at the original support, is coprime to $u$, and has at most four prime factors. Splitting at two gives $v\equiv1\pmod8$. Thus $d=uv$ is an odd fundamental discriminant with the required finite local classes and prime restrictions.

Let $\sigma$ be the prescribed sign. The quadratic-twist root-number formula, with the given local classes, gives $\varepsilon(A^{(u)})=\sigma$. Since $v$ is square at every conductor prime of $A^{(u)}$, nonvanishing forces

```math
1=\varepsilon((A^{(u)})^{(v)})
   =\varepsilon(A^{(u)})\mathrm{sgn}(v).
```

Hence $\mathrm{sgn}(d)=\sigma$. The twist $(A^{(u)})^{(v)}$ is $A^{(d)}$, proving the assertion. The prime count is at most five regardless of the size of the support or of the chosen primes.

□

**Proposition B.2.** For a nonempty unit filter as above having root number $-1$, and for every finite exclusion set and prime bound, there is a discriminant $d$ on that filter for which $L'(A^{(d)},1)\ne0$, with all prime factors satisfying the restrictions.

*Proof.* Bump–Friedberg–Hoffstein (1990, Theorem (i), pp. 543–544) supplies, for a weight-two newform of sign $\varepsilon$ and a finite set of primes containing its level, a fundamental discriminant $v$ with $\varepsilon v\lt 0$, splitting at all specified primes, whose twist has a simple central zero. This statement requires no nonzero central value for the original form.

Choose a positive prime $u$ representing the prescribed finite unit classes as in Proposition B.1. If the required sign is $\sigma$, then $\varepsilon(A^{(u)})=-\sigma$. Apply the cited derivative theorem to $A^{(u)}$, requiring splitting at the original support, at every conductor prime, at $u$, at all excluded primes and at every prime at most the bound. The product $d=uv$ is fundamental, has the prescribed local classes, and has sign $-\varepsilon(A^{(u)})=\sigma$. Its twist has a simple central zero. The splitting conditions give every prime restriction.

□

The discriminant sizes and the precision of the congruences may depend on the filter. Proposition B.1 keeps only the prime count uniform. This is sufficient when a previously chosen twist and a fixed finite product are absorbed into the curve before the proposition is applied.

## Appendix C. Cyclotomic comparison for the auxiliary curve

Throughout this section, $E=F$ is the auxiliary curve of Lemma A.1. In particular, $E$ is non-CM, $E[2]\subset E(\mathbb{Q})$, $E$ has potentially good reduction at $2$, and every odd prime of bad reduction is multiplicative. Write $N=N_E$, $T=T_2E$, and $V=T\otimes_{\mathbb{Z}_2}\mathbb{Q}_2$. The positive determinant construction and its binary interpolation are adapted from OpenAI (2026, section on cyclotomic interpolation). We give the specialized construction, including its coefficient maps and integral central comparison.

An allowed discriminant $h$ is an odd fundamental discriminant, with $h\in\mathbb{Q}_q^{\times 2}$ for every $q\mid 2N$; the trivial character $h=1$ is included. Thus $(h,2N)=1$ and $h\equiv1\pmod8$. All discriminants in a binary family have the same sign. Fix nonzero periods $\Omega_E^+$ and $\Omega_E^-$ in the two rational Betti period lines, and a compatible embedding of algebraic numbers into $\overline{\mathbb{Q}}_2$. Put

```math
L_*(h)=\frac{\sqrt{\vert h\vert }\,L(E^{(h)},1)}{\Omega_E^{\mathrm{sgn}(h)}}.
```

Changing either fixed period changes the valuations below by a fixed constant. The value is algebraic; a purely imaginary choice of the minus period only introduces a root of unity into comparisons with a real period convention. If $s_2(E^{(h)})=0$, then both the Mordell–Weil rank and the divisible corank of its $2$‑primary Shafarevich–Tate group vanish. Consequently that group is finite, and we set

```math
s(h)=\mathrm{length}_{\mathbb{Z}_2}
       \mathrm{Sha}(E^{(h)}/\mathbb{Q})[2^\infty].
```

When also $L(E^{(h)},1)\ne0$, define

```math
D(h)=v_2(L_*(h))-2\omega(\vert h\vert )-s(h).
```

**Theorem C.1 (Cyclotomic lower bound).** There is a constant $C_E$ such that every allowed $h$ with $L(E^{(h)},1)\ne0$ satisfies

```math
v_2(L_*(h))\ge 2\omega(\vert h\vert )+s(h)-C_E.
```

The constant is independent of the number and sizes of the primes of $h$.

**Theorem C.2 (Cyclotomic transfer to the missing vertex).**

Let $h_0$ be allowed and satisfy $s_2(E^{(h_0)})=0$. Suppose that for arbitrarily large $b$ there are a finite set $Q$ of primes not dividing $2Nh_0$ and linear forms $\lambda_q:\mathbb{F}_2^b\to\mathbb{F}_2$ such that

```math
h_x=h_0\prod_{q\in Q}(q^*)^{\lambda_q(x)},\qquad
 q^*=(-1)^{(q-1)/2}q,
```

are allowed and have the same sign. Suppose that a constant $B$, independent of the family, satisfies

```math
L(E^{(h_x)},1)\ne0,\qquad D(h_x)\le B\qquad(x\ne0).
```

Then $L(E^{(h_0)},1)\ne0$ and $D(h_0)\le B+C_E$. The constant $C_E$ is independent of $h_0$, $Q$, and $b$.

### C.1. Positive cochains and derived coefficient change

Let $S$ be finite and contain $2$, the real place, and the ramification of the coefficients. For a finite $2$‑primary $G_{\mathbb{Q},S}$‑module $M$, define

```math
\mathcal{F}_S(M)=
 \mathrm{Cone}\bigl(
 C^\bullet(G_{\mathbb{Q},S},M)\longrightarrow
 C^\bullet(\mathrm{Gal}(\mathbb{C}/\mathbb{R}),M)
 \bigr)[-1].
```

The real cochains in this definition are ordinary cochains in nonnegative degrees. Complete real Tate cochains will instead occur in Poitou–Tate duality.

**Lemma C.3.** The cohomology of $\mathcal{F}_S(M)$ is finite and is concentrated in degrees $1$ and $2$. The same degree bounds hold for finite-type compact coefficient modules by passage to inverse limits.

*Proof.* The map on degree-zero cohomology is injective. We also need surjectivity of global restriction in degree two. If $2^aM=0$, put $M^D=\mathrm{Hom}(M,\mu_{2^a})$. Restriction

```math
H^0(G_{\mathbb{Q},S},M^D)\longrightarrow H^0(\mathbb{Q}_2,M^D)
```

is injective. Its dual, under local Tate duality, is a surjection

```math
H^2(\mathbb{Q}_2,M)\longrightarrow
 H^0(G_{\mathbb{Q},S},M^D)^\vee.
```

Given a prescribed real degree-two class, choose a class at $2$ that cancels its obstruction in this last group and set the other finite local classes to zero. The finite Poitou–Tate sequence then supplies a global class with the prescribed real restriction. In every degree strictly greater than two, restriction from global cohomology to real cohomology is an isomorphism. These are precisely the real-place clauses of Milne (2006, I, Theorem 4.10) and Nekovář (2006, 5.7.1.4–5.7.1.7). The cone sequence proves the assertion for $M$.

For a compact coefficient module, take its finite coefficient quotients. Continuous cochains are their inverse limit. The cohomology groups at each finite quotient are finite, so their inverse systems satisfy the Mittag–Leffler condition. The inverse-limit cohomology sequence therefore preserves the degree bounds.

□

**Proposition C.4.** Let $R$ be a complete Noetherian local $\mathbb{Z}_2$‑algebra with finite residue field, and let $\mathcal{T}$ be finite free over $R$ with continuous $G_{\mathbb{Q},S}$‑action. Then $\mathcal{F}_S(\mathcal{T})$ is represented by a finite free complex in degrees $1$ and $2$. For a coefficient quotient $R\to B$ there is a natural isomorphism

```math
\mathcal{F}_S(\mathcal{T})\otimes_R^{\mathbf{L}}B
 \simeq \mathcal{F}_S(\mathcal{T}\otimes_R B).
```

The maps commute with restriction and with Shapiro’s maps. At a nonarchimedean place, or over a totally imaginary number field, the ordinary complex has perfect amplitude $[0,2]$ under the same finite-free coefficient hypotheses. The compact-support cone over a totally imaginary number field has perfect amplitude $[0,3]$.

*Proof.* Continuous cochains on admissible modules are exact on short exact sequences, commute with filtered direct limits, and satisfy the projection formula for complexes of flat modules Nekovář (2006, 3.4.2–3.4.4). The same statements hold for the positive cone with its actual restriction map. Global and real Galois groups satisfy the finite-cohomology condition Nekovář (2006, 5.7.1.1); hence the complete-local finiteness argument Nekovář (2006, 4.2.3–4.2.5) gives finite-type cohomology. It is bounded by Lemma C.3.

For completeness, derived coefficient change does not require $B$ to be flat. Take a resolution of a finite-type $R$‑module $B$ by finite free modules and let $P_n$ be its brutal truncation in degrees $[-n,0]$. If $K_n$ is the leftmost resolution syzygy, there is a triangle

```math
K_n[n]\longrightarrow P_n\longrightarrow B\longrightarrow K_n[n+1].
```

The projection formula holds for $P_n$ on the level of cochains. Applying the positive functor to the last term gives cohomology only in degrees $[-n,1-n]$, by Lemma C.3. It cannot change any fixed cohomological degree for sufficiently large $n$. The same truncation argument on the tensor side proves the derived projection formula and gives Tor amplitude $[1,2]$. Filtered direct limits extend the Tor bound to arbitrary $R$‑modules. The perfectness criterion Nekovář (2006, 4.2.8 and the proof of 4.2.9) now applies. A minimal finite free model over $R$ has zero differential after reduction to the residue field. Its residual cohomology is concentrated in degrees $1,2$, so its terms outside those degrees vanish.

All comparisons came from cochain maps. In particular, quotienting a cyclotomic coefficient module by $\gamma^{2^n}-1$ uses its two-term Koszul resolution and the same coefficient exact sequence on the global and ordinary real cochains. Shapiro’s maps commute with these restriction maps; see also Nekovář (2006, 8.4.8.1).

For a nonarchimedean local field of characteristic zero and for a totally imaginary number field, the relevant $2$‑cohomological dimension is two. The same finite-Tor argument applies to ordinary cochains, or directly Nekovář (2006, 4.2.9 and 5.1.1–5.1.2). Forming the actual compact-support cone adds at most one degree.

□

### C.2. Residual concentration at the height-one prime

Let $\Gamma=\mathrm{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$ be the real cyclotomic $\mathbb{Z}_2$‑group, choose $\gamma\in\Gamma$, and write

```math
\Lambda=\mathbb{Z}_2[[\Gamma]]=\mathbb{Z}_2[[t]],\qquad
 \gamma=1+t,\qquad
 \mathcal{O}=\widehat{\Lambda_{(2)}},\qquad
 \Omega=\mathbb{F}_2((t)).
```

For a binary family, put $G=(\mathbb{Z}/2\mathbb{Z})^b$ and $R=\Lambda[G]$. Let $\psi:G_{\mathbb{Q}}\to G$ be the universal quadratic character, so its character at $x$ is $\chi_{h_x/h_0}$. The action on $\mathbf{T}=T\otimes_{\mathbb{Z}_2}R$ is

```math
\rho_T\chi_{h_0}\psi\kappa_\Gamma^{-1},
```

where $\kappa_\Gamma:G_{\mathbb{Q}}\to\Gamma$ is the group-valued cyclotomic quotient. Put

```math
\mathcal{C}_S^+=\mathcal{F}_S(\mathbf{T}),
```

where $S$ contains $2N$ and the prime factors of all the $h_x$. Since the signs are fixed, both $\psi$ and $\kappa_\Gamma$ are trivial at the real place. In the zeta-class construction we take $S$ to be exactly the real place together with the primes dividing $2N$ or one of the $h_x$.

**Lemma C.5.** Every layer $K_n$ of degree $2^n$ in the real cyclotomic $\mathbb{Z}_2$‑extension has odd ordinary class number.

*Proof.* The assertion holds for $K_0=\mathbb{Q}$. Suppose it holds for $K_n$. If the $2$‑primary part $P$ of the ordinary class group of $K_{n+1}$ were nonzero, the involution of $K_{n+1}/K_n$ would act on the nonzero space $\mathrm{Hom}(P,\mathbb{F}_2)$ with a nonzero fixed vector: in characteristic two, the square of its difference from the identity is zero. Class field theory would then give an everywhere-unramified quadratic extension $L/K_{n+1}$, invariant under that involution. Here “everywhere-unramified” includes splitting at real places, as appropriate to the ordinary Hilbert class field. Thus $L/K_n$ is Galois of degree four and its Galois group is abelian.

Only the unique prime above $2$ can ramify in $L/K_n$, and its inertia group has order two: the ramification index in $K_{n+1}/K_n$ is two and $L/K_{n+1}$ is unramified. The fixed field of this inertia group is consequently an everywhere-unramified quadratic extension of $K_n$. This contradicts the odd class number of $K_n$.

□

**Lemma C.6.** There is an isomorphism

```math
\mathcal{C}_S^+\otimes_R^{\mathbf{L}}\mathcal{O}[G]
       \simeq \mathcal{O}[G]^2[-1].
```

It introduces no denominator depending on $S$ or on $G$.

*Proof.* The ring $\mathcal{O}[G]$ is local with residue field $\Omega$; its residue map sends $2$ to zero and every element of $G$ to one. Every quadratic character therefore disappears. Full rational $2$‑torsion makes $T/2T$ a direct sum of two trivial modules. It suffices to compute one trivial summand.

Let $d_n=[K_n:\mathbb{Q}]=2^n$ and let $s_n$ be the number of finite places of $K_n$ above $S$. The numbers $s_n$ are bounded in $n$. The prime $2$ is totally ramified, and the Frobenius of each fixed odd prime has nonzero image in $\Gamma$: an odd positive rational prime cannot equal $1$ or $-1$ in $\mathbb{Z}_2^\times$. By Lemma C.5, the $S$‑class group has no $2$‑primary part.

The unit signature map is surjective. For $n\ge1$, take a primitive $2^{n+2}$th root $\zeta$ and put $\varepsilon=1+\zeta+\zeta^{-1}$. The minimal polynomials of $\zeta+\zeta^{-1}$ satisfy

```math
f_1(X)=X^2-2,\qquad f_{n+1}(X)=f_n(X^2-2),\qquad f_n(-1)=-1.
```

Thus $\varepsilon$ is a unit of norm $-1$. Its signature has odd augmentation in the regular $\mathbb{F}_2[\mathrm{Gal}(K_n/\mathbb{Q})]$‑module. The group algebra of a cyclic $2$‑group over $\mathbb{F}_2$ is local, so that signature is a unit and its conjugates span every signature. For $n=0$, use $-1$.

Kummer theory and the Brauer invariant sequence now give

```math
\dim_{\mathbb{F}_2}H^1(G_{K_n,S},\mu_2)=d_n+s_n.
```

Restriction in degree one to the $d_n$ real places is surjective. Degree-zero restriction has cokernel of dimension $d_n-1$. In degree two, restriction to the real places is also surjective; its kernel has dimension $s_n-1$, because the finite and real Brauer invariants have one sum relation and a finite place above $2$ is present. The positive complex therefore has dimensions

```math
d_n+s_n-1\quad\text{in degree }1,\qquad
 s_n-1\quad\text{in degree }2,
```

and zero cohomology elsewhere.

By Proposition C.4, reduction to $K_n$ is derived reduction modulo $t^{2^n}$ of a perfect complex over $\mathbb{F}_2[[t]]$. For such a complex, the universal-coefficient sequence and the structure theorem over $\mathbb{F}_2[[t]]$ show that its degree‑$i$ dimension modulo $t^{2^n}$ is $2^n\mathrm{rank}H^i+O(1)$. Its torsion modules contribute only a bounded term. After inverting $t$, the trivial summand therefore has dimension one in degree one and is zero otherwise. The two trivial summands have dimension two in degree one. A minimal finite free model over $\mathcal{O}[G]$ has zero residual differentials. This residual concentration forces exactly one term, free of rank two in degree one.

□

The fixed integral invariant line of $T\chi_{h_0}$ at the real place has a primitive generator. Its connecting image defines $a\in H^1(\mathcal{C}_S^+)$. Global rational invariants vanish: the non-CM image on the kernel of the cyclotomic character and the finitely many quadratic characters contains an open subgroup of $\mathrm{SL}_2(\mathbb{Z}_2)$ and fixes no nonzero vector. Thus $a$ spans the real-place summand. Its normalization depends only on $E$ and the fixed real sign. Since $H^1(\mathbb{R},\mathbf{T})$ is killed by $2$, twice an ordinary global class lifts to positive cohomology. Two lifts have the same wedge with $a$.

### C.3. A fixed-form integral zeta class

Let $f=f_E$ be the fixed weight-two newform. We use Kato’s integral classes at this form, followed by the fixed comparison of its rational representation with $V$. Kato (2004, 8.9–8.12) gives an integral trace to

```math
\mathbb{Z}_2[\mathrm{Gal}(\mathbb{Q}(\mu_m)/\mathbb{Q})]
 \otimes_{\mathbb{Z}_2}V_{2,\mathbb{Z}_2}(Y_1(N))(1),
```

then an integral projection to the lattice of $f$. One fixed power $2^{c_E}$ sends that lattice into $T$. Choose fixed symbols in $\mathrm{SL}_2(\mathbb{Z})$ with nonzero projections in both required period lines; their existence follows from Kato (2004, 13.6 and 13.9). The two sign choices cost only a fixed lattice constant.

Let $m$ be odd and divisible by all the tame conductors in the family. Write $\Gamma_n=\Gamma/\Gamma^{2^n}$ and use the field $\mathbb{Q}(\mu_{m2^{n+2}})$, so that its real cyclotomic quotient is exactly $\Gamma_n$. Shapiro’s isomorphism and the coefficient map

```math
\begin{aligned}
 \mathbb{Z}_2[\mathrm{Gal}(\mathbb{Q}(\mu_{m2^{n+2}})/\mathbb{Q})]
   &\longrightarrow \mathbb{Z}_2[\Gamma_n\times G],\\
 [\sigma]&\longmapsto
 \chi_{h_0}(\sigma)[\sigma\vert _{\Gamma_n}][\psi(\sigma)]
 \end{aligned}
```

push the actual class into the required coefficient module. We use the inverse group actions on both sides when identifying this module with $\mathbf{T}$. This is an integral homomorphism of coefficient modules, not division by an idempotent. In particular it introduces no factor $\vert G\vert ^{-1}$ and uses no surjectivity assertion for cohomological specialization. Since $2\in S$, Kato’s norm relation has no new Euler factor as $n$ increases. The inverse limit is an integral smoothed class, up to $2^{c_E}$.

**Lemma C.7.** The weight-two smoothing factors can be removed over $\mathcal{O}[G]$ without any additional $2$‑denominator. Their central values have bounded, fixed valuations as the tame support varies.

*Proof.* For $k=2$ and $r=r'=1$, the factors are $(c^2-c\sigma_c)(d^2-d\sigma_d)$ Kato (2004, Theorem 6.6). Fix $e\ge\max(2,v_2(N))$ and choose $c,d\gt 1$ with

```math
c,d\equiv1\pmod{3N_{\mathrm{odd}}m},\qquad
 c,d\equiv1+2^e\pmod{2^{e+1}}.
```

They satisfy the required coprimality conditions and act trivially on all tame characters. Taking $5$ as a generator of $1+4\mathbb{Z}_2$, the exponent $\kappa(c)=\log(c)/\log(5)$ has valuation $e-2$. Thus the reduction of $c^2-c\sigma_c$ to $\Omega$ is

```math
1-(1+t)^{\kappa(c)}\ne0.
```

Indeed its first nonzero term has degree $2^{e-2}$. It is consequently a unit in the local ring $\mathcal{O}[G]$. At $t=0$ its value is $c(c-1)$, of valuation $e$. The same argument applies to $d$ and to inverse group actions.

□

Denote the unsmoothed ordinary class by $z_S^{(0)}$. Before the comparison below, its character components are regarded as elements of $\mathrm{Frac}(A)\otimes_A H^1(C_{S,h})$, where $A=\Lambda[1/2]$. Their smoothing denominators are nonzero power series with nonzero central values. The following normalization makes the roles of Betti and de Rham vectors explicit. Choose a rational Betti generator $b^\epsilon$ in the required sign line and a de Rham generator $\omega_f$ such that

```math
\mathrm{per}_f(\omega_f)^\epsilon
     =\Omega_f^\epsilon b^\epsilon,\qquad
 \delta(f,1,\xi)^\epsilon=d_\xi^\epsilon b^\epsilon,
 \qquad d_\xi^\epsilon\in\mathbb{Q}^\times.
```

The periods $\Omega_f^\epsilon$ and $\Omega_E^\epsilon$ differ by fixed nonzero rational comparison factors. Kato’s unnormalized character-sum formula, followed by explicit reciprocity, Kato (2004, Theorems 6.6 and 9.7), therefore has de Rham coefficient $d_\xi^\epsilon L_S(E^{(h)},1)/\Omega_f^\epsilon$ before identifying the quadratic twisting line.

For a primitive quadratic character of odd conductor $\vert h\vert $, choose its Gauss sum $\tau_h$ with $\tau_h^2=h$. The character eigenline in $\mathbb{Q}(\mu_{\vert h\vert })$ is generated by $\tau_h$, which is a $2$‑adic unit. Since $h$ is a square in $\mathbb{Q}_2$, its image under the chosen embedding belongs to $\mathbb{Q}_2^\times$. The de Rham basis of the twisted representation can thus be taken to $\tau_h\omega_f$. Dividing the preceding coefficient by $\tau_h$ gives

```math
\frac{d_\xi^\epsilon L_S(E^{(h)},1)}
      {\tau_h\Omega_f^\epsilon}.
```

The ratio between $1/\tau_h$ and $\sqrt{\vert h\vert }$ is a root of unity times $1/h$, and has valuation zero. Comparing with a minimal differential at $2$ contributes a bounded index, because all the allowed $h$ are local squares there.

There is no growing trace factor in this computation. With the left-coset Shapiro convention, restriction of the pushed class is the unnormalized sum $\sum_\sigma\chi_h(\sigma)\sigma z$; this is also the sum in Kato’s Theorem 6.6. If a character is imprimitive at a larger tame level, first taking the trace to its conductor gives the same sum and Kato’s norm relation supplies exactly the omitted Euler factors. Projection from the full cyclotomic group to its real component has order two and changes only a fixed normalization. Consequently

**Equation (C.1).**

```math
v_2\bigl(\exp_2^*z_{S,h}^{(0)}(0)\bigr)
 =v_2(L_*(h))+
 \sum_{\substack{q\in S\ \mathrm{finite}\\ q\nmid2Nh}}
       v_2\bigl(\#E^{(h)}(\mathbb{F}_q)\bigr)+O_E(1)
```

when the value is nonzero. A zero central value gives zero dual exponential. The error in (C.1) is bounded in absolute value independently of the varying support. At a good unused prime the omitted factor is $\#E^{(h)}(\mathbb{F}_q)/q$; at a good ramified prime it is $1$. Factors at primes of $N$ are fixed because the local twists there are fixed.

### C.4. Rational divisibility and the local Euler factors

Put $A=\Lambda[1/2]$. After a quadratic twist and the Tate twist identifying Kato’s representation with $V_h=V\chi_h$, Kato’s Theorems 12.4 and 12.5(3) apply over $A$. The Tate twist acts on the Iwasawa algebra by its usual automorphism and preserves all height-one length statements. The non-CM open-image theorem Serre (1972), in the form recorded in Kato (2004, 12.8.2 and 13.4), supplies the characteristic-zero irreducibility and a nonidentity unipotent with a one-dimensional fixed space. Intersecting the image with the kernel of a quadratic character preserves an open subgroup. No residual irreducibility or integral $p\ne2$ assertion is used.

**Lemma C.8.** For every allowed $h$, the local correction in Kato’s rational height-one inequality vanishes. Thus the multiplier at $2$ can be taken to be $F_2=1$.

*Proof.* Potential good reduction is preserved by quadratic twisting. Kato (2004, 12.5(3), including (12.5.1), and 12.7) states that a nonzero local degree-two term at a rational height-one prime can occur, in weight two, only for a form which is not potentially of good reduction at the coefficient prime. The hypothesis of Lemma A.1 excludes this case.

□

Write $C_{j_*}$ for Kato’s rational global complex, and $C_{S,h}$ for ordinary rational global Iwasawa cohomology with the primes of $S$ removed. At an odd prime put $W_q=H^1(I_q,V_h)$. The localization cone is

**Equation (C.2).**

```math
Q_q=\left[W_q\otimes_{\mathbb{Q}_2}A
    \xrightarrow{\,1-\gamma_q\mathrm{Fr}_{W_q}\,}
    W_q\otimes_{\mathbb{Q}_2}A\right]
```

in degrees one and two. Here $\gamma_q$ is the scalar arithmetic Frobenius action in the inverse cyclotomic coefficient module. Its exponent in $\Gamma$ is nonzero. Hence $D_q=\det(1-\gamma_q\mathrm{Fr}_{W_q})$ is nonzero, and

```math
H^1(Q_q)=0,\qquad
 \mathrm{length}_{A_{\mathfrak{p}}}H^2(Q_q)_{\mathfrak{p}}
       =v_{\mathfrak{p}}(D_q).
```

The map in (C.2) remains injective after localization at a prime dividing its determinant; localization does not mean reduction modulo that prime. The localization sequence gives

```math
H^1(C_{j_*})\simeq H^1(C_{S,h}),\qquad
 0\longrightarrow H^2(C_{j_*})\longrightarrow H^2(C_{S,h})
 \longrightarrow\bigoplus_{q\in S\setminus\{2,\infty\}}H^2(Q_q)
 \longrightarrow H^3(C_{j_*}).
```

Only the resulting upper bound on the degree-two length is needed.

The determinants can all be written explicitly in the present case. At a good unused prime, $W_q=V_h(-1)$ and

```math
D_q=P_q(\chi_h(q)\gamma_q),\qquad
 P_q(Z)=1-\frac{a_q(E)}qZ+\frac1q Z^2.
```

At a good active prime, inertia acts by $-1$ rationally, so $W_q=0$ and $D_q=1$. At a multiplicative prime of $E$, the local twist is trivial and

```math
W_q=\mathbb{Q}_2(-1)\otimes\mathrm{unr}(a_q(E)),\qquad
 D_q=1-\frac{a_q(E)}q\gamma_q,
 \qquad a_q(E)\in\{1,-1\}.
```

This follows from the Tate-curve extension and its nonsplit unramified twist. In particular, $W_q$ is the actual inertia cohomology; it is not replaced by $V_h^{I_q}(-1)$. These bad-prime determinants are exactly the omitted multiplicative $L$‑factors and have nonzero central values.

**Lemma C.9.** Let $Z_h$ be Kato’s rational zeta submodule for the form of $E^{(h)}$ in the corresponding real cyclotomic component. With consistent Frobenius conventions, the fixed-form class satisfies

```math
A z_{S,h}^{(0)}=
 \left(\prod_{q\in S\setminus\{2,\infty\}}D_q\right) Z_h
 \quad\text{inside }H^1(C_{S,h}).
```

Consequently, for every height-one prime $\mathfrak{p}$ of $A$,

**Equation (C.3).**

```math
\mathrm{length}_{A_{\mathfrak{p}}}H^2(C_{S,h})_{\mathfrak{p}}
 \le
 \mathrm{length}_{A_{\mathfrak{p}}}
 \bigl(H^1(C_{S,h})/Az_{S,h}^{(0)}\bigr)_{\mathfrak{p}}.
```

*Proof.* The rational global cohomology is free of rank one over $A$, by Kato (2004, Theorem 12.4). A rational generator $z_{{\mathrm{BK}},h}$ of $Z_h$ can be chosen using one fixed nonzero Betti vector for the form of $E^{(h)}$ in the required sign. Compare its explicit reciprocity formula with that of the fixed-form trace at finite-order cyclotomic characters $ν$.

The omitted Euler factors in the two formulas have ratio exactly $\prod_qD_q(ν)$, by the preceding local calculation. The comparison of the two fixed period vectors, for this one $h$, is a nonzero scalar; no bound for its valuation is needed here. The remaining character dependence in the twisting identifications is group-like. More explicitly, for $ν$ of conductor $2^n$, coprime Gauss-sum factorization gives

```math
\tau(\chi_hν)=\chi_h(2)^nν(\vert h\vert )\tau(\chi_h)\tau(ν).
```

Here $\chi_h(2)=1$. Thus the factor depending on $n$ disappears, and the remaining factor $ν(\vert h\vert )$ is the value of the group-like unit $[\vert h\vert ]\in\Lambda^\times$. Reversing the action convention inverts this unit. Using product Gauss bases instead simply absorbs it into the chosen generator of the same $A$‑module $Z_h$. The common cyclotomic Gauss factors cancel. Hence the reciprocity formulas differ by the displayed Euler product, a scalar in $\mathbb{Q}_2^\times$, and a group-like unit. This calculation uses Kato (2004, Theorems 6.6, 9.7, 12.5(1), and Lemma 13.10(2)) with the unnormalized trace convention already specified.

Fix an $A$‑basis $b_h$ of $H^1(C_{S,h})$. The unsmoothed fixed-form trace initially has a coefficient in $\mathrm{Frac}(A)$ relative to $b_h$: its smoothing factors need not be units of $A$. Subtract the comparison class just described, and multiply the difference by a nonzero power-series denominator and a power of $2$. The result is $F(t)b_h$ with $F(t)\in\mathbb{Z}_2[[t]]$.

For this fixed $h$, cyclotomic nonvanishing Kato (2004, Theorem 13.5(2)) supplies infinitely many finite-order characters at which the common $L$‑value is nonzero. A nonzero power series in $\Lambda$ has only finitely many finite-order character zeros, by Weierstrass preparation. Exclude these zeros for the denominator just cleared and for the finitely many interpolation factors. At every remaining character $ν$, the explicit reciprocity formula for $z_{{\mathrm{BK}},h}$ has nonzero dual exponential. Since $z_{{\mathrm{BK}},h}$ is an $A$‑multiple of $b_h$, the specialization of $b_h$ also has nonzero dual exponential. The difference of the two reciprocity formulas is zero, so

```math
F(ν)\,\exp_ν^*(b_h(ν))=0
```

implies $F(ν)=0$. These are infinitely many distinct characters. Weierstrass preparation now gives $F=0$. Thus the fixed-form trace equals a unit of $A$ times the Euler product times $z_{{\mathrm{BK}},h}$. In particular it belongs to $H^1(C_{S,h})$, and the asserted submodule equality follows. This comparison makes no claim about uniform lattices of the varying newforms.

Kato’s rational inequality bounds $H^2(C_{j_*})$ by the index of $Z_h$; its local correction is zero by Lemma C.8. The localization sequence adds at most $\sum_qv_{\mathfrak{p}}(D_q)$ to the degree-two length. Multiplication of a rank-one submodule by $\prod_qD_q$ adds exactly that amount to its index. This proves (C.3). No additional fixed multiplier is needed: here one can take $F_E=1$.

□

We henceforth write $z_S=z_S^{(0)}$. The inverse cyclotomic action in (C.2) is also the action used in Kato’s norm relation Kato (2004, Theorem 8.12); thus the displayed Euler factors agree before character evaluation.

### C.5. The integral determinant coordinate

Choose an $R$‑basis $\mathbf{e}$ of the invertible module $\det_R^{-1}\mathcal{C}_S^+$. In generic cohomology put

```math
a\wedge\widetilde{2z_S}=u\mathbf{e}.
```

The generic positive degree-one cohomology has rank two: ordinary rational cohomology has rank one and the real invariant line contributes one more. Its degree-two cohomology is torsion. Over $\mathcal{O}[G]$, Lemma C.6 identifies the determinant with the exterior square of an integral free degree-one module. The fixed-form lattice comparison, integral coefficient map, and unsmoothing therefore give

```math
2^{C_{\mathrm{int}}}u\in\mathcal{O}[G]
```

with one $C_{\mathrm{int}}$ independent of $S$, $h_0$, and $G$.

On the other hand, (C.3) implies $u_x\in A$ for every character $x$. Indeed, after inverting $2$, the real invariant line is primitive and contributes no height-one torsion. The inverse-determinant valuation at a height-one prime is the index of the zeta vector minus the length of degree-two torsion. It is nonnegative by (C.3). Normality of $\Lambda$ therefore excludes every pole except possibly at $(2)$.

**Lemma C.10 (Integral Fourier intersection).** If every $u_x$ belongs to $\Lambda[1/2]$ and $2^C u\in\mathcal{O}[G]$, then $2^C u\in\Lambda[G]$.

*Proof.* Fourier inversion expresses each group-basis coefficient of $u$ as a sum of its character values divided by $\vert G\vert $. As $\vert G\vert $ is a power of two, that coefficient belongs to $\Lambda[1/2]$. The corresponding coefficient of $2^Cu$ belongs also to $\mathcal{O}$. For a power series with bounded $2$‑denominator, nonnegative valuation in $\mathcal{O}$ means that all its coefficients are integral. Thus $\mathcal{O}\cap\Lambda[1/2]=\Lambda$.

□

We have consequently proved the uniform assertion

**Equation (C.4).**

```math
2^{C_{\mathrm{int}}}u\in\Lambda[G].
```

This argument introduces no loss depending on the size of the quadratic group.

### C.6. The integral central comparison

**Lemma C.11 (Derived Kummer reduction).** Let $K/\mathbb{Q}_2$ be finite, put $T_h=T_2E^{(h)}$, and put $M=E^{(h)}(K)^{\wedge}_2$. The Kummer condition is represented by the perfect complex $M[-1]\to R\Gamma(K,T_h)$. Its derived reduction modulo $2^n$ has degree-zero group $M[2^n]$ and degree-one group $M/2^nM$; the induced maps are respectively the local invariant map and the finite Kummer map.

*Proof.* The compact point group $M$ is a finite-rank free $\mathbb{Z}_2$‑module plus a finite group, so it has a free resolution of length one. After the shift by $-1$, tensoring this resolution with $\mathbb{Z}/2^n\mathbb{Z}$ gives the two displayed groups. The actual Kummer map is obtained from the inverse system of the multiplication-by‑$2^n$ sequences. Its compatibility with reduction follows from these same sequences. In degree zero this can also be read from the Bockstein sequence: $H^0(K,T_h)=0$, and $H^1(K,T_h)_{\mathrm{tors}}=E^{(h)}(K)[2^\infty]$. Consequently the reduction retains precisely the torsion invariants $E^{(h)}(K)[2^n]$, as well as the usual degree-one Kummer image. The statement is about derived reduction, so it does not require flatness of the coefficient quotient.

□

**Proposition C.12.** There is a constant $C_{\mathrm{loc}}$, depending only on $E$ and the fixed period choices, such that the following holds. If $s_2(E^{(h)})=0$, then

```math
u_h(0)=0\quad\Longleftrightarrow\quad L(E^{(h)},1)=0.
```

If these values are nonzero, then

**Equation (C.5).**

```math
\bigl\vert v_2(u_h(0))-D(h)\bigr\vert \le C_{\mathrm{loc}}.
```

The estimate is independent of all varying tame primes.

*Proof.* Write $T_h=T_2E^{(h)}$, $A_h=E^{(h)}[2^\infty]$, and

```math
H=H^1(G_{\mathbb{Q},S},T_h),\qquad
 H_2=H^2(G_{\mathbb{Q},S},T_h).
```

For a finite or real place $v$, let $K_v$ be the inverse-limit Kummer image of $E^{(h)}(\mathbb{Q}_v)^{\wedge}_2$ in $H^1(\mathbb{Q}_v,T_h)$. The inverse-limit Kummer sequence and local duality Milne (2006, I, Theorem 3.2) identify its quotient with $T_2H^1(\mathbb{Q}_v,E^{(h)})$. At an odd finite place the $2$‑completion of the local point group is finite, so this Tate module is zero. It is also zero at the real place. At $2$, the local point group has a free $\mathbb{Z}_2$‑part of rank one, and

```math
L_2=H^1(\mathbb{Q}_2,T_h)/K_2
```

is free of rank one. These assertions use the full Kummer condition, including at the bad primes.

The dual exponential induces an isomorphism from $L_2\otimes\mathbb{Q}_2$ to its one-dimensional de Rham target. For an elliptic curve, compatibility of the Kummer map with the exponential and formal logarithm, together with their local-duality adjunction, is given by Bloch–Bloch and Kato (1990, Proposition 3.8 and Example 3.11). It is valid for every reduction type. Choose a generator $ℓ_h$ of $L_2$ and use a minimal differential in the target. Define

```math
\delta_{2,h}=v_2(\exp_2^*ℓ_h).
```

The integer $\delta_{2,h}$ is bounded independently of $h$: the local curve is fixed up to isomorphism and a minimal differential is fixed up to a unit. Equivalently, the formal logarithm is an integral isomorphism on a fixed sufficiently small formal subgroup, and its adjoint gives the asserted fixed lattice index.

Here is the integral Poitou–Tate calculation, including its real term. At each finite level $E^{(h)}[2^n]$, the two Kummer images are exact annihilators under the Weil pairing and local Tate duality. The finite Poitou–Tate sequence therefore gives the Selmer comparison sequence. Explicitly, a character of the finite Selmer subgroup extends to global degree-one cohomology because $\mathbb{Q}/\mathbb{Z}$ is injective. Its Poitou–Tate connecting image in global degree two is independent of that extension: the difference comes from a local Kummer image, by the exact-annihilator relation. The same relation identifies the kernel with the image of the singular local quotient. Taking inverse limits on the compact side and direct limits on its dual side is exact: all the finite-level groups are finite and the inverse systems satisfy Mittag–Leffler. The real terms are complete Tate cohomology, agreeing with ordinary cohomology in the positive degrees used below; see Milne (2006, I, Theorem 4.10) and Nekovář (2006, 5.7.1.6). Since all singular compact local quotients except $L_2$ vanish, the resulting tail is

**Equation (C.6).**

```math
\begin{aligned}
0\longrightarrow L_2/J
 &\longrightarrow\mathrm{Sel}_{2^\infty}(E^{(h)}/\mathbb{Q})^\vee
 \longrightarrow H_2\\
 &\longrightarrow
 \left(\bigoplus_{\substack{q\in S\\ q\ \mathrm{finite}}}
       H^2(\mathbb{Q}_q,T_h)\right)\oplus H^2(\mathbb{R},T_h)
 \longrightarrow H^0(\mathbb{Q},A_h)^\vee\longrightarrow0,
\end{aligned}
```

where $J$ is the image of $H$ in $L_2$.

The assumption $s_2(E^{(h)})=0$ makes the discrete Selmer group finite of length $s(h)$ and the compact Selmer group torsion. Tensoring the same comparison sequence with $\mathbb{Q}_2$ identifies $H\otimes\mathbb{Q}_2$ with $L_2\otimes\mathbb{Q}_2$ and makes $H_2\otimes\mathbb{Q}_2=0$. Thus $J$ has finite index, say $i=\mathrm{length}(L_2/J)$, and $H_2$ is finite. Put

```math
g=\mathrm{length}H^0(\mathbb{Q},A_h),\qquad
 a_q=\mathrm{length}H^0(\mathbb{Q}_q,A_h),\qquad
 r_j=\mathrm{length}H^j(\mathbb{R},T_h)\quad(j=1,2).
```

Local duality and (C.6) give the exact identity

**Equation (C.7).**

```math
\mathrm{length}H_2
   =s(h)-i+\sum_{\substack{q\in S\\ q\ \mathrm{finite}}}a_q+r_2-g.
```

Also $H_{\mathrm{tors}}=H^0(\mathbb{Q},A_h)$, by the cohomology sequence of $0\to T_h\to V_h\to A_h\to0$ and the vanishing of rational invariants.

We next compute the determinant coordinate without suppressing any finite index. Put $K=\ker(H\to H^1(\mathbb{R},T_h))$, let $k_0=\mathrm{length}K_{\mathrm{tors}}$, and let $k$ be the index length of $K/K_{\mathrm{tors}}$ in $H/H_{\mathrm{tors}}$. The positive cone sequence gives

```math
0\longrightarrow\mathbb{Z}_2a\longrightarrow H^1(\mathcal{C}_{S,h}^+(0))
 \longrightarrow K\longrightarrow0.
```

This positive degree-one group is free, since its complex has a finite free model in degrees $1,2$. The index of $a$ in its saturated real line is therefore $2^{k_0}$. If $\alpha$ is the coordinate of $z_{S,h}(0)$ in a generator of $H/H_{\mathrm{tors}}$, then the valuation of $a\wedge\widetilde{2z_{S,h}(0)}$ in the exterior square of the positive degree-one lattice is

```math
k_0+1+v_2(\alpha)-k.
```

The image of $H$ in $H^1(\mathbb{R},T_h)$ has length $g-k_0+k$. Surjectivity onto $H^2(\mathbb{R},T_h)$, proved in Lemma C.3, consequently gives

```math
\mathrm{length}H^2(\mathcal{C}_{S,h}^+(0))
   =\mathrm{length}H_2+r_1-g+k_0-k-r_2.
```

For a perfect complex with free degree-one cohomology and finite degree-two cohomology, its inverse determinant lattice maps to $2^{\mathrm{length}H^2}$ times the exterior power of the free degree-one lattice. This follows directly from Smith normal form, or from the block $[\mathbb{Z}_2\xrightarrow{2^a}\mathbb{Z}_2]$ in degrees one and two. A vector’s determinant coordinate therefore subtracts that length. The preceding two identities give

**Equation (C.8).**

```math
v_2(u_h(0))
  =v_2(\alpha)-\mathrm{length}H_2+g+1+r_2-r_1.
```

Since the image of a free generator of $H$ generates $J$,

```math
v_2(\alpha)=v_2(\exp_2^*z_{S,h}(0))-i-\delta_{2,h}.
```

Substitution of (C.7) into (C.8) cancels $i$ and yields

**Equation (C.9).**

```math
v_2(u_h(0))=
 v_2(\exp_2^*z_{S,h}(0))-s(h)
 -\sum_{\substack{q\in S\\ q\ \mathrm{finite}}}a_q
 +2g+1-\delta_{2,h}-r_1.
```

Full rational $2$‑torsion makes complex conjugation congruent to the identity modulo $2$. Thus $(1+c)/2$ and $(1-c)/2$ are integral projectors, each of rank one. In particular $r_1=r_2=1$.

At a good active prime, inertia acts by $-1$ on $A_h$; its invariants are exactly $E[2]$, all fixed by Frobenius, so $a_q=2$. At a good unused prime, reduction identifies the local $2$‑primary torsion with $E^{(h)}(\mathbb{F}_q)[2^\infty]$, so $a_q=v_2(\#E^{(h)}(\mathbb{F}_q))$. These unused terms cancel precisely the Euler terms in (C.1), and the active terms sum to $2\omega(\vert h\vert )$. The terms at $2N$ are fixed. Finally, $g\le a_2$, because global torsion injects into local torsion at $2$, and $a_2$ is fixed. Formula (C.9) proves the *two-sided* bound (C.5). It is a central lattice computation; it makes no equality assertion for Iwasawa characteristic ideals.

The same rational comparison sequence showed that the central positive complex has only degree-one rational cohomology, of dimension two. This equals its generic rank, so the determinant and its wedge specialize under derived coefficient change without a rank change. If $L(E^{(h)},1)=0$, explicit reciprocity gives zero dual exponential. The ordinary rational class then satisfies the Kummer condition at $2$ and, automatically, at every other place. Its rational finite Selmer group is zero, so the class is zero and its wedge with $a$ vanishes. Conversely, a nonzero central value has nonzero dual exponential, hence a nonzero ordinary free-line coordinate and a nonzero wedge. This proves the asserted equivalence.

□

### C.7. Binary congruences and the two consequences

**Lemma C.13.** Let $z_1,\ldots,z_r\in\mathbb{Z}_2[G]$. If $b\gt r(2^M-1)$, then there is $x\ne0$ such that

```math
(z_j)_x\equiv(z_j)_0\pmod{2^M}\qquad(1\le j\le r).
```

*Proof.* Expanding sign characters as products of $1-2x_i$ gives

```math
z(x)=a_\emptyset+
 \sum_{\emptyset\ne I\subseteq\{1,\ldots,b\}}
       2^{\vert I\vert }a_I\prod_{i\in I}x_i,
 \qquad a_I\in\mathbb{Z}_2.
```

The $j$th binary digit of a $2$‑adic integer $a$ is the coefficient of $Y^{2^j}$ in $(1+Y)^a$ over $\mathbb{F}_2$. On the Boolean cube, a monomial $x_I=\prod_{i\in I}x_i$ contributes

```math
1+x_I\bigl((1+Y)^{2^{\vert I\vert }a_I}-1\bigr).
```

Its nonconstant terms start in degree at least $2^{\vert I\vert }$ in $Y$. Since $\vert I\vert \le2^{\vert I\vert }$, the coefficient of $Y^{2^j}$ has Boolean degree at most $2^j$. The formulas extend to all $2$‑adic coefficients by continuity in each finite coefficient quotient.

The $rM$ digit equalities are therefore Boolean equations of total degree at most $r(2^M-1)$. Their common-zero indicator is the product of one plus each equation. A Boolean polynomial of degree less than $b$ has even sum over $\mathbb{F}_2^b$, since every monomial omits at least one variable. Thus the number of common zeros is even. It already contains $0$, so it contains a nonzero point.

□

*Proof of Theorem C.1.* For $L(E^{(h)},1)\ne0$, the forward analytic-rank-zero theorem Kolyvagin (1990) gives $s_2(E^{(h)})=0$ and finiteness of its Shafarevich–Tate group. Apply the construction to this single character. Equation (C.4) gives $v_2(u_h(0))\ge-C_{\mathrm{int}}$, and the central comparison gives $D(h)\ge-C_{\mathrm{int}}-C_{\mathrm{loc}}$.

□

*Proof of Theorem C.2.* Choose an integer $M$ with

```math
M-C_{\mathrm{int}}\gt B+C_{\mathrm{loc}}.
```

For a family with $b\gt 2^M-1$, apply Lemma C.13 to the constant coefficient of the element $2^{C_{\mathrm{int}}}u\in\Lambda[G]$. It gives $x\ne0$ with

```math
v_2(u_x(0)-u_0(0))\ge M-C_{\mathrm{int}}.
```

The hypotheses at $x$, the forward theorem, and Proposition C.12 give $v_2(u_x(0))\le B+C_{\mathrm{loc}}$. The ultrametric inequality now implies

```math
u_0(0)\ne0,\qquad
 v_2(u_0(0))=v_2(u_x(0))\le B+C_{\mathrm{loc}}.
```

Since the base has Selmer corank zero, Proposition C.12 gives $L(E^{(h_0)},1)\ne0$ and $D(h_0)\le B+2C_{\mathrm{loc}}$. One constant $C_E$ can cover both stated theorems and the two fixed real signs.

□

## Appendix D. Ring-class determinants

Throughout this section $E=F$ is the auxiliary curve, $N$ is its conductor, and $T=T_2E$. In particular, $E$ is non-CM and $E[2]\subset E(\mathbb{Q})$. Put

```math
\Lambda=\mathbb{Z}_2[[t]],\qquad
 \mathcal{O}=\widehat{\Lambda_{(2)}},\qquad
 \Omega=\mathbb{F}_2((t)),\qquad v_2(2)=1.
```

We use the ring-class deformation, determinant switch, and binary transfer construction of OpenAI (2026), with the integral local conditions and finite descent specified below.

Let $K=\mathbb{Q}(\sqrt{k})$ be imaginary quadratic, split at every prime dividing $2N$, with $\mathcal{O}_K^\times=\{1,-1\}$. Let $h$ be a product of distinct signed good odd primes, all split in $K$, with $(h,k)=1$. For a fixed modular parametrization $\pi:X_0(N)\to E$ normalized by $\pi(\infty)=0$, choose coherently oriented CM points $y_c\in E(H_c)$, where $H_c$ is the ring-class field of conductor $c$. The primitive, unaveraged sum is

```math
P_h(K)=\sum_{\sigma\in\mathrm{Gal}(H_{\vert h\vert }/K)}
                   \chi_h(\sigma)\,\sigma(y_{\vert h\vert })
              \in E^{(h)}(K).
```

Here the last inclusion uses the quadratic-twist identification. When $L(E^{(h)},s)L(E^{(hk)},s)$ has a simple zero at $s=1$, the Gross–Zagier–Kolyvagin theorem makes $P_h(K)$ nontorsion and $E^{(h)}(K)$ of rank one. Write $j_h(k)$ for the $2$‑adic valuation of its index in the free completed Mordell–Weil lattice. In this situation write

```math
s(h)=v_2\#\mathrm{Sha}(E^{(h)}/\mathbb{Q})[2^\infty],
 \qquad w(h)=\omega(\vert h\vert ).
```

These Shafarevich–Tate groups are finite by the same forward theorem.

**Theorem D.1 (Ring-class lower bound).** For every $A\geq0$ there is a constant $C(E,A)$ such that every such simple-zero instance with $\omega(\vert k\vert )\leq A$ satisfies

```math
2j_h(k)\geq 4w(h)+s(h)+s(hk)-C(E,A).
```

**Theorem D.2 (Ring-class missing vertex).** Fix $K$ as above and suppose

```math
\mathrm{corank}_{\mathbb{Z}_2}
       \mathrm{Sel}_{2^\infty}(E/K)=1.
```

Suppose there are binary families of arbitrarily large dimension $b$,

```math
h_x=\prod_{q\in Q}(q^*)^{\lambda_q(x)},\qquad
 x\in\mathbb{F}_2^b,\qquad
 \lambda_q:\mathbb{F}_2^b\longrightarrow\mathbb{F}_2\text{ linear},
```

where the primes in $Q$ are good, odd, split in $K$, and outside the fixed support. Assume all vertices have the same local squareclasses at $2N$ and the same real sign as $h_0=1$. Suppose every $x\ne0$ has a simple zero of $L(E^{(h_x)},s)L(E^{(h_xk)},s)$ and

```math
2j_{h_x}(k)-4w(h_x)-s(h_x)-s(h_xk)\leq B
```

with one constant $B$ for all families. Then

```math
\mathrm{ord}_{s=1}\bigl(L(E,s)L(E^{(k)},s)\bigr)=1.
```

No finiteness assumption on $\mathrm{Sha}(E/K)$ is made.

### D.1. Moving scalar characters

**Lemma D.3.** There is a constant $c_E$ with the following property. For any finite list of oriented split odd primes outside $2N$ and any integers $n_i\to\infty$, there are distinct split primes $r_i$ and characters

```math
\xi_i:\mathrm{Gal}(H_{r_i}/K)\longrightarrow\mathbb{Z}/2^{n_i}
```

surjective on inertia at $r_i$, trivial at the primes over $2N$, and odd on the prescribed oriented Frobenii. One may require $r_i\to1$ in $\mathbb{Z}_2$ and

```math
v_2(2-a_{r_i}),\quad v_2(2+a_{r_i}),\quad
 v_2\det(1-\mathrm{Fr}_{r_i}\vert T),\quad
 v_2\det(1+\mathrm{Fr}_{r_i}\vert T)\leq c_E.
```

The constant is independent of $K$ and of the list.

*Proof.* Choose split prime ideals $\mathfrak{p}_j$, with disjoint conjugate pairs, containing the prescribed ideals and ideals over $2N$, and enlarge the list to generate $\mathrm{Cl}(K)$. Assign weight $1$ to prescribed odd ideals, weight $0$ to the others, and opposite weights to conjugates. For a basis $m^{(a)}$ of the relation lattice choose

```math
(\beta_a)=\prod_j\mathfrak{p}_j^{m_j^{(a)}}.
```

Over $K(\mu_{2^\infty})$, prescribe the action on the $2^n$th roots of $\beta_a/\overline\beta_a$ by $\zeta_{2^n}^{-\sum_jm_j^{(a)}w_j}$. These prescriptions respect every Kummer relation: at an odd ideal with nonzero weight the cyclotomic extension is unramified, so a $2^n$th-power relation has each relevant valuation divisible by $2^n$. Weights over $2$ are zero. Kummer duality therefore supplies the prescribed automorphism.

For a split prime $r$, the ring-class exact sequence is

```math
1\longrightarrow\mathbb{F}_r^\times
 \longrightarrow\mathrm{Pic}(\mathbb{Z}+r\mathcal{O}_K)
 \longrightarrow\mathrm{Cl}(K)\longrightarrow1.
```

The units $\pm1$ are diagonal in the split residue quotient. The displayed principal relations say exactly that a primitive residue character of order $2^n$ extends with the prescribed values on the $\mathfrak{p}_j$. Conjugation inverts this character.

For compatibility with the Tate representation, let $H_E$ be its image over $\mathbb{Q}(\mu_{2^\infty})$. It is open in $\mathrm{SL}_2(\mathbb{Z}_2)$ by the open-image theorem Serre (1972). The image over $K(\mu_{2^\infty})$ has index at most two in $H_E$. Every such subgroup contains $[H_E,H_E]$, and its commutator contains $[[H_E,H_E],[H_E,H_E]]$. The latter contains a fixed open subgroup $U_E$: the Lie algebra $\mathfrak{sl}_2(\mathbb{Q}_2)$ is perfect. Lifted commutators fix the radical extension, which is abelian over the cyclotomic field. Thus a permitted Tate image can be varied throughout its $U_E$‑coset without changing the Kummer prescriptions.

There are finitely many such cosets. In each choose a matrix $g_C$ with trace different from $2$ and $-2$. This is possible because neither trace equation contains an analytic open subset of $\mathrm{SL}_2$. The maximum of $v_2(2\pm\mathrm{tr}g_C)$ is a fixed $c_E$. Restrict a lift with this Tate image to a finite extension containing the required radical roots, roots of unity, and sufficiently much $2$‑power torsion. Chebotarev supplies infinitely many primes realizing this finite condition, with a chosen place realizing its representative. Requiring $r\equiv1\pmod{2^M}$ for $M\gt c_E$ gives the two determinant bounds from $\det\mathrm{Fr}_r=r$. Finite avoidance gives distinct $r_i$ outside the previous support.

□

Put $A_i=(\mathbb{Z}/2^i)[t]/(t^i)$ and choose $n_i\geq2i$. Then $\Psi_i=(1+t)^{\xi_i}$ is well defined: the coefficients of $(1+t)^{2^{n_i}}-1$ below degree $i$ are divisible by $2^i$. These are finite characters. No prime is required to split in an infinite extension, and no compatibility of the chosen moving primes is assumed before the limiting construction.

### D.2. Integral local conditions and finite diagrams

**Lemma D.4 (Finite free models).** Let $(A,\mathfrak{m},\kappa)$ be an Artin local ring and let $D$ be a complex of flat $A$‑modules with finite-dimensional residual cohomology in a bounded interval. There is a bounded finite free complex $C$ and maps $i,p,h$ with

```math
pi=1,\qquad 1-ip=dh+hd,\qquad
 \mathrm{rank}C^j=\dim_\kappa H^j(D\otimes_A\kappa).
```

Every specified finite collection of chain maps, homotopies, pairings, and triangles can be transported through these contractions.

*Proof.* A flat module over an Artin local ring is free. Indeed, lift a basis modulo $\mathfrak{m}$; nilpotence kills the cokernel, and flatness and nilpotence kill the kernel. Split the residual complex into its cohomology and contractible disks, and lift the graded bases. If $d_0$ is the lifted disk differential, write $d=d_0+\epsilon$. For the disk contraction $(i_0,p_0,h_0)$, the inverses of $1+h_0\epsilon$ and $1+\epsilon h_0$ are finite geometric sums. The formulas

```math
\begin{aligned}
 d_C&=p_0\epsilon(1+h_0\epsilon)^{-1}i_0,\qquad
 i=(1+h_0\epsilon)^{-1}i_0,\\
 p&=p_0(1+\epsilon h_0)^{-1},\qquad
 h=h_0(1+\epsilon h_0)^{-1}
 \end{aligned}
```

give the asserted identities by substitution. They apply to infinite disk sums because every geometric sum terminates. Transport a map $f$ as $p'fi$ and retain the induced composition homotopies. A quasi-isomorphism between bounded free complexes has a contractible cone, which supplies its homotopy inverse.

□

Continuous cochains with finite free Artin coefficients are flat: the locally constant functions are filtered unions of finite free modules over finite clopen partitions. Reduction gives the actual reduced cochains. We apply Lemma D.4 to these cochains and their Selmer cones, keeping maps back to the original cochains.

**Lemma D.5 (Kummer conditions and coefficient duality).**

For a finite extension $L$ of a nonarchimedean local field of characteristic zero and an elliptic curve $B/L$, the condition

```math
U_L=B(L)^\wedge_2[-1]\longrightarrow R\Gamma(L,T_2B)
```

is perfect and exactly self-orthogonal under local Tate duality. Its derived reduction modulo $2^a$ has

```math
H^0=B(L)[2^a],\qquad H^1=B(L)/2^aB(L),
```

with the invariant isomorphism and Kummer injection as its maps to local cohomology. The local and totally imaginary global duality diagrams are natural under arbitrary, including nonflat, coefficient quotients.

*Proof.* The completed point group is finitely generated over $\mathbb{Z}_2$ and has a free resolution of length one. Its integral Kummer map defines the indicated derived morphism; the Kummer exact sequences give the asserted maps after reduction. The cup product on $U_L\otimes^{\mathbf{L}}U_L$ followed by the invariant map to $\mathbb{Z}_2[-2]$ is zero. Indeed, this source has amplitude $[0,2]$, and its morphisms to $\mathbb{Z}_2[-2]$ are determined by the map on degree-two cohomology; the possible $\mathrm{Ext}^1(H^3,-)$ term is zero. That map vanishes at every finite exponent by finite Kummer isotropy and hence vanishes integrally. Choose one nullhomotopy on free models. The resulting quotient-to-dual map is a quasi-isomorphism modulo $2$, by the perfect finite Kummer pairing, and therefore integrally by derived Nakayama. This proves exact orthogonality for every reduction type, also at $2$ Milne (2006, I, Theorem 3.2 and Corollary 3.4).

Start the invariant morphisms with $R\Gamma(L,\mathbb{Z}_2(1))\to\mathbb{Z}_2[-2]$ and, globally, the compact-support morphism to $\mathbb{Z}_2[-3]$. Define their $A$‑valued versions by derived tensor. Associativity gives naturality for every $A\to B$. The Weil pairing between $T\chi_h\Psi\otimes A$ and $T\chi_h\Psi^{-1}\otimes A$ is $A$‑bilinear; the character factors cancel before the invariant map. For a bounded free complex,

```math
R\mathrm{Hom}_A(C,A)\otimes_A^{\mathbf{L}}B
 \simeq R\mathrm{Hom}_B(C\otimes_A^{\mathbf{L}}B,B).
```

In bases this is transpose followed by reduction. Cone formation, restrictions, and the chosen isotropy homotopies commute with these operations. The usual local and Poitou–Tate duality morphisms therefore give coefficient-natural relative dualities Nekovář (2006, Proposition 5.2.4 and Theorem 6.3.4). A finite Frobenius-ring trace may check perfectness at an Artin stage; it is not used as a transition morphism.

□

For $M_i=T\otimes\chi_h\Psi_i\otimes A_i$ the Selmer complex is the actual mapping cone

```math
C_i=\mathrm{Cone}\left(
 R\Gamma(G_{K,S_i},M_i)\oplus\bigoplus_{v\in S_i}U_v
 \longrightarrow\bigoplus_{v\in S_i}R\Gamma(K_v,M_i)
 \right)[-1].
```

Use the integral Kummer condition at $2N$, the full condition at primes dividing $h$ and at $r_i$, and the unramified condition at other good places. The full condition has orthogonal condition zero. At a derivative prime we instead use the following truncations.

**Lemma D.6 (The derivative local complex).** Choose inert derivative primes $ℓ$ with rational Frobenius tending on $T$ to a fixed complex conjugation $J$. At retained precision $2^a$, impose $ℓ^2\equiv1\pmod{2^{a+1}}$ as well. The local complex has the split form

```math
M\oplus(F\oplus S)[-1]\oplus M[-2],\qquad F=S=M,
```

with zero differential and coordinates $f(c)=c(\gamma^2)$, $s(c)=c(\sigma)$, where $\gamma$ is rational Frobenius and $\sigma$ is oriented tame inertia. The conditions

```math
U_F=M\oplus F[-1],\quad U_S=M\oplus S[-1],\quad
 U_{\mathrm{str}}=M,\quad U_{\mathrm{rel}}=M\oplus(F\oplus S)[-1]
```

have compatible integral duality triangles; the first two are self-orthogonal and the last two are orthogonal complements. The mixed pairing is a unit multiple of $\langle x,Jy\rangle$.

*Proof.* The tame presentation is $\phi\sigma\phi^{-1}\sigma^{-q}=1$, $q=ℓ^2$. After trivial coefficient action its Fox complex has ranks $(1,2,1)$, differential $d^0=0$, $d^1=(0,1-q)$. Its cup diagonal has zero pure-finite term, unit mixed terms, and pure-tame coefficient $\pm\binom q2$. Both $1-q$ and $\binom q2$ vanish modulo $2^a$ under the imposed congruence. Equivalently, the field contains the $2^{a+1}$st roots of unity, so the norm-residue identity $(x,x)=(x,-1)$ makes the scalar square terms zero. Local Tate duality makes the mixed term a unit. This computation is coefficientwise and applies to the free Artin module, including its nilpotent variables. The pure-plane cup maps are zero already on these finite complexes; choose their zero homotopies. Conjugation acts by $J$ on the finite coordinate and by $-J$ on the singular coordinate, giving the displayed mixed pairing. The stated orthogonal complements and duality triangles follow directly.

□

### D.3. Integral derivative classes at two

**Lemma D.7 (Uniform direct descent).** There is an integer $e$ depending only on $E$ such that $2^e$ kills the $2$‑primary torsion over every compositum of ring-class fields of any imaginary quadratic $K$. If $L/F$ is such a finite Galois extension, $m=2^a$, and $R\in E(L)$ has invariant image in $E(L)/mE(L)$, the formula

```math
b_R(\sigma)=2^e\bigl((\sigma-1)Q-B_{\bar\sigma}\bigr),
 \quad mQ=R,\quad mB_\delta=(\delta-1)R,\quad B_1=0
```

defines a canonical class $d_m(R)\in H^1(F,E[m])$. It restricts to the Kummer class of $2^eR$, is additive in the invariant Kummer class, and commutes with embeddings and conductor corestrictions.

*Proof.* By open image choose $g$ acting on $T$ by $u\mathrm{Id}$, $u\in1+4\mathbb{Z}_2$, $u\ne1$. For complex conjugation $\tau$, $g^2\tau g^2\tau^{-1}$ fixes every ring-class field of $K$: $g^2$ belongs to $G_K$ and $\tau$ inverts the abelian ring-class action. Its Tate action is $u^4$. Thus $e=v_2(u^4-1)$ works uniformly.

The expression in parentheses belongs to $E[m]$. Moreover $db_R=-2^e dB=0$, since $dB\in E(L)[m]$. Changing $B$ has no effect, changing $Q$ gives a coboundary, and replacing $R$ by $R+mW$ is absorbed by $Q+W$ and $B_\delta+(\delta-1)W$. These observations also prove additivity and naturality. For a conductor corestriction, write $\sigma r=r'h$ for coset representatives and set

```math
Q_{\mathrm{norm}}=\sum_r rQ,\qquad
 B_{\mathrm{norm}}(\sigma)=\sum_r r'B_{\bar h}.
```

The coset permutation gives the required multiples for the norm point, and the corestricted cocycle is exactly the displayed direct descent formula. Choices in a smaller field differ by torsion in the larger ring-class field and are killed by the same $2^e$.

□

**Lemma D.8 (Finite derivative identities).** One fixed integer $L\ne0$ gives, for every finite set $I$ of derivative slots, classes $z_I$ in the corresponding Selmer complex with singular conditions at $I$. At a new derivative prime $ℓ$ their coordinates satisfy

```math
f(z_{I\cup\{ℓ\}})=0,\qquad
 s(z_{I\cup\{ℓ\}})=Jf(z_I).
```

The same $L$ works for every active and derivative support, and the identities survive integral weighted transfer and coefficient reduction.

*Proof.* A fixed multiple of the parametrization kills its cusp differences by Manin–Manin (1972) and Drinfeld (1973). For $c=\vert h\vert r$ and inert good $ℓ\nmid c$, the CM point relations are

```math
\mathrm{Tr}_{H_{cℓ}/H_c}y_{cℓ}=a_ℓ y_c,
 \qquad \widetilde y_{cℓ}
                  =F_ℓ\widetilde y_c.
```

These are the norm and reduction relations from the CM Hecke correspondence Kolyvagin (1990). For squarefree $n=\prod_{ℓ\in I}ℓ$, the relative ring-class group is the product of cyclic groups of orders $ℓ+1$. Put

```math
D_ℓ=\sum_{j=1}^{ℓ}j\sigma_ℓ^j,\qquad
 D_I=\prod_{ℓ\in I}D_ℓ.
```

The exact identity $(\sigma_ℓ-1)D_ℓ=(ℓ+1)-\mathrm{Tr}$ makes the Kummer class of $D_Iy_{cn}$ invariant modulo $m$ when $m$ divides $a_ℓ$ and $ℓ+1$ for every $ℓ\in I$. Apply Lemma D.7 once to this full extension.

Fix $ℓ\in I$ and write $X=D_{I\setminus\{ℓ\}}y_{cn/ℓ}$, $Y=D_{I\setminus\{ℓ\}}y_{cn}$. Choose in the direct descent

```math
B_{\sigma_ℓ}=[(ℓ+1)/m]Y-[a_ℓ/m]X.
```

The prime $(ℓ)$ is principal in $K$ and splits in the lower ring-class field; hence $F_ℓ^2\widetilde X=\widetilde X$. For $mQ_X=X$, the lower finite coordinate and upper singular coordinate are

```math
\begin{aligned}
 f&=2^e(F_ℓ^2-1)\widetilde Q_X
      =2^e(a_ℓ F_ℓ-(ℓ+1))\widetilde Q_X,\\
 s&=2^e\bigl([a_ℓ/m]\widetilde X
             -[(ℓ+1)/m]F_ℓ\widetilde X\bigr).
 \end{aligned}
```

The Frobenius polynomial gives

```math
(F_ℓ-a_ℓ)(a_ℓ F_ℓ-(ℓ+1))
       =a_ℓ-(ℓ+1)F_ℓ.
```

Therefore $s=(F_ℓ-a_ℓ)f=Jf$ at the retained precision. For the upper finite coordinate,

```math
\widetilde{D_ℓ Y}
       =[ℓ(ℓ+1)/2]F_ℓ\widetilde X.
```

Require $v_2(ℓ+1)\geq a+1$. Its displayed division by $m$ is an $\mathbb{F}_{ℓ^2}$‑point. Lift it to the unramified lower local field; multiplication by $m$ is an automorphism on the formal group at odd $ℓ$. An $m$‑division point of $D_ℓ Y$ thus exists in the upper local field with that reduction. A Frobenius-square lift fixing this field has zero Kummer value, and its $B_1$ is zero. This proves the upper finite identity. The calculation applies at each retained derivative prime, preserving the earlier singular conditions.

At a place over $2N$ the descent extensions are unramified. The first cohomology of the identity-component point group under an unramified extension vanishes by Lang’s theorem, smooth lifting, and the formal-group trace calculation. The remaining obstruction is killed by the exponent of the geometric component group. The finitely many permitted local quadratic types have a common such multiple. Include it, the cusp multiple, and $2^e$ in $L$.

Finally use the actual weighted coset sum. If $F/K$ is Galois and $gr=r'h(g,r)$, a cocycle $b$ on $G_F$ gives

```math
\mathrm{Cor}_\theta(b)(g)
       =\sum_r r'\cdot b(h(g,r)),
```

where the action includes the scalar and quadratic character $\theta$. The crossed identity follows termwise; changing representatives gives a coboundary. There is no division by the degree. At derivative primes the lower ring-class character is locally trivial because $(ℓ)$ is principal. Transporting the place and Frobenius in each summand preserves both displayed identities with the same scalar weight. The calculation in Lemma D.7 also proves compatibility with split conductor norms. Local lifts and degree-zero boundary witnesses are then included in the actual Selmer cone. Coefficient change uses the derived Kummer complexes, retaining their degree-zero torsion invariants.

□

### D.4. Limits with retained evaluations

At each finite stage, complete descent, all weighted coset sums, and their local lifts before applying Lemma D.4. Only the target complexes over $K$ enter the limit; no bound on the degrees of the ring-class source fields is needed. For fixed $K$, active support, derivative slots, and finite group $G$, their residual dimensions are bounded. Indeed, the residual representation is the trivial $E[2]$, and Kummer theory bounds global $H^1$ by the ranks of the relevant $S$‑unit groups and the fixed $2$‑class group of $K$. There are only boundedly many moving primes. Global duality and local Euler characteristics bound the other dimensions. The same argument applies over $A_i[G]$, whose residue field is $\mathbb{F}_2$.

Fix one nonprincipal ultrafilter for this inner construction. After fixing the finitely many graded ranks on a large set, every matrix has a unique coefficientwise limit modulo each $(2^j,t^j)$; these compatible limits define matrices over $\Lambda$ or $\Lambda[G]$. All specified maps, cycles, boundary witnesses, homotopies, inverses, and duality identities survive, since each is a finite polynomial matrix identity. When adjoining another derivative slot, extend the same finite-stage diagrams and retain their old contractions and this same ultrafilter. Passing to a slower cofinal precision preserves all old limits.

**Lemma D.9 (Evaluation on arbitrary sequences).** Let $C$ be one of the resulting global complexes or Selmer complexes whose local maps are isomorphisms on $H^0$ and injections on $H^1$. Put $\Sigma=\prod_iG_K$ and $\Gamma=\Sigma\rtimes\langle\tau\rangle$, with simultaneous complex conjugation. For every field $L$ receiving a map from $\Lambda$, retained evaluation gives injections

```math
H^1(C\otimes_\Lambda L)\hookrightarrow H^1_{\mathrm{abs}}(\Sigma,L^2),
 \qquad H^0(C\otimes_\Lambda L)\hookrightarrow(L^2)^\Sigma.
```

The analogous assertion holds for the rank-four representation induced to $\Gamma$. The degree-two crossed-cocycle identities are retained for all sequences, not only a finite detecting list.

*Proof.* Compose the maps from finite models to original cochains with evaluation in degrees zero, one, and two. For sequences $g=(g_i)$ and $h=(h_i)$, their coefficientwise limits satisfy

```math
e_g^1d=(\rho(g)-1)e^0,\qquad
 e_{g,h}^2d=\rho(g)e_h^1-e_{gh}^1+e_g^1.
```

One fixed ultrafilter defines these limits for every sequence. The second identity makes the evaluation of a cycle an actual abstract crossed homomorphism; the first sends boundaries to coboundaries.

For injectivity, choose representatives for residual $H^1$ and evaluate pairs $(c,m)$ by $b_c(g)-(\rho(g)-1)m$. Their common kernel consists of $(0,m)$ with $m$ invariant. A list of at most $\dim H^1+\mathrm{rank}M$ elements already detects this kernel. Evaluation on it gives a map to the two-term complex

```math
V_i=[\,A_i^d\xrightarrow{((\rho_i(g_j)-1))_j}
                         (A_i^d)^r\,],\qquad d=2\text{ or }4.
```

The Selmer-cone sequence supplies the asserted residual injection into global cohomology, because all its local $H^0$ maps are isomorphisms. The evaluation cone has no residual cohomology in degrees at most zero. Cancel its unit disks and retain the contraction. Its finite free model then starts in degree one and continues to do so after every field base change. The long exact sequence proves injection on $H^1$ and the asserted statement on $H^0$. A crossed cocycle that is a coboundary on every sequence is in particular a coboundary on this detecting list.

□

**Lemma D.10 (Exact kernels and finite realization).** Let $H\subset\Sigma$ consist of sequences whose entries act trivially on the full Tate module, all ring-class fields of $K$, and the quadratic characters in use. Restriction of the classes in Lemma D.9 to $H$ is injective at every characteristic-zero test and at the residual $\Omega$‑test. An actual element $u\in H$ can be realized at successively increasing finite precision by derivative Frobenii $\tau u$, without changing any previous finite diagram. Their finite localization is evaluation on $(\tau u)^2$.

*Proof.* Use $z=g^2\tau g^2\tau^{-1}$ from Lemma D.7. It is central modulo $H$ and acts on coefficients by the fixed scalar $u_0^4\ne1$. For a cocycle on $\Sigma/H$, comparison of $b(zg)$ and $b(gz)$ gives

```math
(u_0^4-1)b(g)=(g-1)b(z).
```

Thus this cocycle is a coboundary in characteristic zero; inflation–restriction gives injectivity on $H$. The valuation of $u_0^4-1$ is fixed as $K$ varies. At the residual test replace $z$ by moving inertia, whose Tate action is trivial and scalar action is $1+t$. It is central modulo the exact kernel, and $t$ is a unit in $\Omega$.

At one Artin stage, every coordinate cochain in the finite model is locally constant through a finite quotient. Enlarge that quotient by the finite ring-class data, all previous data, and a sufficiently deep Tate quotient. Chebotarev realizes the conjugacy class of the actual element $\tau u$, with a place realizing its chosen representative. It gives an inert prime outside the old support. Exact Tate triviality of $u$ permits arbitrary extra precision in $a_ℓ\equiv0$ and $ℓ\equiv-1$; exact ring-class triviality makes its square trivial on the lower ring-class fields. These are finite conditions at every stage. For a crossed cocycle in the induced representation,

```math
b((\tau u)^2)=(1+\tau)b(u),
```

since $u$ acts trivially and $\tau^2=1$. Projection to either induced summand identifies this image with the rank-two finite plane.

□

**Lemma D.11 (Uniform functional and residual size).** After the inner limit, the class $z_I$ has a closed degree-two functional $\lambda_I$ obtained from the same integral duality diagram. In finite free models over $\mathcal{O}$, both are integral up to one fixed power of $2$, independently of the active support and the number of switches. The same assertion holds over $\mathcal{O}[G]$ for a whole fixed binary family. After any fixed number of switches, minimal $\mathcal{O}$‑models have size bounded in terms of $E$, a bound on $\omega(\vert k\vert )$, and that number of switches.

*Proof.* At an active prime, residual Frobenius is the nonconstant scalar $z=(1+t)^a$, with $a$ odd. The determinant of $z-1$ on the trivial rank-two residual Tate module is nonzero in $\Omega$. At $r$, inertia minus one is $t$, also a unit. The full local complexes are therefore acyclic over $\mathcal{O}$ and have contractions using only unit pivots. Over $\mathcal{O}[G]$ the same conclusion follows after reduction modulo $(2,I_G)$, whose residue field is $\Omega$.

The actual comparison $q:C_I^\perp\to C_I$ has cone equal to the sum of these full local complexes; at derivative places the chosen planes are already exactly self-orthogonal. Thus $q$ has an integral homotopy inverse. Conjugation transports $z_I$ linearly to the separate inverse-character complex. Lift it through that comparison and apply the integral Poitou–Tate morphism

```math
C_I^{\perp,\vee}\longrightarrow
                 R\mathrm{Hom}(C_I,\mathcal{O})[-3].
```

Its degree-one image is a closed degree-two functional. Every map used is integral, and any fixed normalization at the old support requires only one fixed exponent. Contracting arbitrarily many acyclic summands introduces no inverse of $2$. Later switches and minimal-model contractions likewise use integral maps. This proves the asserted uniformity, also over the group ring. Inverses of the same derived isomorphism agree; representatives at other localizations therefore define this same generic functional.

For the size bound first work with the genuine finite cochains over $\overline A_i=\mathbb{F}_2[t]/(t^i)$. The quadratic character $\chi_h$ disappears modulo $2$. Thus the reduced representation descends to the smaller permitted support containing only $2N$, the auxiliary prime, and the fixed derivative slots. Construct its smaller-support Selmer complex and its actual inflation and localization triangle to the original reduced complex. The quotient is the sum of the active singular local complexes.

Modulo $t$, the smaller-support representation is the trivial rank-two $E[2]$. The maximal pro‑$2$ Galois group over $\mathbb{Q}$ allowing also the ramification of $K$ has a generator bound from Kummer theory, depending only on the number of these primes. Its subgroup over $K$ has index at most two and satisfies Schreier’s bound. Every finite $2$‑extension over $K$ with this support lies in the same maximal pro‑$2$ extension: adjoining its quadratic conjugate still gives a $2$‑extension over $\mathbb{Q}$. This bounds the continuous residual $H^1$ of these genuine finite cochains, and duality bounds the other residual dimensions. Lemma D.4 therefore gives smaller-support free models over $\overline A_i$ of uniformly bounded ranks. Retain these models and their localization triangle in the same inner limit. Only then invert $t$. The active singular blocks become acyclic by the nonconstant residual Frobenius computation above, so the original $\Omega$‑complex is equivalent to this bounded smaller-support model. Moving inertia excludes invariants and duality excludes degree three. Minimal $\mathcal{O}$‑models therefore have two equal bounded terms in degrees one and two. This bound is proved on continuous finite arithmetic cochains; no generator bound on abstract sequence-group cohomology is used.

□

**Lemma D.12 (Outer characteristic-zero evaluation).** For any family of these bounded $\mathcal{O}_j$‑models, keep the integral evaluation and duality diagrams and a nonprincipal ultrafilter $\mathcal{U}$. The ring

```math
\mathcal{O}_\infty=
 \left(\prod_{\mathcal{U}}\mathcal{O}_j\right)\Big/
 \{(a_j):v_2(a_j)\to_{\mathcal{U}}\infty\}
```

is a DVR with uniformizer $2$ and characteristic-zero fraction field. The outer $H^1$ injects into crossed-homomorphism classes on the product of the inner sequence groups and remains injective on the product of their exact kernels. All degree-two evaluation identities and every retained finite integral diagram survive.

*Proof.* A nonzero element has bounded valuations on a large set. A finite partition then makes that valuation one integer $n$, so the element is $2^n$ times a unit. Products add these finite valuations, and every nonzero ideal has a least valuation. This proves the DVR assertion. No fixed $2^n$ vanishes, so its fraction field has characteristic zero.

Evaluation matrices remain integral through the contractions of Lemma D.11. Hence the identities of Lemma D.9 pass to this quotient. In particular, an outer cycle represented by $x_j$ with $v_2(d_jx_j)\to\infty$ satisfies the crossed identity: the integral degree-two evaluation of $d_jx_j$ also tends to zero. No exact inner lift of this new cycle is required. Choose bounded detecting lists over the residue fields and retain their cones contracted to degrees at least one. These contractions use unit pivots and survive the outer quotient, proving injectivity as before. The fixed scalar $u_0^4-1$ from Lemma D.10 remains nonzero, giving restriction injectivity on the product of exact kernels.

To express a localization test in the original finite models, first fix its $2$‑adic precision, below the vanishing order of any approximate coboundaries. Each of its finitely many $\mathcal{O}$‑coefficients then has a Laurent expansion with finite negative support. Multiply the test by a common power of $t$ and retain the finitely many coefficients needed to detect its nonzero value. These are evaluations of the original Artin cochains at sufficiently large stages, and hence factor through a finite Galois quotient. Apply Chebotarev to that quotient together with the old data and the additional Tate precision. Multiplication by $t$ affects only this finite realization test; it is a unit after localization and does not alter any arithmetic class or central normalization. Let the retained precision grow cofinally, preserving the inner and outer ultrafilters and all old diagrams and contractions. This retains both the new evaluations and the earlier arithmetic identities.

□

### D.5. The determinant switch and uniform valuation

For a perfect cohomological complex write

```math
\mathcal{D}(C)=\bigotimes_j(\det C^j)^{(-1)^{j+1}}.
```

When generic cohomology has dimension one in degrees one and two and vanishes elsewhere, the class and its actual paired functional define

```math
[z_I]\otimes[\lambda_I]\in
 H^1(C_I)\otimes H^2(C_I)^*\simeq\mathcal{D}(C_I).
```

Denote its coordinate in an integral determinant basis by $u_I$. Changing that basis multiplies $u_I$ by a unit. For a generically acyclic constituent set this class-dual coordinate to zero. For $I=\emptyset$ write $u_h$.

**Lemma D.13 (Exact integral switch).** At a derivative prime let the integral localization and duality triangles be those of Lemma D.6, over a DVR $O$. Suppose the finite-condition complex has generic $H^1$ spanned by $A$, and the derivative class $B$ has

```math
f(A)=v\ne0,\qquad f(B)=0,\qquad s(B)=Jv.
```

The singular-condition complex has generic rank one, spanned by $B$, and the two actual class-dual determinant coordinates satisfy

```math
v_O(u_F)=v_O(u_S).
```

Neither localization is required to be primitive.

*Proof.* Work first over the fraction field. Nonzero localization of $A$ makes strict $H^1$ zero. The relaxed localization image is self-annihilating in $F\oplus S$, hence has dimension two. It contains $(v,0)$ and $(0,Jv)$, so its intersections with the two planes are precisely these lines. This proves the rank assertion.

Let $V=H^1(C_{\mathrm{rel}})$ have basis $A,B$. Duality identifies $H^2(C_{\mathrm{str}})$ with $V^*$; let $A^*,B^*$ be the dual basis. The integral triangles

```math
C_{\mathrm{str}}\longrightarrow C_F\longrightarrow F[-1],\qquad
 C_{\mathrm{str}}\longrightarrow C_S\longrightarrow S[-1]
```

have boundaries dual to relaxed localization. In the first,

```math
\delta_F(x)=\epsilon\langle x,v\rangle B^*,\qquad
                                  \epsilon\in O^\times.
```

Choose a fractional $x$ with $\delta_F(x)=B^*$. The exterior product $v\wedge x$ has unit volume in $\det_O F$ because the alternating form is unimodular. Similarly choose $y$ in the singular plane mapping to $A^*$; $Jv\wedge y$ has unit volume. The determinant isomorphisms carry the two class-dual tensors to

```math
(A^*\wedge B^*)^*\otimes(v\wedge x),\qquad
 (A^*\wedge B^*)^*\otimes(Jv\wedge y),
```

up to units and signs. The plane determinant lattices are unimodularly identified, so their valuations agree. These are the integral triangles, including their torsion elementary divisors. For example, $v=2^de_1$ is paired with $2^{-d}e_2$; their exterior product is a unit. No factor $2^d$ is discarded or charged anew at the switch.

□

**Lemma D.14 (Rank-two evaluation).** At an inner characteristic-zero test with $\Psi^2\ne1$, and at every outer characteristic-zero test, the rank-four induced representation $W$ is absolutely irreducible. For two independent Selmer classes their joint evaluations on the exact kernel span $W\oplus W$. Some actual kernel element has rank-two finite localization. One of the classes may be any prescribed nonzero class.

*Proof.* Moving inertia distinguishes $\Psi$ and $\Psi^{-1}$. The Tate representation over $K$ is absolutely irreducible by open image, and multiplication of its matrices by character scalars does not change invariant subspaces. These facts prove irreducibility of the induction. In the outer case a uniform finite witness is needed. The images of the quadratic subgroups have index at most two in the fixed compact Tate image; there are finitely many such subgroups. On a large set choose one and finitely many of its matrices spanning $M_2(\mathbb{Q}_2)$. Their spanning determinant is a fixed nonzero $2$‑adic number. Character scalars are units, so this determinant remains nonzero in the outer fraction field. Moving inertia separates the two blocks, and conjugation interchanges them. Moreover $1+t$ has infinite order already in each $\Omega$: for a nonzero integer $n$, $(1+t)^n-1$ is a nonzero Laurent-series unit. It remains nonzero in the outer quotient.

Restriction to the exact kernel is injective by Lemmas D.10 and D.12. There the cocycles are additive homomorphisms with equivariant image. A proper submodule of $W\oplus W$ projecting onto both factors would impose a scalar relation, since $W$ is absolutely simple. That relation would contradict independence after restriction. Thus the joint span is the whole direct sum. Projection by $1+\tau$ gives all pairs in the finite plane. If their determinant quadratic vanished on the additive image, its polar form would vanish on every pair in that image, hence the quadratic would vanish on its entire field span. This is impossible. An actual rank-two evaluation therefore exists and is realized by Lemma D.10.

□

**Proposition D.15 (Power-series regularity and uniform bound).**

For a primitive constituent whose generic cohomology is acyclic or has the rank-one pattern above, its coordinate lies in $\Lambda[1/2]$. For the simple-zero instances,

```math
v_{(2)}(u_h)\geq-C(E,A),\qquad \omega(\vert k\vert )\leq A.
```

*Proof.* The zero coordinate needs no argument. Otherwise the arithmetic class spans generic $H^1$. At a height-one prime $\mathfrak{p}\ne(2)$, use the DVR $\Lambda_{\mathfrak{p}}$ and its characteristic-zero residue field. The full active local complexes are acyclic because ramified quadratic inertia minus one is $-2$. At $r$ the same holds unless the scalar inertia is one; that case is $t=0$, where the bounded nonzero Frobenius determinant from Lemma D.3 suffices. Degree-zero evaluation and global duality exclude degrees zero and three, so unit cancellation leaves a square two-term model. Its generic kernel is saturated; a primitive kernel vector has nonzero $\mathfrak{p}$‑fiber.

If the fiber dimension is $s\gt 1$ and $\Psi^2\ne1$, choose a rank-two finite localization by Lemma D.14, including that primitive vector. The relaxed localization image is self-annihilating and contains the entire finite plane, so equals that plane. The strict kernel has dimension $s-2$, and the singular condition adds no class. The fiber rank drops by two. Generic localization is nonzero, so Lemmas D.8 and D.13 preserve generic rank one, a nonzero arithmetic class, and the determinant valuation.

If $\Psi^2=1$, the induced representation splits into two inequivalent absolutely irreducible quadratic twists. They are inequivalent because a nontrivial quadratic self-twist would contradict the open Tate image. Conjugation splits the Selmer fiber into these two signs. Each sign has a finite and a singular line, with a symmetric hyperbolic local pairing. Since the residue characteristic is zero, its only isotropic lines are the two axes. If both signs occur globally, independent evaluations in the two signs give rank two, nonzero on a prescribed nonzero component of the primitive vector. If only one sign occurs and $s\gt 1$, first choose a nonzero rank-one localization on that vector. The relaxed image is the finite line in that sign and the singular line in the other sign. A switch retains the old strict kernel of dimension $s-1$ and introduces the other sign. The next rank-two switch reduces the dimension by two. Repetition terminates at dimension one; it cannot pass below one because a primitive generic-kernel vector survives every switch. The terminal minimal DVR model is one-by-one with zero differential. The class and functional are integral there, so its determinant coordinate is integral. Reversing the exact switches proves nonnegative valuation at $\mathfrak{p}$. Intersecting all such height-one valuation rings in the normal ring $\Lambda$ proves $u_h\in\Lambda[1/2]$.

For the uniform bound at $(2)$, suppose instead that a sequence of simple-zero coordinates has valuations tending to $-\infty$. By Lemma D.11 the minimal models have bounded size and one common functional clearing exponent $a$. Fix their size on a large set and write

```math
C_j=[\,\mathcal{O}_j^n\xrightarrow{D_j}\mathcal{O}_j^n\,].
```

Apply Lemma D.12. The outer kernel may contain new classes represented only by approximate inner cycles; the retained degree-two identities make them valid classes for evaluation. Primitive vectors in the inner generic kernels supply a nonzero outer class. If the outer dimension is $s\gt 1$, use Lemma D.14 with that class and a second one, and realize the evaluation at the original finite stages. The outer rank drops by two as above. The primitive inner vector localizes nontrivially on a large set, hence so does its nonzero arithmetic multiple. The exact switch preserves each inner determinant valuation, even if that multiple is highly divisible.

Only boundedly many switches are needed, because the initial outer size is bounded. At terminal outer rank one an $(n-1)$‑minor has nonzero image, so its inner determinants have one finite valuation $b$ on a large set. Put it in the upper left block $A_j$ of $D_j$. Fraction-field triangular operations of determinant one leave $A_j$ and a zero one-by-one block. If $\alpha_j$ is the last coordinate of the integral class and $\beta_j$ the value of the functional on the last target basis vector, the determinant formula is

```math
u_j=\pm\frac{\alpha_j\beta_j}{\det A_j},\qquad
 \alpha_j\in\mathcal{O}_j,\quad
 \beta_j\in2^{-a}\mathcal{O}_j.
```

Thus $v_2(u_j)\geq-a-b$, contradicting the assumed losses. All new diagrams were adjoined to the same finite stages and ultrafilters as in Lemma D.12; the common clearing exponent remains valid through every switch.

□

### D.6. Central specialization

**Lemma D.16 (The integral central complex).** Let $C$ be a perfect $\Lambda$‑complex and $C_0=C\otimes_\Lambda^{\mathbf{L}}\mathbb{Z}_2$. If generic and central rational cohomology both have dimension one in degrees one and two and vanish elsewhere, a class-dual tensor represented over $\Lambda_{(t)}$ specializes to its actual central class-dual tensor. The determinant comparison retains all torsion cohomology of $C_0$. For the ordinary integral Kummer Selmer complex, its degree-two torsion has the length of the quotient of $\mathrm{Sel}_{2^\infty}$ by its maximal divisible subgroup.

*Proof.* Derived reduction is termwise reduction of a free model, so its determinant line commutes with base change. The cohomology sequences are

```math
0\longrightarrow H^j(C)/tH^j(C)
 \longrightarrow H^j(C_0)
 \longrightarrow H^{j+1}(C)[t]\longrightarrow0.
```

Over the DVR $\Lambda_{(t)}$, a nonunit differential pivot would create extra central cohomology in adjacent degrees. The equal generic and central dimensions exclude such pivots. Only invertible disks and the two free lines remain, proving specialization of the tensor. The determinant isomorphism over $\mathbb{Z}_2$ still contains every elementary divisor, including those arising from the displayed base-change terms.

For the Kummer complex, derived tensor with $\mathbb{Q}_2/\mathbb{Z}_2$ gives the discrete Selmer group in degree one. Its universal-coefficient sequence has divisible image $H^1(C_0)\otimes\mathbb{Q}_2/\mathbb{Z}_2$ and finite quotient $\mathrm{Tor}_1(H^2(C_0),\mathbb{Q}_2/\mathbb{Z}_2)$. The image is the maximal divisible subgroup: any divisible subgroup maps trivially to the finite quotient. The latter is canonically the torsion of $H^2(C_0)$, proving the length statement. This argument allows a divisible part in the Shafarevich–Tate group.

□

**Lemma D.17 (Active local contribution).** At a good odd prime ramified in a quadratic twist of $E$, the quotient of the full integral local complex by the Kummer condition has only degree-two cohomology, of length two. Thus an active prime split in $K$ contributes exactly four to this quotient length.

*Proof.* The pro‑$2$ tame inertia generator acts by $-1$, so its integral complex has differential $-2$ and only $H^1=T/2T$. Taking residue-field cohomology gives

```math
H^1(K_v,T\chi_h)=E[2]^{\mathrm{Fr}_v},\qquad
 H^2(K_v,T\chi_h)=E[2]/(\mathrm{Fr}_v-1)E[2].
```

Both have length two because $E[2]$ is rational. The local integral Kummer sequence identifies $H^1$ with the completed point group: the residual local Weil–Châtelet group has finite $2$‑primary part and hence zero Tate module. The full/Kummer quotient therefore has exactly the asserted $H^2$. There are two places over every split active prime.

□

**Proposition D.18 (Central determinant formula).** At every known simple-zero instance,

```math
v_2(u_h(0))
   =2j_h(k)-s(h)-s(hk)-4w(h)+O_{E,A}(1),
       \qquad \omega(\vert k\vert )\leq A.
```

The error is independent of the number of primes dividing $h$. At a base of Selmer corank one, generic cohomology has rank at most one. If its central Heegner point is torsion, its primitive class-dual coordinate satisfies $u_0(0)=0$.

*Proof.* At a known simple zero, the forward Gross–Zagier–Kolyvagin theorem gives rank one over $K$ and finite Shafarevich–Tate group. At the split auxiliary prime the point norm relation is

```math
\mathrm{Tr}_{H_{\vert h\vert r_i}/H_{\vert h\vert }}y_{\vert h\vert r_i}
   =(a_{r_i}-\sigma_{r_i}-\sigma_{\bar r_i})y_{\vert h\vert }.
```

At $t=0$ the scalar character is trivial and both Artin symbols have quadratic value $\chi_h(r_i)$. The completed weighted class therefore specializes to the Kummer class of $Lm_iP_h(K)$, where $m_i=a_{r_i}-2\chi_h(r_i)$ and $v_2(m_i)\leq c_E$.

This equality is retained as an equality in the actual target diagram. Choose a free model of the ordinary Kummer Selmer complex and a representative $b_h$ of $P_h(K)$. The central comparison $j_i$ to the relaxed target has, after contraction, a degree-zero witness $v_i$ with

```math
z_i(0)-Lm_i j_i(b_h)=dv_i.
```

The equality follows from Kummer naturality, the point norm, and the injection of Selmer $H^1$ into global cohomology. Retain this witness, its local comparison triangles, and their matrices. The limit $m$ is nonzero and has bounded valuation because the same bound holds at every stage.

The paired functional has a representative over $\Lambda_{(t)}$. There, active inertia minus one is $-2$, a unit, and the central auxiliary Frobenius determinants are nonzero by Lemma D.3. Contract those local complexes and apply the retained global duality. This is the same generic functional as the integral representative over $\mathcal{O}$, and its specialization is rational Kummer duality. Over $\Lambda_{(t)}$, unit cancellation leaves one term in each of degrees one and two, since these are the central rational dimensions. The retained cycle has nonzero central image, so the remaining one-by-one differential must be zero. Generic and central rational ranks are therefore both one, and Lemma D.16 applies.

In the ordinary integral Kummer complex, free degrees one and two are paired unimodularly. The point and its functional each contribute $j_h(k)$. The degree-two torsion subtracts $v_2\#\mathrm{Sha}(E^{(h)}/K)[2^\infty]$ from the inverse determinant coordinate. Torsion in degrees one and three is bounded by the fixed scalar annihilator. More generally an elementary divisor of valuation $d$ with cokernel in degree $j$ contributes $(-1)^{j+1}d$. Lemma D.17 therefore subtracts exactly $4w(h)$. At $r$, the two local determinants have valuations $v_2(r+1-a_r\chi_h(r))\leq c_E$; the point multiplier also has bounded valuation. The unchanged Kummer conditions at $2N$ range through finitely many fixed local types. Consequently

```math
v_2(u_h(0))=2j_h(k)
 -v_2\#\mathrm{Sha}(E^{(h)}/K)[2^\infty]
 -4w(h)+O_E(1).
```

For the rational comparison use the isogenies between

```math
A_h=\mathrm{Res}_{K/\mathbb{Q}}(E^{(h)}_K),\qquad
 B_h=E^{(h)}\times E^{(hk)},
```

whose composites are multiplication by $2$. The Cassels–Tate isogeny identity, with the finite Shafarevich–Tate groups just established, identifies

```math
\frac{\#\mathrm{Sha}(A_h)\mathrm{Reg}(A_h)
                 \mathrm{Per}(A_h)\prod_p c_p(A_h)}
      {\#A_h(\mathbb{Q})_{\mathrm{tors}}\,
       \#A_h^\vee(\mathbb{Q})_{\mathrm{tors}}}
```

with the analogous expression for $B_h$ Milne (2006, I, proof of Theorem 7.3, especially (7.3.1)). This is an isogeny theorem, and does not assume the Birch–Swinnerton-Dyer conjecture. The fixed-degree composites bound the rank-one regulator, period, differential, and torsion ratios by fixed powers of $2$. At split primes the component factors agree exactly; this cancels every prime dividing $h$. At an odd prime dividing $k$ outside $2N$, the Weil restriction of the good curve has connected special fiber, whereas the ramified rational twist has component $2$‑part at most $4$. At other good nonsplit primes both factors are one. The comparisons at $2N$ are fixed. Hence

```math
v_2\#\mathrm{Sha}(E^{(h)}/K)[2^\infty]
       =s(h)+s(hk)+O_{E,A}(1).
```

This proves the formula without any error accumulating with $w(h)$.

At the unknown base, the central Kummer complex has rational dimensions one in degrees one and two by Selmer corank one; relaxation changes only rationally acyclic local terms. Generic dimensions are therefore at most one. If the generic complex is acyclic its coordinate is zero by definition. Otherwise the generic and central ranks agree, and Lemma D.16 specializes its tensor to the actual rational Kummer class-dual tensor. A torsion central point has zero rational Kummer class, so $u_0(0)=0$. No identification of Selmer corank with Mordell–Weil rank is used.

□

*Proof of Theorem D.1.* At a known simple zero, Proposition D.18 verifies the generic rank-one pattern. Proposition D.15 gives $u_h\in\Lambda[1/2]$ and a uniform lower bound for its $(2)$‑valuation. Thus $2^{C(E,A)}u_h\in\Lambda$, and its constant coefficient has the same lower bound. Substitute the central formula and enlarge the constant.

□

### D.7. Universal families and bounded clearing

Fix $K$ and one binary family from Theorem D.2. Put $G=(\mathbb{Z}/2)^b$ and $R=\Lambda[G]$, and write a subscript $0$ for augmentation. At every finite stage form the weighted transfer over $A_i[G]$, using the coefficient map

```math
A_i[\mathrm{Gal}(H_{r_i\prod_{q\in Q}q}/K)]
 \longrightarrow A_i[G],\qquad
 [\sigma]\longmapsto\Psi_i(\sigma)[\varepsilon(\sigma)].
```

Here $\varepsilon$ is the universal quadratic character; the same inverse-action convention is used on both sides. Complete this actual coset sum, its local lifts and boundary witnesses, before taking the finite target models and their limit. Character evaluation commutes with every finite identity. Lemma D.11 constructs the paired functional over $\mathcal{O}[G]$ itself. All comparisons with the ordinary central Kummer complex, including the multiplier $a_{r_i}-2[\varepsilon(\mathrm{Fr}_{\mathfrak{r}_i})]$, are retained in this same diagram.

**Lemma D.19 (Lifting a localization filtration).** Let $G$ be a finite abelian $2$‑group, put $R=\mathbb{Z}_2[[t]][G]$, and let $\epsilon:R\to\Lambda=\mathbb{Z}_2[[t]]$ be augmentation. Let $C$ be a perfect $R$‑complex. Suppose the actual augmentation localization triangle identifies $C\otimes_R^{\mathbf{L}}\Lambda$ with a bounded finite free complex

```math
T_0^\bullet=C_{\mathrm{old}}^\bullet\oplus Q^\bullet,\qquad
 d_{T_0}=\begin{pmatrix}d_{\mathrm{old}}&U_0\\0&A\end{pmatrix},
```

where $Q^\bullet$ is a direct sum of two-term local complexes in degrees one and two. There is a bounded finite free model of $C$, obtained by homotopy equivalences and addition of contractible free disks, whose underlying graded module lifts this displayed decomposition and whose differential has blocks

```math
d_C=\begin{pmatrix}D&U\\ S&B\end{pmatrix},\qquad
 D_0=d_{\mathrm{old}},\quad S_0=0,\quad B_0=A.
```

All entries belong to $R$. Every specified morphism and homotopy in the localization triangle can be transported through these equivalences. In particular, the assertion does not require the old summand to be a subcomplex before augmentation.

*Proof.* The ring $R$ is local, with maximal ideal generated by $2,t$, and the augmentation ideal. Repeatedly cancel a unit differential entry in a bounded finite free model of $C$. Each cancellation splits off a contractible free disk and retains explicit inclusion, projection, and contraction maps. The resulting model $C_{\min}$ is minimal over $R$; its augmentation is minimal over $\Lambda$.

Perform the same cancellations on $T_0$, obtaining $T_0\simeq T_{\min}\oplus E_0$, where $E_0$ is a finite direct sum of contractible disks. The given augmentation comparison induces a homotopy equivalence between $C_{\min}\otimes_R\Lambda$ and $T_{\min}$. A homotopy equivalence between bounded minimal free complexes over a local ring is a chain isomorphism: modulo the maximal ideal its differential is zero and its homotopy-inverse identities are degreewise inverse identities; Nakayama’s lemma then makes every degreewise matrix invertible. Hence

```math
(C_{\min}\otimes_R\Lambda)\oplus E_0\cong T_0
```

as based complexes. Lift $E_0$ to the same identity disks over $R$ and lift each matrix of this graded isomorphism to $R$. These lifted matrices are invertible because their augmented determinants are $\Lambda$‑units. Conjugating the actual differential on $C_{\min}\oplus E_0\otimes_\Lambda R$ by these matrices gives the asserted blocks and their exact augmentation identities. Transport of the specified maps and homotopies uses the retained contractions and these chain isomorphisms.

□

**Lemma D.20 (Simultaneous elimination).** Write $\mathcal{O}=\widehat{\Lambda_{(2)}}$. Suppose $A=\mathrm{diag}(A_1,\ldots,A_m)$ has entries in $\Lambda$, with $\det\overline A_j\ne0$ and $\mathrm{ord}_t(\det\overline A_j)\le h$. If $B=A+2E$ and $E$ has power-series entries, then $B$ is invertible over $\mathcal{O}$, and every entry of $B^{-1}$ modulo $2^M$ has no Laurent term of degree below $-Mh$. The same lower bound holds for the entries of $P-UB^{-1}S$ when $P,U,S$ have power-series entries. These bounds do not depend on $m$.

Consequently, if $G$ is elementary abelian and $B$ is the lifted block in Lemma D.19, it is invertible over $\mathcal{O}[G]$. Eliminating this block leaves a complex of the old graded size. Its augmentation is exactly $C_{\mathrm{old}}$, and all its sign constituents satisfy the preceding Laurent bound.

*Proof.* The natural coefficient description is

```math
\mathcal{O}/2^M\mathcal{O}
       =(\mathbb{Z}/2^M\mathbb{Z})((t)).
```

Indeed, if $s\notin(2)$, write $s=t^dv+2w$ with $v\in\Lambda^\times$; the finite geometric expansion of $s^{-1}$ modulo $2^M$ is a Laurent series with finite negative support. Conversely every such series is obtained by inverting $t$.

Write $\det A_j=t^{d_j}v_j+2w_j$, with $d_j\le h$ and $v_j\in\Lambda^\times$, and set

```math
C_j=\frac{\mathrm{adj}(A_j)}{t^{d_j}v_j},\qquad
 C=\mathrm{diag}(C_j).
```

The entries of $C$ have pole at most $h$, and $BC=1+2F$, where the entries of $F$ have the same bound. Thus

```math
B^{-1}\equiv C\sum_{j=0}^{M-1}(-2F)^j\pmod{2^M}.
```

The $j$th summand has pole at most $(j+1)h$. Matrix addition and multiplication by power-series matrices cannot worsen the asserted bound, regardless of the number of blocks.

The group ring $\mathcal{O}[G]$ is local. The residual determinant of the universal $B$ equals $\prod_j\det\overline A_j$, which is nonzero in $\mathbb{F}_2((t))$, so $B$ is invertible. A sign character sends the augmentation ideal to $2\Lambda$. Consequently $B_x=A+2E_x$ with power-series $E_x$. The usual contractible-pair elimination leaves the Schur differential $D-UB^{-1}S$. Its augmentation is $d_{\mathrm{old}}$ because $S_0=0$. The preceding calculation gives the uniform bound at every sign character.

□

For the ring-class complexes of $E$ with full rational $2$‑torsion, the augmentation block at a split conductor prime has residual Frobenius scalar $z=(1+t)^a$ with $a$ odd. At each of the two split places its singular determinant has residual $t$‑order two; hence one may take $h=4$ for the combined block. This proves the uniform elimination assertion in the group-ring construction of OpenAI (2026) while retaining the actual localization triangle.

**Lemma D.21 (Primitive correction).** There is a multiplier $\eta\in\mathcal{O}[G]$ such that the character coordinates of $\eta u_{\mathrm{rel}}$ are the primitive coordinates $u_{h_x}$, up to $\Lambda$‑units. This correction has no denominator depending on the number of conductor primes.

*Proof.* At an unused split prime $q$, let $z$ be the full scalar Frobenius at one orientation; the other has $z^{-1}$. The point norm and the singular local determinant are

```math
e_q=a_q-z-z^{-1},\qquad
 l_q=\det(1-q^{-1}z\mathrm{Fr}_q\vert T)
             \det(1-q^{-1}z^{-1}\mathrm{Fr}_q\vert T).
```

Conductor norms commute with direct descent and weighted transfer, so $e_q$ multiplies the actual class. It is symmetric under conjugation and therefore multiplies its actual paired functional as well. The localization triangle gives

```math
u_{\mathrm{rel}}=e_q^2u_{\mathrm{prim}}/l_q.
```

Both $e_q$ and $l_q$ are units in $\mathcal{O}[G]$: modulo its maximal ideal the scalar is $(1+t)^a$ with $a$ odd. Before character evaluation, their reductions satisfy

```math
(1+a_qz+z^2)(1+a_qz^{-1}+z^{-2})
       =a_q^2+z^2+z^{-2}=(a_q+z+z^{-1})^2.
```

Hence $l_q/e_q^2-1\in2\mathcal{O}[G]$. If $g_q\in G$ is the inertia bit, so $g_q(x)=(-1)^{\lambda_q(x)}$, then

```math
\eta=\prod_{q\in Q}
       \left(1+\frac{l_q/e_q^2-1}{2}(1+g_q)\right)
          \in\mathcal{O}[G].
```

Its $q$‑factor equals $l_q/e_q^2$ at an unused character and $1$ at an active character. Primitive central values are compared through the primitive point and its Selmer complex in Proposition D.18; no evaluation of an arbitrary element of $\mathcal{O}$ at $t=0$ is used.

□

**Lemma D.22 (Clearing a bounded complex).** Let $D$ be a based finite free $\mathcal{O}[G]$‑complex of total rank at most $r_0$, with augmentation $D_0$ defined over $\Lambda$. Suppose its central integral complex has rational dimensions one in degrees one and two, zero elsewhere, and total torsion length at most $h_1$. Let $z$ be an integral cycle and let $\lambda\in2^{-a_0}(D^2)^*$ be closed. Assume each character constituent is generically acyclic or has the rank-one pattern. An arbitrary multiplier $\eta\in\mathcal{O}[G]$ is allowed in its determinant coordinates. There are $f,d\in\mathcal{O}[G]$ with

```math
f_xu_x=d_x,\qquad f_0\in\Lambda,\qquad
 v_2(f_0(0))\leq C(r_0,h_1,a_0)\lt \infty.
```

If the character evaluations of the differential have uniformly bounded negative Laurent support modulo each $2^M$, the same holds for $f_x$.

*Proof.* Put the central integral complex in elementary-divisor bases over $\mathbb{Z}_2$ and lift those constant integral basis changes. Its positive pivot valuations sum to at most $h_1$. Formally cancel the same pivot positions upstairs, recording numerators and denominators in the rational basis changes and determinant comparison. There are at most $r_0$ operations. A product $P$ of bounded powers of pivot numerators clears all denominators. It is a polynomial of bounded degree in the differential entries, its augmentation belongs to $\Lambda$, and $v_2(P_0(0))$ is bounded in terms of $r_0,h_1$.

Where $P_x\ne0$, the remaining complex is one-by-one in degrees one and two. A nonzero differential forces the projected cycle to vanish, giving the stipulated zero coordinate. Otherwise the coordinate is the product of the projected class and functional with the canceled-pivot determinant factor. Thus

```math
u_x=2^{-a_0}\eta_xQ_x/P_x,\qquad Q\in\mathcal{O}[G].
```

Take $f=2^{a_0}P^2$ and $d=\eta P Q$. The equality holds also where $P_x=0$, since both sides are then zero. The central valuation and Laurent assertions follow because $f$ is a bounded-degree polynomial in the differential entries. No Laurent bound is required for $z,\lambda,\eta$, or $d$.

□

**Proposition D.23 (Uniform family clearing).** Under the hypotheses of Theorem D.2, the corrected universal coordinates satisfy Lemma D.22, with common central-valuation and fixed-precision negative Laurent bounds independent of $b$ and $\#Q$.

*Proof.* At augmentation the actual localization triangle has old complex equal to the base complex with only the auxiliary prime relaxed, and quotient the sum of singular complexes at the new split primes. Choose a finite free cone model for this triangle. Lemma D.19 lifts its graded filtration to the actual universal complex. Lemma D.20, with $h=4$, eliminates all new blocks at once. The remaining core has the bounded old size, its augmentation equals the old complex, and its sign constituents have uniform Laurent bounds. Its class and functional have the fixed clearing exponent of Lemma D.11.

The old central rational dimensions are one by the base Selmer corank. The quotient of the fixed base discrete Selmer group by its maximal divisible subgroup is finite, since its Pontryagin dual is finitely generated over $\mathbb{Z}_2$. Lemma D.16 bounds degree-two torsion by this fixed length; the scalar torsion bound handles the other degrees. The auxiliary terms are bounded by Lemma D.3. Thus total central torsion has a bound independent of the family, without finite base Shafarevich–Tate group.

Nonzero vertices have generic rank one by the simple-zero theorem; the zero vertex has rank at most one by Selmer corank. Generic invariants vanish, duality pairs degrees one and two, and unused local blocks are generically acyclic. The hypotheses of Lemma D.22 therefore hold. The determinant of the eliminated block is an $\mathcal{O}[G]$‑unit. Put its inverse and the correction $\eta$ from Lemma D.21 in the permitted numerator multiplier; neither enters $f$. The clearing lemma now proves both uniform bounds.

□

### D.8. Coefficient comparison and the missing vertex

**Lemma D.24 (Binary coefficient tests).** For $q$ specified Laurent coefficients of sign evaluations of elements of $\mathcal{O}[G]$, and $M\geq1$, there is a nonzero address agreeing with zero modulo $2^M$ on all tests whenever

```math
b\gt q(2^M-1).
```

*Proof.* Coefficient extraction gives $q$ elements of $\mathbb{Z}_2[G]$; it commutes with sign evaluation because $G$ is finite. For one of these elements the value function has a Boolean expansion

```math
a_\emptyset+\sum_{\emptyset\ne I\subseteq\{1,\ldots,b\}}
                 2^{\vert I\vert }a_I\prod_{i\in I}x_i,
       \qquad a_I\in\mathbb{Z}_2,
```

obtained by expanding products of $1-2x_i$. Its $j$th binary digit is a Boolean polynomial of degree at most $2^j$. Indeed, the digit is the coefficient of $Y^{2^j}$ in $(1+Y)^a$ modulo $2$; a monomial $x_I$ contributes the factor $1+x_I((1+Y)^{2^{\vert I\vert }a_I}-1)$. Its nonconstant terms start in $Y$‑degree $2^{\vert I\vert }$, and $\vert I\vert \leq2^{\vert I\vert }$. Thus all digit equalities for the $q$ tests have total degree at most $q(2^M-1)$. Their common-zero indicator is the product of $1+$ each equality polynomial. A Boolean polynomial of degree less than $b$ has even sum over $\mathbb{F}_2^b$, since every monomial omits a variable. Hence the number of common zeros is even. Zero is one, so another exists. This is the binary Chevalley–Warning argument used in OpenAI (2026).

□

**Lemma D.25 (Transfer through a bounded factor).** Suppose $f,d\in\mathcal{O}[G]$, $u_x\in\Lambda[1/2]$, and $f_xu_x=d_x$ for every character. Suppose $f_0\in\Lambda$ and $c=v_2(f_0(0))\lt \infty$. If every $f_x$ modulo $2^M$ has no powers below $-L(M)$, then for

```math
M\gt c,\qquad b\gt (L(M)+2)(2^M-1)
```

there is $x\ne0$ with

```math
v_2(u_x(0)-u_0(0))\geq M-2c.
```

*Proof.* Apply Lemma D.24 to the coefficients of $f_x$ in degrees $-L(M),\ldots,0$ and to the constant coefficient of $d_x$. At the resulting nonzero address all negative coefficients of $f_x$ are divisible by $2^M$, while its constant coefficient is congruent to $f_0(0)$ and has valuation $c$. Consequently $v_{\mathcal{O}}(f_x)\leq c$. Since $d_x$ is integral, $v_{\mathcal{O}}(u_x)\geq-c$, and the same holds for $u_0$. Their power-series coefficients therefore belong to $2^{-c}\mathbb{Z}_2$. They have no negative powers because they lie in $\Lambda[1/2]$.

The Laurent expansion of an element of $\mathcal{O}$ has coefficients tending $2$‑adically to zero in negative degrees, so the constant-term convolution converges and gives

```math
[t^0]d_x\equiv[t^0]f_x\,u_x(0)\pmod{2^{M-c}},\qquad
 [t^0]d_0=f_0(0)u_0(0).
```

Use the chosen coefficient congruences and divide by $f_0(0)$. This gives the claimed precision. Only one coefficient of $d$ was tested; its negative support need not be bounded.

□

*Proof of Theorem D.2.* The universal family is constructed before character evaluation, with the actual integral class and functional. Its primitive constituents belong to $\Lambda[1/2]$ by Propositions D.15 and D.18, and Lemma D.21 identifies them with the corrected universal coordinates, up to $\Lambda$‑units. The assumed nonzero-vertex bound and Proposition D.18 give

```math
v_2(u_x(0))\leq B_1\qquad(x\ne0)
```

for one constant depending only on the fixed data and $B$.

If the derivative of $L(E,s)L(E^{(k)},s)$ at one vanished, the Gross–Zagier formula for the conductor-one primitive Heegner sum would give height zero, hence a torsion point Gross and Zagier (1986). Proposition D.18 then gives $u_0(0)=0$, using only the base Selmer corank. By Proposition D.23 the clearing factors have a common bound $c_*$ for $v_2(f_0(0))$ and common bounds $L(M)$. Choose

```math
M\gt \max\{c_*,B_1+2c_*\}
```

and then a family whose dimension exceeds the threshold in Lemma D.25. It supplies a nonzero vertex with $v_2(u_x(0))\geq M-2c_*\gt B_1$, a contradiction. Thus the derivative is nonzero. The split Heegner functional-equation sign is negative, so the product has a simple zero.

□

## Appendix E. Coefficient systems and the comparison of Heegner sums

Throughout this section $E=F$ is the auxiliary curve. By Lemma A.1, it is non-CM, has full rational two-torsion, has functional sign $-1$, and satisfies

```math
v_2(N)=4,\qquad w_{16}(E)=-1,\qquad a_{19}(E)=0,\qquad 19\nmid N.
```

All varying primes are odd and of good reduction. Thus their weights are one and $w(h)=\omega(\vert h\vert )$. A fixed-support filter specifies a real sign, unit squareclasses at finitely many primes containing $2N$, and finitely many exclusions. Its parameters are squarefree and prime to its support. We use the normalized central value $L_*(h)$ and the notation $s(h)$ and $s_2(E^{(h)})$ established above.

The constructions below specialize the coefficient, graph, and assembly arguments of OpenAI (2026). We retain the ordinary coefficient symbols throughout.

### E.1. The two Heegner sums

Fix a modular parametrization $\phi:X_0(N)\longrightarrow E$ with $\phi(\infty)=O$. Let $h\gt 0$, $k\lt 0$, and $h_*\lt 0$ be pairwise coprime odd fundamental discriminants prime to $2N$. Assume that $k$ is a square at every prime of $2Nh$, that $h,h_*$ are squares at $2N$, and that the quadratic fields below have unit group $\{\pm1\}$. Let $R_h(k)$ be the unaveraged conductor‑$h$ ring-class character sum over $\mathbb{Q}(\sqrt{k})$ for the restriction of $\chi_h$. Let $P_h$ be the unaveraged conductor-one genus-character sum over $\mathbb{Q}(\sqrt{hh_*})$ for its genus character $\chi_{h_*}$. Both use $\phi$ and the absolute canonical height.

**Proposition E.1 (Exact height ratio).**

Suppose that $E^{(h)},E^{(hk)},E^{(h_*)}$ have respective analytic orders $1,0,0$ at $s=1$. Then

```math
\frac{\widehat h(R_h(k))}{\widehat h(P_h)}
 =\frac{\sqrt{\vert hk\vert }\,L(E^{(hk)},1)}
 {\sqrt{\vert h_*\vert }\,L(E^{(h_*)},1)}.
```

For the corresponding free-line index valuations,

**Equation (E.1).**

```math
2j_h(k)-2j(P_h)=v_2(L_*(hk))+O(1).
```

The constant is independent of the number and sizes of the primes of $h$ and $k$.

*Proof.* In the unaveraged normalization of Cai, Shu and Tian (2014, Theorem 1.1), the varying denominator is $c\sqrt{\vert D\vert }$, where $D$ is the quadratic field discriminant and $c$ the ring-class conductor. The additional factors are $2^{-\mu(N,D)}$ and the inverse square of $[\mathcal{O}_c^\times:\mathbb{Z}^\times]$. Here $(N,D)=1$ and the unit index is one in both applications. Both fields have degree two, so their conversion to absolute height also agrees. A common nonzero constant $C_\phi$ therefore gives

```math
L'(E^{(h)},1)L(E^{(hk)},1)
   =\frac{C_\phi}{h\sqrt{\vert k\vert }}\widehat h(R_h(k)),\qquad
 L'(E^{(h)},1)L(E^{(h_*)},1)
   =\frac{C_\phi}{\sqrt{\vert hh_*\vert }}\widehat h(P_h).
```

The first character has exact conductor $h$: every prime of $h$ splits in $\mathbb{Q}(\sqrt{k})$, and its quadratic character remains ramified on each split factor. The second is the unramified genus character. Artin formalism gives the two displayed factorizations. Division proves the height ratio.

The free components of both points belong to the rational $h$‑twist line; the other twist summands have rank zero by the forward theorem. Restriction and signed trace have composite multiplication by two over a quadratic extension and by four in the biquadratic realization. Thus comparison with the rational free lattice changes an index by a bounded integer. On a rank-one lattice the valuation of a height ratio is twice the index difference. The fixed nonzero factor $L_*(h_*)$ gives (E.1). There is no varying product of conductor-prime factors in this normalization.

□

### E.2. Even coefficients

Fix a root-number $+1$ filter $d=\sigma D$, where $\sigma\in\{\pm1\}$ and $D\gt 0$ is squarefree, and choose a nonvanishing seed $D_0$ by the fixed-local-type nonvanishing theorem. All compared indices have the same unit squareclasses as $D_0$ at the fixed support. For every application of the cyclotomic bounds to the original curve $E=F$, this filter is required to have $d$ a square at every prime of $2N$. The coefficient construction itself has the more general fixed-local-type scope stated below.

**Proposition E.2 (Even coefficient system).**

There is an algebraic holomorphic cusp form $g=\sum_{n\ge1}a(n)q^n$ of weight $3/2$, orthogonal to unary theta series, with fixed level and characters $\eta,\psi$ of $2$‑power order, such that $\psi/\eta=\chi_{-\sigma}$ and

**Equation (E.2).**

```math
a(p^2n)=
 \bigl(\eta(p)a_p(E)-\psi(p)(-n/p)\bigr)a(n)
       -p\eta(p)^2a(n/p^2)
```

outside the support. Its squarefree coefficients vanish off the filter. Normalize $a(D_0)=1$. For every admissible squarefree $D$ there are a $2$‑power root of unity $\zeta_D$ and $r_D\in\mathbb{Q}$ with

**Equation (E.3).**

```math
a(D)=\zeta_Dr_D,\qquad
 r_D^2=\frac{L_*(\sigma D)}{L_*(\sigma D_0)}.
```

Thus nonvanishing of the coefficient is equivalent to nonvanishing of the central value.

*Proof.* We use the even construction of OpenAI (2026), spelling out its scalar realization. Put $\rho=\pi_{E^{(\sigma)}}$ in unitary normalization. Nonvanishing of $L(\rho\otimes\chi_{D_0},1/2)$ implies that the global metaplectic space $T_{D_0}(\rho)$ and its $D_0$ Fourier functional are nonzero; these implications are recorded in the proof of Waldspurger (1981, Proposition 18, p. 467). Its finite normalized central signs are

```math
\omega_p=\chi_{D_0,p}(-1)
       \epsilon(\rho_p\otimes\chi_{D_0,p},1/2)
```

by Waldspurger (1981, Assertion 10, p. 397). Choose $2$‑primary unit characters $\psi_p$ with $\psi_p(-1)=\omega_p\chi_{-1,p}(-1)$. At good primes outside $2N$ this value is one, including primes of $D_0$: the two unramified characters of $\rho_p$ have product one and their quadratic epsilon-factor product is $\chi_{D_0,p}(-1)$. At infinity the weight-two epsilon factor is $-1$. The global sign of the nonvanishing twist is $+1$, so the product of the prescribed finite values of $\psi_p(-1)$ is one. The Chinese remainder theorem gives an even Dirichlet character $\psi$ of $2$‑power order supported on $2N$ with these values. Set

```math
\chi_0=\psi\chi_{-1},\qquad \eta=\psi\chi_{-\sigma}.
```

Then $\pi_{E\otimes\eta}\otimes\chi_0^{-1}=\rho$ and $\chi_{0,p}(-1)=\omega_p$.

At an exceptional finite prime use the Kirillov model in Waldspurger (1981, Assertion 7, p. 396), with character $\mu_p=\chi_{0,p}$. The $D_0$ squareclass belongs to its Whittaker support, so its Schwartz subspace contains

```math
t_p=\mathbf{1}_{D_0(\mathbb{Z}_p^\times)^2}.
```

This vector is nonzero at $D_0$, has integral support, and is invariant under unit-square multiplication of its argument. The Kirillov action therefore gives the required normalized diagonal character $\gamma_p(u)\chi_{0,p}(u)^{-1}$ for every unit $u$. Integral upper unipotents fix it, and smoothness gives invariance under sufficiently deep lower unipotents. Elsewhere choose spherical vectors, whose squarefree local coefficients at valuations zero and one are both one. The positive index $D_0$ selects the holomorphic weight‑$3/2$ component at infinity. The scalar-realization criterion in Waldspurger (1981, Theorem 2(1), p. 458, and Lemma 41, p. 476) now gives a classical vector with nonzero $D_0$ coefficient.

Impose coprimality and unit-squareclass coefficient sieves at the fixed support. They retain $D_0$ and commute with good $T(p^2)$, since an index and its multiple or quotient by $p^2$ satisfy the same conditions. The classical good-Hecke formula Shimura (1973) has eigenvalues $\eta(p)a_p(E)$, giving (E.2) and excluding unary constituents. The algebraic $q$‑expansion model of the half-integral-weight space Ramsey (2006, Sections 3–4) and these algebraic linear conditions permit an algebraic vector with nonzero $D_0$ coefficient. Only extension of characteristic-zero fields is used here; no integral base-change assertion at two is required. Its level and denominators are fixed.

Let $V$ be the entire cusp space at this level and character with these good eigenvalues. Its existence verifies (H1) of Waldspurger (1981, Proposition 2). For every $f\in V$, Waldspurger (1981, Corollary 2, pp. 483–484) gives

**Equation (E.4).**

```math
a_f(D)^2=
 \psi(D/D_0)\frac{L_*(\sigma D)}{L_*(\sigma D_0)}a_f(D_0)^2.
```

Its real factor is $\sqrt{D/D_0}$, already incorporated in $L_*$. Bad local factors agree, and the good squarefree factors at valuations zero and one are both one. The final paragraph of that corollary removes (H2) for indices in the same squareclass at two. The two coefficient functionals are proportional on all of $V$: their squared relation factors into two linear forms in the polynomial ring on $V$, which is a domain. One factor vanishes identically. This includes oldvectors and their linear combinations.

Put $\xi=a(D)/a(D_0)$. Let an algebraic automorphism $u$ act on the $2$‑power character roots by an odd exponent $e$, and set $ν=\eta^{(e-1)/2}$. At a common level supported on the same primes, $g^u$ and $g\otimesν$ have the same character $\psi^e=\psiν^2$ and the same good eigenvalues $\eta(p)^ea_p(E)$. The full-space proportionality gives

```math
u(\xi)=ν(D/D_0)\xi.
```

Choose unit square roots of $D/D_0$ at the conductor of $\eta$ and let $\zeta_D$ be their value under $\eta$. Then $\zeta_D^2=\eta(D/D_0)$, $u(\zeta_D)=\zeta_D^e$, and $ν(D/D_0)=\zeta_D^{e-1}$. Thus $\xi/\zeta_D\in\mathbb{Q}$. Different choices change it by at most a sign. Since $\psi/\eta$ is quadratic and the ratio is locally square, division of (E.4) by $\zeta_D^2$ proves the assertion.

□

On a filter of parameters locally square at $2N$, the cyclotomic lower bound, Theorem C.1, gives

**Equation (E.5).**

```math
v_2(a(D))\ge\omega(D)+\tfrac12s(\sigma D)-C_g
              \ge\omega(D)-C_g
```

at nonzero coefficients. Phase removal makes their finite normalized valuations integers, so a least normalized depth is attained.

### E.3. An integral Kummer detector

Fix an odd negative fundamental discriminant $h_*\lt -4$, square at $2N$, with $L(E^{(h_*)},1)\ne0$. Let $S_0$ contain the primes of $2Nh_*$ and every other fixed prime needed for the intrinsic coefficient tests. At every finite prime of $S_0$ choose the square unit class, and require positive parameters. This is the prepared positive filter; in particular, it contains the parameter $1$. Choose a positive simple-zero witness $D_w$ on this final filter by Proposition B.2. The choices of $h_*$ and $D_w$ are supplied by the classical nonvanishing results. The genus Gross–Zagier formula makes $P_{D_w}$ nontorsion.

A single integer $L\gt 0$ kills torsion in all biquadratic fields containing the genus sums and the cuspidal constants in the Atkin–Lehner formulas for $\phi$. For the torsion assertion choose two distinct good primes $p,q$, and put

```math
C_p=\prod_{f=1}^4\#E(\mathbb{F}_{p^f}),\qquad
 C_q=\prod_{f=1}^4\#E(\mathbb{F}_{q^f}).
```

Over a field of degree at most four, prime-to‑$p$ torsion injects into a reduction of residue degree at most four and is killed by $C_p$; its $p$‑primary torsion is killed by $C_q$. Thus $C_pC_q$ is a uniform annihilator. After multiplication by $L$, each genus point has the exact Galois transformation rule of the $D$‑twist and defines a rational point on $E^{(D)}$ under the twisting isomorphism.

Let $T=T_2E$, let $C$ be complex conjugation on $T$, and choose a primitive integral row $b:T\to\mathbb{Z}_2$ with $bC=b$. It is obtained from a rational invariant row by clearing denominators and dividing its content. No integral eigenspace decomposition is used.

**Lemma E.3 (Translation lattice).**

Let $A/\mathbb{Q}$ be non-CM and $Q\in A(\mathbb{Q})$ nontorsion. For a compatible division tower let $c_Q:G_{\mathbb{Q}}\to T_2A$ be its Kummer cocycle. On $H=\ker\rho_{T_2A}$ its image contains $2^aT_2A$ for some $a$. This remains true after intersecting $H$ with the kernel of any fixed finite Galois data.

*Proof.* On $H$ the cocycle is a homomorphism with compact image, hence a closed $\mathbb{Z}_2$‑submodule. Moreover $c_Q(ghg^{-1})=\rho(g)c_Q(h)$. The non-CM open-image theorem makes the rational Tate representation irreducible and supplies a scalar $u\ne1$ in its image. If $c_Q(H)=0$, the rational Kummer class factors through the Tate image. Comparison at $ug$ and $gu$ gives $(u-1)c(g)=(\rho(g)-1)c(u)$, making it a rational coboundary. This contradicts Kummer injectivity for the nontorsion point $Q$. Its nonzero rational span is therefore all of $V_2A$, so the closed image contains a full lattice. A finite-index subgroup of $H$ has translation image of finite index, proving the last assertion.

□

**Proposition E.4 (Finite-field detection).**

For arbitrarily large $M$ there are fresh good primes $ℓ$ with

```math
\rho_T(\mathrm{Fr}_ℓ)\equiv C\pmod{2^M},\qquad
 (D_w/ℓ)=1,\qquad(h_*/ℓ)=-1,
```

and integral Frobenius-invariant homomorphisms

```math
\lambda_M:E(\mathbb{F}_{ℓ^2})\longrightarrow\mathbb{Z}/2^M\mathbb{Z}
```

for which $\lambda_M(\mathrm{red}_ℓ(LP_{D_w}))$ has one fixed finite valuation. The primes may avoid any prescribed finite set.

*Proof.* Apply Lemma E.3 to $A=E^{(D_w)}$ and the rational point corresponding to $LP_{D_w}$. Since $D_w\gt 0$, conjugation acts by $C$ on its Tate module. Intersect the Tate kernel with the kernels of the fixed quadratic data. Choose $v$ in its translation image with $b(v)=2^a$, and $h$ in this kernel with $c_Q(h)=v$. For actual conjugation $\tau$ put $g=\tau h$. The relation $\tau^2=1$ gives $(1+C)c_Q(\tau)=0$, and hence

```math
c_Q(g^2)=(1+C)v,\qquad b(c_Q(g^2))=2^{a+1}.
```

The element $g$ fixes $\sqrt{D_w}$ and negates $\sqrt{h_*}$. For $M\gt a+1$ take the finite Galois quotient recording $2^M$‑torsion, $2^M$‑division of the point, and these characters. Chebotarev realizes its conjugacy class at infinitely many good primes; choose a place realizing the specified representative.

Lang’s theorem and finite-field Kummer theory give

```math
E(\mathbb{F}_{ℓ^2})/2^ME(\mathbb{F}_{ℓ^2})
 \simeq H^1(\mathbb{F}_{ℓ^2},E[2^M])
 \simeq T/(2^MT+(\mathrm{Fr}_ℓ^2-1)T)=T/2^MT.
```

This is evaluation at arithmetic Frobenius squared. Composition with $b$ defines $\lambda_M$; it is Frobenius-invariant because $bC=b$ and $\mathrm{Fr}_ℓ\equiv C$. Splitting of $D_w$ at $ℓ$ identifies the twisting isomorphism and the prescribed reduction of the division cocycle. Finally the Weil pairing gives $ℓ\equiv\det C=-1\pmod{2^M}$, so $ℓ\equiv3\pmod4$ when $M\ge2$. Choosing successively and excluding the previously chosen primes gives a detector sequence $(ℓ_M)$ with pairwise distinct entries.

□

### E.4. The integral theta bridge

For positive squarefree admissible $D$ put $K_D=\mathbb{Q}(\sqrt{Dh_*})$ and fix one Heegner orientation at each level prime. The unaveraged genus sum is

```math
P_D=\sum_{[\mathfrak{a}]\in\mathrm{Pic}(\mathcal{O}_{K_D})}
       \chi_{h_*}(N\mathfrak{a})\,\phi(x_D^{[\mathfrak{a}]}).
```

The support includes the primes of $h_*$, so they cannot cancel and $\mathcal{O}_{K_D}^\times=\{\pm1\}$.

**Proposition E.5 (Integral theta bridge).**

Let $ℓ\nmid2Nh_*$ be good, $ℓ\equiv3\pmod4$, and $(h_*/ℓ)=-1$. Let $\lambda:E(\mathbb{F}_{ℓ^2})\to\mathbb{Z}/2^M\mathbb{Z}$ be an integral Frobenius-invariant homomorphism. There is a holomorphic weight‑$3/2$ form $g_M=\sum_{n\ge1}a_M(n)q^n$ with integral coefficients in one fixed $2$‑power cyclotomic ring such that

**Equation (E.6).**

```math
a_M(D)\equiv c_0\,2^{\omega(N)}\zeta_M(D)
     \lambda(\mathrm{red}_ℓ(LP_D))\pmod{2^M}
```

at admissible squarefree $D$ with $(D/ℓ)=1$. Here $c_0\gt 0$ is independent of $D,M,ℓ$ and $\zeta_M(D)$ is a $2$‑power root of unity. Coefficients vanish off the support filter and unless $(D/ℓ)=1$. The level is supported on the fixed primes and $ℓ$; its good-prime recurrence is (E.2) modulo $2^M$, with $\psi/\eta=\chi_{-4}$.

*Proof.* We give the theta construction of OpenAI (2026) in the present local type. Its geometric input is the equivariant CM-reduction correspondence of Cornut and Jetchev (2013, Sections 3.2 and 4.9–4.10, Corollary 4.1), valid for arbitrary level prime to $ℓ$.

Let $B/\mathbb{Q}$ be ramified at $ℓ$ and infinity, $R$ an Eichler order of level $N$, and

```math
V=B^0,\quad Q(x)=-x^2,\quad
 X=B^\times\backslash\widehat B^\times/\widehat R^\times.
```

The set $X$ parametrizes supersingular pairs with cyclic level subgroup; all are defined over $\mathbb{F}_{ℓ^2}$. Choose arbitrary integer lifts of $P(z)=\lambda(L\phi_ℓ(z))$. Modulo $2^M$ this is a Brandt eigenfunction of eigenvalue $a_p(E)$ at $p\nmid Nℓ$: Hecke correspondences commute with the elliptic quotient and reduction, and the normalization at infinity removes the Hecke constant. Multiplication by $L$ removes the Atkin–Lehner cuspidal constants, so the operator at $p^e\Vert N$ acts by $w_{p^e}$. An $ℓ$‑uniformizer acts by $+1$, since it induces residue Frobenius.

Construct $f=\prod_pf_p$ on $\widehat V$ as follows. Away from $2Nh_*ℓ$ take $\mathbf{1}_{R_p^0}$. Impose extra fixed squareclass and coprimality conditions on $Q(x)$; they are conjugation-invariant and stable under unit-square scaling of the norm.

At $p^e\Vert N$, require an embedding of the split maximal quadratic algebra with $x^2$ a unit square. The cyclic level quotient selects one of its integral summands. Give the eigenvalue $r$ of $x$ there weight $\alpha_p(r)$, with $\alpha_p$ of $2$‑power order and

```math
\alpha_p(-1)=w_{p^e}\chi_{h_*}(p)^e=w_{p^e}.
```

At odd $p$, a character of the $2$‑primary quotient of $\mathbb{F}_p^\times$ realizes either sign at $-1$. At two use

```math
R_2=\left\{\begin{pmatrix}a&b\\ c&d\end{pmatrix}:
 a,b,d\in\mathbb{Z}_2,\ c\in16\mathbb{Z}_2\right\},
```

impose $(1+x)/2\in R_2$, and take $\alpha_2=\chi_{-4}$. If $r^2=x^2$, the eigenvalues of $(1+x)/2$ differ by the unit $r$. Its idempotent summands are therefore distinct even modulo two. For odd $u$ the identity $(1+ux)/2=u(1+x)/2+(1-u)/2$ leaves the selected summand unchanged and replaces $r$ by $ur$. This proves the required unit-scaling rule.

At $p\mid h_*$ require $x\in M_2(\mathbb{Z}_p)^0$ and $v_p(Q(x))=1$. Its reduction is a nonzero nilpotent. With $X_0=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$ put

```math
\epsilon_p(gX_0g^{-1})=(\det g/p).
```

The centralizer has square determinant, making this well-defined, and

```math
\epsilon_p(uyu^{-1})=(\det u/p)\epsilon_p(y),\qquad
 \epsilon_p(ay)=(a/p)\epsilon_p(y).
```

Use $\epsilon_p(\bar x)$ as the weight. At $ℓ$, the maximal-order residue field is $\mathbb{F}_{ℓ^2}$. Choose a nonzero basis $\beta$ of its trace-zero line and set $f_ℓ(x)=(t/ℓ)$ if $\bar x=t\beta\ne0$, and zero otherwise. Order units conjugate trivially on the residue field; a uniformizer sends $\beta$ to $-\beta$ and changes the weight by $-1$. Both $\beta^2$ and $-1$ are nonsquares, so $Q(x)=-t^2\beta^2$ is a unit square. Since $(\vert h_*\vert /ℓ)=1$, the index $\vert h_*\vert D$ forces $(D/ℓ)=1$.

This compactly supported locally constant function satisfies

**Equation (E.7).**

```math
f(u^{-1}xu)=\chi_{h_*}(\mathrm{Nrd}u)^{-1}f(x)
 \quad(u\in\widehat R^\times).
```

Its total unit-scaling character is even: the level contribution at $-1$ is $\prod w_{p^e}=+1$, whereas the $h_*$ and $ℓ$ contributions are both $-1$. Its values belong to one fixed $2$‑power cyclotomic field, since the moving character at $ℓ$ is quadratic.

Scalar modularity can be checked from the Weil operators. For an additive character of conductor $\mathbb{Z}_p$ these are

```math
\omega(n(b))f_p(x)=e_p(bQ(x))f_p(x),\quad
 \omega(m(u))f_p(x)=\gamma_p(u)\vert u\vert _p^{3/2}f_p(ux),\quad
 \omega(w)f_p=\gamma_p\widehat f_p.
```

Integral upper unipotents fix $f_p$ because $Q$ is integral on its support. If $f_p$ is translation-invariant by $L'_p$, its Fourier transform is supported on $(L'_p)^\vee$. Choose $A_p$ with $p^{A_p}Q((L'_p)^\vee)\subset\mathbb{Z}_p$; Fourier conjugation gives deep lower-unipotent invariance. Relative to the ordinary theta multiplier cubed, the diagonal factor is $(\det Q,u)_p$. The presentation $B=(-a,-b)$ gives $Q=aX^2+bY^2+abZ^2$ with square determinant $(ab)^2$. Thus only the computed unit-scaling character remains. For a matrix with unit upper-left entry,

```math
\begin{pmatrix}a&b\\ c&d\end{pmatrix}=n_-(c/a)m(a)n(b/a).
```

This proves scalar transformation under a sufficiently deep $\Gamma_0(p^{A_p})$; at two include the metaplectic splitting depth. Denote the classical character by $\eta_B$. In the inverse finite adelic action the diagonal entry is the classical lower-right entry $d$, fixing the convention $\eta_B(d)$. The real Gaussian gives weight $3/2$. Positive definiteness gives nonnegative exponents at every cusp, also after finite Weil transforms.

Choose $c_0$ divisible by all possible orders $\vert R_z^\times\vert $, uniformly in $ℓ$. These finite groups act faithfully on the rank-four integral lattice $R_z$, so the finite-subgroup bound for $\mathrm{GL}_4(\mathbb{Z})$ supplies such an integer. Define

```math
H_M(n)=c_0\sum_{z\in X}
 \frac{P(z)\chi_{h_*}(\mathrm{Nrd}z)}{\vert R_z^\times\vert }
 \sum_{\substack{x\in B^0\\ Q(x)=n}}f(z^{-1}xz).
```

Equation (E.7) proves independence of right representatives. The norm character is trivial on positive rational norms, giving independence of left representatives. The Weil calculation proves modularity. Every $c_0/\vert R_z^\times\vert $ is integral, so the coefficients are integral and changing a lift of $P$ by $2^M$ changes them by multiples of $2^M$.

At good $p$, Brandt neighbors are the lines in $\mathbb{F}_p^2$. A nonzero nilpotent has one invariant line; a nonzero semisimple trace-zero matrix of norm $n$ has $1+(-n/p)$ invariant lines; zero reduction contributes $p$ extra lines. If a primitive $y$ has $p^2\mid Q(y)$, put its reduction in the form $X_0$. Its diagonal entry is divisible by $p$, its upper-right entry is a unit, and the norm condition makes its lower-left entry divisible by $p^2$. Exactly the neighbor of its invariant line makes $y/p$ integral. These cases, with the stabilizer weights, give

```math
\begin{aligned}
 H_M(p^2n)&+\eta_B(p)(-n/p)H_M(n)
             +p\eta_B(p)^2H_M(n/p^2)\\
 &\equiv\eta_B(p)\chi_{h_*}(p)a_p(E)H_M(n)\pmod{2^M}.
\end{aligned}
```

Here $\eta_B(p)$ comes from unit scaling at the other places and $\chi_{h_*}(p)$ from the reduced norm of a neighbor.

At $n=\vert h_*\vert D$, representations are exactly optimal embeddings $\mathcal{O}_{K_D}\hookrightarrow R_z$ sending $\sqrt{Dh_*}$ to $x$. The condition at two is integrality of $(1+\sqrt{Dh_*})/2$; fundamental discriminant implies optimality. There are two orientations at each level prime, two at $ℓ$, and one local orbit elsewhere. For a fixed tuple, embedding orbits are parametrized by $\mathrm{Pic}(\mathcal{O}_{K_D})$. Replacing $z_0$ by $az_0$ with $a\in\widehat K_D^\times$ leaves $z_0^{-1}xz_0$ unchanged, and its relative norm character is $\chi_{h_*}(N_{K_D/\mathbb{Q}}a)$. The equivariant reduction correspondence identifies these projected pairs with reductions of the CM class orbit.

An embedding stabilizer is $\{\pm1\}$, so an orbit contributes $c_0/2$ times the unaveraged genus sum. Reversing a level orientation changes the Schwartz weight and the norm-weighted parametrization by the same sign $w_{p^e}\chi_{h_*}(p)^e$; reversing the $ℓ$‑orientation changes both by $-1$. All $2^{\omega(N)+1}$ tuples consequently contribute equally, with one initial root-of-unity factor. The conjugate-pair formulation of the reduction correspondence keeps the factor two at $ℓ$, which cancels the stabilizer denominator. This gives

```math
H_M(\vert h_*\vert D)\equiv c_0\,2^{\omega(N)}\zeta_M(D)
       \lambda(\mathrm{red}_ℓ(LP_D))\pmod{2^M}.
```

Finally put $a_M(n)=H_M(\vert h_*\vert n)$. The operator $U_{\vert h_*\vert }$ preserves modularity and changes the character to $\psi=\eta_B(\vert h_*\vert /\,\cdot\,)$. The recurrence has $\eta=\eta_B\chi_{h_*}$, hence $\psi/\eta=\chi_{-4}$. Every normalization factor is independent of the number of varying primes.

□

## Appendix F. Integral coefficient calculus

We specialize the ordinary coefficient calculus of OpenAI (2026). Let $\mathcal{R}$ be the ring of integers of a finite extension of $\mathbb{Q}_2$ containing the coefficient and character fields, with maximal ideal $\mathfrak{m}$. Divisibility by the integer two means divisibility by $2\mathcal{R}$, which can be strictly smaller than $\mathfrak{m}$. Every division below is justified before reduction.

We treat an even source $g$ and an odd finite-precision source $g_M$ simultaneously. Their recurrence is (E.2), exact in the even case and modulo $2^M$ in the odd case. The characters have $2$‑power order and $\psi/\eta$ is quadratic. Phase-removed squarefree coefficients are rational in the even case and integers modulo $2^M$ in the odd case. Suppose that

**Equation (F.1).**

```math
\begin{aligned}
 v_2(a(D))&\ge\omega(D)-C,\\
 v_2(a_M(D))&\ge\min\{M,\omega(D)-C\}
 \end{aligned}
```

for all admissible squarefree indices, and that the odd sources have a fixed bounded-weight witness with coefficient valuation bounded along a cofinal sequence of precisions. The even premise is (E.5); the odd premise will be proved in Proposition H.3 before the odd calculus is applied. Restrict to the witness sequence and fix a nonprincipal ultrafilter on it. At odd stage $M$, the support is $S_0\cup\{ℓ_M\}$.

**Lemma F.1 (Uniform normalized minimum).**

In the even case $\delta=\min_D(v_2(a(D))-\omega(D))$ is an attained integer. In the odd case there is an attained integer $\delta$ among visible bounded-weight sequences. For every fixed $W$, on an ultrafilter-large set of stages,

```math
v_2(a_M(D))\ge\delta+\omega(D)
 \quad\text{simultaneously for all }\omega(D)\le W.
```

A bounded-weight witness attains equality on an ultrafilter-large set. The integer $\delta$ and this witness weight are fixed before any graph size or cube dimension is chosen.

*Proof.* The coarse bounds give a uniform integer lower bound; a nonzero witness gives a finite upper bound. The minimum of the resulting nonempty set of integers is attained. In the odd case, restrict to values no larger than the fixed witness value; only finitely many integers can occur, so the ultrafilter selects one. If the asserted uniform inequality failed for a fixed $W$ on an ultrafilter-large set, choose a violating $D_M$ at each such stage. This is a bounded-weight sequence with strictly smaller normalized depth. Invisible coefficients cause no exception once $M\gt \delta+W$.

□

For a finite set $U$ of variable primes put

```math
B_U=2^{-\delta-\vert U\vert }\prod_{p\in U}(U_p-\eta(p)V_p)g,
 \qquad U_pf[n]=f[pn],\quad V_pf[n]=f[n/p].
```

Use $g_M$ in the odd case, at sufficient precision for these divisions. The same $\delta$ is used when a prime is omitted from $U$.

**Lemma F.2 (Integral square shells).**

Write $n=Jrm^2$, where $J\subseteq U$ denotes also its squarefree product, and $r$ is squarefree and coprime to $U$. Every coefficient of $B_U$ is integral and

```math
v_2(B_U[Jrm^2])\ge\omega(r)
```

in the even case. For the odd sources, given $W,R$, one sufficiently late actual stage gives integrality and this bound truncated at $R$ for every $\vert U\vert \le W$ and every Fourier index.

*Proof.* Indices meeting the fixed support vanish by the sieves. At the others, the underlying squarefree index is $D=(U/J)r$. After extracting $\eta(p)^s$, the shell recurrence is

```math
b_0=1,\quad b_1=a_p-\kappa,\quad
 b_{s+1}=a_pb_s-pb_{s-1},\qquad
 \kappa=(\psi/\eta)(p)(-D/p).
```

For $p\mid D$ one has $\kappa=0$; otherwise $\kappa=\pm1$. At $p\in U/J$ the operator gives $b_s-b_{s-1}$ with $b_{-1}=0$, which is odd because $a_p$ is even. At $p\in J$ it gives $b_{s+1}-b_s$, which is even. The complete phase is $\eta(Jm)$ times the squarefree phase of $a(D)$. The squarefree bound and the $\vert J\vert $ even differences give

```math
\delta+\omega((U/J)r)+\vert J\vert -\delta-\vert U\vert =\omega(r).
```

All remaining recurrence multipliers are integral.

For odd stages, first use Lemma F.1 below a fixed squarefree-weight threshold. Above it, the coarse bound $\min(M,\omega(D)-C)$ pays the largest normalizing exponent $\max_{\vert U\vert \le W}(\delta+\vert U\vert )$ and the requested precision $R$. Choose the threshold accordingly, then choose $M$ larger than these fixed quantities. Recurrence errors remain divisible by $2^M$ before normalization at every square shell: only integral multipliers occur. This argument is simultaneous in all indices and all prime choices with bounded $\vert U\vert $.

□

Since $E[2]$ is rational, $a_p\equiv p+1\pmod4$. For $\kappa=\pm1$ put $\Delta_s=b_{s+1}-b_s$. The same recurrence and $\Delta_1-\Delta_0\equiv(p-1)(p-\kappa)\equiv0\pmod4$ give

**Equation (F.2).**

```math
\Delta_s/2\equiv(a_p-\kappa-1)/2\pmod2\quad(s\ge0).
```

Choose $i\in\{0,1\}$ so that $\eta\chi_{-4}^i$ is odd, and define

```math
\Theta_J=\sum_{\substack{m\gt 0\\(m,S)=1}}
       \eta(m)\chi_{-4}(m)^i m q^{Jm^2},\qquad
 H_U=\frac12\left(B_U-\sum_{J\subseteq U}B_U[J]\Theta_J\right).
```

The unary character is $\chi_J=\eta\chi_{-4}^i(-J/\,\cdot\,)$; the non-unary character is $\psi_U=\psi\prod_{p\in U}(p/\,\cdot\,)$. Each new prime occurs in the level to exponent at most one. Indeed, if the old level is $L$ and $p\nmid L$, conjugating $\gamma\in\Gamma_0(Lp)$ by $\mathrm{diag}(p,1)$ gives $\left(\begin{smallmatrix}a&pb\\ c/p&d\end{smallmatrix}\right) \in\Gamma_0(L)$. The quotient of theta multipliers is $(p/d)$, unchanged by cubing. Thus $V_p$ raises the level by $p$ with that quadratic character. On the raised level $U_{p^2}$ preserves the level and character, and coefficientwise $U_p=U_{p^2}V_p$. Unary dilation has the same new-prime exponent; the sieves affect only fixed support.

**Lemma F.3 (Integer unary division).**

The form $H_U$ is integral, with the same uniform finite-precision interpretation as Lemma F.2. For a fresh prime $q$ its reduced coefficient is the binary symbol

```math
A(Uq)=\left(2^{-\delta-\vert U\vert -1}a(Uq)
                    \text{ with phase removed}\right)\bmod2.
```

*Proof.* If $r\ne1$, Lemma F.2 makes the coefficient even. For $r=1$, (F.2) shows, after extracting the common phase, that $B_U[Jm^2]\equiv B_U[J]\eta(m)\pmod{2\mathcal{R}}$. Differences at $U/J$ are odd; the divided differences at $J$ have the same parity as on the first shell; the other square-shell multipliers are odd. As $m\chi_{-4}(m)^i$ is odd, this is precisely the unary coefficient. Different $J$ have disjoint squarefree supports. Thus the division is by $2\mathcal{R}$ itself. At a fresh $q$ no unary term contributes. The residue is in $\mathbb{F}_2$ because phase-removed coefficients are integral and $2$‑power roots of unity reduce to one.

□

### F.1. Traces and whole-prime omission

Put $\theta=1+2\sum_{n\gt 0}q^{n^2}$; multiplication by $\theta$ gives weight two and preserves reduced coefficients. Work in the finite-dimensional sum of the characteristic-zero good Hecke eigensystems of $\theta H_U$, its unary terms, and their diamond translates, retaining all old multiplicity spaces. Use the two-dimensional modular Galois representations Deligne (1971) on cusp systems and the two character summands on Eisenstein systems. Their commuting scalar trace and determinant operators are $t(g),d(g)$.

**Lemma F.4 (Integral trace orbit).**

The module generated by $\theta H_U$, the undivided $\theta B_U[J]\Theta_J$, and their good-Hecke and diamond translates is an integral Fourier lattice stable under $t(g),d(g)$. On its reduced trace orbit of $\theta H_U$,

```math
d(g)t(h)=t(h),\qquad
 t(g)t(h)=t(gh)+t(gh^{-1}),\qquad t(1)=0.
```

Every finite trace product is testable by distinct fresh primes avoiding any prescribed Fourier index and finite exclusion set. Moreover

```math
t(g)t(h)\theta H_U=0,\qquad
 t(gu^2)\theta H_U=t(g)\theta H_U
```

after reduction. Thus trace tests factor through the maximal elementary quadratic extension unramified outside $S\cup U$.

*Proof.* The diamond denominator is removed by

```math
\langle u\rangle H_U=\psi_U(u)H_U+
 \frac12\sum_JB_U[J](\psi_U(u)-\chi_J(u))\Theta_J.
```

Each character ratio is quadratic; its difference is zero or twice a unit. All generators are integral, and good Hecke operators preserve integrality. Finitely many Fourier coefficients inject the ambient space into a finite-dimensional coefficient space. After enlarging $\mathcal{R}$ for its finitely many eigensystems, the module embeds in $\mathcal{R}^r$, so it is finitely generated and closed. Simultaneous Chebotarev approximation in those Galois systems approximates $t(g),d(g)$ by $T_q,q\langle q\rangle$ to arbitrary precision. Closedness proves preservation of the lattice. At a coefficient index prime to $q$, the second term of the weight-two Hecke formula vanishes. Iteration with distinct fresh primes gives the trace-testing assertion.

In the determinant formula the first diamond term is scalar and reduces to one. The other terms are integral unary corrections, still unary after multiplication by $\theta$ and reduction. A fresh trace tests them at an index with a new squarefree prime factor and kills them, also after further fresh tests. Hence $d(g)t(h)=t(h)$ on the reduced tested orbit. The matrix identity $\mathrm{tr}(A)\mathrm{tr}(B) =\mathrm{tr}(AB)+\det(B)\mathrm{tr}(AB^{-1})$ then gives the trace identity, and $t(1)=2$ before reduction.

Two fresh traces add two new squarefree primes to an index. Lemma F.2 supplies two factors of two in $B_U$, so one remains after unary division. Chebotarev turns this into $t(g)t(h)\theta H_U=0$ for arbitrary $g,h$. Apply the trace identity to $t(gu)t(u)$ to get invariance under $u^2$. The normal subgroup generated by squares has elementary abelian quotient, giving the asserted factorization. This is factorization of the tested reduced orbit, not of the original Galois representations.

□

Write $U_p^{(2)}$ for the weight-two coefficient operator at a raised prime. Choose tame inertia $\tau_p$ with new quadratic character $-1$ and an arithmetic Frobenius lift $\varphi_p$.

**Lemma F.5 (Exact local trace identity).**

On the characteristic-zero ambient systems,

```math
U_p^{(2)}\{t(g\tau_p\varphi_p)-t(g\varphi_p)\}
 =d(\varphi_p)\{t(g\tau_p)-t(g)\}.
```

It commutes with all further good traces.

*Proof.* An old constituent omitting $p$ has trivial inertia, so both differences vanish, including on its old multiplicity space. Every other constituent has conductor exponent one and primitive ramified quadratic determinant at $p$. Indeed the non-unary term has this character, as does $\Theta_J$ if $p\mid J$; if $p\nmid J$ the unary term already omits $p$. The conductor formula therefore gives a principal series with one unramified and one ramified character. A Steinberg constituent with unramified determinant cannot occur. Local modular compatibility Carayol (1986, Theorem A), in the arithmetic-Frobenius convention, identifies $U_p^{(2)}$ with the unramified Frobenius eigenvalue $\lambda$. Write $\rho(\tau_p)=\mathrm{diag}(1,-1)$ and $\rho(\varphi_p)=\mathrm{diag}(\lambda,\mu)$. If $z$ is the lower-right entry of $\rho(g)$, the differences are $-2z\mu$ and $-2z$, so both sides are $-2z\lambda\mu$. An Eisenstein constituent is the same two-character calculation. These exhaust the constituents, and scalar good traces commute with the level operator on the retained old multiplicities.

□

**Proposition F.6 (Ordinary symbol interface).**

Let $V=U\setminus\{p\}$. Changing one ramification bit at $p$ in the Frobenius label of a fresh $q$ changes $A(Uq)$ by $A(Vq')$, where the retained label of $q'$ is the product of the labels of $q,p$. The replacement source is $H_V$, with the same $g,\eta,\psi,\delta$; its entire ramification support omits the rational prime $p$. A vertex with trivial label at the support and at the other vertices has symbol zero.

*Proof.* Apply Lemma F.5 at coefficient one and reduce using Lemma F.4. Replace its trace arguments by fresh primes. The first-shell formula, including the normalizing powers, is

```math
H_U[pq']\equiv\eta(p)c_p(D')H_V[q']\pmod{\mathfrak{m}},
 \qquad D'=Vq',
```



```math
c_p(D')=\frac{a_p-(\psi/\eta)(p)(-D'/p)-1}{2}\pmod2.
```

The factor $1/2$ is the ratio of normalizations; the numerator is the even first-shell difference. The phase reduces to one. Choose $q'_0,q'_1$ with trace data $g\varphi_p,g\tau_p\varphi_p$. The source $H_V$ is unramified at $p$, so these restrictions give the same omitted-source symbol. Their Legendre terms at $p$ have opposite signs because the character of $p^*=(-1/p)p$ is ramified at $p$ and takes value $-1$ on $\tau_p$. The two values of $c_p$ therefore differ by one. Their shell difference is precisely $A(Vq')$. On the omitted source $\varphi_p$ is ordinary unramified Frobenius, which gives the product label. The trivial-label assertion follows from $t(1)=0$.

□

### F.2. Finite-stage stabilization and unit bounds

The odd assertions above hold simultaneously for every $\vert U\vert $ below a fixed bound. A finite graph with specified support labels and mutual quadratic residue bits determines its symbol: hold all but one vertex fixed and use elementary trace factorization, then replace vertices successively through fresh bridge primes. The rational fixed-support extension is generated by $-1$ and the support primes; the moving prime adds at most the one radical $ℓ_M^*$. Its dimension is uniformly bounded. The old characters are fixed and the new character is quadratic. There are therefore only finitely many addition, projection, and reciprocity-type tables. The ultrafilter selects one abstract table. For every fixed vertex bound it similarly selects one binary truth table on the finitely many typed graphs. These selected tables agree under restriction, because finite intersections of ultrafilter-large sets are large. The bounded-weight witness of Lemma F.1 gives a unit in the resulting table. All finite contraction and isolation identities pass to it.

To realize a construction, first choose its finite graph and networks in this abstract alphabet. Their maximum vertex count is a finite cutoff. Only then select an actual stage in the finite intersection of the required large sets, with sufficient precision, and realize the graph by primes. No stage is required to work for every graph size, and no countable intersection is taken. A later fixed finite enrichment of the labels can be stabilized with the same ultrafilter. The original $\delta$ remains unchanged.

**Corollary F.7 (Uniform bounds at a unit).**

At an even unit,

```math
L_*(h)\ne0,\qquad v_2(L_*(h))\le2\omega(\vert h\vert )+C.
```

At an odd unit, realized at sufficient precision, $E^{(h)}$ has analytic order one and

```math
j(P_h)\le\omega(h)+C.
```

The constants are independent of the number and sizes of the varying primes and, in the odd case, of the moving stage.

*Proof.* A unit has coefficient valuation $\delta+\omega(\vert h\vert )$. In the even case use (E.3). In the odd case choose $M$ above this valuation for all finitely many required indices, making the coefficients visible. Equation (E.6) then detects a nontorsion point, since $L$ kills torsion. Gross–Zagier gives analytic order one. An integral homomorphism into $\mathbb{Z}/2^M\mathbb{Z}$ cannot lower the divisibility index of a point. The factors $L,c_0,2^{\omega(N)}$ are fixed, and comparison of the rational and biquadratic free lattices has bounded index. Thus visibility also gives $j(P_h)\le v_2(a_M(h))+C$ uniformly.

□

## Appendix G. Finite arithmetic graphs and simultaneous addressing

The graph constructions in this section are the rational specializations of OpenAI (2026). Their arithmetic inputs are precisely Proposition F.6 and finite prime realization. All configurations and all outputs of contractions are nonempty.

### G.1. Labels and realization

At a finite support $S$ containing two, a prime type records its unit squareclasses and its residue modulo eight. Its elementary Frobenius label is in the extension generated by $-1$ and the primes of $S$. These quadratic data form a finite $\mathbb{F}_2$‑space; prescribed splitting in a fixed quadratic field restricts to a kernel. Deeper residue classes may be chosen as realization lifts but are not additional coordinates of this alphabet. For every pair of vertices choose one forward Legendre bit. The reverse is fixed by

```math
(p/q)(q/p)=(-1)^{((p-1)/2)((q-1)/2)}.
```

There is no self-residue. A primary vertex has trivial type: it is $1\pmod8$ and a square unit at every support prime.

**Lemma G.1 (Finite realization and product labels).**

Fix finitely many old vertices with all their mutual data. Any individually realizable types for finitely many new vertices, and any prescribed forward bits involving at least one new vertex, can be realized by distinct fresh primes outside a finite exclusion set. Contracted clusters have product types and summed external bits, and can be replaced by fresh prime representatives with those data. The symbol depends only on the resulting finite graph.

*Proof.* For the next prime choose its prescribed reduced residue class at the support. At every old prime choose a nonzero residue realizing the desired Legendre bit; quadratic reciprocity determines the reverse bit from the chosen type. The Chinese remainder theorem combines these conditions, and Dirichlet’s theorem gives infinitely many primes in the resulting reduced progression. Successive choices prove the finite assertion and permit all exclusions.

For a cluster $p_1,\ldots,p_r$ prescribe for its representative $q$ the unit squareclasses of $\prod p_i$ at the support, the residue $q\equiv\prod p_i\pmod4$, and the corresponding products of residues at every remaining vertex. The same argument realizes them. In particular, writing $p^*=(-1/p)p$,

```math
\mathrm{sgn}(q^*)=\prod_i\mathrm{sgn}(p_i^*),\qquad
 [q^*]_v=\prod_i[p_i^*]_v\quad(v\in S).
```

Thus product replacement preserves the signed filter, including its real sign. At any omitted vertex, the fixed radicals and the remaining prime radicals generate the maximal elementary extension with the allowed ramification. Their listed bits therefore determine its trace test. To compare two graph realizations, use fresh bridge primes with matching bits to both and replace vertices successively. Proposition F.6 gives equality at each step.

□

An arithmetic graph is this collection of types and bits. Its unique multilinear polynomial over $\mathbb{F}_2$ in selected pair bits is its terminal polynomial. Write $\Delta_zP=P\vert _{z=0}+P\vert _{z=1}$; on multilinear polynomials this is ordinary differentiation, so the differences commute and square to zero. A graph is partitionable if a contraction forest has a unit symbol as its output. Its terminal polynomial is then nonzero.

**Lemma G.2 (Forest contraction).**

Differentiation along a tree contracts that tree, multiplying its labels and summing its external bits. A derivative containing a cycle is zero.

*Proof.* The one-edge statement is Proposition F.6; induction and product replacement give the tree assertion. For a cycle first contract a spanning path. The closing bit is now internal to the merged cluster and affects no product type or external incidence. Equivalently it is an inertia change at an omitted rational prime; the replacement source is unramified there. Its derivative is zero. Repetition of an edge is also zero by $\Delta_z^2=0$. Other derivatives commute with this zero derivative.

□

### G.2. Network operators

Fix a terminal graph and its polynomial $P$. A network adds primary internal vertices and programmed edges, with no direct terminal–terminal edges. Unprogrammed incidences, including those to specified stationary external vertices, are neutral. The degree of a contraction is the number of terminal vertices lost by merging them.

**Lemma G.3 (Network expansion).**

A network acts on $P$ by a sum of finite-difference operators. Its surviving terms are forests in which every component containing an internal vertex meets a terminal. A component meeting $t$ terminals has degree $t-1$. Networks on disjoint internal vertex sets, with no edges between those sets, multiply as operators on the original terminal polynomial. An operator of degree greater than $\deg P$ annihilates it.

Let $Q$ be the grounded Laplacian on the internal vertices, whose diagonal entries include terminal incidence, and let $c_a$ be the incidence column of terminal $a$. Its degree-zero and pair-contraction coefficients are

**Equation (G.1).**

```math
\det Q,\qquad c_a^{\mathsf{t}}\mathrm{adj}(Q)c_b\quad(a\ne b).
```

These formulas include singular $Q$.

*Proof.* Expand evaluation at the programmed edges from the graph with all primary incidences zero: $f(\mathbf{1})=\sum_{T\subseteq E_0}(\Delta_Tf)(\mathbf{0})$. Lemma G.2 kills cycles. A component without a terminal contracts to an isolated primary vertex, so its symbol is zero; this includes an untouched internal vertex. In a surviving component, primary labels and baseline external bits are neutral. Its contraction is exactly the contraction of its terminal vertices in the original graph. Any terminal tree on those vertices gives the same product labels and external bits, so it supplies an operator of degree $t-1$. Expanding two disjoint networks at once gives the composition of these operators. The final product labels agree in either order, and any resulting cycle vanishes. Polynomial differentiation proves the degree bound.

For the coefficients, write the full Laplacian as $DD^{\mathsf{t}}$, where an incidence column has ones at its two endpoints. Cauchy–Binet applied to its internal principal minor $Q$ counts forests with exactly one terminal in each component: a cycle gives dependent columns, a component without a deleted terminal row gives dependent rows, and a tree with one row deleted has determinant one by leaf removal. These are exactly the degree-zero terms. For the pair coefficient use row set $I\cup\{a\}$ and column set $I\cup\{b\}$. Each counted component has one root from the terminal set minus $a$ and one from that set minus $b$. Thus $a,b$ lie together, and every other terminal lies in its own component. The minor is

```math
\det\begin{pmatrix}Q&c_b\\ c_a^{\mathsf{t}}&0\end{pmatrix}
       =c_a^{\mathsf{t}}\mathrm{adj}(Q)c_b.
```

The corner is zero because there is no direct terminal edge; signs disappear over $\mathbb{F}_2$. The adjugate identity does not require invertibility. This is the required all-minors matrix-tree calculation.

□

An address is $x\in\mathbb{F}_2^b$. A vertex of activation $\lambda\ne0$ is present if $\lambda(x)=1$. We permit either always-active terminals, or moving terminals including at least one with each nonzero activation. Fix $x_*\ne0$ and a bit $z$ between two terminals $a_0,a_1$ active at $x_*$. Choose a dual basis $\lambda_1,\ldots,\lambda_b$ with $\lambda_i(x_*)=1$ for every $i$. Indeed, start with $\lambda_1(x_*)=1$ and add it to a basis of the annihilator of $x_*$. Make $b$ groups of three primary vertices, group $i$ activated by $\lambda_i$. All groups are present exactly at $x_*$.

In each physical three-dimensional group choose a basis $(e_i,u_i,v_i)$ with $e_i=(1,1,1)$. Make the $e_i$ orthonormal and orthogonal to all $u_j,v_j$, and put on the remaining coordinates

```math
H(T,B)=\begin{pmatrix}0&T\\ T^{\mathsf{t}}&B\end{pmatrix},
```

where $B$ is symmetric. Denote the physical matrix by $Q$. The column $h_i=Qe_i$ is supported on group $i$ and independent of $T,B$. Attach it to an anchor terminal of activation $\lambda_i$; for stationary terminals use any fixed terminal. On a set $J$ of active groups,

```math
\sum_{i\in J}h_i\vert _J=Q_J\mathbf{1}_J.
```

Program internal edges using the off-diagonal entries of $Q$. The anchor columns thus make the grounded matrix exactly $Q_J$, including its diagonal, after every group restriction.

Attach an additional column $c$ to $a_0$ and $a_1$. If their moving activations $\alpha,\beta$ differ, attach $c$ also to a terminal of activation $\alpha+\beta$, inactive at $x_*$. The sum of these additional active columns is zero at every address. If the activations agree, or the terminals are stationary, the first two columns already cancel. Coincident terminal roles add their columns. Thus the grounded matrix is unchanged.

**Lemma G.4 (Two address programs).**

There are networks $\mathcal{S}$ and $\mathcal{N}^{(\varepsilon)}$ for $\varepsilon\in\mathbb{F}_2$ with

```math
\mathcal{S}_{x_*}=\Delta_z+O_{\ge2},\qquad
 \mathcal{S}_x=1+O_{\ge1}\quad(x\ne x_*),
```

and

```math
\mathcal{N}_x^{(\varepsilon)}=1+O_{\ge1},\qquad
 \mathcal{N}_x^{(1)}+\mathcal{N}_x^{(0)}=
 \begin{cases}
 \Delta_z+O_{\ge2},&x=x_*,\\
 O_{\ge2},&x\ne x_*.
 \end{cases}
```

Here $O_{\ge d}$ is a sum of operators of degrees at least $d$. Every internal activation is nonzero, so no auxiliary vertex is present at zero.

*Proof.* For $\mathcal{S}$ take $T=I+P$, where $P$ is the cyclic permutation matrix, and take $B$ diagonal with exactly one nonzero entry. A proper principal restriction $P_J$ is a union of directed paths and hence nilpotent. Thus $T_J$ and $H(T_J,B_J)$ are invertible. The empty restriction has determinant one. On the full set, the kernels of $T$ and $T^{\mathsf{t}}$ are spanned by the all-one vector. A radical vector has $v=t\mathbf{1}$; summing $T^{\mathsf{t}}u+Bv=0$ forces $t=0$ because $\mathbf{1}^{\mathsf{t}}B\mathbf{1}=1$. The radical of $Q$ is therefore spanned by $r=\sum_i u_i$. Its adjugate is $rr^{\mathsf{t}}$: it has nonzero rank one and image the kernel, and the only nonzero scalar over $\mathbb{F}_2$ is one. Take $c$ dual to $u_1$, so $c^{\mathsf{t}}r=1$. All anchors pair to zero with $r$. At the target only the columns of $a_0,a_1$ pair nontrivially, and (G.1) gives zero constant and exactly $\Delta_z$ in degree one. At every other address the constant is one. For $b=1$ one has $T=0,B=(1)$ and the same argument applies.

For $\mathcal{N}^{(\varepsilon)}$, take $T=I+L$ with $L$ the consecutive lower shift and $B=\varepsilon E_{bb}$. Every group restriction of $T$ is invertible and

```math
H(T,B)^{-1}=\begin{pmatrix}
 T^{-\mathsf{t}}BT^{-1}&T^{-\mathsf{t}}\\ T^{-1}&0
 \end{pmatrix}.
```

Again take $c$ dual to $u_1$. On $J$, the change in $c^{\mathsf{t}}Q_J^{-1}c$ is $((T_J^{-1})_{b1})^2$, interpreted as zero if either endpoint is absent. The finite sum $(I+L_J)^{-1}=I+L_J+L_J^2+\cdots$ shows that this entry is one exactly when the whole path $1,\ldots,b$ is present, namely at $x_*$. Anchor pairings do not change because $Q_J^{-1}h_i=e_i$ and $e_i,h_i,c$ do not depend on $\varepsilon$. At the target the balancing terminal is absent, so only the $a_0,a_1$ pair coefficient changes. Every constant is one. Lemma G.3 proves the assertions.

□

**Theorem G.5 (Simultaneous addressing).**

Suppose either that one symbol has a nonzero polynomial on a nonempty set of always-active terminals, or that one or two symbols have nonzero terminal polynomials separately at every nonzero address on moving terminals with at least one of each nonzero activation. The symbols may forget different fixed-label coordinates of a common alphabet. Suppose their required total filters hold at every nonzero address. From any fixed realization of the terminal data, one can adjoin finitely many fresh primary auxiliaries, with nonzero activations, so that every symbol equals one at every nonzero address. All old vertices and their mutual data remain unchanged. The auxiliaries may obey fixed splitting and neutral external-incidence conditions included in their primary type.

*Proof.* Use common variables for toggles of the original terminal bits. For one symbol, at address $x\ne0$ choose a top monomial of its polynomial $P_x$, of degree $d_x$, with coefficient one. For each variable of this monomial add a disjoint singular program targeted at $x$. At $x$ its $d_x$ own programs have zero constants, so every surviving term uses at least $d_x$ degrees. Any further degree kills $P_x$. Thus precisely the designated degree-one terms and all other programs’ constants survive, giving that top coefficient, one. A nonzero constant polynomial needs no own program. This also covers stationary terminals.

For two symbols write their polynomials as $P_x,R_x$, of degrees $d_x,e_x$. Multiply the top homogeneous parts in the ordinary polynomial ring, before imposing Boolean relations. Since this ring is a domain, choose a monomial of coefficient one

```math
M_x=\prod_z z^{ν_{xz}},\qquad
 ν_{xz}\in\{0,1,2\},\qquad
 \sum_zν_{xz}=d_x+e_x.
```

For exponent two add one singular program targeted at $x$. For exponent one add one nonsingular program with its own parameter $\varepsilon_{xz}$. All internal vertex sets are disjoint. Let $\Phi(\varepsilon)$ be the product of the final evaluations of both symbols over all nonzero addresses. We show that its sum over all program parameters is one.

A singular program costs at least one degree in each factor at its target. A nonsingular program has constant one independent of its parameter; a term using only these constants everywhere cancels in the sum over that parameter. Every surviving term therefore costs at least one degree somewhere for that program. The total minimum cost is $D=\sum_{x\ne0}(d_x+e_x)$. A nonzero term cannot exceed this budget, since some factor would then receive more derivatives than its degree. Every surviving term uses all minimum costs exactly. Thus each singular program contributes its designated derivative once to each target factor and nothing elsewhere. Each nonsingular program contributes degree one to exactly one factor; after summing its parameter this is zero away from its target and is $\Delta_z$ at its target. No higher network coefficient remains.

At a fixed address, with $Z_2$ and $Z_1$ the exponent-two and exponent-one variables, the allocation sum is

```math
\sum_{J\subseteq Z_1}
 [z_{Z_2}z_J]P_x^{\mathrm{top}}
 [z_{Z_2}z_{Z_1\setminus J}]R_x^{\mathrm{top}}
 =[M_x](P_x^{\mathrm{top}}R_x^{\mathrm{top}})=1.
```

Coefficients of incorrect degree are zero. Each factor receives its full degree, so the result is independent of the original terminal-bit evaluation. The allocations at different addresses are independent, giving $\sum_\varepsilon\Phi(\varepsilon)=1$. Some choice therefore has all required evaluations one. Finally Lemma G.1 realizes the finite networks with fresh primes. Primary types preserve the filters and the stipulated external conditions; all activations are nonzero.

□

**Lemma G.6 (Minimum seeds and neutral packets).**

At the least positive vertex count of a unit witness, its mutual edge bits are immaterial and its value depends only on its fixed labels. Suppose one or two symbols with total filter zero have such nonempty witnesses. If a common finite alphabet projects onto the individual labels needed by each witness, there is a finite packet of common labels of total zero such that every nonempty union of copies is partitionable separately for both symbols.

*Proof.* At a minimum positive count $r\ge2$, differentiation in an edge gives a symbol on $r-1$ nonempty vertices, hence zero by minimality. For $r=1$ there is no edge. Thus edge bits are immaterial, whether or not the empty configuration is a unit.

Take ample copies of common labels projecting to every needed individual witness label, then duplicate the entire list. Its total is zero in the common elementary alphabet. For a witness with labels $a_1,\ldots,a_r$ of total zero, retain $r-1$ anchors with the first $r-1$ labels and merge all other vertices into one nonempty cluster. Its projected label is forced to be $a_r$. The contracted graph is a witness regardless of its edge bits. This uses only sufficiently many copies, so works for every nonempty union of packets and separately for each symbol. Simultaneous surjectivity onto a product of alphabets is unnecessary; the two contraction forests may differ.

□

## Appendix H. Assembly for the auxiliary curve

The arithmetic interpolation inputs are Theorems C.1, C.2, D.1, and D.2. Their uniformities have different roles. The cyclotomic transfer gives a bound independent of a stationary base and its prime count, although its dimension threshold may depend on that base. The ring-class lower bound is uniform when the negative companion has bounded prime count. The final ring-class transfer uses one fixed companion and a constant independent of the cube. We establish the odd coefficient lower bound before choosing its minimum or using its symbol.

### H.1. Partitionable even parameters and bounded companions

**Proposition H.1 (Partitionable even estimate).**

Fix an even symbol for $E=F$ on a filter of parameters locally square at every prime of $2N$. If a partitionable parameter $d$ has $s_2(E^{(d)})=0$, then

```math
L_*(d)\ne0,\qquad v_2(L_*(d))-2\omega(\vert d\vert )-s(d)\le C,
```

where $C$ depends only on the fixed symbol and local data.

*Proof.* If there are no prime factors, partitionability means the empty configuration is itself a unit, and Corollary F.7 applies directly. Otherwise hold the prime factors of $d$ stationary. Their terminal polynomial is nonzero by its contraction certificate. The stationary one-symbol case of Theorem G.5 gives arbitrarily large binary cubes based at $d$, with no old prime removed and only primary new primes, whose nonzero addresses are units. Corollary F.7 and $s(d_x)\ge0$ give the uniform upper bound required by Theorem C.2. The base corank is zero, so that theorem yields the assertion. Its base-dependent dimension threshold does not enter the constant.

□

**Lemma H.2 (Bounded companion).**

Fix the positive odd-sign filter, its support $S_0$, and the negative genus partner $h_*$ above. There are constants $A,C$ such that every $h$ in this filter of analytic order one has a negative odd fundamental discriminant $k'$ satisfying

```math
(k',2Nhh_*)=1,\qquad k'\text{ is a square at }2Nh,
 \qquad \omega(\vert k'\vert )\le A,
```

whose quadratic field has no extra units, and

**Equation (H.1).**

```math
L_*(hk')\ne0,\qquad
 v_2(L_*(hk'))\le2\omega(\vert hk'\vert )+s(hk')+C.
```

*Proof.* Prepare an even negative-discriminant symbol for each possible total type at the fixed support that can occur below. There are finitely many such preparations. Their positive squarefree indices have nontrivial type at two: the absolute value of an odd negative fundamental discriminant that is square at two is $7\pmod8$. Consequently an even unit seed for each such filter has positive vertex count. At its least positive count its edge bits are immaterial by Lemma G.6.

Insert into $\vert k'\vert $ a bounded dummy supply with sufficiently many copies of the anchor labels of every prepared seed. Lemma G.1 realizes them outside all primes already used. Include a fresh prime greater than three, so the eventual imaginary field is not an extra-unit field. The number of dummy primes depends only on the finite preparation. Let $d_0$ be their product. Apply the bounded-prime nonvanishing theorem, Proposition B.1, to the curve obtained by absorbing $h$ and $d_0$. Prescribe the sign and local unit classes of the remaining factor so that the final $k'$ is negative, odd fundamental, coprime to the old support and $h$, and square at every prime of $2Nh$. These are compatible nonzero residue conditions in a reduced progression. The final root number is $+1$: twisting $E^{(h)}$ by the negative $k'$ coprime to its conductor and square at $2Nh$ multiplies its odd sign by $\chi_{k'}(-N_{E^{(h)}})=-1$. The theorem therefore gives $L(E^{(hk')},1)\ne0$ with at most five additional prime factors. Its size threshold may depend on $h$ and the progression; the prime-count bound does not.

For the actual resulting total type, retain all but the last anchor of the corresponding seed and merge every other factor of $\vert hk'\vert $ into its last cluster. There are enough dummy labels, the last cluster is nonempty, and its type is forced by the total. The result is the seed, regardless of mutual bits. Thus $hk'$ is partitionable for one of the finitely many prepared even symbols. Analytic nonvanishing gives Selmer corank zero by the forward theorem. Proposition H.1 gives (H.1). The finite preparation and the dummy bound plus five give $A,C$ independent of $h$.

□

**Proposition H.3 (Odd coefficient lower bound).**

Every analytically rank-one $h$ in the prepared positive filter obeys

**Equation (H.2).**

```math
2j(P_h)\ge2\omega(h)+s(h)-C.
```

The theta sources of Proposition E.5 consequently satisfy the odd premises of (F.1), with a constant independent of $M,ℓ_M$, and the number of varying primes. They also have the bounded-weight visible witness needed in Lemma F.1.

*Proof.* Choose $k'$ by Lemma H.2. Theorem D.1, Proposition E.1, and (H.1) give

```math
\begin{aligned}
 2j(P_h)
 &\ge4\omega(h)+s(h)+s(hk')-v_2(L_*(hk'))-C\\
 &\ge2\omega(h)+s(h)-2\omega(\vert k'\vert )-C\\
 &\ge2\omega(h)+s(h)-C'.
\end{aligned}
```

The ring-class constant is uniform because $\omega(\vert k'\vert )\le A$. Only even symbols and independently nonvanishing companions have entered this argument.

If $P_D$ is torsion, multiplication by $L$ makes its theta coefficient zero modulo $2^M$. If it is nontorsion, the genus Gross–Zagier formula with fixed nonzero $L(E^{(h_*)},1)$ gives analytic order one of $E^{(D)}$, so (H.2) applies. An integral reduction homomorphism cannot lower its divisibility index, and all factors in (E.6) are fixed integers or units. The bounded lattice comparison over degree-four fields therefore gives $v_2(a_M(D))\ge\min(M,\omega(D)-C)$ for every admissible $D$. Proposition E.4 supplies a fixed $D_w$ with bounded coefficient valuation, since $c_0,2^{\omega(N)}$ and $L$ are independent of the stage. This is the required witness.

□

We may now apply the odd minimum, calculus, and finite-table stabilization of Section F. In particular its depth $\delta$ and its unit bound are fixed before any cube dimension is chosen.

### H.2. An ordinary split-prime seed

Choose a minimum-depth negative even witness $k\lt 0$, prime to the intrinsic odd support $S_0$, square at $2N$, and let $K=\mathbb{Q}(\sqrt{k})$. Its odd negative fundamental discriminant has a prime factor outside $2N$. Since $\mathbb{Q}(E[8])$ is unramified outside $2N$,

```math
K\cap\mathbb{Q}(E[8])=\mathbb{Q}.
```

Chebotarev therefore gives fresh primes split in $K$ whose action on $E[8]$ is in the conjugacy class of Frobenius at $19$. For them

**Equation (H.3).**

```math
p\equiv3\pmod8,\qquad a_p(E^{(k)})\equiv0\pmod8.
```

The congruence for $p$ follows also from the Weil-pairing determinant.

**Proposition H.4 (Nonempty ordinary split witness).**

The even coefficient symbol for $E^{(k)}$, normalized at the index $1$, has a nonempty unit witness supported on primes split in $K$ and with total filter that of one.

*Proof.* The proof of Proposition E.2 applies to any fixed elliptic curve and nonvanishing twist index: its local Kirillov construction allows arbitrary bad local representations and arbitrary fixed level depth. Apply that proof to $E^{(k)}$ at the nonvanishing index $1$, adjoin all primes of $k$ to its fixed support, and normalize $a(1)=1$. The additional additive bad primes of $E^{(k)}$ are therefore fixed exceptional places of that construction. Restrict $D$ to the positive unit filter, square at $2Nk$ and at all the original fixed tests.

Its square comparison reads

```math
2v_2(a(D))
  =v_2\!\left(\frac{\sqrt D\,L(E^{(kD)},1)}{L(E^{(k)},1)}\right)
  =v_2\!\left(\frac{L_*(kD)}{L_*(k)}\right).
```

The fixed period of $E^{(k)}$ cancels from the first ratio. Let $a_0$ be the original even coefficient source for $E$. Since $kD$ remains on the original negative filter and $(k,D)=1$, minimality of $k$ gives

```math
v_2(a(D))=v_2(a_0(\vert k\vert D))-v_2(a_0(\vert k\vert ))\ge\omega(D).
```

The normalization therefore uses the original $F$‑bound on $kD$, and its minimum depth is zero. If no nonempty split unit existed, rational phase removal would give $v_2(a(D))\ge\omega(D)+1$ for every nonempty admissible product of split primes.

For a good split prime $p$ put $a=a_p(E^{(k)})$. The integral calculus gives

```math
B_p=(U_p-\eta(p)V_p)g/2,\qquad
 H_p=(B_p-B_p[1]\Theta_1-B_p[p]\Theta_p)/2.
```

For the positive even filter $\psi/\eta=\chi_{-4}$ and $\psi$ is even. Hence $\eta$ is odd, the unary exponent is $i=0$, and $\Theta_p$ has the same scalar character as $B_p$. The phase-free first shells are $1,a-1,a(a-1)-p$, so

**Equation (H.4).**

```math
H_p[p]=0,\qquad
 H_p[p^3]=\eta(p)^2\frac{(a-1)(a-p-1)}4.
```

Put $f=\theta H_p$. On an old unramified constituent the Hecke polynomial gives

```math
(U_p^{(2)})^2t(\varphi_p)
      =(U_p^{(2)})^3+d(\varphi_p)U_p^{(2)}.
```

On a conductor-one principal series, $U_p^{(2)}$ is the unramified eigenvalue $\lambda$, while trace and determinant are $\lambda+\mu,\lambda\mu$, giving the same identity. These exhaust the retained ambient systems, as in Lemma F.5. Assume $p\equiv3\pmod4$. The coefficient of $\theta\Theta_1$ at $p$ is exactly zero because $p$ is not a sum of two squares. The other two summands have the same character, so their determinant action has a common scalar. Since $f[p]\equiv H_p[p]=0\pmod{\mathfrak{m}}$, the coefficient $(d(\varphi_p)f)[p]$ is zero modulo $\mathfrak{m}$. Evaluate the displayed cubic identity at coefficient one to obtain

**Equation (H.5).**

```math
[t(\varphi_p)f]_{p^2}\equiv H_p[p^3]\pmod{\mathfrak{m}}.
```

All divisions have already occurred in the integral Fourier lattice.

Realize the finite trace data of $\varphi_p$ by a fresh prime $p'$ split in $K$, with the same support-unit labels as $p$. Then $pp'$ lies on the filter, and the left side of (H.5) tests $H_p[p^2p']$. Here the underlying squarefree index is $pp'$ and $\kappa=0$. The coefficient differs from $2^{-2}a(pp')$ only by the odd factor $a-1$ and the unit phase $\eta(p)$. The assumed extra valuation makes it zero modulo $\mathfrak{m}$. Equation (H.4) therefore gives $(a-1)(a-p-1)/4\equiv0\pmod2$. Since $a$ is even and $a\equiv p+1\pmod4$, this forces $a\equiv p+1\pmod8$. A fresh prime in (H.3) contradicts this: $a\equiv0$ whereas $p+1\equiv4\pmod8$.

□

### H.3. Compatible moving stages and the fixed companion

If the stabilized odd symbol is a unit at the empty configuration, a sufficiently precise actual stage already detects analytic order one at $h=1$. Otherwise choose a nonempty minimum positive-count witness for it. Choose $k$ as above after the intrinsic odd support and normalization have been fixed. Since the detecting primes $ℓ_M$ were chosen pairwise distinct, discard the finitely many stages with $ℓ_M\mid k$. This cofinite restriction belongs to the existing nonprincipal ultrafilter and preserves its stabilized tables, minimum depth, and witness; no detector sequence is replaced. The ramification of $k$ outside $S_0$ then gives

```math
K\cap\mathbb{Q}\bigl(\sqrt{-1},\sqrt p:
                   p\in S_0\cup\{ℓ_M\}\bigr)=\mathbb{Q}.
```

Indeed the field on the right is unramified at every prime of $k$. Consequently every intrinsic odd label has a lift represented by a prime split in $K$. Proposition H.4 supplies a nonempty even minimum witness on the split-prime alphabet for $E^{(k)}$.

Take the common quadratic alphabet of the odd and even tests, restricted to primes split in $K$. It projects onto each individual label set needed by these witnesses: odd surjectivity follows from the displayed disjointness, and even surjectivity is its defining split restriction. Only these individual projections are needed for Lemma G.6. The fixed support of $k$ is a finite enrichment, so stabilize its tables with the same ultrafilter as in Section F.2. This preserves the intrinsic odd minimum and witness.

For each $b$, assign a copy of a common neutral packet to every nonzero linear form on $\mathbb{F}_2^b$, activating all its vertices by that form. At each $x\ne0$ at least one packet is active. Its union is partitionable separately for both tests, so both terminal polynomials are nonzero. Every packet has common total zero, keeping the positive local filter and the splitting conditions. Theorem G.5 adds primary auxiliaries, also split in $K$, and makes both symbols units at every nonzero address. First choose these finite graphs and all their networks in the stabilized alphabet; only then choose an actual stage meeting their finite weight and precision requirements and realize them by primes. No new prime is active at zero, so the resulting family has

```math
h_x=\prod_q(q^*)^{\lambda_q(x)},\qquad h_0=1.
```

The total type makes each $h_x$ positive with the prescribed local squareclasses. All active primes are split in the one fixed field $K$. The varying detector prime is a coefficient-label prime; it is not an additional ramified place of the ring-class interpolation over this fixed $K$.

**Theorem H.5 (Rank one for the auxiliary curve).**

If $s_2(E/\mathbb{Q})=1$, then

```math
\mathrm{ord}_{s=1}L(E,s)=1,
 \qquad\mathrm{rank}E(\mathbb{Q})=1,
```

and $\mathrm{Sha}(E/\mathbb{Q})$ is finite.

*Proof.* In the empty-unit case this follows from the detected nonzero genus point, Gross–Zagier, and the forward theorem. Otherwise use the families just constructed, for arbitrarily large $b$. At every nonzero address the odd unit gives

```math
\mathrm{ord}_{s=1}L(E^{(h_x)},s)=1,\qquad
 j(P_{h_x})\le\omega(h_x)+C_1,
```

and the even unit for $E^{(k)}$ gives

```math
L(E^{(kh_x)},1)\ne0,\qquad
 v_2(L_*(kh_x))\le2\omega(h_x)+C_2.
```

Here $k$ is fixed, so its prime count is absorbed in $C_2$. The constants use the original coefficient minima and are independent of the cube, its vertex count, and the chosen actual odd stage. Proposition E.1 gives

```math
2j_{h_x}(k)\le4\omega(h_x)+C_3,
```

and therefore

```math
2j_{h_x}(k)-4\omega(h_x)-s(h_x)-s(kh_x)\le C_3.
```

The two $s$‑terms are nonnegative and finite by the forward theorem. Since $L(E^{(k)},1)\ne0$, that theorem also gives $s_2(E^{(k)}/\mathbb{Q})=0$. Restriction and quadratic projection after tensoring with $\mathbb{Q}_2$ give the corank identity

```math
s_2(E/K)=s_2(E/\mathbb{Q})+s_2(E^{(k)}/\mathbb{Q})=1.
```

All hypotheses of the fixed-field ring-class missing-vertex theorem, Theorem D.2, are now satisfied, with one constant for arbitrarily large cubes. Its base Heegner point is nontorsion and $L(E,s)L(E^{(k)},s)$ has order one at $s=1$. The second factor is nonzero there, so $E$ has analytic order one. The forward Gross–Zagier–Kolyvagin theorem gives rank one and finiteness of $\mathrm{Sha}$.

□

## References

C. Breuil, B. Conrad, F. Diamond and R. Taylor (2001). On the modularity of elliptic curves over $\mathbb{Q}$: wild $3$‑adic exercises. *Journal of the American Mathematical Society* **14**, 843-939.

S. Bloch and K. Kato (1990). $L$‑functions and Tamagawa numbers of motives. In *The Grothendieck Festschrift*, Vol. I, Progress in Mathematics 86, Birkhäuser, 333-400.

D. Bump, S. Friedberg and J. Hoffstein (1990). Nonvanishing theorems for $L$‑functions of modular forms and their derivatives. *Inventiones Mathematicae* **102**, 543-618.

L. Cai, J. Shu and Y. Tian (2014). Explicit Gross-Zagier and Waldspurger formulae. *Algebra & Number Theory* **8**, 2523-2572.

H. Carayol (1986). Sur les représentations $ℓ$‑adiques associées aux formes modulaires de Hilbert. *Annales scientifiques de l’École Normale Supérieure* (4) **19**, 409-468.

J. W. S. Cassels (1965). Arithmetic on curves of genus 1. VIII. On conjectures of Birch and Swinnerton-Dyer. *Journal für die reine und angewandte Mathematik* **217**, 180-199.

C. Cornut and D. Jetchev (2013). Liftings of reduction maps for quaternion algebras. *Bulletin of the London Mathematical Society* **45**, 370-386.

P. Deligne (1971). Formes modulaires et représentations $ℓ$‑adiques. *Séminaire Bourbaki*, 1968/69, Exposé 355, Lecture Notes in Mathematics 179, Springer, 139-172.

V. G. Drinfeld (1973). Two theorems on modular curves. *Functional Analysis and Its Applications* **7**, 155-156.

A. Dujella (2026). *Open problems on Diophantine m-tuples and elliptic curves*. University of Zagreb, list dated 28 October 2026, Problem 3.10.

A. Dujella. *High rank elliptic curves with prescribed torsion*. Archive of rank-ten to rank-fourteen records for torsion group $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$, Dujella-Peral 2017 rank-eleven entry.

A. Dujella and G. Soydan (2022). On elliptic curves induced by rational Diophantine quadruples. *Proceedings of the Japan Academy, Series A* **98**, 1-6. Preprint: arXiv:2105.07293.

T. Fisher, E. F. Schaefer and M. Stoll (2010). The yoga of the Cassels-Tate pairing. *LMS Journal of Computation and Mathematics* **13**, 451-460.

B. H. Gross and D. B. Zagier (1986). Heegner points and derivatives of $L$‑series. *Inventiones Mathematicae* **84**, 225-320.

J. Hoffstein and W. Luo (1997). Nonvanishing of $L$‑series and the combinatorial sieve. With an appendix by D. E. Rohrlich. *Mathematical Research Letters* **4**, 435-444.

K. Kato (2004). $p$‑adic Hodge theory and values of zeta functions of modular forms. *Astérisque* **295**, 117-290.

V. A. Kolyvagin (1990). Euler systems. In *The Grothendieck Festschrift*, Vol. II, Progress in Mathematics 87, Birkhäuser, 435-483.

Yu. I. Manin (1972). Parabolic points and zeta-functions of modular curves. *Mathematics of the USSR-Izvestiya* **6**, 19-64.

J. S. Milne (2006). *Arithmetic Duality Theorems*, second edition. BookSurge.

J. Nekovář (2006). *Selmer Complexes*. Astérisque 310, Société Mathématique de France.

OpenAI (2026). *A pointwise 2-converse for elliptic curves with rational two-torsion*. OpenAI Math Release preprint, 7 October 2026.

B. Poonen and M. Stoll (1999). The Cassels-Tate pairing on polarized abelian varieties. *Annals of Mathematics* **150**, 1109-1149.

N. Ramsey (2006). Geometric and $p$‑adic modular forms of half-integral weight. *Annales de l’Institut Fourier* **56**, 599-624.

D. E. Rohrlich (1994). Elliptic curves and the Weil-Deligne group. In *Elliptic Curves and Related Topics*, CRM Proceedings and Lecture Notes 4, American Mathematical Society, 125-157.

J.-P. Serre (1972). Propriétés galoisiennes des points d’ordre fini des courbes elliptiques. *Inventiones Mathematicae* **15**, 259-331.

G. Shimura (1973). On modular forms of half integral weight. *Annals of Mathematics* **97**, 440-481.

J. H. Silverman (2009). *The Arithmetic of Elliptic Curves*, second edition. Graduate Texts in Mathematics 106, Springer.

J.-L. Waldspurger (1981). Sur les coefficients de Fourier des formes modulaires de poids demi-entier. *Journal de Mathématiques Pures et Appliquées* **60**, 375-484.

Z. Wang and S. Zhang (2022). *On the quadratic twist of elliptic curves with full 2-torsion*. Preprint dated 20 February 2022, Section 2.3.
