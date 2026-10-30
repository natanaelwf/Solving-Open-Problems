[← Appendix E](appendix-e.md) · [Main article](README.md) · [References →](references.md)

---

## Appendix F. Integral coefficient calculus

We specialize the ordinary coefficient calculus of OpenAI (2026). Let $`\mathcal{R}`$ be the ring of integers of a finite extension of $`\mathbb{Q}_2`$ containing the coefficient and character fields, with maximal ideal $`\mathfrak{m}`$. Divisibility by the integer two means divisibility by $`2\mathcal{R}`$, which can be strictly smaller than $`\mathfrak{m}`$. Every division below is justified before reduction.

We treat an even source $`g`$ and an odd finite-precision source $`g_M`$ simultaneously. Their recurrence is (E.2), exact in the even case and modulo $`2^M`$ in the odd case. The characters have $`2`$‑power order and $`\psi/\eta`$ is quadratic. Phase-removed squarefree coefficients are rational in the even case and integers modulo $`2^M`$ in the odd case. Suppose that

**Equation (F.1).**

```math
\begin{aligned}
 v_2(a(D))&\ge\omega(D)-C,\\
 v_2(a_M(D))&\ge\min\{M,\omega(D)-C\}
 \end{aligned}
```

for all admissible squarefree indices, and that the odd sources have a fixed bounded-weight witness with coefficient valuation bounded along a cofinal sequence of precisions. The even premise is (E.5); the odd premise will be proved in Proposition H.3 before the odd calculus is applied. Restrict to the witness sequence and fix a nonprincipal ultrafilter on it. At odd stage $`M`$, the support is $`S_0\cup\{ℓ_M\}`$.

**Lemma F.1 (Uniform normalized minimum).**

In the even case $`\delta=\min_D(v_2(a(D))-\omega(D))`$ is an attained integer. In the odd case there is an attained integer $`\delta`$ among visible bounded-weight sequences. For every fixed $`W`$, on an ultrafilter-large set of stages,

```math
v_2(a_M(D))\ge\delta+\omega(D)
 \quad\text{simultaneously for all }\omega(D)\le W.
```

A bounded-weight witness attains equality on an ultrafilter-large set. The integer $`\delta`$ and this witness weight are fixed before any graph size or cube dimension is chosen.

*Proof.* The coarse bounds give a uniform integer lower bound; a nonzero witness gives a finite upper bound. The minimum of the resulting nonempty set of integers is attained. In the odd case, restrict to values no larger than the fixed witness value; only finitely many integers can occur, so the ultrafilter selects one. If the asserted uniform inequality failed for a fixed $`W`$ on an ultrafilter-large set, choose a violating $`D_M`$ at each such stage. This is a bounded-weight sequence with strictly smaller normalized depth. Invisible coefficients cause no exception once $`M\gt \delta+W`$.

For a finite set $`U`$ of variable primes put

```math
B_U=2^{-\delta-\vert U\vert }\prod_{p\in U}(U_p-\eta(p)V_p)g,
 \qquad U_pf[n]=f[pn],\quad V_pf[n]=f[n/p].
```

Use $`g_M`$ in the odd case, at sufficient precision for these divisions. The same $`\delta`$ is used when a prime is omitted from $`U`$.

**Lemma F.2 (Integral square shells).**

Write $`n=Jrm^2`$, where $`J\subseteq U`$ denotes also its squarefree product, and $`r`$ is squarefree and coprime to $`U`$. Every coefficient of $`B_U`$ is integral and

```math
v_2(B_U[Jrm^2])\ge\omega(r)
```

in the even case. For the odd sources, given $`W,R`$, one sufficiently late actual stage gives integrality and this bound truncated at $`R`$ for every $`\vert U\vert \le W`$ and every Fourier index.

*Proof.* Indices meeting the fixed support vanish by the sieves. At the others, the underlying squarefree index is $`D=(U/J)r`$. After extracting $`\eta(p)^s`$, the shell recurrence is

```math
b_0=1,\quad b_1=a_p-\kappa,\quad
 b_{s+1}=a_pb_s-pb_{s-1},\qquad
 \kappa=(\psi/\eta)(p)(-D/p).
```

For $`p\mid D`$ one has $`\kappa=0`$; otherwise $`\kappa=\pm1`$. At $`p\in U/J`$ the operator gives $`b_s-b_{s-1}`$ with $`b_{-1}=0`$, which is odd because $`a_p`$ is even. At $`p\in J`$ it gives $`b_{s+1}-b_s`$, which is even. The complete phase is $`\eta(Jm)`$ times the squarefree phase of $`a(D)`$. The squarefree bound and the $`\vert J\vert `$ even differences give

```math
\delta+\omega((U/J)r)+\vert J\vert -\delta-\vert U\vert =\omega(r).
```

All remaining recurrence multipliers are integral.

For odd stages, first use Lemma F.1 below a fixed squarefree-weight threshold. Above it, the coarse bound $`\min(M,\omega(D)-C)`$ pays the largest normalizing exponent $`\max_{\vert U\vert \le W}(\delta+\vert U\vert )`$ and the requested precision $`R`$. Choose the threshold accordingly, then choose $`M`$ larger than these fixed quantities. Recurrence errors remain divisible by $`2^M`$ before normalization at every square shell: only integral multipliers occur. This argument is simultaneous in all indices and all prime choices with bounded $`\vert U\vert `$.

Since $`E[2]`$ is rational, $`a_p\equiv p+1\pmod4`$. For $`\kappa=\pm1`$ put $`\Delta_s=b_{s+1}-b_s`$. The same recurrence and $`\Delta_1-\Delta_0\equiv(p-1)(p-\kappa)\equiv0\pmod4`$ give

**Equation (F.2).**

```math
\Delta_s/2\equiv(a_p-\kappa-1)/2\pmod2\quad(s\ge0).
```

Choose $`i\in\{0,1\}`$ so that $`\eta\chi_{-4}^i`$ is odd, and define

```math
\Theta_J=\sum_{\substack{m\gt 0\\(m,S)=1}}
       \eta(m)\chi_{-4}(m)^i m q^{Jm^2},\qquad
 H_U=\frac12\left(B_U-\sum_{J\subseteq U}B_U[J]\Theta_J\right).
```

