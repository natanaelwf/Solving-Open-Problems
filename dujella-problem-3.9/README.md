# A Rational Diophantine Triple Answering Dujella's Problem 3.9

## An affirmative answer with torsion $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}$ and rank at least $8$ over $\mathbb{Q}(i)$

**Publication date:** 29 August 2026  
**Status:** Complete solution  
**Field:** Number theory, rational Diophantine triples, elliptic curves  

## Abstract

We give an explicit rational Diophantine triple whose induced elliptic curve satisfies

$$
E(\mathbb{Q}(i))_{\mathrm{tors}}\cong
\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z},
\qquad
\mathrm{rank}\,E(\mathbb{Q}(i))\ge 8.
$$

This answers Problem 3.9 in Dujella's list of open problems. The torsion statement is proved by a halving criterion and reduction at two split primes. The rank statement is certified by exact $2$-Kummer calculations on a rational curve and its $(-1)$-quadratic twist. The underlying specialization, whose rank is at least 8, was reported by Vinko Petričević in joint work with Andrej Dujella. The purpose of this article is to exhibit a rational Diophantine triple inducing that curve and to give a self-contained exact certificate.

## 1. Statement of the problem and the example

In the version of Dujella's open-problem list dated 29 August 2026, Problem 3.9 asks whether there is an elliptic curve over $\mathbb{Q}(i)$, induced by a rational Diophantine triple, with torsion group $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}$ and rank greater than $6$. We use the standard convention that a rational Diophantine triple is a set of three distinct nonzero rational numbers whose pairwise products, after adding $1$, are rational squares. In particular, $0=0^2$ is allowed. Dujella, Jukić Bokun, and Soldo (2017) explicitly use nonnegative rational square roots and, in the construction relevant here, take $b=-1/a$.

**Theorem 1.** Set

$$
\begin{aligned}
a&=\frac{338256750896}{519329865153},\\
b&=-\frac{519329865153}{338256750896},\\
c&=\frac{2118453423815502078396715008}
        {395270688488063020499821199375}.
\end{aligned}
$$

Then $\{a,b,c\}$ is a rational Diophantine triple. The elliptic curve

$$
C:\quad y_0^2=(a x_0+1)(b x_0+1)(c x_0+1)
$$

satisfies

$$
C(\mathbb{Q}(i))_{\mathrm{tors}}\cong \mathbb{Z}/4\mathbb{Z}\times \mathbb{Z}/4\mathbb{Z},
\qquad
\mathrm{rank}\,C(\mathbb{Q}(i))\ge 8.
$$

Consequently, $C$ gives an affirmative answer to Problem 3.9.

The rest of the note proves the theorem. All numerical identities below are exact rational or integer identities.

## 2. The triple and a convenient integral model

Direct simplification gives

$$
\begin{aligned}
ab+1&=0^2,\\
ac+1&=\left(\frac{44175660045337}{44098756684775}\right)^2,\\
bc+1&=\left(\frac{8926353364485863}{8963306864035225}\right)^2.
\end{aligned}
$$

The three displayed numbers are nonzero and pairwise distinct, so they form a rational Diophantine triple.

Put

$$
x=abc\,x_0,
\qquad
y=abc\,y_0.
$$

Then the induced curve becomes

$$
C':\quad y^2=(x+ab)(x+ac)(x+bc).
$$

Since $ab=-1$, the roots of the cubic on the right are

$$
\rho_0=1,
\qquad
\rho_1=-ac,
\qquad
\rho_2=-bc.
$$

Consider the integral curve

$$
E:\quad Y^2=X^3-X^2-AX-B,
$$

where

$$
\begin{aligned}
A&=1264285630784571919597349762400,\\
B&=546907189853176652858460972620151389392800000.
\end{aligned}
$$

Its cubic factors as

$$
X^3-X^2-AX-B=(X-R_0)(X-R_1)(X-R_2),
$$

with

