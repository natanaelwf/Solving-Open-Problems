# Elliptic Curves of Rank at Least Eleven Induced by Rational Diophantine Quadruples

## An affirmative answer to Dujella's Problem 3.10

**Author:** Natanael Wildner Fraga  
**Date:** 30 October 2026  
**Status:** Complete affirmative solution  
**Field:** Number theory, rational Diophantine quadruples, elliptic curves

## Abstract

We prove that infinitely many rational Diophantine quadruples induce elliptic curves over $`\mathbb{Q}`$ of rank at least eleven, answering Dujella's Problem 3.10. Starting from a curve of Dujella and Peral, an explicit genus-one construction reduces the question to positive rank of one auxiliary elliptic curve $`F`$. Complete local $`2`$‑descent and a Cassels-pairing calculation give $`\dim_{\mathbb{F}_2}\mathrm{Sel}_2(F/\mathbb{Q})=9`$, infinite-Selmer corank one, and finite two-primary Shafarevich-Tate quotient $`(\mathbb{Z}/2\mathbb{Z})^6`$. A specialized proof using the cyclotomic, ring-class, and coefficient constructions of OpenAI (2026) gives analytic rank and Mordell-Weil rank one for $`F`$ and finiteness of its Shafarevich-Tate group. The local comparisons, integral descent, determinant estimates, and finite graph arguments are supplied in the appendices. Given any nontorsion rational point on $`F`$, one of its first eight positive even multiples yields a valid quadruple. Every curve produced by this construction is $`\mathbb{Q}`$‑isomorphic to the source curve. The finite arithmetic certificates use exact integer and rational computations.

**Keywords:** Diophantine quadruples; elliptic curves; $`2`$‑descent; Cassels pairing.  
**2020 Mathematics Subject Classification:** 11D09, 11G05, 11Y50.

## 1. The problem and the precise conclusion

A rational Diophantine quadruple is a set of four distinct nonzero rational numbers $`\{a,b,c,d\}`$ such that

```math
ab+1,\quad ac+1,\quad ad+1,\quad bc+1,\quad bd+1,\quad cd+1
```

are squares in $`\mathbb{Q}`$. Negative entries and the square $`0=0^2`$ are allowed.

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

Problem 3.10 in Dujella's list asks whether a curve of this kind can have rank greater than ten over $`\mathbb{Q}`$. The problem is an existence question about a curve; it does not require infinitely many isomorphism classes.

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

1. $`\mathrm{rank}E_0(\mathbb{Q})\ge11`$.
2. $`\dim_{\mathbb{F}_2}\mathrm{Sel}_2(F/\mathbb{Q})=9`$ and $`s_2(F)=1`$.
3. $`\mathrm{ord}_{s=1}L(F,s)=\mathrm{rank}F(\mathbb{Q})=1`$, the group $`\mathrm{Sha}(F/\mathbb{Q})`$ is finite, and $`\mathrm{Sha}(F/\mathbb{Q})[2^\infty]\cong(\mathbb{Z}/2\mathbb{Z})^6`$.
4. Infinitely many distinct rational Diophantine quadruples induce curves $`\mathbb{Q}`$‑isomorphic to $`E_0`$. For any given nontorsion rational point on $`F`$, the construction in Section 3 produces an admissible quadruple from at least one of its first eight positive even multiples.

**Corollary 1.2.** There is an elliptic curve over $`\mathbb{Q}`$ induced by a rational Diophantine quadruple with rank greater than ten. Thus Dujella's Problem 3.10 has an affirmative answer.

Sections 2 and 3 prove the source rank bound and the reconstruction. Sections 4 and 5 establish the finite Selmer and Cassels-pairing calculations. Section 6 applies the specialized positive-rank theorem proved in the appendices. The determinant and coefficient constructions used there are those of OpenAI (2026); their required local and integral comparisons are proved with the hypotheses of the auxiliary curve. The source curve and its eleven points are due to Dujella and Peral. The conclusion concerns infinitely many quadruples in one $`\mathbb{Q}`$‑isomorphism class of induced curves.

## 2. A curve of rank at least eleven

The curve (1.2) and the following points come from Dujella and Peral's 2017 entry in Dujella's table. The coordinate translation from that entry is $`X=x-1471642492697005494`$, $`Y=y`$.

| $`i`$ | $`X_i`$ | $`Y_i`$ |
|---:|---:|---:|
| 1 | $`-2455690635183512034`$ | $`3930819100635430521717292170`$ |
| 2 | $`-1251776678706189504`$ | $`2609613406782334033646479200`$ |
| 3 | $`-1272661460204312304`$ | $`2640823754547721254370236000`$ |
| 4 | $`-1994688924155600904`$ | $`3547293495901125966835824600`$ |
| 5 | $`440641873774783296`$ | $`538787101369161261182781600`$ |
| 6 | $`-127433871797554344`$ | $`508258934492965396363625640`$ |
| 7 | $`-1352464454208354354`$ | $`2757613161989370207496135050`$ |
| 8 | $`-2756837135466868104`$ | $`4084604229675007831346026200`$ |
| 9 | $`-1057278032568400104`$ | $`2306272930055777531757724200`$ |
| 10 | $`-913127974330002354`$ | $`2066868814798457862205063050`$ |
| 11 | $`1640792454010339014`$ | $`3724723407453925712515593606`$ |