The unary character is $`\chi_J=\eta\chi_{-4}^i(-J/\,\cdot\,)`$; the non-unary character is $`\psi_U=\psi\prod_{p\in U}(p/\,\cdot\,)`$. Each new prime occurs in the level to exponent at most one. Indeed, if the old level is $`L`$ and $`p\nmid L`$, conjugating $`\gamma\in\Gamma_0(Lp)`$ by $`\mathrm{diag}(p,1)`$ gives $`\left(\begin{smallmatrix}a&pb\\ c/p&d\end{smallmatrix}\right) \in\Gamma_0(L)`$. The quotient of theta multipliers is $`(p/d)`$, unchanged by cubing. Thus $`V_p`$ raises the level by $`p`$ with that quadratic character. On the raised level $`U_{p^2}`$ preserves the level and character, and coefficientwise $`U_p=U_{p^2}V_p`$. Unary dilation has the same new-prime exponent; the sieves affect only fixed support.

**Lemma F.3 (Integer unary division).**

The form $`H_U`$ is integral, with the same uniform finite-precision interpretation as Lemma F.2. For a fresh prime $`q`$ its reduced coefficient is the binary symbol

```math
A(Uq)=\left(2^{-\delta-\vert U\vert -1}a(Uq)
                    \text{ with phase removed}\right)\bmod2.
```

*Proof.* If $`r\ne1`$, Lemma F.2 makes the coefficient even. For $`r=1`$, (F.2) shows, after extracting the common phase, that $`B_U[Jm^2]\equiv B_U[J]\eta(m)\pmod{2\mathcal{R}}`$. Differences at $`U/J`$ are odd; the divided differences at $`J`$ have the same parity as on the first shell; the other square-shell multipliers are odd. As $`m\chi_{-4}(m)^i`$ is odd, this is precisely the unary coefficient. Different $`J`$ have disjoint squarefree supports. Thus the division is by $`2\mathcal{R}`$ itself. At a fresh $`q`$ no unary term contributes. The residue is in $`\mathbb{F}_2`$ because phase-removed coefficients are integral and $`2`$‑power roots of unity reduce to one.

### F.1. Traces and whole-prime omission

Put $`\theta=1+2\sum_{n\gt 0}q^{n^2}`$; multiplication by $`\theta`$ gives weight two and preserves reduced coefficients. Work in the finite-dimensional sum of the characteristic-zero good Hecke eigensystems of $`\theta H_U`$, its unary terms, and their diamond translates, retaining all old multiplicity spaces. Use the two-dimensional modular Galois representations Deligne (1971) on cusp systems and the two character summands on Eisenstein systems. Their commuting scalar trace and determinant operators are $`t(g),d(g)`$.

**Lemma F.4 (Integral trace orbit).**

The module generated by $`\theta H_U`$, the undivided $`\theta B_U[J]\Theta_J`$, and their good-Hecke and diamond translates is an integral Fourier lattice stable under $`t(g),d(g)`$. On its reduced trace orbit of $`\theta H_U`$,

```math
d(g)t(h)=t(h),\qquad
 t(g)t(h)=t(gh)+t(gh^{-1}),\qquad t(1)=0.
```

Every finite trace product is testable by distinct fresh primes avoiding any prescribed Fourier index and finite exclusion set. Moreover

```math
t(g)t(h)\theta H_U=0,\qquad
 t(gu^2)\theta H_U=t(g)\theta H_U
```

after reduction. Thus trace tests factor through the maximal elementary quadratic extension unramified outside $`S\cup U`$.

*Proof.* The diamond denominator is removed by

```math
\langle u\rangle H_U=\psi_U(u)H_U+
 \frac12\sum_JB_U[J](\psi_U(u)-\chi_J(u))\Theta_J.
```

Each character ratio is quadratic; its difference is zero or twice a unit. All generators are integral, and good Hecke operators preserve integrality. Finitely many Fourier coefficients inject the ambient space into a finite-dimensional coefficient space. After enlarging $`\mathcal{R}`$ for its finitely many eigensystems, the module embeds in $`\mathcal{R}^r`$, so it is finitely generated and closed. Simultaneous Chebotarev approximation in those Galois systems approximates $`t(g),d(g)`$ by $`T_q,q\langle q\rangle`$ to arbitrary precision. Closedness proves preservation of the lattice. At a coefficient index prime to $`q`$, the second term of the weight-two Hecke formula vanishes. Iteration with distinct fresh primes gives the trace-testing assertion.

In the determinant formula the first diamond term is scalar and reduces to one. The other terms are integral unary corrections, still unary after multiplication by $`\theta`$ and reduction. A fresh trace tests them at an index with a new squarefree prime factor and kills them, also after further fresh tests. Hence $`d(g)t(h)=t(h)`$ on the reduced tested orbit. The matrix identity $`\mathrm{tr}(A)\mathrm{tr}(B) =\mathrm{tr}(AB)+\det(B)\mathrm{tr}(AB^{-1})`$ then gives the trace identity, and $`t(1)=2`$ before reduction.

Two fresh traces add two new squarefree primes to an index. Lemma F.2 supplies two factors of two in $`B_U`$, so one remains after unary division. Chebotarev turns this into $`t(g)t(h)\theta H_U=0`$ for arbitrary $`g,h`$. Apply the trace identity to $`t(gu)t(u)`$ to get invariance under $`u^2`$. The normal subgroup generated by squares has elementary abelian quotient, giving the asserted factorization. This is factorization of the tested reduced orbit, not of the original Galois representations.

Write $`U_p^{(2)}`$ for the weight-two coefficient operator at a raised prime. Choose tame inertia $`\tau_p`$ with new quadratic character $`-1`$ and an arithmetic Frobenius lift $`\varphi_p`$.

**Lemma F.5 (Exact local trace identity).**

On the characteristic-zero ambient systems,

```math
U_p^{(2)}\{t(g\tau_p\varphi_p)-t(g\varphi_p)\}
 =d(\varphi_p)\{t(g\tau_p)-t(g)\}.
```

It commutes with all further good traces.

