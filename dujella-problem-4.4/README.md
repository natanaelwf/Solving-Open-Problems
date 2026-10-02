# Uniqueness of a Smaller Extension of a Diophantine Triple

## A complete negative solution to Dujella's Problem 4.4

**Publication date:** 2 October 2026  
**Field:** Number theory, Diophantine tuples

## Abstract

We prove that there are no positive integers $a_1\lt a_2\lt b\lt c\lt d$ for which both $\{a_1,b,c,d\}$ and $\{a_2,b,c,d\}$ are Diophantine quadruples. This gives a negative answer to Problem 4.4 in Dujella's list of open problems. Starting from published necessary conditions for such a pair of quadruples, we compare the residues of their Pell representations and force the initial values to be $\pm1$ with even indices. Two positive regular descents give an additional lower bound for $c$, which permits an application of an explicit theorem on simultaneous approximation. A congruence argument and the approximation estimate then yield the incompatible bounds $n\gt4b$ and $n\lt100\log b$ for the same index. The proof uses the cited published results and requires no additional finite search.

**Keywords:** Diophantine quadruples; Pell equations; regular descent; simultaneous approximation.

## 1. Introduction and statement of the result

A Diophantine tuple is a set of distinct positive integers such that the product of any two distinct elements, increased by $1$, is a perfect square. We consider extensions of a fixed Diophantine triple by a positive integer smaller than each of its elements.

Problem 4.4 in Dujella's problem list asks whether two Diophantine quadruples $\{a_1,b,c,d\}$ and $\{a_2,b,c,d\}$ can satisfy

```math
a_1\lt a_2\lt b\lt c\lt d.
```

Cipu, Dujella and Fujita (2022) established necessary inequalities for any such configuration and proved that there are only finitely many possibilities. We show that there are none.

**Theorem 1.1.** There do not exist positive integers

```math
a_1\lt a_2\lt b\lt c\lt d
```

such that both $\{a_1,b,c,d\}$ and $\{a_2,b,c,d\}$ are Diophantine quadruples.

**Corollary 1.2.** For a fixed Diophantine triple $\{b,c,d\}$ with $b\lt c\lt d$, there is at most one positive integer $a\lt b$ such that $\{a,b,c,d\}$ is a Diophantine quadruple.

**Proof of Corollary 1.2.** Two such integers could be ordered as $a_1\lt a_2\lt b$, contradicting Theorem 1.1.

The assertion concerns uniqueness when a smaller extension exists. No condition on $a_1a_2+1$ is imposed. In particular, the union of the two quadruples is not assumed to be a Diophantine quintuple.

For the proof of Theorem 1.1, suppose throughout that a counterexample exists and write:

**Equation (1.1).**

```math
\begin{aligned}
u&=a_1,\\
A&=a_2,\\
B&=b,\\
C&=c,\\
D&=d.
\end{aligned}
```

All square roots below are positive, and all logarithms are natural. Square roots arising from the Diophantine conditions are integers.

## 2. Published restrictions and the Pell representations

### 2.1. Necessary inequalities

The Main Theorem and Corollary 1.3 of Cipu, Dujella and Fujita (2022) apply to precisely the configuration in Equation (1.1). They give:

**Equation (2.1).**

```math
\begin{aligned}
A&\gt13824,\\
B&\gt13A,\\
B&\lt A^{3/2},
\end{aligned}
```

and:

**Equation (2.2).**

```math
16u^2B^3\lt C\lt16AB^3.
```

In particular:

**Equation (2.3).**

```math
\begin{aligned}
B&\gt179712,\\
B^2&\lt A^3,\\
C&\gt B^3,\\
C&\gt4B,\\
C&\lt16B^4.
\end{aligned}
```

Here $179712=13\cdot13824$, and we used $u\ge1$ and $A\lt B$.

### 2.2. The complete classification needed here

Fix $a\in\{u,A\}$ and put

```math
\begin{aligned}
r^2&=aB+1,\\
s^2&=aC+1,\\
T^2&=BC+1,\\
Z^2&=CD+1.
\end{aligned}
```