**Proposition 2.1.** The curve $`E_0`$ has rank at least eleven over $`\mathbb{Q}`$.

*Proof.* Integer substitution verifies that all eleven points lie on $`E_0`$. For a split cubic, the Kummer map (Silverman, 2009) injects $`E_0(\mathbb{Q})/2E_0(\mathbb{Q})`$ into $`(\mathbb{Q}^\times/\mathbb{Q}^{\times2})^3`$. Away from the two-torsion points it is

```math
\kappa(X,Y)=([X],[X+A],[X+B]).
```

At $`(0,0)`$ and $`(-A,0)`$ the values are, respectively,

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

Thus the Kummer image has dimension at least thirteen. Since $`E_0(\mathbb{Q})[2]\cong(\mathbb{Z}/2\mathbb{Z})^2`$, the Mordell-Weil theorem gives

```math
\dim_{\mathbb{F}_2}E_0(\mathbb{Q})/2E_0(\mathbb{Q})
=\mathrm{rank}E_0(\mathbb{Q})+2.
```

Therefore $`\mathrm{rank}E_0(\mathbb{Q})\ge11`$. This argument requires neither saturation nor finiteness of $`\mathrm{Sha}`$.

## 3. The auxiliary curve and the reconstruction

### 3.1. A source double and its auxiliary

Choose

```math
P=(X_0,Y_0)=(912833416575231921,-1757195268626559090518724150).
```

This point is a double on $`E_0`$. An exact certificate is

```math
H=(5761058741699892246,-18144092568468363333046645050),\qquad 2H=P.
```

Both the curve equation for $`H`$ and the duplication identity hold over $`\mathbb{Q}`$. One can also check

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

In particular, $`uv,uw,vw`$ are nonzero rational squares. Set

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

For $`\tau=105/59803606`$ one has $`C=\tau^2\alpha`$ and $`D=\tau^2\beta`$. Thus

**Equation (3.4).**

```math
\psi:F\longrightarrow F_P,\qquad
(\xi,\eta)\longmapsto(\tau^2\xi,\tau^3\eta)
```

is a $`\mathbb{Q}`$‑isomorphism preserving the origin and doubles. Direct rational arithmetic verifies

**Equation (3.5).**

```math
uvw(u-v)(u-w)(v-w)hjkCD(C-D)\ne0.
```

### 3.2. Universal identities

**Lemma 3.1.** Let $`Q=(x,y)\in F_P(\mathbb{Q})`$ with $`y\ne0`$. Define

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

If $`Q\in2F_P(\mathbb{Q})`$, all six quantities are rational squares.

*Proof.* Work first in $`\mathbb{Z}[u,v,w,x]`$, with the definitions (3.3), $`T=x+vwjk`$ and $`Y_2=x(x+C)(x+D)`$. Put

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

These are polynomial identities before specialization. On $`F_P`$ one has $`Y_2=y^2`$ and $`(a,b,c,d)=(N_a,N_b,N_c,N_d)/(2Vy)`$. Division by $`4V^2y^2`$ proves (3.7).

If $`Q`$ is a double, the split-cubic Kummer criterion gives $`x,x+C,x+D\in\mathbb{Q}^{\times2}`$. By (3.2), all the remaining factors in the denominators of (3.7) are rational squares. This proves the last assertion.

### 3.3. Admissibility and infinitude

**Lemma 3.2.** For every nontorsion $`R\in F(\mathbb{Q})`$, at least one of

```math
Q_n=\psi(2nR),\qquad 1\le n\le8,
```

produces four distinct nonzero rational numbers through (3.6).

*Proof.* Each $`Q_n`$ is affine and has $`y\ne0`$. Their abscissas are distinct, since equal abscissas would give $`2mR=\pm2nR`$ and contradict nontorsion.

The factor $`\lambda`$ cannot vanish at any rational affine point with $`y\ne0`$. Otherwise $`T=0`$ and $`b=a`$, while the first identity in (3.7) would give $`a^2+1=0`$.

The numerator $`N(x)=2c_0(x+vwjk)+K`$ of $`a`$ is a nonzero polynomial of degree at most one: if $`c_0=0`$, its constant term is $`K\ne0`$. The numerators of $`b,c,d`$ are

```math
N(x)-\frac{u}{2V}(x+vwjk)^2,\quad
N(x)-\frac{v}{2V}(x+vwjk)^2,\quad
N(x)-\frac{w}{2V}(x+vwjk)^2.
```

They are genuine quadratics. Thus at most seven abscissas can give a zero entry. At least one of the eight abscissas is good. Every pairwise difference of the entries is $`\lambda`$ times one of $`u,v,w,v-u,w-u,w-v`$, all nonzero by (3.5). All six squares in (3.7) are nonzero, since $`x(x+C)(x+D)=y^2\ne0`$, $`T\ne0`$, and (3.5) holds.

**Proposition 3.3.** If $`\mathrm{rank}F(\mathbb{Q})\gt 0`$, infinitely many distinct rational Diophantine quadruples induce curves $`\mathbb{Q}`$‑isomorphic to $`E_0`$.

*Proof.* Lemmas 3.1 and 3.2 produce an admissible quadruple from a double. Its induced coefficients satisfy

```math
\begin{aligned}
(b-a)(d-c)&=\lambda^2u(w-v)=\lambda^2A,\\
(c-a)(d-b)&=\lambda^2v(w-u)=\lambda^2B.
\end{aligned}
```