*Proof.* An old constituent omitting $`p`$ has trivial inertia, so both differences vanish, including on its old multiplicity space. Every other constituent has conductor exponent one and primitive ramified quadratic determinant at $`p`$. Indeed the non-unary term has this character, as does $`\Theta_J`$ if $`p\mid J`$; if $`p\nmid J`$ the unary term already omits $`p`$. The conductor formula therefore gives a principal series with one unramified and one ramified character. A Steinberg constituent with unramified determinant cannot occur. Local modular compatibility Carayol (1986, Theorem A), in the arithmetic-Frobenius convention, identifies $`U_p^{(2)}`$ with the unramified Frobenius eigenvalue $`\lambda`$. Write $`\rho(\tau_p)=\mathrm{diag}(1,-1)`$ and $`\rho(\varphi_p)=\mathrm{diag}(\lambda,\mu)`$. If $`z`$ is the lower-right entry of $`\rho(g)`$, the differences are $`-2z\mu`$ and $`-2z`$, so both sides are $`-2z\lambda\mu`$. An Eisenstein constituent is the same two-character calculation. These exhaust the constituents, and scalar good traces commute with the level operator on the retained old multiplicities.

**Proposition F.6 (Ordinary symbol interface).**

Let $`V=U\setminus\{p\}`$. Changing one ramification bit at $`p`$ in the Frobenius label of a fresh $`q`$ changes $`A(Uq)`$ by $`A(Vq')`$, where the retained label of $`q'`$ is the product of the labels of $`q,p`$. The replacement source is $`H_V`$, with the same $`g,\eta,\psi,\delta`$; its entire ramification support omits the rational prime $`p`$. A vertex with trivial label at the support and at the other vertices has symbol zero.

*Proof.* Apply Lemma F.5 at coefficient one and reduce using Lemma F.4. Replace its trace arguments by fresh primes. The first-shell formula, including the normalizing powers, is

```math
H_U[pq']\equiv\eta(p)c_p(D')H_V[q']\pmod{\mathfrak{m}},
 \qquad D'=Vq',
```

```math
c_p(D')=\frac{a_p-(\psi/\eta)(p)(-D'/p)-1}{2}\pmod2.
```

The factor $`1/2`$ is the ratio of normalizations; the numerator is the even first-shell difference. The phase reduces to one. Choose $`q'_0,q'_1`$ with trace data $`g\varphi_p,g\tau_p\varphi_p`$. The source $`H_V`$ is unramified at $`p`$, so these restrictions give the same omitted-source symbol. Their Legendre terms at $`p`$ have opposite signs because the character of $`p^*=(-1/p)p`$ is ramified at $`p`$ and takes value $`-1`$ on $`\tau_p`$. The two values of $`c_p`$ therefore differ by one. Their shell difference is precisely $`A(Vq')`$. On the omitted source $`\varphi_p`$ is ordinary unramified Frobenius, which gives the product label. The trivial-label assertion follows from $`t(1)=0`$.

### F.2. Finite-stage stabilization and unit bounds

The odd assertions above hold simultaneously for every $`\vert U\vert `$ below a fixed bound. A finite graph with specified support labels and mutual quadratic residue bits determines its symbol: hold all but one vertex fixed and use elementary trace factorization, then replace vertices successively through fresh bridge primes. The rational fixed-support extension is generated by $`-1`$ and the support primes; the moving prime adds at most the one radical $`ℓ_M^*`$. Its dimension is uniformly bounded. The old characters are fixed and the new character is quadratic. There are therefore only finitely many addition, projection, and reciprocity-type tables. The ultrafilter selects one abstract table. For every fixed vertex bound it similarly selects one binary truth table on the finitely many typed graphs. These selected tables agree under restriction, because finite intersections of ultrafilter-large sets are large. The bounded-weight witness of Lemma F.1 gives a unit in the resulting table. All finite contraction and isolation identities pass to it.

To realize a construction, first choose its finite graph and networks in this abstract alphabet. Their maximum vertex count is a finite cutoff. Only then select an actual stage in the finite intersection of the required large sets, with sufficient precision, and realize the graph by primes. No stage is required to work for every graph size, and no countable intersection is taken. A later fixed finite enrichment of the labels can be stabilized with the same ultrafilter. The original $`\delta`$ remains unchanged.

**Corollary F.7 (Uniform bounds at a unit).**

At an even unit,

```math
L_*(h)\ne0,\qquad v_2(L_*(h))\le2\omega(\vert h\vert )+C.
```

At an odd unit, realized at sufficient precision, $`E^{(h)}`$ has analytic order one and

```math
j(P_h)\le\omega(h)+C.
```

The constants are independent of the number and sizes of the varying primes and, in the odd case, of the moving stage.

*Proof.* A unit has coefficient valuation $`\delta+\omega(\vert h\vert )`$. In the even case use (E.3). In the odd case choose $`M`$ above this valuation for all finitely many required indices, making the coefficients visible. Equation (E.6) then detects a nontorsion point, since $`L`$ kills torsion. Gross–Zagier gives analytic order one. An integral homomorphism into $`\mathbb{Z}/2^M\mathbb{Z}`$ cannot lower the divisibility index of a point. The factors $`L,c_0,2^{\omega(N)}`$ are fixed, and comparison of the rational and biquadratic free lattices has bounded index. Thus visibility also gives $`j(P_h)\le v_2(a_M(h))+C`$ uniformly.

## Appendix G. Finite arithmetic graphs and simultaneous addressing

The graph constructions in this section are the rational specializations of OpenAI (2026). Their arithmetic inputs are precisely Proposition F.6 and finite prime realization. All configurations and all outputs of contractions are nonempty.

### G.1. Labels and realization

At a finite support $`S`$ containing two, a prime type records its unit squareclasses and its residue modulo eight. Its elementary Frobenius label is in the extension generated by $`-1`$ and the primes of $`S`$. These quadratic data form a finite $`\mathbb{F}_2`$‑space; prescribed splitting in a fixed quadratic field restricts to a kernel. Deeper residue classes may be chosen as realization lifts but are not additional coordinates of this alphabet. For every pair of vertices choose one forward Legendre bit. The reverse is fixed by

```math
(p/q)(q/p)=(-1)^{((p-1)/2)((q-1)/2)}.
```

There is no self-residue. A primary vertex has trivial type: it is $`1\pmod8`$ and a square unit at every support prime.

**Lemma G.1 (Finite realization and product labels).**

Fix finitely many old vertices with all their mutual data. Any individually realizable types for finitely many new vertices, and any prescribed forward bits involving at least one new vertex, can be realized by distinct fresh primes outside a finite exclusion set. Contracted clusters have product types and summed external bits, and can be replaced by fresh prime representatives with those data. The symbol depends only on the resulting finite graph.