$$
R_0=1298283376802401,
\quad
R_1=-637703335220400,
\quad
R_2=-660580041582000.
$$

Define

$$
s=\frac{421275422609655575}{9535001089},
\qquad
\beta=R_0-s^2.
$$

Using the three identities above, one checks

$$
s\frac{44175660045337}{44098756684775}=44259049,
\qquad
s\frac{8926353364485863}{8963306864035225}=43999849.
$$

It follows that

$$
s^2\rho_0+\beta=R_0,
\qquad
s^2\rho_1+\beta=R_2,
\qquad
s^2\rho_2+\beta=R_1.
$$

Both cubics are monic. Therefore the root correspondence above gives the polynomial identity

$$
\left.(X^3-X^2-AX-B)\right|_{X=s^2x+\beta}
=s^6(x+ab)(x+ac)(x+bc).
$$

Consequently,

$$
X=s^2x+\beta,
\qquad
Y=s^3y
$$

is a $\mathbb{Q}$-isomorphism $C'\to E$. Combined with the first scaling, it gives the direct isomorphism

$$
X=s^2abc\,x_0+\beta,
\qquad
Y=s^3abc\,y_0
$$

from $C$ to $E$. Thus it remains to prove the torsion and rank assertions for $E$.

## 3. The torsion subgroup over $\mathbb{Q}(i)$

### 3.1. Full $4$-torsion

We use the standard halving criterion for a curve

$$
y^2=(x-e_0)(x-e_1)(x-e_2)
$$

with full rational $2$-torsion: the point $(e_j,0)$ is divisible by $2$ over a field $K$ if and only if both differences $e_j-e_k$, $k\ne j$, are squares in $K$. This is the standard halving criterion arising in $2$-descent; see Silverman (2009).

For these roots,

$$
R_0-R_1=43999849^2,
\qquad
R_0-R_2=44259049^2,
\qquad
R_1-R_2=4782960^2.
$$

Every positive signed difference is a square in $\mathbb{Q}$, and every negative signed difference is a square in $\mathbb{Q}(i)$ because $-1=i^2$. Hence each nonzero point of $E[2]$ is divisible by $2$ over $\mathbb{Q}(i)$. Halves of two independent $2$-torsion points generate a subgroup isomorphic to $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}$. Since $E[4]$ has exactly $16$ geometric points,

$$
E[4]\subseteq E(\mathbb{Q}(i)).
$$

### 3.2. Excluding additional torsion

The rational primes $17$ and $29$ split in $\mathbb{Z}[i]$:

$$
17=(4+i)(4-i),
\qquad
29=(5+2i)(5-2i).
$$

At either prime above $p$, the residue field is $\mathbb{F}_p$. The reductions of $R_0,R_1,R_2$ are distinct, so the curve has good reduction. Direct point counts give


| $p$  | reduced roots | $N_+$ | $\sum_x\chi(f(x))$ | $\mathrm{card}\,E(\mathbb{F}_p)$ |
|:----:|:-------------:|:--------------:|:------------------:|:-------------------:|
| $17$ |    $4,6,8$    |      $6$       |        $-2$        |        $16$         |
| $29$ |   $2,6,22$    |      $14$      |        $2$         |        $32$         |


Here $N_+$ denotes the number of $x\in\mathbb{F}_p$ for which $\chi(f(x))=1$, where $f(X)=(X-R_0)(X-R_1)(X-R_2)$. The quadratic character is extended by $\chi(0)=0$, so

$$
\mathrm{card}\,E(\mathbb{F}_p)=p+1+\sum_{x\in\mathbb{F}_p}\chi(f(x)).
$$

For completeness, the values with $\chi(f(x))=1$ are

$$
\begin{aligned}
p=17:&\quad x\in\{3,9,13,14,15,16\},\\
p=29:&\quad x\in\{3,5,8,10,12,15,16,17,19,21,23,24,25,26\}.
\end{aligned}
$$