The map $`(X,Y)\mapsto(\lambda^2X,\lambda^3Y)`$ is therefore a $`\mathbb{Q}`$‑isomorphism from $`E_0`$ to (1.1). Proposition 2.1 transfers the rank lower bound.

For infinitude, take all $`Q_n=\psi(2nR)`$ with $`n\ge1`$. Only finitely many have a bad abscissa. As a rational function on the smooth projective curve $`F_P`$,

```math
\lambda=-\frac{(x+vwjk)^2}{2Vy}
```

has a simple pole at the origin, since $`\mathrm{ord}_O(x)=-2`$ and $`\mathrm{ord}_O(y)=-3`$. Hence it is nonconstant and has finite fibers. Infinitely many good $`Q_n`$ give infinitely many values of $`\lambda`$. The ordered quadruple determines $`\lambda=(b-a)/u`$, and an unordered set has at most twenty-four orderings. This proves the assertion for distinct sets.

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

All displayed factors are prime. The accompanying data include recursive Lucas certificates: for each $`n\gt 2`$, a complete factorization of $`n-1`$ and an integer $`a`$ satisfying

```math
a^{n-1}\equiv1\pmod n,\qquad
\gcd\bigl(a^{(n-1)/q}-1,n\bigr)=1
\quad(q\mid n-1, q\text{ prime}).
```

If $`p\mid n`$ is prime, these conditions force the order of $`a`$ modulo $`p`$ to be divisible by $`n-1`$. Hence $`p\ge n`$, proving primality. Recursion terminates at 2.

Let $`S`$ be the ordered list of primes dividing $`2\alpha\beta(\alpha-\beta)`$:

**Equation (4.2).**

```math
\begin{gathered}
2,3,5,7,11,13,23,31,43,47,67,73,89,173,181,283,\\
421,461,599,953,4217,4943,7643,8893,23971,111121,\\
552823181,1073681107,354212181139.
\end{gathered}
```

Use the first two Kummer coordinates $`([\xi],[\xi+\alpha])`$; the third is their product. Each global coordinate is supported on $`(-1,p:p\in S)`$, so the ambient binary space has dimension sixty.

### 4.2. Exact local images

For odd $`p`$, write $`z=p^v u`$ with $`u\in\mathbb{Z}_p^\times`$ and encode its squareclass by

```math
(v\bmod2,\epsilon_p(u)),\qquad
\epsilon_p(u)=\begin{cases}0,&u\text{ square modulo }p,\\1,&u\text{ nonsquare modulo }p.\end{cases}
```

At 2, use the squareclass basis $`(2,-1,5)`$; the odd unit modulo eight specifies its last two bits. Concatenate the first and second Kummer coordinates with the first in the least significant bits.

The torsion witnesses $`T_0,T_\alpha`$ have Kummer pairs

```math
T_0:(\alpha\beta,\alpha),\qquad
T_\alpha:(-\alpha,\alpha(\alpha-\beta)).
```

An integer witness $`n`$ below means a local point of abscissa $`\xi=n`$. Direct valuation and unit tests show that $`n(n+\alpha)(n+\beta)`$ is a nonzero square in $`\mathbb{Q}_p`$. Each pair in the table records a witness followed by its encoded vector in decimal.

| $`p`$ | First witness (vector) | Second witness (vector) | Third witness (vector) |
|---:|:---:|:---:|:---:|
| $`2`$ | $`T_0\;(50)`$ | $`T_\alpha\;(4)`$ | $`-2\;(3)`$ |
| $`3`$ | $`T_0\;(3)`$ | $`T_\alpha\;(2)`$ |  |
| $`5`$ | $`T_0\;(15)`$ | $`2\;(10)`$ |  |
| $`7`$ | $`T_0\;(8)`$ | $`T_\alpha\;(12)`$ |  |
| $`11`$ | $`T_0\;(2)`$ | $`11\;(1)`$ |  |
| $`13`$ | $`T_\alpha\;(8)`$ | $`-1\;(12)`$ |  |
| $`23`$ | $`T_0\;(8)`$ | $`-2\;(2)`$ |  |
| $`31`$ | $`T_0\;(3)`$ | $`T_\alpha\;(2)`$ |  |
| $`43`$ | $`T_\alpha\;(10)`$ | $`43\;(5)`$ |  |
| $`47`$ | $`T_\alpha\;(10)`$ | $`1\;(8)`$ |  |
| $`67`$ | $`T_\alpha\;(10)`$ | $`67\;(5)`$ |  |
| $`73`$ | $`T_0\;(15)`$ | $`-5\;(10)`$ |  |
| $`89`$ | $`T_0\;(8)`$ | $`T_\alpha\;(6)`$ |  |
| $`173`$ | $`T_0\;(1)`$ | $`-2\;(2)`$ |  |
| $`181`$ | $`-2\;(2)`$ | $`181\;(1)`$ |  |
| $`283`$ | $`T_0\;(2)`$ | $`-6\;(10)`$ |  |
| $`421`$ | $`T_0\;(3)`$ | $`2\;(2)`$ |  |
| $`461`$ | $`T_\alpha\;(4)`$ | $`-4\;(8)`$ |  |
| $`599`$ | $`T_0\;(15)`$ | $`T_\alpha\;(5)`$ |  |
| $`953`$ | $`T_0\;(2)`$ | $`953\;(1)`$ |  |
| $`4217`$ | $`-8\;(8)`$ | $`-1193\;(4)`$ |  |
| $`4943`$ | $`T_\alpha\;(6)`$ | $`4\;(8)`$ |  |
| $`7643`$ | $`T_0\;(8)`$ | $`T_\alpha\;(4)`$ |  |
| $`8893`$ | $`T_0\;(8)`$ | $`T_\alpha\;(6)`$ |  |
| $`23971`$ | $`T_0\;(2)`$ | $`-1\;(10)`$ |  |
| $`111121`$ | $`T_0\;(15)`$ | $`7\;(10)`$ |  |
| $`552823181`$ | $`T_0\;(10)`$ | $`552823181\;(5)`$ |  |
| $`1073681107`$ | $`T_\alpha\;(10)`$ | $`1\;(8)`$ |  |
| $`354212181139`$ | $`T_0\;(8)`$ | $`-1\;(2)`$ |  |