*Proof.* For the next prime choose its prescribed reduced residue class at the support. At every old prime choose a nonzero residue realizing the desired Legendre bit; quadratic reciprocity determines the reverse bit from the chosen type. The Chinese remainder theorem combines these conditions, and Dirichlet’s theorem gives infinitely many primes in the resulting reduced progression. Successive choices prove the finite assertion and permit all exclusions.

For a cluster $`p_1,\ldots,p_r`$ prescribe for its representative $`q`$ the unit squareclasses of $`\prod p_i`$ at the support, the residue $`q\equiv\prod p_i\pmod4`$, and the corresponding products of residues at every remaining vertex. The same argument realizes them. In particular, writing $`p^*=(-1/p)p`$,

```math
\mathrm{sgn}(q^*)=\prod_i\mathrm{sgn}(p_i^*),\qquad
 [q^*]_v=\prod_i[p_i^*]_v\quad(v\in S).
```

Thus product replacement preserves the signed filter, including its real sign. At any omitted vertex, the fixed radicals and the remaining prime radicals generate the maximal elementary extension with the allowed ramification. Their listed bits therefore determine its trace test. To compare two graph realizations, use fresh bridge primes with matching bits to both and replace vertices successively. Proposition F.6 gives equality at each step.

An arithmetic graph is this collection of types and bits. Its unique multilinear polynomial over $`\mathbb{F}_2`$ in selected pair bits is its terminal polynomial. Write $`\Delta_zP=P\vert _{z=0}+P\vert _{z=1}`$; on multilinear polynomials this is ordinary differentiation, so the differences commute and square to zero. A graph is partitionable if a contraction forest has a unit symbol as its output. Its terminal polynomial is then nonzero.

**Lemma G.2 (Forest contraction).**

Differentiation along a tree contracts that tree, multiplying its labels and summing its external bits. A derivative containing a cycle is zero.

*Proof.* The one-edge statement is Proposition F.6; induction and product replacement give the tree assertion. For a cycle first contract a spanning path. The closing bit is now internal to the merged cluster and affects no product type or external incidence. Equivalently it is an inertia change at an omitted rational prime; the replacement source is unramified there. Its derivative is zero. Repetition of an edge is also zero by $`\Delta_z^2=0`$. Other derivatives commute with this zero derivative.

### G.2. Network operators

Fix a terminal graph and its polynomial $`P`$. A network adds primary internal vertices and programmed edges, with no direct terminal–terminal edges. Unprogrammed incidences, including those to specified stationary external vertices, are neutral. The degree of a contraction is the number of terminal vertices lost by merging them.

**Lemma G.3 (Network expansion).**

A network acts on $`P`$ by a sum of finite-difference operators. Its surviving terms are forests in which every component containing an internal vertex meets a terminal. A component meeting $`t`$ terminals has degree $`t-1`$. Networks on disjoint internal vertex sets, with no edges between those sets, multiply as operators on the original terminal polynomial. An operator of degree greater than $`\deg P`$ annihilates it.

Let $`Q`$ be the grounded Laplacian on the internal vertices, whose diagonal entries include terminal incidence, and let $`c_a`$ be the incidence column of terminal $`a`$. Its degree-zero and pair-contraction coefficients are

**Equation (G.1).**

```math
\det Q,\qquad c_a^{\mathsf{t}}\mathrm{adj}(Q)c_b\quad(a\ne b).
```

These formulas include singular $`Q`$.

*Proof.* Expand evaluation at the programmed edges from the graph with all primary incidences zero: $`f(\mathbf{1})=\sum_{T\subseteq E_0}(\Delta_Tf)(\mathbf{0})`$. Lemma G.2 kills cycles. A component without a terminal contracts to an isolated primary vertex, so its symbol is zero; this includes an untouched internal vertex. In a surviving component, primary labels and baseline external bits are neutral. Its contraction is exactly the contraction of its terminal vertices in the original graph. Any terminal tree on those vertices gives the same product labels and external bits, so it supplies an operator of degree $`t-1`$. Expanding two disjoint networks at once gives the composition of these operators. The final product labels agree in either order, and any resulting cycle vanishes. Polynomial differentiation proves the degree bound.

For the coefficients, write the full Laplacian as $`DD^{\mathsf{t}}`$, where an incidence column has ones at its two endpoints. Cauchy–Binet applied to its internal principal minor $`Q`$ counts forests with exactly one terminal in each component: a cycle gives dependent columns, a component without a deleted terminal row gives dependent rows, and a tree with one row deleted has determinant one by leaf removal. These are exactly the degree-zero terms. For the pair coefficient use row set $`I\cup\{a\}`$ and column set $`I\cup\{b\}`$. Each counted component has one root from the terminal set minus $`a`$ and one from that set minus $`b`$. Thus $`a,b`$ lie together, and every other terminal lies in its own component. The minor is

```math
\det\begin{pmatrix}Q&c_b\\ c_a^{\mathsf{t}}&0\end{pmatrix}
       =c_a^{\mathsf{t}}\mathrm{adj}(Q)c_b.
```

The corner is zero because there is no direct terminal edge; signs disappear over $`\mathbb{F}_2`$. The adjugate identity does not require invertibility. This is the required all-minors matrix-tree calculation.

An address is $`x\in\mathbb{F}_2^b`$. A vertex of activation $`\lambda\ne0`$ is present if $`\lambda(x)=1`$. We permit either always-active terminals, or moving terminals including at least one with each nonzero activation. Fix $`x_*\ne0`$ and a bit $`z`$ between two terminals $`a_0,a_1`$ active at $`x_*`$. Choose a dual basis $`\lambda_1,\ldots,\lambda_b`$ with $`\lambda_i(x_*)=1`$ for every $`i`$. Indeed, start with $`\lambda_1(x_*)=1`$ and add it to a basis of the annihilator of $`x_*`$. Make $`b`$ groups of three primary vertices, group $`i`$ activated by $`\lambda_i`$. All groups are present exactly at $`x_*`$.

In each physical three-dimensional group choose a basis $`(e_i,u_i,v_i)`$ with $`e_i=(1,1,1)`$. Make the $`e_i`$ orthonormal and orthogonal to all $`u_j,v_j`$, and put on the remaining coordinates