Writing $X_a^2=aD+1$ and $Y^2=BD+1$, elimination of $D$ gives:

**Equation (2.4).**

```math
\begin{aligned}
aZ^2-CX_a^2&=a-C,\\
BZ^2-CY^2&=B-C.
\end{aligned}
```

The Pell classification in Cipu, Fujita and Miyazaki (2018, Theorem 2.1), together with the recurrence representation stated there, gives nonnegative integers $m,n$ and initial solutions with positive auxiliary coordinates $x_0,y_1$ such that $Z=v_m=w_n$, where:

**Equation (2.5).**

```math
\begin{aligned}
v_0&=z_0,\\
v_1&=sz_0+Cx_0,\\
v_{j+2}&=2sv_{j+1}-v_j,\\
w_0&=z_1,\\
w_1&=Tz_1+Cy_1,\\
w_{j+2}&=2Tw_{j+1}-w_j.
\end{aligned}
```

Set $\rho=Cr-sT$. The possibilities relevant to these representations are exactly the following; the case in which both indices are even has been divided into two rows.

| $m$ | $n$ | $\lvert z_0\rvert$ | $\lvert z_1\rvert$ | Sign condition |
|---|---|---:|---:|---|
| even | even | $1$ | $1$ | $z_0=z_1$ |
| even | even | $\rho$ | $\rho$ | $z_0=z_1$ |
| odd | even | $T$ | $\rho$ | $z_0z_1\lt0$ |
| even | odd | $\rho$ | $s$ | $z_0z_1\lt0$ |
| odd | odd | $T$ | $s$ | $z_0z_1\gt0$ |

In the first row, $x_0=y_1=1$. We do not need the auxiliary coordinates in the remaining rows. Notice that $\rho\gt0$, since

```math
\begin{aligned}
(Cr)^2-(sT)^2
&=C^2-(a+B)C-1\\
&\gt C(C-2B)-1\\
&\gt0.
\end{aligned}
```

The classification used here assumes $a\lt B\lt C\lt D$. The additional clause in the cited theorem concerning extensions larger than the regular extension is not needed.

Because $s^2\equiv T^2\equiv1\pmod C$, induction in Equation (2.5) gives:

**Equation (2.6).**

```math
\begin{aligned}
v_{2j}&\equiv z_0\pmod C,\\
v_{2j+1}&\equiv sz_0\pmod C,\\
w_{2j}&\equiv z_1\pmod C,\\
w_{2j+1}&\equiv Tz_1\pmod C.
\end{aligned}
```

The first row of the table therefore gives $Z\equiv\pm1\pmod C$. Each remaining row gives $Z\equiv\pm sT\pmod C$, using $\rho\equiv-sT\pmod C$ where appropriate. Thus every representation belongs to one of the following two types:

```math
\begin{aligned}
\mathcal P&:\quad Z\equiv\pm1\pmod C,\\
\mathcal Q&:\quad Z\equiv\pm sT\pmod C,
\end{aligned}
```

where type $\mathcal P$ is the first row and type $\mathcal Q$ comprises the other four rows.

**Lemma 2.1.** The representations corresponding to both $a=u$ and $a=A$ are of type $\mathcal P$, with the same sign.

**Proof.** Write $s_1^2=uC+1$ and $s_2^2=AC+1$. We have

```math
0\lt s_1\lt s_2\lt T,
\qquad
2T\lt C.
```

For the last inequality, since $C\gt4B$ and $B,C$ are integers,

```math
\begin{aligned}
C^2-4T^2
&=C(C-4B)-4\\
&\ge C-4\\
&\gt0.
\end{aligned}
```

Moreover, $T^2\equiv1\pmod C$, so $T$ is invertible modulo $C$.

If both representations had type $\mathcal Q$, their residues for the same integer $Z$ would give $s_1\equiv\pm s_2\pmod C$. This is impossible: both $s_2-s_1$ and $s_2+s_1$ lie strictly between $0$ and $C$.