The displayed vectors are independent. They form complete local bases because

```math
\#\bigl(F(\mathbb{Q}_p)/2F(\mathbb{Q}_p)\bigr)
=\frac{\#F(\mathbb{Q}_p)[2]}{\vert 2\vert _p}
=\begin{cases}4,&p\ne2,\\8,&p=2.\end{cases}
```

At the real place, $`\alpha\gt \beta\gt 0`$, so the possible abscissas lie in $`[-\alpha,-\beta]\cup[0,\infty)`$. The local sign pairs are $`(0,0)`$ and $`(1,0)`$; the global sign bit of the second coordinate must therefore vanish.

For $`p\notin S`$, the curve has good reduction and $`p`$ is odd. The Kummer image is the unramified subgroup, of size four. Both global coordinates already have even valuation there. Thus no further local condition is required.

### 4.3. The global matrix

For each $`p\in S`$, take the annihilator of the displayed local span under the ordinary binary dot product and compose it with the localization of the sixty global squareclass coordinates. Append the real sign condition. Call the resulting matrix $`M`$.

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

Their scalar products with every row vanish. By the local characterization of the Selmer group, $`\ker M=\mathrm{Sel}_2(F/\mathbb{Q})`$. Hence

**Equation (4.3).**

```math
\dim_{\mathbb{F}_2}\mathrm{Sel}_2(F/\mathbb{Q})=60-51=9.
```

## 5. The Cassels pairing and the infinite Selmer corank

### 5.1. Coverings and tangent forms

Decode the nine kernel vectors in Section 4.3 as squarefree triples $`(d_1,d_2,d_3)`$, in coordinate order $`\xi,\xi+\alpha,\xi+\beta`$. The third coordinate is the squarefree representative of the product of the first two.

| Basis index | $`d_1`$ | $`d_2`$ | $`d_3`$ |
|---:|---:|---:|---:|
| 1 | $`-111121`$ | $`3481843271918419`$ | $`-31333800739`$ |
| 2 | $`842`$ | $`680227`$ | $`572751134`$ |
| 3 | $`519`$ | $`3912270811`$ | $`2030468550909`$ |
| 4 | $`364165`$ | $`3957385`$ | $`57645644341`$ |
| 5 | $`4631`$ | $`96492094703942371`$ | $`446854890573957120101`$ |
| 6 | $`1450240171`$ | $`6917393371`$ | $`812437801`$ |
| 7 | $`542249478131`$ | $`315261648618539539`$ | $`3084099617887841`$ |
| 8 | $`5316809`$ | $`3091171201321`$ | $`3084099617887841`$ |
| 9 | $`599`$ | $`2014054874539`$ | $`3362362061`$ |

For a triple $`d`$, the associated covering has projective coordinates $`(t_0,t_1,t_2,t_3)`$ and equations

**Equation (5.1).**

```math
\begin{aligned}
H_1&=(\beta-\alpha)t_0^2+d_2t_2^2-d_3t_3^2=0,\\
H_2&=-\beta t_0^2+d_3t_3^2-d_1t_1^2=0,\\
H_3&=\alpha t_0^2+d_1t_1^2-d_2t_2^2=0.
\end{aligned}
```

They sum to zero; any two define the covering. An affine local point is specified by $`t_0=1`$ and

```math
t_1^2=\xi/d_1,\qquad t_2^2=(\xi+\alpha)/d_2,\qquad t_3^2=(\xi+\beta)/d_3.
```

View $`H_i`$ as a conic in its three occurring variables. Choose a primitive integral point $`Q_i`$ and let $`L_i`$ be its primitive tangent form. The supplied certificate contains all twenty-seven such conic points. The tangent coefficients are the coordinatewise products of the conic coefficients and $`Q_i`$, divided by their common content. Exact substitution verifies the conic equations and primitivity.

Cassels's formula, in this split-cubic convention, is

**Equation (5.2).**

```math
\langle d,d'\rangle=\sum_v\sum_{i=1}^3[L_i(P_v),d'_i]_v\in\mathbb{F}_2,
```

where $`P_v`$ is a local covering point avoiding the tangent zeros and $`[\ ,\ ]_v`$ is the additive quadratic Hilbert symbol. Here $`H_i`$ omits $`t_i`$, and $`L_i`$ pairs with $`d'_i`$. The formula and its identification with Cassels-Tate are given by Fisher, Schaefer and Stoll (2010, Section 3 and Theorem 5.2); see also Wang and Zhang (2022, Section 2.3). The common denominator in the tangent functions cancels because $`d'_1d'_2d'_3`$ is a square. Rational rescaling of any tangent does not change the global sum, by Hilbert reciprocity.