Together with the three reduced roots in each row, these lists give the displayed orders directly.

For good reduction at a prime of residue characteristic $p$, reduction is injective on torsion of order prime to $p$. Reduction at a prime above $17$ therefore shows that every torsion subgroup of order prime to $17$ has order dividing $16$. In particular, the $2$-primary torsion has order at most $16$, and all odd-primary torsion vanishes except possibly the $17$-primary part. The latter injects at a prime above $29$, but $17\nmid 32$, so it is also trivial. Hence

$$
\mathrm{card}\,E(\mathbb{Q}(i))_{\mathrm{tors}}\le 16.
$$

Together with the inclusion above, this proves

$$
E(\mathbb{Q}(i))_{\mathrm{tors}}\cong \mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}.
$$

## 4. A rank lower bound over $\mathbb{Q}(i)$

### 4.1. Quadratic-twist decomposition

For an elliptic curve over $\mathbb{Q}$ and a quadratic extension $\mathbb{Q}(\sqrt d)$,

$$
\mathrm{rank}\,E(\mathbb{Q}(\sqrt d))=\mathrm{rank}\,E(\mathbb{Q})+\mathrm{rank}\,E^{(d)}(\mathbb{Q}),
$$

where $E^{(d)}$ is the $d$-quadratic twist. Thus

$$
\mathrm{rank}\,E(\mathbb{Q}(i))=\mathrm{rank}\,E(\mathbb{Q})+\mathrm{rank}\,E^{(-1)}(\mathbb{Q}).
$$

This is the decomposition into the two eigenspaces of complex conjugation; it is also the method used for this family by Dujella and Jukić Bokun (2010) and by Petričević (2023).

A convenient integral model of the $(-1)$-twist is

$$
E^-:\quad y^2+xy=x^3-C_4x+C_6,
$$

where

$$
\begin{aligned}
C_4&=79017851924035744974834360150,\\
C_6&=8545424841455885200913452697189865459262500.
\end{aligned}
$$

Indeed, $16C_4=A$ and $64C_6=B$, and the change of variables

$$
U=4x,
\qquad
V=8y+4x
$$

turns the generalized twist model into

$$
V^2=(U-660580041582000)(U-637703335220400)(U+1298283376802401),
$$

which is $V^2=U^3+U^2-AU+B$, the $(-1)$-twist of $E$.

### 4.2. The $2$-Kummer certificate

Let

$$
E_0:\quad y^2=(x-e_0)(x-e_1)(x-e_2),
\qquad e_j\in\mathbb{Q}.
$$

The standard $2$-descent map gives an injective homomorphism

$$
\delta:E_0(\mathbb{Q})/2E_0(\mathbb{Q})\hookrightarrow
(\mathbb{Q}^{\times}/\mathbb{Q}^{\times 2})^2.
$$

For $x\ne e_0,e_1$,

$$
\delta(x,y)=([x-e_0],[x-e_1]).
$$

For the $2$-torsion point $T=(e_1,0)$, the same map is represented by

$$
\delta(T)=([e_1-e_0],[(e_1-e_0)(e_1-e_2)]).
$$

Valuation parity $v_p\bmod 2$ and the real sign are linear characters on $\mathbb{Q}^{\times}/\mathbb{Q}^{\times 2}$. Therefore an invertible binary character matrix certifies independence of Kummer classes.

### 4.3. The rational curve $E$

The points $P_1,\ldots,P_4,S,T$ are listed in Appendix A. Exact substitution verifies that they lie on $E$, and the duplication formula gives $2S=(R_0,0)$ while $T=(R_1,0)$. Thus $S$ and $T$ represent the two torsion directions in $E(\mathbb{Q})/2E(\mathbb{Q})$. Their Kummer square classes, with $(e_0,e_1,e_2)=(R_0,R_1,R_2)$, are