```math
H(T,B)=\begin{pmatrix}0&T\\ T^{\mathsf{t}}&B\end{pmatrix},
```

where $`B`$ is symmetric. Denote the physical matrix by $`Q`$. The column $`h_i=Qe_i`$ is supported on group $`i`$ and independent of $`T,B`$. Attach it to an anchor terminal of activation $`\lambda_i`$; for stationary terminals use any fixed terminal. On a set $`J`$ of active groups,

```math
\sum_{i\in J}h_i\vert _J=Q_J\mathbf{1}_J.
```

Program internal edges using the off-diagonal entries of $`Q`$. The anchor columns thus make the grounded matrix exactly $`Q_J`$, including its diagonal, after every group restriction.

Attach an additional column $`c`$ to $`a_0`$ and $`a_1`$. If their moving activations $`\alpha,\beta`$ differ, attach $`c`$ also to a terminal of activation $`\alpha+\beta`$, inactive at $`x_*`$. The sum of these additional active columns is zero at every address. If the activations agree, or the terminals are stationary, the first two columns already cancel. Coincident terminal roles add their columns. Thus the grounded matrix is unchanged.

**Lemma G.4 (Two address programs).**

There are networks $`\mathcal{S}`$ and $`\mathcal{N}^{(\varepsilon)}`$ for $`\varepsilon\in\mathbb{F}_2`$ with

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

Here $`O_{\ge d}`$ is a sum of operators of degrees at least $`d`$. Every internal activation is nonzero, so no auxiliary vertex is present at zero.

*Proof.* For $`\mathcal{S}`$ take $`T=I+P`$, where $`P`$ is the cyclic permutation matrix, and take $`B`$ diagonal with exactly one nonzero entry. A proper principal restriction $`P_J`$ is a union of directed paths and hence nilpotent. Thus $`T_J`$ and $`H(T_J,B_J)`$ are invertible. The empty restriction has determinant one. On the full set, the kernels of $`T`$ and $`T^{\mathsf{t}}`$ are spanned by the all-one vector. A radical vector has $`v=t\mathbf{1}`$; summing $`T^{\mathsf{t}}u+Bv=0`$ forces $`t=0`$ because $`\mathbf{1}^{\mathsf{t}}B\mathbf{1}=1`$. The radical of $`Q`$ is therefore spanned by $`r=\sum_i u_i`$. Its adjugate is $`rr^{\mathsf{t}}`$: it has nonzero rank one and image the kernel, and the only nonzero scalar over $`\mathbb{F}_2`$ is one. Take $`c`$ dual to $`u_1`$, so $`c^{\mathsf{t}}r=1`$. All anchors pair to zero with $`r`$. At the target only the columns of $`a_0,a_1`$ pair nontrivially, and (G.1) gives zero constant and exactly $`\Delta_z`$ in degree one. At every other address the constant is one. For $`b=1`$ one has $`T=0,B=(1)`$ and the same argument applies.

For $`\mathcal{N}^{(\varepsilon)}`$, take $`T=I+L`$ with $`L`$ the consecutive lower shift and $`B=\varepsilon E_{bb}`$. Every group restriction of $`T`$ is invertible and

```math
H(T,B)^{-1}=\begin{pmatrix}
 T^{-\mathsf{t}}BT^{-1}&T^{-\mathsf{t}}\\ T^{-1}&0
 \end{pmatrix}.
```

Again take $`c`$ dual to $`u_1`$. On $`J`$, the change in $`c^{\mathsf{t}}Q_J^{-1}c`$ is $`((T_J^{-1})_{b1})^2`$, interpreted as zero if either endpoint is absent. The finite sum $`(I+L_J)^{-1}=I+L_J+L_J^2+\cdots`$ shows that this entry is one exactly when the whole path $`1,\ldots,b`$ is present, namely at $`x_*`$. Anchor pairings do not change because $`Q_J^{-1}h_i=e_i`$ and $`e_i,h_i,c`$ do not depend on $`\varepsilon`$. At the target the balancing terminal is absent, so only the $`a_0,a_1`$ pair coefficient changes. Every constant is one. Lemma G.3 proves the assertions.

**Theorem G.5 (Simultaneous addressing).**

Suppose either that one symbol has a nonzero polynomial on a nonempty set of always-active terminals, or that one or two symbols have nonzero terminal polynomials separately at every nonzero address on moving terminals with at least one of each nonzero activation. The symbols may forget different fixed-label coordinates of a common alphabet. Suppose their required total filters hold at every nonzero address. From any fixed realization of the terminal data, one can adjoin finitely many fresh primary auxiliaries, with nonzero activations, so that every symbol equals one at every nonzero address. All old vertices and their mutual data remain unchanged. The auxiliaries may obey fixed splitting and neutral external-incidence conditions included in their primary type.

*Proof.* Use common variables for toggles of the original terminal bits. For one symbol, at address $`x\ne0`$ choose a top monomial of its polynomial $`P_x`$, of degree $`d_x`$, with coefficient one. For each variable of this monomial add a disjoint singular program targeted at $`x`$. At $`x`$ its $`d_x`$ own programs have zero constants, so every surviving term uses at least $`d_x`$ degrees. Any further degree kills $`P_x`$. Thus precisely the designated degree-one terms and all other programs’ constants survive, giving that top coefficient, one. A nonzero constant polynomial needs no own program. This also covers stationary terminals.

For two symbols write their polynomials as $`P_x,R_x`$, of degrees $`d_x,e_x`$. Multiply the top homogeneous parts in the ordinary polynomial ring, before imposing Boolean relations. Since this ring is a domain, choose a monomial of coefficient one

```math
M_x=\prod_z z^{ν_{xz}},\qquad
 ν_{xz}\in\{0,1,2\},\qquad
 \sum_zν_{xz}=d_x+e_x.
```

For exponent two add one singular program targeted at $`x`$. For exponent one add one nonsingular program with its own parameter $`\varepsilon_{xz}`$. All internal vertex sets are disjoint. Let $`\Phi(\varepsilon)`$ be the product of the final evaluations of both symbols over all nonzero addresses. We show that its sum over all program parameters is one.