### 5.2. Exact local certificates

For each of the nine coverings and every $`p\in S`$, the data specify a rational abscissa $`\xi`$ and rational approximations $`u_i`$ to the three square roots. Put

```math
r_1=\xi/d_1,\qquad r_2=(\xi+\alpha)/d_2,\qquad r_3=(\xi+\beta)/d_3.
```

Each of these 261 certificates satisfies

**Equation (5.3).**

```math
v_p(u_i^2-r_i)\gt 2v_p(2u_i).
```

For a nonintegral approximation, use $`t_i=u_i z`$: the normalized polynomial $`z^2-r_i/u_i^2`$ has unit constant term and satisfies $`v_p(1-r_i/u_i^2)\gt 2v_p(2)`$. Thus the integral form of Hensel's lemma applies as well. It supplies an actual root $`s_i^2=r_i`$ with

```math
v_p(s_i-u_i)\ge e_i:=v_p(u_i^2-r_i)-v_p(2u_i).
```

An exact rational root is assigned error bound $`+\infty`$. Thus $`(1,s_1,s_2,s_3)`$ is a genuine local point. For $`L_j=\sum_{i=0}^3ℓ_{ji}t_i`$, set $`u_0=1`$, $`e_0=+\infty`$ and

```math
a_j=\sum_iℓ_{ji}u_i,\qquad
E_j=\min_{ℓ_{ji}\ne0}\bigl(v_p(ℓ_{ji})+e_i\bigr).
```

Then $`v_p(L_j(P_p)-a_j)\ge E_j`$. The certificates verify

**Equation (5.4).**

```math
E_j\gt v_p(a_j)\quad(p\ne2),\qquad
E_j\gt v_2(a_j)+2\quad(p=2).
```

Consequently the true tangent value is nonzero and has the same squareclass as $`a_j`$.

For odd $`p`$, write $`a=p^r u`$, $`b=p^s w`$ with $`p`$‑adic units $`u,w`$. The symbol is

```math
[a,b]_p=rs\frac{p-1}{2}+r\epsilon_p(w)+s\epsilon_p(u)\pmod2.
```

At 2, the unit residues modulo eight give

```math
[a,b]_2=\frac{u-1}{2}\frac{w-1}{2}
+r\frac{w^2-1}{8}+s\frac{u^2-1}{8}\pmod2.
```

At the real place choose $`\xi=1`$ for $`d_1\gt 0`$ and $`\xi=-(\alpha+\beta)/2`$ for the sole triple with $`d_1\lt 0`$. All three $`r_i`$ are positive. Rational intervals with denominator $`2^{320}`$ enclose their square roots. Propagating the signed intervals through the tangents gives intervals avoiding zero. The resulting signs determine $`[a,b]_\infty`$, which equals one precisely when $`a\lt 0`$ and $`b\lt 0`$.

### 5.3. Vanishing outside the support

For $`p\notin S`$, the diagonal conic coefficients and every $`d'_i`$ are units. Primitive conic points reduce to nonzero smooth points. The contents removed from the tangent forms have support in $`S`$, as the certificate verifies.

The covering has good reduction outside $`S`$. Choose a primitive integral local point avoiding the tangent zeros. Each conic projection is primitive: otherwise another equation in (5.1), with unit coefficients, would force all four projective coordinates to vanish modulo $`p`$.

On a smooth conic over $`\mathbb{Z}_p`$, a tangent at an integral smooth point cuts out twice that point. Its nonzero evaluation on a primitive integral point therefore has even valuation: away from the tangent point it is a unit, and near that point it is a unit times the square of a local parameter. Since $`d'_i`$ is a unit and $`p`$ is odd, the Hilbert symbol is zero. A projective rescaling contributes a common factor to all three tangents, which cancels because $`d'_1d'_2d'_3`$ is a square. Thus all places outside $`S\cup\{\infty\}`$ contribute zero.

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

It is alternating and has rank six. Its principal minor on one-based indices $`\{1,2,3,4,5,8\}`$ has determinant one over $`\mathbb{F}_2`$. The two rational two-torsion classes have coordinate masks 428 and 393, with the least significant bit first. Both lie in the radical.

The exact certificate checks the arithmetic construction of every matrix entry, including the conic tangents, (5.3), (5.4), the real intervals and all local symbols. These checks determine the arithmetic Cassels pairing (5.5).

### 5.5. The finite quotient and the corank

**Proposition 5.1.** Put $`r=\mathrm{rank}F(\mathbb{Q})`$ and let $`\delta`$ be the corank of the maximal divisible subgroup of $`\mathrm{Sha}(F/\mathbb{Q})[2^\infty]`$. Then

**Equation (5.6).**

```math
r+\delta=1,\qquad
\mathrm{Sha}(F/\mathbb{Q})[2^\infty]
\cong(\mathbb{Q}_2/\mathbb{Z}_2)^\delta\oplus(\mathbb{Z}/2\mathbb{Z})^6.
```

In particular, $`s_2(F)=1`$.

*Proof.* Since the two-primary group is cofinitely generated, it has an abstract decomposition