| point |                  $[x-R_0]$                  |             $[x-R_1]$             |
|:-----:|:-------------------------------------------:|:---------------------------------:|
| $P_1$ |             $41\cdot47\cdot113$             |         $5\cdot13\cdot47$         |
| $P_2$ |             $41\cdot47\cdot233$             |     $2\cdot13\cdot47\cdot73$      |
| $P_3$ |    $-41\cdot47\cdot103\cdot113\cdot233$     |    $-2\cdot13\cdot47\cdot103$     |
| $P_4$ |        $-47\cdot61\cdot113\cdot149$         |    $-47\cdot61\cdot73\cdot149$    |
|  $S$  | $47\cdot61\cdot103\cdot113\cdot149\cdot233$ | $2\cdot47\cdot61\cdot103\cdot149$ |
|  $T$  |                    $-1$                     |               $-1$                |


The exact square factors behind this table are also printed in Appendix A.

Apply, in this order, the six characters

$$
v_5(\delta_2),\quad
v_{73}(\delta_2),\quad
v_2(\delta_2),\quad
v_{103}(\delta_1),\quad
\mathrm{sgn}_2(\delta_1),\quad
v_{61}(\delta_1),
$$

where $\mathrm{sgn}_2$ is $1$ on negative classes and $0$ on positive classes. The resulting row matrix is

$$
M_E=
\begin{pmatrix}
1&0&0&0&0&0\\
0&1&1&0&0&0\\
0&0&1&1&1&0\\
0&1&0&0&1&1\\
0&0&1&1&0&1\\
0&0&0&0&1&0
\end{pmatrix},
\qquad
\det(M_E)=-1.
$$

Its reduction modulo $2$ is nonsingular. Hence the six classes are independent in $E(\mathbb{Q})/2E(\mathbb{Q})$ and

$$
\dim_{\mathbb{F}_2}E(\mathbb{Q})/2E(\mathbb{Q})\ge 6.
$$

Since $E$ has full rational $2$-torsion,

$$
\dim_{\mathbb{F}_2}E(\mathbb{Q})/2E(\mathbb{Q})
=\mathrm{rank}\,E(\mathbb{Q})+\dim_{\mathbb{F}_2}E(\mathbb{Q})[2]
=\mathrm{rank}\,E(\mathbb{Q})+2.
$$

Therefore

$$
\mathrm{rank}\,E(\mathbb{Q})\ge 4.
$$

### 4.4. The $(-1)$-twist

The four points $Q_1,\ldots,Q_4$ in Appendix A lie on the generalized twist model. After the change of variables above, they lie on the monic twist model. We also use the points $S^-$ and $T^-$ printed there; on the monic model, $2S^-=(660580041582000,0)$ and $T^-=(637703335220400,0)$. For the first Kummer coordinate $U-660580041582000$, the square classes are


| point |          $[U-660580041582000]$          |
|:-----:|:---------------------------------------:|
| $Q_1$ | $2\cdot3\cdot5\cdot41\cdot113\cdot233$  |
| $Q_2$ |    $3\cdot7\cdot73\cdot113\cdot233$     |
| $Q_3$ |         $2\cdot3\cdot7\cdot73$          |
| $Q_4$ |    $-2\cdot5\cdot73\cdot113\cdot233$    |
| $S^-$ | $5\cdot7\cdot13\cdot73\cdot113\cdot233$ |
| $T^-$ |                  $-1$                   |


Using the characters

$$
v_2,\quad v_5,\quad v_{41},\quad v_7,\quad \mathrm{sgn}_2,\quad v_{13},
$$

we obtain

$$
M_-=
\begin{pmatrix}
1&1&1&0&0&0\\
0&0&0&1&0&0\\
1&0&0&1&0&0\\
1&1&0&0&1&0\\
0&1&0&1&0&1\\
0&0&0&0&1&0
\end{pmatrix},
\qquad
\det(M_-)=-1.
$$