If one representation had type $\mathcal P$ and the other type $\mathcal Q$, then $sT\equiv\pm1\pmod C$ for $s=s_1$ or $s=s_2$. Multiplication by $T$ would give $s\equiv\pm T\pmod C$. This is again impossible because $0\lt s\lt T$ and $s+T\lt2T\lt C$.

Both representations therefore have type $\mathcal P$. Their signs agree because they give the same residue of $Z$ modulo $C$, and $C\gt2$.

From now on we use only the representation for $\{A,B,C,D\}$. Put $S=\sqrt{AC+1}$. By Lemma 2.1, for one fixed $\varepsilon\in\{-1,1\}$ we have:

**Equation (2.7).**

```math
\begin{aligned}
v_0&=\varepsilon,\\
v_1&=C+\varepsilon S,\\
v_{j+2}&=2Sv_{j+1}-v_j,\\
w_0&=\varepsilon,\\
w_1&=C+\varepsilon T,\\
w_{j+2}&=2Tw_{j+1}-w_j,
\end{aligned}
```

with $Z=v_m=w_n$ and $m,n$ even. Since $D\gt C$, we have $Z\gt C\gt1$, so neither index is zero. Hence:

**Equation (2.8).**

```math
m\ge2,
\qquad
n\ge2.
```

## 3. Two positive regular descents

**Lemma 3.1.** If $\{A,B,C\}$ is a Diophantine triple with $B\gt13A$ and $C\gt B^3$, then:

**Equation (3.1).**

```math
C\gt16A^2B^2.
```

**Proof.** Let $R=\sqrt{AB+1}$ and $C_0=A+B+2R$. For real $X\ge0$, define

```math
\begin{aligned}
f(X)
&=A+B+(2AB+1)X\\
&\qquad+2R\sqrt{AX+1}\sqrt{BX+1}.
\end{aligned}
```

All factors are positive, both square roots are increasing, and $2AB+1\gt0$, so $f$ is strictly increasing.

For an integer $X$ such that $AX+1=S_X^2$ and $BX+1=T_X^2$ are integer squares, put:

**Equation (3.2).**

```math
\begin{aligned}
d_{\pm}(A,B,X)
&=A+B+(2AB+1)X\\
&\qquad\pm2RS_XT_X.
\end{aligned}
```

These are integers and satisfy:

**Equation (3.3).**

```math
\begin{aligned}
Ad_-(A,B,X)+1&=(RS_X-AT_X)^2,\\
Bd_-(A,B,X)+1&=(RT_X-BS_X)^2.
\end{aligned}
```

Indeed, expanding the first square gives

```math
\begin{aligned}
&(RS_X-AT_X)^2\\
&=(AB+1)(AX+1)\\
&\qquad+A^2(BX+1)\\
&\qquad-2ARS_XT_X\\
&=1+A\bigl(A+B+(2AB+1)X\bigr)\\
&\qquad-2ARS_XT_X,
\end{aligned}
```

and the second identity follows by interchanging $A$ and $B$. Another direct expansion yields:

**Equation (3.4).**

```math
\begin{aligned}
d_+(A,B,X)d_-(A,B,X)
&=(X-A-B)^2\\
&\qquad-4(AB+1).
\end{aligned}
```

If $X\gt C_0$, the right side of Equation (3.4) is positive and smaller than $X^2$. Also $RS_XT_X\gt ABX$ for $X\gt0$, and consequently $d_+(A,B,X)\gt4ABX$. Thus, for $X\gt C_0$:

**Equation (3.5).**

```math
0\lt d_-(A,B,X)\lt\frac{X}{4AB}.
```

For $X\gt C_0$, we next verify that the descent is inverted by $f$:

**Equation (3.6).**

```math
f\bigl(d_-(A,B,X)\bigr)=X.
```

Since $X\gt C_0\gt B$, the identities