```math
\mathrm{Sha}(F/\mathbb{Q})[2^\infty]
\cong(\mathbb{Q}_2/\mathbb{Z}_2)^\delta\oplus T,
```

with $`T`$ finite. No assumption that $`\delta=0`$ is made. The finite Kummer exact sequence and (4.3) imply

**Equation (5.7).**

```math
r+\delta+t=7,\qquad t=\dim_{\mathbb{F}_2}T[2].
```

The Cassels-Tate pairing is nondegenerate modulo the maximal divisible subgroup. For an elliptic curve it is alternating, including on the two-primary part: its principal polarization is induced by the rational divisor of the origin, as in Poonen and Stoll (1999). Thus $`T`$ has a perfect alternating pairing into $`\mathbb{Q}/\mathbb{Z}`$.

For completeness, this implies an orthogonal decomposition into blocks $`(\mathbb{Z}/2^{e_i}\mathbb{Z})^2`$. Choose an element of maximal order $`2^{e_i}`$. Nondegeneracy supplies a partner whose pairing with it has that exact order. They generate a perfect block, which splits off orthogonally; induction finishes the decomposition. Hence $`t`$ is even.

The pairing on $`\mathrm{Sel}_2`$ is the pullback of the restriction of Cassels-Tate to $`\mathrm{Sha}(F)[2]`$. Its rank six gives $`t\ge6`$. Equation (5.7) gives $`t\le7`$, so evenness forces $`t=6`$ and $`r+\delta=1`$.

In a block $`(\mathbb{Z}/2^e\mathbb{Z})^2`$ with $`e\ge2`$, the restriction of the pairing to the subgroup killed by two vanishes: its basic pairing is multiplied by $`2^{2e-2}`$, which makes it integral. The rank-six restriction on the six-dimensional finite two-torsion therefore forces every $`e_i=1`$. This proves (5.6). Finally, the infinite Kummer exact sequence identifies $`s_2(F)`$ with $`r+\delta`$.

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

*Proof.* Proposition 5.1 gives $`s_2(F)=1`$ with the usual local Kummer conditions. Lemma A.1 verifies full rational two-torsion, the non-CM hypothesis, the local reduction types, functional sign $`-1`$, and $`a_{19}(F)=0`$. Theorem H.5, proved in the appendices for precisely this curve and its indicated twisting classes, gives analytic order one. The forward Gross-Zagier-Kolyvagin theorem gives Mordell-Weil rank one and finiteness of $`\mathrm{Sha}`$. Thus $`\delta=0`$ in (5.6), proving the displayed two-primary group.

For clarity, the dependency order of the positive-rank proof is as follows. Classical nonvanishing supplies seeds with prescribed local classes. Cyclotomic determinants yield a uniform lower bound for normalized central values and a transfer statement for a binary family with one untested vertex. Even half-integral-weight coefficients and finite graph identities then bound suitable nonvanishing companions. The ring-class lower bound and an exact comparison of unaveraged Heegner sums give the lower bound required for the odd coefficient system. A fixed companion and simultaneous addressing produce arbitrarily large binary families with one uniform index bound. The ring-class transfer theorem makes the base Heegner point nontorsion. Each implication, including the treatment of a possibly divisible Shafarevich-Tate group at the base, is proved in the appendices.

*Proof of Theorem 1.1 and Corollary 1.2.* Proposition 2.1 proves the first statement, and Proposition 5.1 proves the second. Theorem 6.1 proves the third. Choose a nontorsion point on $`F`$, whose existence follows from its rank one. Proposition 3.3 and the explicit exclusions in Lemma 3.2 give the fourth statement. Every curve produced by this construction is $`\mathbb{Q}`$‑isomorphic to $`E_0`$, so its rank is at least eleven. This proves the corollary.

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

The verifier recomputes the derived data. It checks all eleven source points, the thirteen independent Kummer classes, the source double, the auxiliary scaling, the nondegeneracy conditions, and the six polynomial identities (3.8). It reconstructs the local Selmer images and the global matrix of rank 51. It checks the conic equations, primitivity, tangent contents, exact Hensel inequalities, tangent precision bounds and real intervals, and recomputes all 7,290 local Hilbert symbols contributing to (5.5). It also verifies the rank-six matrix, its indicated principal minor and the two torsion classes in its radical. The local-invariant checks verify the good model of the $`(-1)`$‑twist at two, the valuation proving that $`F`$ is non-CM, and all odd split and nonsplit reduction types.

These finite checks establish the arithmetic inputs of Theorem 1.1. Proposition 5.1 additionally uses the classical Kummer sequences and Cassels-Tate duality. The positive-rank implication is proved in the mathematical appendices.

## Appendix A. Local invariants and conventions

In the remaining sections write $`E=F`$ for the auxiliary curve in (1.3), and let $`N`$ be its conductor. The cyclotomic and ring-class constructions use separate copies of

```math
\Lambda=\mathbb{Z}_2[[t]],\qquad
 \mathcal{O}=\widehat{\Lambda_{(2)}},\qquad
 \Omega=\mathbb{F}_2((t)).
```

The completion is at the height-one prime $`(2)`$. In particular $`t`$ is a unit in $`\mathcal{O}`$. Specialization at $`t=0`$ is performed over $`\Lambda[1/2]`$ or $`\Lambda_{(t)}`$, never by an evaluation map on $`\mathcal{O}`$.