Only one Kummer coordinate is needed here: a relation among the full Kummer classes would give the same relation among their first-coordinate images. Since the displayed images are independent, the full classes are independent. The twist also has full rational $2$-torsion, so

$$
\mathrm{rank}\,E^{(-1)}(\mathbb{Q})\ge 4.
$$

Combining the quadratic-twist decomposition, the bound $\mathrm{rank}\,E(\mathbb{Q})\ge 4$, and the twist bound, we conclude that

$$
\mathrm{rank}\,E(\mathbb{Q}(i))\ge 4+4=8>6.
$$

The torsion computation and the final rank bound, transported through the $\mathbb{Q}$-isomorphism above, complete the proof of Theorem 1.

**Remark 1.** The argument proves the lower bound $\mathrm{rank}\,E(\mathbb{Q}(i))\ge 8$. It does not prove that the rank is exactly $8$, and exact equality is not required by Problem 3.9.


## 5. Origin of the rank specialization

The specialization underlying $E$, with parameter $v=180/6643$, and four rational points on each of the curve and its $(-1)$-twist were reported by Petričević (2023), in joint work with Dujella. The present note supplies the additional datum required by Problem 3.9: an explicit rational Diophantine triple inducing a $\mathbb{Q}$-isomorphic curve. Appendix B records an exact pullback that produces the displayed triple from this specialization.

## Appendix A. Exact points and square-class decompositions

### A.1. Points on $E$

The curve is $E$. The points used above are

$$
\begin{aligned}
x(P_1)&=\frac{18434717483122731307680720}{784728169},\\
y(P_1)&=\frac{79058306885031575731369370665045739520}{21982590198197},\\
x(P_2)&=\frac{205575756477590805858000}{19351201},\\
y(P_2)&=\frac{92664057348302315420944897563312000}{85125933199},\\
x(P_3)&=-\frac{1333100296085788798313904}{2019513721},\\
y(P_3)&=\frac{13040064683254174542549826666008960}{90754927108019},\\
x(P_4)&=-\frac{307245410407559064903399631}{465158100625},\\
y(P_4)&=\frac{16672539824494902460966518939675019528}{317249453578765625},\\
S&=(3245674849686002,\ 171874625371303506531698),\\
T&=(-637703335220400,\ 0).
\end{aligned}
$$

Direct substitution gives $y(P)^2=X(P)^3-X(P)^2-AX(P)-B$ for every listed point.

The exact decompositions used in the Kummer table are

$$
\begin{aligned}
x(P_1)-R_0
 &= (41\cdot47\cdot113)
    \left(\frac{8943203351}{28013}\right)^2,\\
x(P_1)-R_1
 &= (5\cdot13\cdot47)
    \left(\frac{78727900032}{28013}\right)^2,\\
x(P_2)-R_0
 &= (41\cdot47\cdot233)
    \left(\frac{633960983}{4399}\right)^2,\\
x(P_2)-R_1
 &= (2\cdot13\cdot47\cdot73)
    \left(\frac{1562959080}{4399}\right)^2,\\
x(P_3)-R_0
 &= -(41\cdot47\cdot103\cdot113\cdot233)
    \left(\frac{27510385}{44939}\right)^2,\\
x(P_3)-R_1
 &= -(2\cdot13\cdot47\cdot103)
    \left(\frac{599588712}{44939}\right)^2,\\
x(P_4)-R_0
 &= -(47\cdot61\cdot113\cdot149)
    \left(\frac{4344595208}{682025}\right)^2,\\
x(P_4)-R_1
 &= -(47\cdot61\cdot73\cdot149)
    \left(\frac{583366147}{682025}\right)^2,\\
x(S)-R_0
 &= (47\cdot61\cdot103\cdot113\cdot149\cdot233)\,41^2,\\
x(S)-R_1
 &= (2\cdot47\cdot61\cdot103\cdot149)\,6643^2.
\end{aligned}
$$

For $T=(R_1,0)$,