```math
\begin{aligned}
(RS_X)^2-(AT_X)^2
&=A(B+X-A)+1\\
&\gt0,\\
(RT_X)^2-(BS_X)^2
&=B(A+X-B)+1\\
&\gt0
\end{aligned}
```

show that the positive square roots in Equation (3.3) are exactly $RS_X-AT_X$ and $RT_X-BS_X$. Their product is

```math
(2AB+1)S_XT_X-R(2ABX+A+B).
```

Substitution in $f(d_-)$ cancels the constant terms and the terms containing $S_XT_X$. The remaining coefficient of $X$ is

```math
(2AB+1)^2-4AB(AB+1)=1,
```

which proves Equation (3.6).

The inequality $B\gt13A$ implies $B\ge14$ and

```math
R^2=AB+1
\lt\frac{B^2}{13}+1
\lt\frac{B^2}{9},
```

because $4B^2/117\gt1$ for $B\ge14$. Therefore $R\lt B/3$. The identities

```math
\begin{aligned}
AC_0+1&=(A+R)^2,\\
BC_0+1&=(B+R)^2
\end{aligned}
```

give $f(C_0)=4R(A+R)(B+R)$, whence:

**Equation (3.7).**

```math
\begin{aligned}
f(C_0)
&\lt\frac{4B}{3}
\left(\frac{B}{13}+\frac{B}{3}\right)
\left(B+\frac{B}{3}\right)\\
&=\frac{256}{351}B^3\\
&\lt B^3.
\end{aligned}
```

Also $f(C_0)\gt4ABC_0\gt C_0$, by the same estimate for $d_+$ used above. Hence $C\gt B^3\gt C_0$.

Set $E=d_-(A,B,C)$. By Equation (3.5), $E$ is a positive integer, and Equation (3.6) gives $f(E)=C$. If $E\le C_0$, monotonicity and Equation (3.7) would imply $C=f(E)\le f(C_0)\lt B^3$, a contradiction. Therefore $E\gt C_0$. The identities in Equation (3.3) make $AE+1$ and $BE+1$ integer squares, so a second descent is available:

```math
H=d_-(A,B,E).
```

Again $H$ is a positive integer. Applying Equation (3.5) twice gives

```math
1\le H
\lt\frac{E}{4AB}
\lt\frac{C}{16A^2B^2},
```

proving Equation (3.1).

**Remark.** The two regular descents are auxiliary constructions involving $A,B,C$. No regularity assumption on the original quadruple $\{A,B,C,D\}$ is used.

## 4. A lower bound for the even index

**Lemma 4.1.** For the fixed representation in Equation (2.7):

**Equation (4.1).**

```math
n\gt\sqrt{C/B}\gt4uB\ge4B.
```

**Proof.** Define

```math
\begin{aligned}
\alpha&=S+\sqrt{AC},\\
\beta&=T+\sqrt{BC},\\
p&=\sqrt{C/A},\\
q_0&=\sqrt{C/B}.
\end{aligned}
```

Since $S^2-AC=T^2-BC=1$, the closed forms of the recurrences are:

**Equation (4.2).**

```math
\begin{aligned}
2v_j&=(p+\varepsilon)\alpha^j-(p-\varepsilon)\alpha^{-j},\\
2w_j&=(q_0+\varepsilon)\beta^j-(q_0-\varepsilon)\beta^{-j}.
\end{aligned}
```

These formulas have the initial values in Equation (2.7) and satisfy its characteristic equations, so they hold for every nonnegative integer $j$.

For $h\gt1$ and $x\gt1$, set

```math
G_\varepsilon(h,x)
=(h+\varepsilon)x-\frac{h-\varepsilon}{x}.
```

This function is strictly increasing in both variables, since

```math
\begin{aligned}
\frac{\partial G_\varepsilon}{\partial h}
&=x-x^{-1}\gt0,\\
\frac{\partial G_\varepsilon}{\partial x}
&=h+\varepsilon+\frac{h-\varepsilon}{x^2}\gt0.
\end{aligned}
```