Parameters indexing the cyclotomic and ring-class families are odd fundamental discriminants, coprime to the fixed support and unit squares at all primes dividing $`2N`$. We allow $`h=1`$ as the parameter of the original curve. A local filter fixes the sign and the unit squareclasses at a finite set containing $`2N`$. Write

```math
s_2(E)=\mathrm{corank}_{\mathbb{Z}_2}
                  \mathrm{Sel}_{2^\infty}(E/\mathbb{Q}),
 \qquad w(h)=\omega(\vert h\vert ).
```

Define the normalized central value for every allowed $`h`$, and define $`s(h)`$ when the indicated group is finite:

```math
s(h)=\mathrm{length}_{\mathbb{Z}_2}
                 \mathrm{Sha}(E^{(h)}/\mathbb{Q})[2^\infty],
 \qquad
 L_*(h)=\frac{\sqrt{\vert h\vert }\,L(E^{(h)},1)}
                    {\Omega_E^{\mathrm{sgn}(h)}}.
```

Nonzero periods in the two sign lines are fixed throughout. All valuations above $`2`$ are normalized by $`v(2)=1`$.

We use the modularity theorem of Breuil, Conrad, Diamond and Taylor (2001), local Tate and global Poitou–Tate duality as in Milne (2006), the non-CM open-image theorem of Serre (1972), and the forward rank and finiteness theorems of Gross and Zagier (1986) and Kolyvagin (1990). Thus analytic order zero or one gives the corresponding Mordell–Weil rank and a finite Tate–Shafarevich group. The Kummer exact sequence always gives

```math
s_2(E)=\mathrm{rank}E(\mathbb{Q})
       +\mathrm{corank}_{\mathbb{Z}_2}
                       \mathrm{Sha}(E/\mathbb{Q})[2^\infty].
```

Restriction and the projections $`1+c,1-c`$ for a quadratic extension $`K=\mathbb{Q}(\sqrt{k})`$ have composites equal to multiplication by two. They preserve the local Kummer conditions. Rationalizing therefore gives

**Equation (A.1).**

```math
s_2(E/K)=s_2(E/\mathbb{Q})+s_2(E^{(k)}/\mathbb{Q}).
```

No integral direct-sum decomposition is needed.

**Lemma A.1.** The curve $`E`$ is non-CM, has full rational two-torsion and has potentially good reduction at $`2`$. Its conductor and root number satisfy

```math
N=2^4\prod_{p\in S\setminus\{2\}}p,\qquad
 \varepsilon(E)=-1,
```

where $`S`$ is the list (4.2). Every odd bad prime is multiplicative. Moreover $`E`$ has good reduction at $`19`$ and $`a_{19}(E)=0`$.

*Proof.* The factorizations (4.1) give

```math
\gcd(\alpha,\beta)=1,\qquad \alpha\equiv3\pmod4,
 \qquad v_2(\beta)=4.
```

The roots $`0,-\alpha,-\beta`$ are distinct and rational. The invariants are

```math
\begin{aligned}
 c_4&=16(\alpha^2-\alpha\beta+\beta^2),\\
 c_6&=-64(\alpha+\beta)^3+288(\alpha+\beta)\alpha\beta,\\
 \Delta&=16\alpha^2\beta^2(\alpha-\beta)^2,
\end{aligned}
```

and their two-adic valuations are $`(4,6,12)`$. For the twist by $`-1`$, substitute $`x_-=4X`$ and $`y_-=8Y+4X`$. This gives the integral model

**Equation (A.2).**

```math
Y^2+XY=X^3-\frac{\alpha+\beta+1}{4}X^2
                     +\frac{\alpha\beta}{16}X.
```

Its discriminant is $`\Delta/2^{12}`$, which is odd. The twist therefore has good reduction at $`2`$.

Fix an auxiliary coefficient prime $`ℓ\ne2`$. The quadratic character $`\chi`$ of $`\mathbb{Q}_2(i)`$ has conductor exponent two; on odd units it is $`\chi(u)=(-1)^{(u-1)/2}`$. Twisting the two-dimensional unramified $`ℓ`$‑adic representation of (A.2) by this character gives conductor exponent four. Its two unramified unitary eigencharacters have product one. The unramified factors in their epsilon constants cancel, leaving the square of the normalized quadratic Gauss factor $`W(\chi)`$. The identity $`W(\chi)^2=\chi(-1)=-1`$ therefore gives $`\varepsilon_2(E)=-1`$. These are the conductor and epsilon-factor identities of Rohrlich (1994), valid also in residue characteristic two. The displayed model is minimal: a smaller integral discriminant would have valuation zero, contradicting the ramified quadratic inertia just exhibited.

At every odd $`p\in S`$, coprimality gives $`v_p(c_4)=0`$ and $`v_p(\Delta)\gt 0`$. The reduction is multiplicative, with conductor exponent one. The node has split tangent directions according as

```math
\beta\ (p\mid\alpha),\qquad
 \alpha\ (p\mid\beta),\qquad
 -\alpha\ (p\mid\alpha-\beta)
```

is a square modulo $`p`$. The nonsplit primes are exactly

```math
23,47,89,283,4943,8893,23971,1073681107,354212181139.
```

The remaining nineteen odd bad primes are split. Their local root numbers therefore have product $`-1`$. Together with the real root number $`-1`$ and the root number at $`2`$, this gives $`\varepsilon(E)=-1`$.