A singular program costs at least one degree in each factor at its target. A nonsingular program has constant one independent of its parameter; a term using only these constants everywhere cancels in the sum over that parameter. Every surviving term therefore costs at least one degree somewhere for that program. The total minimum cost is $`D=\sum_{x\ne0}(d_x+e_x)`$. A nonzero term cannot exceed this budget, since some factor would then receive more derivatives than its degree. Every surviving term uses all minimum costs exactly. Thus each singular program contributes its designated derivative once to each target factor and nothing elsewhere. Each nonsingular program contributes degree one to exactly one factor; after summing its parameter this is zero away from its target and is $`\Delta_z`$ at its target. No higher network coefficient remains.

At a fixed address, with $`Z_2`$ and $`Z_1`$ the exponent-two and exponent-one variables, the allocation sum is

```math
\sum_{J\subseteq Z_1}
 [z_{Z_2}z_J]P_x^{\mathrm{top}}
 [z_{Z_2}z_{Z_1\setminus J}]R_x^{\mathrm{top}}
 =[M_x](P_x^{\mathrm{top}}R_x^{\mathrm{top}})=1.
```

Coefficients of incorrect degree are zero. Each factor receives its full degree, so the result is independent of the original terminal-bit evaluation. The allocations at different addresses are independent, giving $`\sum_\varepsilon\Phi(\varepsilon)=1`$. Some choice therefore has all required evaluations one. Finally Lemma G.1 realizes the finite networks with fresh primes. Primary types preserve the filters and the stipulated external conditions; all activations are nonzero.

**Lemma G.6 (Minimum seeds and neutral packets).**

At the least positive vertex count of a unit witness, its mutual edge bits are immaterial and its value depends only on its fixed labels. Suppose one or two symbols with total filter zero have such nonempty witnesses. If a common finite alphabet projects onto the individual labels needed by each witness, there is a finite packet of common labels of total zero such that every nonempty union of copies is partitionable separately for both symbols.

*Proof.* At a minimum positive count $`r\ge2`$, differentiation in an edge gives a symbol on $`r-1`$ nonempty vertices, hence zero by minimality. For $`r=1`$ there is no edge. Thus edge bits are immaterial, whether or not the empty configuration is a unit.

Take ample copies of common labels projecting to every needed individual witness label, then duplicate the entire list. Its total is zero in the common elementary alphabet. For a witness with labels $`a_1,\ldots,a_r`$ of total zero, retain $`r-1`$ anchors with the first $`r-1`$ labels and merge all other vertices into one nonempty cluster. Its projected label is forced to be $`a_r`$. The contracted graph is a witness regardless of its edge bits. This uses only sufficiently many copies, so works for every nonempty union of packets and separately for each symbol. Simultaneous surjectivity onto a product of alphabets is unnecessary; the two contraction forests may differ.

## Appendix H. Assembly for the auxiliary curve

The arithmetic interpolation inputs are Theorems C.1, C.2, D.1, and D.2. Their uniformities have different roles. The cyclotomic transfer gives a bound independent of a stationary base and its prime count, although its dimension threshold may depend on that base. The ring-class lower bound is uniform when the negative companion has bounded prime count. The final ring-class transfer uses one fixed companion and a constant independent of the cube. We establish the odd coefficient lower bound before choosing its minimum or using its symbol.

### H.1. Partitionable even parameters and bounded companions

**Proposition H.1 (Partitionable even estimate).**

Fix an even symbol for $`E=F`$ on a filter of parameters locally square at every prime of $`2N`$. If a partitionable parameter $`d`$ has $`s_2(E^{(d)})=0`$, then

```math
L_*(d)\ne0,\qquad v_2(L_*(d))-2\omega(\vert d\vert )-s(d)\le C,
```

where $`C`$ depends only on the fixed symbol and local data.

*Proof.* If there are no prime factors, partitionability means the empty configuration is itself a unit, and Corollary F.7 applies directly. Otherwise hold the prime factors of $`d`$ stationary. Their terminal polynomial is nonzero by its contraction certificate. The stationary one-symbol case of Theorem G.5 gives arbitrarily large binary cubes based at $`d`$, with no old prime removed and only primary new primes, whose nonzero addresses are units. Corollary F.7 and $`s(d_x)\ge0`$ give the uniform upper bound required by Theorem C.2. The base corank is zero, so that theorem yields the assertion. Its base-dependent dimension threshold does not enter the constant.

**Lemma H.2 (Bounded companion).**

Fix the positive odd-sign filter, its support $`S_0`$, and the negative genus partner $`h_*`$ above. There are constants $`A,C`$ such that every $`h`$ in this filter of analytic order one has a negative odd fundamental discriminant $`k'`$ satisfying

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

*Proof.* Prepare an even negative-discriminant symbol for each possible total type at the fixed support that can occur below. There are finitely many such preparations. Their positive squarefree indices have nontrivial type at two: the absolute value of an odd negative fundamental discriminant that is square at two is $`7\pmod8`$. Consequently an even unit seed for each such filter has positive vertex count. At its least positive count its edge bits are immaterial by Lemma G.6.

Insert into $`\vert k'\vert `$ a bounded dummy supply with sufficiently many copies of the anchor labels of every prepared seed. Lemma G.1 realizes them outside all primes already used. Include a fresh prime greater than three, so the eventual imaginary field is not an extra-unit field. The number of dummy primes depends only on the finite preparation. Let $`d_0`$ be their product. Apply the bounded-prime nonvanishing theorem, Proposition B.1, to the curve obtained by absorbing $`h`$ and $`d_0`$. Prescribe the sign and local unit classes of the remaining factor so that the final $`k'`$ is negative, odd fundamental, coprime to the old support and $`h`$, and square at every prime of $`2Nh`$. These are compatible nonzero residue conditions in a reduced progression. The final root number is $`+1`$: twisting $`E^{(h)}`$ by the negative $`k'`$ coprime to its conductor and square at $`2Nh`$ multiplies its odd sign by $`\chi_{k'}(-N_{E^{(h)}})=-1`$. The theorem therefore gives $`L(E^{(hk')},1)\ne0`$ with at most five additional prime factors. Its size threshold may depend on $`h`$ and the progression; the prime-count bound does not.