$$
R_1-R_0=-43999849^2,
\qquad
(R_1-R_0)(R_1-R_2)=-(43999849\cdot4782960)^2,
$$

so the torsion formula above gives the class $(-1,-1)$.

### A.2. Points on the $(-1)$-twist

The first four points are on the generalized twist model:

$$
\begin{aligned}
Q_1&=(469572437338020,\ 8659141260066207245250),\\
x(Q_2)&=\frac{7862279875666677393237}{17606416},\\
y(Q_2)&=\frac{583152676543238826927776148008847}{73876521536},\\
Q_3&=(177864765470100,\ 343279086114405591450),\\
x(Q_4)&=\frac{447490645354678560274980}{2884441849},\\
y(Q_4)&=\frac{22220310008210701689236734902375750}{154914718384243}.
\end{aligned}
$$

After $(U,V)=(4x,8y+4x)$, they lie on the monic twist model. On that model we also use

$$
S^-=(872269302587040,\ 10381666643412520725360),
\qquad
T^-=(637703335220400,\ 0).
$$

The exact first-coordinate decompositions are

$$
\begin{aligned}
U(Q_1)-660580041582000
 &= (2\cdot3\cdot5\cdot41\cdot113\cdot233)\,6132^2,\\
U(Q_2)-660580041582000
 &= (3\cdot7\cdot73\cdot113\cdot233)
    \left(\frac{11079471}{2098}\right)^2,\\
U(Q_3)-660580041582000
 &= (2\cdot3\cdot7\cdot73)\,128820^2,\\
U(Q_4)-660580041582000
 &= -(2\cdot5\cdot73\cdot113\cdot233)
    \left(\frac{77500332}{53707}\right)^2,\\
U(S^-)-660580041582000
 &= (5\cdot7\cdot13\cdot73\cdot113\cdot233)\,492^2,\\
U(T^-)-660580041582000
 &= -4782960^2.
\end{aligned}
$$

## Appendix B. Derivation of the inducing triple

This appendix is not needed for the proof of Theorem 1; it explains how the explicit triple can be recovered from the reported specialization of rank at least 8.

A standard one-parameter family carrying full $4$-torsion over $\mathbb{Q}(i)$ is given by Dujella and Jukić Bokun (2010):

$$
\mathcal E_v:\quad
 y^2+4xy+(4-64v^4)y=x^3+(1-16v^4)x^2.
$$

The change

$$
X=x+1-16v^4,
\qquad
Y=y+2x+2-32v^4
$$

gives the full-$2$-torsion model

$$
F_v:\quad
Y^2=X\bigl(X+(1-4v^2)^2\bigr)\bigl(X+(1+4v^2)^2\bigr).
$$

The two-parameter family of Dujella, Jukić Bokun, and Soldo (2017) is

$$
a=\frac{\tau u+1}{\tau-u},
\qquad
b=-\frac1a,
\qquad
c=\frac{4\tau u}{(\tau u+1)(\tau-u)}.
$$

It is a rational Diophantine triple whenever the displayed expressions are admissible. Impose

$$
u(\tau^2+1)=4v^2\tau(u^2+1).
$$

Set

$$
r_1=\frac{\tau+u}{\tau-u},
\qquad
r_2=\frac{\tau u-1}{\tau u+1}.
$$

This condition is equivalent to

$$
r_1+r_2=4v^2(r_1-r_2).
$$

With $\lambda=2/(r_1-r_2)$, translation of the scaled induced curve by $x\mapsto x-1$, followed by

$$
X=\lambda^2(x-1),
\qquad
Y=\lambda^3y,
$$

sends its roots to

$$
0,
\quad -(1-4v^2)^2,
\quad -(1+4v^2)^2.
$$

Thus the curve induced by the two-parameter family is $\mathbb{Q}$-isomorphic to $F_v$.

Viewed as a quadratic in $u$, the condition above has square discriminant precisely when