At $`13`$, $`v_{13}(\alpha-\beta)=2`$ and $`v_{13}(\alpha\beta)=0`$. Consequently $`v_{13}(j(E))=-4`$. A CM $`j`$‑invariant is an algebraic integer, so $`E`$ is non-CM.

Modulo $`19`$ the equation is $`y^2=x(x+2)(x+4)`$. Its three points of ordinate zero have abscissas $`0,15,17`$. Each of $`5,6,7,11,12,13,14,18`$ gives two further affine points, and the remaining abscissas give none. Hence $`\#E(\mathbb{F}_{19})=20`$ and $`a_{19}(E)=0`$.

The local condition at a fixed nonarchimedean place is the derived Kummer condition. If $`B/L`$ is an elliptic curve, it is represented by $`B(L)^\wedge_2[-1]\to R\Gamma(L,T_2B)`$, using a free resolution before coefficient reduction. This retains both $`B(L)[2^n]`$ in degree zero and $`B(L)/2^nB(L)`$ in degree one. Over an imaginary quadratic field the Selmer complex is the cone

```math
\mathrm{Cone}\left(
 R\Gamma(G_{K,S},M)\oplus\bigoplus_{v\in S}U_v
       \longrightarrow\bigoplus_{v\in S}R\Gamma(K_v,M)
                 \right)[-1].
```

The positive real cone used over $`\mathbb{Q}`$ is specified separately in the cyclotomic argument.

## Appendix B. Classical nonvanishing with prescribed local classes

We use the following form of Hoffstein–Luo (1997, pp. 435–436). For an elliptic curve $`A/\mathbb{Q}`$ and an arbitrary finite set $`S`$ of rational primes, there are infinitely many odd fundamental discriminants $`v`$ with at most four prime factors such that $`L(A^{(v)},1)\ne0`$ and $`\chi_v(p)=1`$ at every $`p\in S`$. The bound on the number of prime factors is absolute.

**Proposition B.1.** Fix a nonempty filter of odd fundamental discriminants, given by a real sign and unit squareclasses at a finite set containing $`2N_A`$, and having root number $`+1`$ for the corresponding twists of $`A`$. For every finite exclusion set and every real bound $`B`$, the filter contains a discriminant $`d`$ such that

```math
L(A^{(d)},1)\ne0,\qquad \omega(\vert d\vert )\le5,
```

and every prime factor of $`d`$ exceeds $`B`$ and avoids the exclusions.

*Proof.* The prescribed unit class at two is $`1`$ or $`5`$ modulo eight, since an odd fundamental discriminant is $`1`$ modulo four. Choose a nonzero residue representative at every odd support prime. The Chinese remainder theorem and Dirichlet’s theorem give a positive prime $`u\gt B`$ in these classes, avoiding the exclusions. In particular $`u`$ is an odd fundamental discriminant. Apply Hoffstein–Luo to $`A^{(u)}`$ with a split set containing the original support, the primes of $`2N_{A^{(u)}}`$, $`u`$, the exclusions and every prime at most $`B`$.

The resulting $`v`$ is a local unit square at the original support, is coprime to $`u`$, and has at most four prime factors. Splitting at two gives $`v\equiv1\pmod8`$. Thus $`d=uv`$ is an odd fundamental discriminant with the required finite local classes and prime restrictions.

Let $`\sigma`$ be the prescribed sign. The quadratic-twist root-number formula, with the given local classes, gives $`\varepsilon(A^{(u)})=\sigma`$. Since $`v`$ is square at every conductor prime of $`A^{(u)}`$, nonvanishing forces

```math
1=\varepsilon((A^{(u)})^{(v)})
   =\varepsilon(A^{(u)})\mathrm{sgn}(v).
```

Hence $`\mathrm{sgn}(d)=\sigma`$. The twist $`(A^{(u)})^{(v)}`$ is $`A^{(d)}`$, proving the assertion. The prime count is at most five regardless of the size of the support or of the chosen primes.

**Proposition B.2.** For a nonempty unit filter as above having root number $`-1`$, and for every finite exclusion set and prime bound, there is a discriminant $`d`$ on that filter for which $`L'(A^{(d)},1)\ne0`$, with all prime factors satisfying the restrictions.

*Proof.* Bump–Friedberg–Hoffstein (1990, Theorem (i), pp. 543–544) supplies, for a weight-two newform of sign $`\varepsilon`$ and a finite set of primes containing its level, a fundamental discriminant $`v`$ with $`\varepsilon v\lt 0`$, splitting at all specified primes, whose twist has a simple central zero. This statement requires no nonzero central value for the original form.

Choose a positive prime $`u`$ representing the prescribed finite unit classes as in Proposition B.1. If the required sign is $`\sigma`$, then $`\varepsilon(A^{(u)})=-\sigma`$. Apply the cited derivative theorem to $`A^{(u)}`$, requiring splitting at the original support, at every conductor prime, at $`u`$, at all excluded primes and at every prime at most the bound. The product $`d=uv`$ is fundamental, has the prescribed local classes, and has sign $`-\varepsilon(A^{(u)})=\sigma`$. Its twist has a simple central zero. The splitting conditions give every prime restriction.

The discriminant sizes and the precision of the congruences may depend on the filter. Proposition B.1 keeps only the prime count uniform. This is sufficient when a previously chosen twist and a fixed finite product are absorbed into the curve before the proposition is applied.

---

[Appendix C →](appendix-c.md)