As $p\gt q_0\gt1$, the equality $v_m=w_n$ in Equation (4.2) forces $\alpha^m\lt\beta^n$. Hence:

**Equation (4.3).**

```math
m\log\alpha\lt n\log\beta.
```

We have $\alpha\gt2\sqrt{AC}$ and $\beta\lt(5/2)\sqrt{BC}$, the latter following from $1+\sqrt2\lt5/2$. Since $C\gt B^3$,

```math
\begin{aligned}
\beta^3
&\lt\frac{125}{8}B^{3/2}C^{3/2}\\
&\lt\frac{125}{8}C^2\\
&\lt16A^2C^2\\
&\lt\alpha^4.
\end{aligned}
```

Together with Equation (4.3), this gives:

**Equation (4.4).**

```math
m\lt\frac43n.
```

Write $m=2k$ and $n=2\ell$, where $k,\ell$ are positive integers. The recurrence implies:

**Equation (4.5).**

```math
v_{2k}
\equiv\varepsilon+2C(\varepsilon Ak^2+kS)
\pmod{4C^2}.
```

For completeness, the subsequence $E_k=v_{2k}$ satisfies

```math
\begin{aligned}
E_{k+2}&=(2+4AC)E_{k+1}-E_k,\\
E_0&=\varepsilon,\\
E_1&=\varepsilon+2C(S+\varepsilon A).
\end{aligned}
```

If $Q(k)=\varepsilon+2C(\varepsilon Ak^2+kS)$, then

```math
\begin{aligned}
&Q(k+2)-(2+4AC)Q(k+1)+Q(k)\\
&\qquad=-8AC^2\bigl(\varepsilon A(k+1)^2+(k+1)S\bigr).
\end{aligned}
```

The two initial values agree, and the right side is divisible by $4C^2$, proving Equation (4.5) by induction. The analogous formula holds for $w_{2\ell}$, with $A,S,k$ replaced by $B,T,\ell$. Thus $v_{2k}=w_{2\ell}$ implies:

**Equation (4.6).**

```math
\begin{aligned}
F&:=\varepsilon(Ak^2-B\ell^2)\\
&\qquad+kS-\ell T\\
&\equiv0\pmod C.
\end{aligned}
```

In fact, the computation gives divisibility by $2C$; divisibility by $C$ will suffice.

By Equation (4.4) and $B\gt13A$,

```math
Ak^2
\lt\frac{16}{9}A\ell^2
\lt B\ell^2.
```

Also $T^2-9S^2=(B-9A)C-8\gt0$, so $S\lt T/3$ and:

**Equation (4.7).**

```math
kS\lt\frac49\ell T.
```

Suppose, contrary to the assertion, that $n\le\sqrt{C/B}$. Since $n=2\ell$, we obtain:

**Equation (4.8).**

```math
\begin{aligned}
B\ell^2&\le\frac C4,\\
\frac{B\ell}{T}&\lt\frac12,\\
\ell T&\le\frac C2\sqrt{1+\frac1{BC}}\\
&\lt\frac{3C}{4}.
\end{aligned}
```

For $\varepsilon=1$, both terms of $F=(Ak^2-B\ell^2)+(kS-\ell T)$ are negative, while

```math
F\gt-B\ell^2-\ell T\gt-C.
```

Therefore $-C\lt F\lt0$.

For $\varepsilon=-1$, we have

```math
\begin{aligned}
F&=(B\ell^2-Ak^2)\\
&\qquad+kS-\ell T\\
&\gt-\ell T\\
&\gt-C.
\end{aligned}
```

On the other hand, Equations (4.7) and (4.8) give

```math
\begin{aligned}
F
&\lt B\ell^2+kS-\ell T\\
&\lt\left(\frac12+\frac49-1\right)\ell T\\
&=-\frac1{18}\ell T\\
&\lt0.
\end{aligned}
```

Again $-C\lt F\lt0$. Both cases contradict Equation (4.6), so $n\gt\sqrt{C/B}$. Finally, Equation (2.2) gives $\sqrt{C/B}\gt4uB$, completing the proof.