$$
\eta^2=\tau^4+(2-64v^4)\tau^2+1.
$$

The substitutions

$$
r=\frac{\eta+1}{\tau^2},
\qquad
W=2r+2,
\qquad
z=2\tau(r^2-1)
$$

transform the quartic equation into

$$
D_v:\quad z^2=W(W-4)(W-64v^4).
$$

The degree-$2$ isogeny from $F_v$ to $D_v$ is

$$
W=\frac{Y^2}{X^2},
\qquad
z=\frac{Y\bigl((1-16v^4)^2-X^2\bigr)}{X^2}.
$$

Now take

$$
v=\frac{180}{6643},
\qquad
L=44129449.
$$

Then

$$
1-4v^2=\frac{43999849}{L},
\qquad
1+4v^2=\frac{44259049}{L},
$$

and the map

$$
X_E=L^2X+R_0,
\qquad
Y_E=L^3Y
$$

identifies $F_v$ with $E$. Transfer $P_1$ from Appendix A to $F_v$ by

$$
X_1=\frac{x(P_1)-R_0}{L^2},
\qquad
Y_1=\frac{y(P_1)}{L^3}.
$$

Applying the displayed $2$-isogeny gives

$$
\begin{aligned}
W&=\frac{4293625223577600}{318418364406961},\\
z&=-\frac{16346043633252561844056883200}
          {393628226387937104654720357}.
\end{aligned}
$$

The inverse formulas

$$
r=\frac{W-2}{2},
\qquad
\tau=\frac{z}{2(r^2-1)},
\qquad
\eta=r\tau^2-1
$$

give

$$
\begin{aligned}
\tau&=-\frac{257579450961}{396627408848},\\
\eta&=\frac{37798484235380372589723575}
           {26585947944961874728120576}.
\end{aligned}
$$

Choosing the corresponding root of the condition above,

$$
u=\frac{\tau^2+1+\eta}{8v^2\tau}
  =-\frac{1229610544128}{1649489479}.
$$

Substitution of these values into the two-parameter family gives exactly the triple stated in Theorem 1.

## Appendix C. Ancillary exact verification

The accompanying script `verify_problem_3_9.py` uses only Python's standard library and exact integer or rational arithmetic. It checks the Diophantine identities, the coefficient-level isomorphism, both finite-field point counts, all listed points and square-class decompositions, the two binary matrix ranks, and the pullback in Appendix B.

Run it from this directory with

```console
python3 verify_problem_3_9.py
```

A successful run prints

```text
All exact checks passed.
  triple: verified
  Q-isomorphism: verified coefficient-by-coefficient
  torsion: E[4] over Q(i), #E(F_17)=16, #E(F_29)=32
  Kummer ranks: 6 for E and 6 for its (-1)-twist
  conclusion: torsion = Z/4Z x Z/4Z and rank over Q(i) >= 8
  reconstruction of the triple from v=180/6643: verified
```

The script is supplementary; every mathematical certificate used in the proof is displayed in the article.

## References

- Dujella, A. (2026). *Open problems on Diophantine $m$-tuples and elliptic curves*, version dated 29 August 2026, Problem 3.9.

- Dujella, A., and Jukić Bokun, M. (2010). *On the rank of elliptic curves over $\mathbb{Q}(i)$ with torsion group $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}$*. Proc. Japan Acad. Ser. A Math. Sci. **86**, 93–96.

- Dujella, A., Jukić Bokun, M., and Soldo, I. (2017). *On the torsion group of elliptic curves induced by Diophantine triples over quadratic fields*. Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. RACSAM **111**, 1177–1185.

- Petričević, V. (2023). *Searching for elliptic curves with high rank in the PARI/GP software package*. Presentation, 23 June 2023, joint work with A. Dujella.

- Silverman, J. H. (2009). *The Arithmetic of Elliptic Curves*, 2nd ed. Graduate Texts in Mathematics 106, Springer.