For the actual resulting total type, retain all but the last anchor of the corresponding seed and merge every other factor of $`\vert hk'\vert `$ into its last cluster. There are enough dummy labels, the last cluster is nonempty, and its type is forced by the total. The result is the seed, regardless of mutual bits. Thus $`hk'`$ is partitionable for one of the finitely many prepared even symbols. Analytic nonvanishing gives Selmer corank zero by the forward theorem. Proposition H.1 gives (H.1). The finite preparation and the dummy bound plus five give $`A,C`$ independent of $`h`$.

**Proposition H.3 (Odd coefficient lower bound).**

Every analytically rank-one $`h`$ in the prepared positive filter obeys

**Equation (H.2).**

```math
2j(P_h)\ge2\omega(h)+s(h)-C.
```

The theta sources of Proposition E.5 consequently satisfy the odd premises of (F.1), with a constant independent of $`M,ℓ_M`$, and the number of varying primes. They also have the bounded-weight visible witness needed in Lemma F.1.

*Proof.* Choose $`k'`$ by Lemma H.2. Theorem D.1, Proposition E.1, and (H.1) give

```math
\begin{aligned}
 2j(P_h)
 &\ge4\omega(h)+s(h)+s(hk')-v_2(L_*(hk'))-C\\
 &\ge2\omega(h)+s(h)-2\omega(\vert k'\vert )-C\\
 &\ge2\omega(h)+s(h)-C'.
\end{aligned}
```

The ring-class constant is uniform because $`\omega(\vert k'\vert )\le A`$. Only even symbols and independently nonvanishing companions have entered this argument.

If $`P_D`$ is torsion, multiplication by $`L`$ makes its theta coefficient zero modulo $`2^M`$. If it is nontorsion, the genus Gross–Zagier formula with fixed nonzero $`L(E^{(h_*)},1)`$ gives analytic order one of $`E^{(D)}`$, so (H.2) applies. An integral reduction homomorphism cannot lower its divisibility index, and all factors in (E.6) are fixed integers or units. The bounded lattice comparison over degree-four fields therefore gives $`v_2(a_M(D))\ge\min(M,\omega(D)-C)`$ for every admissible $`D`$. Proposition E.4 supplies a fixed $`D_w`$ with bounded coefficient valuation, since $`c_0,2^{\omega(N)}`$ and $`L`$ are independent of the stage. This is the required witness.

We may now apply the odd minimum, calculus, and finite-table stabilization of Section F. In particular its depth $`\delta`$ and its unit bound are fixed before any cube dimension is chosen.

### H.2. An ordinary split-prime seed

Choose a minimum-depth negative even witness $`k\lt 0`$, prime to the intrinsic odd support $`S_0`$, square at $`2N`$, and let $`K=\mathbb{Q}(\sqrt{k})`$. Its odd negative fundamental discriminant has a prime factor outside $`2N`$. Since $`\mathbb{Q}(E[8])`$ is unramified outside $`2N`$,

```math
K\cap\mathbb{Q}(E[8])=\mathbb{Q}.
```

Chebotarev therefore gives fresh primes split in $`K`$ whose action on $`E[8]`$ is in the conjugacy class of Frobenius at $`19`$. For them

**Equation (H.3).**

```math
p\equiv3\pmod8,\qquad a_p(E^{(k)})\equiv0\pmod8.
```

The congruence for $`p`$ follows also from the Weil-pairing determinant.

**Proposition H.4 (Nonempty ordinary split witness).**

The even coefficient symbol for $`E^{(k)}`$, normalized at the index $`1`$, has a nonempty unit witness supported on primes split in $`K`$ and with total filter that of one.

*Proof.* The proof of Proposition E.2 applies to any fixed elliptic curve and nonvanishing twist index: its local Kirillov construction allows arbitrary bad local representations and arbitrary fixed level depth. Apply that proof to $`E^{(k)}`$ at the nonvanishing index $`1`$, adjoin all primes of $`k`$ to its fixed support, and normalize $`a(1)=1`$. The additional additive bad primes of $`E^{(k)}`$ are therefore fixed exceptional places of that construction. Restrict $`D`$ to the positive unit filter, square at $`2Nk`$ and at all the original fixed tests.

Its square comparison reads

```math
2v_2(a(D))
  =v_2\!\left(\frac{\sqrt D\,L(E^{(kD)},1)}{L(E^{(k)},1)}\right)
  =v_2\!\left(\frac{L_*(kD)}{L_*(k)}\right).
```

The fixed period of $`E^{(k)}`$ cancels from the first ratio. Let $`a_0`$ be the original even coefficient source for $`E`$. Since $`kD`$ remains on the original negative filter and $`(k,D)=1`$, minimality of $`k`$ gives

```math
v_2(a(D))=v_2(a_0(\vert k\vert D))-v_2(a_0(\vert k\vert ))\ge\omega(D).
```

The normalization therefore uses the original $`F`$‑bound on $`kD`$, and its minimum depth is zero. If no nonempty split unit existed, rational phase removal would give $`v_2(a(D))\ge\omega(D)+1`$ for every nonempty admissible product of split primes.

For a good split prime $`p`$ put $`a=a_p(E^{(k)})`$. The integral calculus gives

```math
B_p=(U_p-\eta(p)V_p)g/2,\qquad
 H_p=(B_p-B_p[1]\Theta_1-B_p[p]\Theta_p)/2.
```

For the positive even filter $`\psi/\eta=\chi_{-4}`$ and $`\psi`$ is even. Hence $`\eta`$ is odd, the unary exponent is $`i=0`$, and $`\Theta_p`$ has the same scalar character as $`B_p`$. The phase-free first shells are $`1,a-1,a(a-1)-p`$, so

**Equation (H.4).**

```math
H_p[p]=0,\qquad
 H_p[p^3]=\eta(p)^2\frac{(a-1)(a-p-1)}4.
```

Put $`f=\theta H_p`$. On an old unramified constituent the Hecke polynomial gives

```math
(U_p^{(2)})^2t(\varphi_p)
      =(U_p^{(2)})^3+d(\varphi_p)U_p^{(2)}.
```

On a conductor-one principal series, $`U_p^{(2)}`$ is the unramified eigenvalue $`\lambda`$, while trace and determinant are $`\lambda+\mu,\lambda\mu`$, giving the same identity. These exhaust the retained ambient systems, as in Lemma F.5. Assume $`p\equiv3\pmod4`$. The coefficient of $`\theta\Theta_1`$ at $`p`$ is exactly zero because $`p`$ is not a sum of two squares. The other two summands have the same character, so their determinant action has a common scalar. Since $`f[p]\equiv H_p[p]=0\pmod{\mathfrak{m}}`$, the coefficient $`(d(\varphi_p)f)[p]`$ is zero modulo $`\mathfrak{m}`$. Evaluate the displayed cubic identity at coefficient one to obtain