## 5. An upper bound from simultaneous approximation

### 5.1. The external approximation theorem

We use Cipu, Dujella and Fujita (2022, Theorem 3.1), which states a version of Cipu, Filipin and Fujita (2016, Theorem 2.1) without a coprimality hypothesis. To record its constants exactly, put:

**Equation (5.1).**

```math
\begin{aligned}
c_0&=\frac{951}{250},\\
c_1&=\frac{2629}{1000},\\
K&=\frac{287}{200}\,10^{28}.
\end{aligned}
```

These are $3.804$, $2.629$ and $1.435\cdot10^{28}$, respectively.

**Theorem 5.1 (Cipu, Dujella and Fujita).** Let $h,k,N$ be positive integers satisfying $0\lt h\lt k$, $k\ge5$ and $hk\mid N$. Set $h'=\max\{k-h,h\}$ and suppose that

```math
N\ge c_0h'k^2(k-h)^2.
```

For $\theta_1=\sqrt{1+k/N}$ and $\theta_2=\sqrt{1+h/N}$, every choice of integers $p_1,p_2,q$ with $q\gt0$ satisfies:

**Equation (5.2).**

```math
\max_{i=1,2}
\left|\theta_i-\frac{p_i}{q}\right|
\gt\frac{h}{Kh'kN}\,q^{-\lambda},
```

where:

**Equation (5.3).**

```math
\lambda
=1+
\frac{\log(10h'kN/h)}
{\log\bigl(c_1N^2/(hk(k-h)^2)\bigr)}
\lt2.
```

### 5.2. Verification of the hypotheses

Apply Theorem 5.1 with

```math
\begin{aligned}
h&=A,\\
k&=B,\\
N&=ABC,\\
\Delta&=B-A.
\end{aligned}
```

Since $B\gt13A$, we have $\Delta\gt A$ and therefore $h'=\Delta$. The conditions $0\lt h\lt k$, $k\ge5$ and $hk\mid N$ hold immediately. The remaining quantitative condition is:

**Equation (5.4).**

```math
C\ge c_0\frac{B\Delta^3}{A}.
```

By Lemma 3.1 and $B^2\lt A^3$:

**Equation (5.5).**

```math
C
\gt16A^2B^2
\gt\frac{16B^4}{A}
\gt c_0\frac{B\Delta^3}{A},
```

because $\Delta\lt B$ and $c_0\lt16$. This verifies every hypothesis.

The theorem now concerns

```math
\begin{aligned}
\theta_1&=\sqrt{1+\frac1{AC}},\\
\theta_2&=\sqrt{1+\frac1{BC}},
\end{aligned}
```

and gives:

**Equation (5.6).**

```math
\max_i
\left|\theta_i-\frac{p_i}{q}\right|
\gt\frac1{K\Delta B^2C}\,q^{-\lambda},
```

with:

**Equation (5.7).**

```math
\lambda
=1+
\frac{\log(10\Delta B^2C)}
{\log(c_1ABC^2/\Delta^2)}
\lt2.
```

### 5.3. Integer approximants from the quadruple

Put

```math
\begin{aligned}
X&=\sqrt{AD+1},\\
Y&=\sqrt{BD+1},\\
q&=ABZ,\\
p_1&=BSX,\\
p_2&=ATY.
\end{aligned}
```

These are integers and $q\gt0$. Theorem 5.1 does not require the resulting fractions to be in lowest terms.

For the first approximation, the identity

```math
\begin{aligned}
\left(\frac{SX}{AZ\theta_1}\right)^2
&=\frac{C(AD+1)}{A(CD+1)}\\
&=1+\frac{C-A}{AZ^2}
\end{aligned}
```

and positivity give

```math
\frac{p_1}{q}
=\theta_1\sqrt{1+\frac{C-A}{AZ^2}}.
```

For $x\gt0$, we have $\sqrt{1+x}-1=x/(\sqrt{1+x}+1)\lt x/2$. Since $\theta_1\lt2$, it follows that

```math
\left|\theta_1-\frac{p_1}{q}\right|
\lt\frac{C-A}{AZ^2}
\lt\frac{C}{AZ^2}.
```

The same argument for the second approximation gives the stronger bound $C/(BZ^2)$, so:

**Equation (5.8).**

```math
\max_i
\left|\theta_i-\frac{p_i}{q}\right|
\lt\frac{C}{AZ^2}.
```

Combining Equations (5.6) and (5.8), and substituting $q=ABZ$, yields

```math
Z^{2-\lambda}
\lt\frac{K\Delta B^2C^2}{A}(AB)^\lambda.
```

Because $AB\gt1$ and $\lambda\lt2$, this implies:

**Equation (5.9).**

```math
Z^{2-\lambda}
\lt KA\Delta B^4C^2.
```

### 5.4. Eliminating the exponent

Define:

**Equation (5.10).**

```math
\begin{aligned}
U&=2\cdot10^{14}\sqrt{A\Delta}\,B^2C,\\
V&=\frac{2\sqrt{AB}\,C}{\Delta},\\
L&=\frac{AC}{4B\Delta^3}.
\end{aligned}
```

As $K\lt4\cdot10^{28}$, Equation (5.9) gives:

**Equation (5.11).**

```math
Z^{2-\lambda}\lt U^2.
```

Write $P_0=10\Delta B^2C$ and $Q_0=c_1ABC^2/\Delta^2$. Lemma 3.1, $\Delta\lt B$ and $B^2\lt A^3$ give:

**Equation (5.12).**

```math
L
\gt\frac{A\cdot16A^2B^2}{4B\cdot B^3}
=\frac{4A^3}{B^2}
\gt4.
```

Moreover,

```math
\begin{aligned}
\frac{Q_0}{P_0}
&=\frac{2629}{10000}\frac{AC}{B\Delta^3}\\
&\gt L,\\
Q_0&\lt V^2,
\end{aligned}
```

because $2629/10000\gt1/4$ and $c_1\lt4$. Since $P_0\gt1$ and $L\gt4$, we have $Q_0\gt1$ and $V\gt1$. In particular, the logarithms used as denominators below are positive. Equation (5.7) implies

```math
2-\lambda
=\frac{\log(Q_0/P_0)}{\log Q_0}
\gt\frac{\log L}{2\log V}
\gt0.
```

Taking logarithms in Equation (5.11), with $Z\gt1$ and $U\gt1$, therefore yields:

**Equation (5.13).**

```math
\log Z
\lt\frac{4\log U\log V}{\log L}.
```

### 5.5. From the height of $Z$ to the index $n$

We return to the fixed representation in Equation (2.7), with the same index $n$ as in Lemma 4.1. Equation (4.2) gives

```math
\begin{aligned}
2Z&=(q_0+\varepsilon)\beta^n\\
&\qquad-(q_0-\varepsilon)\beta^{-n},\\
q_0&=\sqrt{C/B}\gt B\gt4.
\end{aligned}
```

Since $n\ge2$ and $\beta\gt2$, we have $\beta^{-2n}\lt1/16$. For either sign of $\varepsilon$,

```math
\begin{aligned}
\frac{2Z}{\beta^n}
&\ge q_0-1-(q_0+1)\beta^{-2n}\\
&\gt\frac{15q_0-17}{16}\\
&\gt2.
\end{aligned}
```

Consequently $Z\gt\beta^n$, and $\beta\gt2\sqrt{BC}$ gives:

**Equation (5.14).**

```math
\log Z
\gt n\log\beta
\gt\frac n2\log(4BC).
```

Combining Equations (5.13) and (5.14), we obtain:

**Equation (5.15).**

```math
n
\lt\frac{8\log U\log V}{\log(4BC)\log L}.
```

## 6. Completion of the proof

By $\sqrt{A\Delta}\lt B$ and $C\lt16B^4$,

```math
U\lt32\cdot10^{14}B^7\lt B^{10}.
```