**Equation (H.5).**

```math
[t(\varphi_p)f]_{p^2}\equiv H_p[p^3]\pmod{\mathfrak{m}}.
```

All divisions have already occurred in the integral Fourier lattice.

Realize the finite trace data of $`\varphi_p`$ by a fresh prime $`p'`$ split in $`K`$, with the same support-unit labels as $`p`$. Then $`pp'`$ lies on the filter, and the left side of (H.5) tests $`H_p[p^2p']`$. Here the underlying squarefree index is $`pp'`$ and $`\kappa=0`$. The coefficient differs from $`2^{-2}a(pp')`$ only by the odd factor $`a-1`$ and the unit phase $`\eta(p)`$. The assumed extra valuation makes it zero modulo $`\mathfrak{m}`$. Equation (H.4) therefore gives $`(a-1)(a-p-1)/4\equiv0\pmod2`$. Since $`a`$ is even and $`a\equiv p+1\pmod4`$, this forces $`a\equiv p+1\pmod8`$. A fresh prime in (H.3) contradicts this: $`a\equiv0`$ whereas $`p+1\equiv4\pmod8`$.

### H.3. Compatible moving stages and the fixed companion

If the stabilized odd symbol is a unit at the empty configuration, a sufficiently precise actual stage already detects analytic order one at $`h=1`$. Otherwise choose a nonempty minimum positive-count witness for it. Choose $`k`$ as above after the intrinsic odd support and normalization have been fixed. Since the detecting primes $`ℓ_M`$ were chosen pairwise distinct, discard the finitely many stages with $`ℓ_M\mid k`$. This cofinite restriction belongs to the existing nonprincipal ultrafilter and preserves its stabilized tables, minimum depth, and witness; no detector sequence is replaced. The ramification of $`k`$ outside $`S_0`$ then gives

```math
K\cap\mathbb{Q}\bigl(\sqrt{-1},\sqrt p:
                   p\in S_0\cup\{ℓ_M\}\bigr)=\mathbb{Q}.
```

Indeed the field on the right is unramified at every prime of $`k`$. Consequently every intrinsic odd label has a lift represented by a prime split in $`K`$. Proposition H.4 supplies a nonempty even minimum witness on the split-prime alphabet for $`E^{(k)}`$.

Take the common quadratic alphabet of the odd and even tests, restricted to primes split in $`K`$. It projects onto each individual label set needed by these witnesses: odd surjectivity follows from the displayed disjointness, and even surjectivity is its defining split restriction. Only these individual projections are needed for Lemma G.6. The fixed support of $`k`$ is a finite enrichment, so stabilize its tables with the same ultrafilter as in Section F.2. This preserves the intrinsic odd minimum and witness.

For each $`b`$, assign a copy of a common neutral packet to every nonzero linear form on $`\mathbb{F}_2^b`$, activating all its vertices by that form. At each $`x\ne0`$ at least one packet is active. Its union is partitionable separately for both tests, so both terminal polynomials are nonzero. Every packet has common total zero, keeping the positive local filter and the splitting conditions. Theorem G.5 adds primary auxiliaries, also split in $`K`$, and makes both symbols units at every nonzero address. First choose these finite graphs and all their networks in the stabilized alphabet; only then choose an actual stage meeting their finite weight and precision requirements and realize them by primes. No new prime is active at zero, so the resulting family has

```math
h_x=\prod_q(q^*)^{\lambda_q(x)},\qquad h_0=1.
```

The total type makes each $`h_x`$ positive with the prescribed local squareclasses. All active primes are split in the one fixed field $`K`$. The varying detector prime is a coefficient-label prime; it is not an additional ramified place of the ring-class interpolation over this fixed $`K`$.

**Theorem H.5 (Rank one for the auxiliary curve).**

If $`s_2(E/\mathbb{Q})=1`$, then

```math
\mathrm{ord}_{s=1}L(E,s)=1,
 \qquad\mathrm{rank}E(\mathbb{Q})=1,
```

and $`\mathrm{Sha}(E/\mathbb{Q})`$ is finite.

*Proof.* In the empty-unit case this follows from the detected nonzero genus point, Gross–Zagier, and the forward theorem. Otherwise use the families just constructed, for arbitrarily large $`b`$. At every nonzero address the odd unit gives

```math
\mathrm{ord}_{s=1}L(E^{(h_x)},s)=1,\qquad
 j(P_{h_x})\le\omega(h_x)+C_1,
```

and the even unit for $`E^{(k)}`$ gives

```math
L(E^{(kh_x)},1)\ne0,\qquad
 v_2(L_*(kh_x))\le2\omega(h_x)+C_2.
```

Here $`k`$ is fixed, so its prime count is absorbed in $`C_2`$. The constants use the original coefficient minima and are independent of the cube, its vertex count, and the chosen actual odd stage. Proposition E.1 gives

```math
2j_{h_x}(k)\le4\omega(h_x)+C_3,
```

and therefore

```math
2j_{h_x}(k)-4\omega(h_x)-s(h_x)-s(kh_x)\le C_3.
```

The two $`s`$‑terms are nonnegative and finite by the forward theorem. Since $`L(E^{(k)},1)\ne0`$, that theorem also gives $`s_2(E^{(k)}/\mathbb{Q})=0`$. Restriction and quadratic projection after tensoring with $`\mathbb{Q}_2`$ give the corank identity

```math
s_2(E/K)=s_2(E/\mathbb{Q})+s_2(E^{(k)}/\mathbb{Q})=1.
```

All hypotheses of the fixed-field ring-class missing-vertex theorem, Theorem D.2, are now satisfied, with one constant for arbitrarily large cubes. Its base Heegner point is nontorsion and $`L(E,s)L(E^{(k)},s)`$ has order one at $`s=1`$. The second factor is nonzero there, so $`E`$ has analytic order one. The forward Gross–Zagier–Kolyvagin theorem gives rank one and finiteness of $`\mathrm{Sha}`$.

---

[← Appendix E](appendix-e.md) · [Main article](README.md) · [References →](references.md)