The last inequality follows from

```math
\begin{aligned}
B^3
&\gt179712^3\\
&=5804051165872128\\
&\gt32\cdot10^{14}.
\end{aligned}
```

Also $B\gt13A$ implies $\sqrt{AB}\lt\Delta$, since

```math
\Delta^2-AB
=B(B-3A)+A^2
\gt0.
```

Hence

```math
V\lt2C\lt32B^4\lt B^5,
```

using $B\gt32$. Thus

```math
\begin{aligned}
\log U&\lt10\log B,\\
\log V&\lt5\log B.
\end{aligned}
```

On the other hand, $C\gt B^3$ and Equation (5.12) give

```math
\begin{aligned}
\log(4BC)&\gt4\log B,\\
\log L&\gt\log4\gt1.
\end{aligned}
```

Substituting these inequalities in Equation (5.15) yields:

**Equation (6.1).**

```math
n\lt100\log B.
```

Lemma 4.1, however, gives $n\gt4B$. For $B\gt179712\gt625$, we have $\log B\lt\sqrt B$ and $100\sqrt B\lt4B$. Indeed, $\sqrt x-\log x$ is increasing for $x\ge4$ and is positive at $x=4$. We reach the contradiction

```math
\begin{aligned}
4B
&\lt n\\
&\lt100\log B\\
&\lt100\sqrt B\\
&\lt4B.
\end{aligned}
```

This proves Theorem 1.1.

The proof combines the published inequalities and Pell classification with the residue comparison, two positive descents, and an estimate for the same even index in a fixed recurrence. It establishes the claimed uniqueness of a smaller extension without assuming the regularity of all Diophantine quadruples.

## References

1. M. Cipu, A. Dujella and Y. Fujita. *Extensions of a Diophantine Triple by Adjoining Smaller Elements*. Mediterranean Journal of Mathematics **19** (2022), Article 187, 20 pp. [DOI: 10.1007/s00009-022-02088-1](https://doi.org/10.1007/s00009-022-02088-1). The Main Theorem, Corollary 1.3 and Theorem 3.1 are used above.
2. M. Cipu, A. Dujella and Y. Fujita. *Extensions of a Diophantine Triple by Adjoining Smaller Elements II*. Periodica Mathematica Hungarica **89** (2024), 54-60. [DOI: 10.1007/s10998-023-00569-8](https://doi.org/10.1007/s10998-023-00569-8). Consulted to check the scope of the correction discussed below.
3. M. Cipu, A. Filipin and Y. Fujita. *Bounds for Diophantine Quintuples II*. Publicationes Mathematicae Debrecen **88** (2016), 59-78. [DOI: 10.5486/PMD.2016.7257](https://doi.org/10.5486/PMD.2016.7257). Theorem 2.1 is the source of the approximation result in the form stated by Cipu, Dujella and Fujita (2022).
4. M. Cipu, Y. Fujita and T. Miyazaki. *On the Number of Extensions of a Diophantine Triple*. International Journal of Number Theory **14** (2018), 899-917. [DOI: 10.1142/S1793042118500549](https://doi.org/10.1142/S1793042118500549). Theorem 2.1 supplies the classification used in Section 2.
5. A. Dujella. *[Open Problems on Diophantine m-Tuples and Elliptic Curves](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf)*. Online problem list, Problem 4.4, p. 9 of the version consulted on 2 October 2026.

**Note on the 2024 correction.** Cipu, Dujella and Fujita (2024, p. 2 of the author manuscript) correct Theorems 1.6 and 1.7 of Y. Fujita, *The Number of Irregular Diophantine Quadruples for a Fixed Diophantine Pair or Triple*, Contemporary Mathematics **768** (2021), 105-118. The correction concerns the ordering $a_1\lt b\lt a_2\lt c$ in the first of these assertions; the paper explicitly preserves the case $a_2\lt b$. It does not retract the Main Theorem of Cipu, Dujella and Fujita (2022). No corrected assertion for the different ordering is used in the present proof.
