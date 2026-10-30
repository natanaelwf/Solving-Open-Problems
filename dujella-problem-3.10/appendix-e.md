[← Appendix D, sections D.5–D.8](appendix-d-continued.md) · [Main article](README.md) · [Appendices F–H →](appendices-f-h.md)

---

## Appendix E. Coefficient systems and the comparison of Heegner sums

Throughout this section $`E=F`$ is the auxiliary curve. By Lemma A.1, it is non-CM, has full rational two-torsion, has functional sign $`-1`$, and satisfies

```math
v_2(N)=4,\qquad w_{16}(E)=-1,\qquad a_{19}(E)=0,\qquad 19\nmid N.
```

All varying primes are odd and of good reduction. Thus their weights are one and $`w(h)=\omega(\vert h\vert )`$. A fixed-support filter specifies a real sign, unit squareclasses at finitely many primes containing $`2N`$, and finitely many exclusions. Its parameters are squarefree and prime to its support. We use the normalized central value $`L_*(h)`$ and the notation $`s(h)`$ and $`s_2(E^{(h)})`$ established above.

The constructions below specialize the coefficient, graph, and assembly arguments of OpenAI (2026). We retain the ordinary coefficient symbols throughout.

### E.1. The two Heegner sums

Fix a modular parametrization $`\phi:X_0(N)\longrightarrow E`$ with $`\phi(\infty)=O`$. Let $`h\gt 0`$, $`k\lt 0`$, and $`h_*\lt 0`$ be pairwise coprime odd fundamental discriminants prime to $`2N`$. Assume that $`k`$ is a square at every prime of $`2Nh`$, that $`h,h_*`$ are squares at $`2N`$, and that the quadratic fields below have unit group $`\{\pm1\}`$. Let $`R_h(k)`$ be the unaveraged conductor‑$`h`$ ring-class character sum over $`\mathbb{Q}(\sqrt{k})`$ for the restriction of $`\chi_h`$. Let $`P_h`$ be the unaveraged conductor-one genus-character sum over $`\mathbb{Q}(\sqrt{hh_*})`$ for its genus character $`\chi_{h_*}`$. Both use $`\phi`$ and the absolute canonical height.

**Proposition E.1 (Exact height ratio).**

Suppose that $`E^{(h)},E^{(hk)},E^{(h_*)}`$ have respective analytic orders $`1,0,0`$ at $`s=1`$. Then

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

The constant is independent of the number and sizes of the primes of $`h`$ and $`k`$.

*Proof.* In the unaveraged normalization of Cai, Shu and Tian (2014, Theorem 1.1), the varying denominator is $`c\sqrt{\vert D\vert }`$, where $`D`$ is the quadratic field discriminant and $`c`$ the ring-class conductor. The additional factors are $`2^{-\mu(N,D)}`$ and the inverse square of $`[\mathcal{O}_c^\times:\mathbb{Z}^\times]`$. Here $`(N,D)=1`$ and the unit index is one in both applications. Both fields have degree two, so their conversion to absolute height also agrees. A common nonzero constant $`C_\phi`$ therefore gives

```math
L'(E^{(h)},1)L(E^{(hk)},1)
   =\frac{C_\phi}{h\sqrt{\vert k\vert }}\widehat h(R_h(k)),\qquad
 L'(E^{(h)},1)L(E^{(h_*)},1)
   =\frac{C_\phi}{\sqrt{\vert hh_*\vert }}\widehat h(P_h).
```

The first character has exact conductor $`h`$: every prime of $`h`$ splits in $`\mathbb{Q}(\sqrt{k})`$, and its quadratic character remains ramified on each split factor. The second is the unramified genus character. Artin formalism gives the two displayed factorizations. Division proves the height ratio.

The free components of both points belong to the rational $`h`$‑twist line; the other twist summands have rank zero by the forward theorem. Restriction and signed trace have composite multiplication by two over a quadratic extension and by four in the biquadratic realization. Thus comparison with the rational free lattice changes an index by a bounded integer. On a rank-one lattice the valuation of a height ratio is twice the index difference. The fixed nonzero factor $`L_*(h_*)`$ gives (E.1). There is no varying product of conductor-prime factors in this normalization.

### E.2. Even coefficients

Fix a root-number $`+1`$ filter $`d=\sigma D`$, where $`\sigma\in\{\pm1\}`$ and $`D\gt 0`$ is squarefree, and choose a nonvanishing seed $`D_0`$ by the fixed-local-type nonvanishing theorem. All compared indices have the same unit squareclasses as $`D_0`$ at the fixed support. For every application of the cyclotomic bounds to the original curve $`E=F`$, this filter is required to have $`d`$ a square at every prime of $`2N`$. The coefficient construction itself has the more general fixed-local-type scope stated below.

**Proposition E.2 (Even coefficient system).**

There is an algebraic holomorphic cusp form $`g=\sum_{n\ge1}a(n)q^n`$ of weight $`3/2`$, orthogonal to unary theta series, with fixed level and characters $`\eta,\psi`$ of $`2`$‑power order, such that $`\psi/\eta=\chi_{-\sigma}`$ and

**Equation (E.2).**

```math
a(p^2n)=
 \bigl(\eta(p)a_p(E)-\psi(p)(-n/p)\bigr)a(n)
       -p\eta(p)^2a(n/p^2)
```

outside the support. Its squarefree coefficients vanish off the filter. Normalize $`a(D_0)=1`$. For every admissible squarefree $`D`$ there are a $`2`$‑power root of unity $`\zeta_D`$ and $`r_D\in\mathbb{Q}`$ with

**Equation (E.3).**

```math
a(D)=\zeta_Dr_D,\qquad
 r_D^2=\frac{L_*(\sigma D)}{L_*(\sigma D_0)}.
```

Thus nonvanishing of the coefficient is equivalent to nonvanishing of the central value.

*Proof.* We use the even construction of OpenAI (2026), spelling out its scalar realization. Put $`\rho=\pi_{E^{(\sigma)}}`$ in unitary normalization. Nonvanishing of $`L(\rho\otimes\chi_{D_0},1/2)`$ implies that the global metaplectic space $`T_{D_0}(\rho)`$ and its $`D_0`$ Fourier functional are nonzero; these implications are recorded in the proof of Waldspurger (1981, Proposition 18, p. 467). Its finite normalized central signs are

```math
\omega_p=\chi_{D_0,p}(-1)
       \epsilon(\rho_p\otimes\chi_{D_0,p},1/2)
```

by Waldspurger (1981, Assertion 10, p. 397). Choose $`2`$‑primary unit characters $`\psi_p`$ with $`\psi_p(-1)=\omega_p\chi_{-1,p}(-1)`$. At good primes outside $`2N`$ this value is one, including primes of $`D_0`$: the two unramified characters of $`\rho_p`$ have product one and their quadratic epsilon-factor product is $`\chi_{D_0,p}(-1)`$. At infinity the weight-two epsilon factor is $`-1`$. The global sign of the nonvanishing twist is $`+1`$, so the product of the prescribed finite values of $`\psi_p(-1)`$ is one. The Chinese remainder theorem gives an even Dirichlet character $`\psi`$ of $`2`$‑power order supported on $`2N`$ with these values. Set

```math
\chi_0=\psi\chi_{-1},\qquad \eta=\psi\chi_{-\sigma}.
```

Then $`\pi_{E\otimes\eta}\otimes\chi_0^{-1}=\rho`$ and $`\chi_{0,p}(-1)=\omega_p`$.

At an exceptional finite prime use the Kirillov model in Waldspurger (1981, Assertion 7, p. 396), with character $`\mu_p=\chi_{0,p}`$. The $`D_0`$ squareclass belongs to its Whittaker support, so its Schwartz subspace contains

```math
t_p=\mathbf{1}_{D_0(\mathbb{Z}_p^\times)^2}.
```

This vector is nonzero at $`D_0`$, has integral support, and is invariant under unit-square multiplication of its argument. The Kirillov action therefore gives the required normalized diagonal character $`\gamma_p(u)\chi_{0,p}(u)^{-1}`$ for every unit $`u`$. Integral upper unipotents fix it, and smoothness gives invariance under sufficiently deep lower unipotents. Elsewhere choose spherical vectors, whose squarefree local coefficients at valuations zero and one are both one. The positive index $`D_0`$ selects the holomorphic weight‑$`3/2`$ component at infinity. The scalar-realization criterion in Waldspurger (1981, Theorem 2(1), p. 458, and Lemma 41, p. 476) now gives a classical vector with nonzero $`D_0`$ coefficient.

Impose coprimality and unit-squareclass coefficient sieves at the fixed support. They retain $`D_0`$ and commute with good $`T(p^2)`$, since an index and its multiple or quotient by $`p^2`$ satisfy the same conditions. The classical good-Hecke formula Shimura (1973) has eigenvalues $`\eta(p)a_p(E)`$, giving (E.2) and excluding unary constituents. The algebraic $`q`$‑expansion model of the half-integral-weight space Ramsey (2006, Sections 3–4) and these algebraic linear conditions permit an algebraic vector with nonzero $`D_0`$ coefficient. Only extension of characteristic-zero fields is used here; no integral base-change assertion at two is required. Its level and denominators are fixed.

Let $`V`$ be the entire cusp space at this level and character with these good eigenvalues. Its existence verifies (H1) of Waldspurger (1981, Proposition 2). For every $`f\in V`$, Waldspurger (1981, Corollary 2, pp. 483–484) gives

**Equation (E.4).**

```math
a_f(D)^2=
 \psi(D/D_0)\frac{L_*(\sigma D)}{L_*(\sigma D_0)}a_f(D_0)^2.
```

Its real factor is $`\sqrt{D/D_0}`$, already incorporated in $`L_*`$. Bad local factors agree, and the good squarefree factors at valuations zero and one are both one. The final paragraph of that corollary removes (H2) for indices in the same squareclass at two. The two coefficient functionals are proportional on all of $`V`$: their squared relation factors into two linear forms in the polynomial ring on $`V`$, which is a domain. One factor vanishes identically. This includes oldvectors and their linear combinations.

Put $`\xi=a(D)/a(D_0)`$. Let an algebraic automorphism $`u`$ act on the $`2`$‑power character roots by an odd exponent $`e`$, and set $`ν=\eta^{(e-1)/2}`$. At a common level supported on the same primes, $`g^u`$ and $`g\otimesν`$ have the same character $`\psi^e=\psiν^2`$ and the same good eigenvalues $`\eta(p)^ea_p(E)`$. The full-space proportionality gives

```math
u(\xi)=ν(D/D_0)\xi.
```

Choose unit square roots of $`D/D_0`$ at the conductor of $`\eta`$ and let $`\zeta_D`$ be their value under $`\eta`$. Then $`\zeta_D^2=\eta(D/D_0)`$, $`u(\zeta_D)=\zeta_D^e`$, and $`ν(D/D_0)=\zeta_D^{e-1}`$. Thus $`\xi/\zeta_D\in\mathbb{Q}`$. Different choices change it by at most a sign. Since $`\psi/\eta`$ is quadratic and the ratio is locally square, division of (E.4) by $`\zeta_D^2`$ proves the assertion.

On a filter of parameters locally square at $`2N`$, the cyclotomic lower bound, Theorem C.1, gives

**Equation (E.5).**

```math
v_2(a(D))\ge\omega(D)+\tfrac12s(\sigma D)-C_g
              \ge\omega(D)-C_g
```

at nonzero coefficients. Phase removal makes their finite normalized valuations integers, so a least normalized depth is attained.

### E.3. An integral Kummer detector

Fix an odd negative fundamental discriminant $`h_*\lt -4`$, square at $`2N`$, with $`L(E^{(h_*)},1)\ne0`$. Let $`S_0`$ contain the primes of $`2Nh_*`$ and every other fixed prime needed for the intrinsic coefficient tests. At every finite prime of $`S_0`$ choose the square unit class, and require positive parameters. This is the prepared positive filter; in particular, it contains the parameter $`1`$. Choose a positive simple-zero witness $`D_w`$ on this final filter by Proposition B.2. The choices of $`h_*`$ and $`D_w`$ are supplied by the classical nonvanishing results. The genus Gross–Zagier formula makes $`P_{D_w}`$ nontorsion.

A single integer $`L\gt 0`$ kills torsion in all biquadratic fields containing the genus sums and the cuspidal constants in the Atkin–Lehner formulas for $`\phi`$. For the torsion assertion choose two distinct good primes $`p,q`$, and put

```math
C_p=\prod_{f=1}^4\#E(\mathbb{F}_{p^f}),\qquad
 C_q=\prod_{f=1}^4\#E(\mathbb{F}_{q^f}).
```

Over a field of degree at most four, prime-to‑$`p`$ torsion injects into a reduction of residue degree at most four and is killed by $`C_p`$; its $`p`$‑primary torsion is killed by $`C_q`$. Thus $`C_pC_q`$ is a uniform annihilator. After multiplication by $`L`$, each genus point has the exact Galois transformation rule of the $`D`$‑twist and defines a rational point on $`E^{(D)}`$ under the twisting isomorphism.

Let $`T=T_2E`$, let $`C`$ be complex conjugation on $`T`$, and choose a primitive integral row $`b:T\to\mathbb{Z}_2`$ with $`bC=b`$. It is obtained from a rational invariant row by clearing denominators and dividing its content. No integral eigenspace decomposition is used.

**Lemma E.3 (Translation lattice).**

Let $`A/\mathbb{Q}`$ be non-CM and $`Q\in A(\mathbb{Q})`$ nontorsion. For a compatible division tower let $`c_Q:G_{\mathbb{Q}}\to T_2A`$ be its Kummer cocycle. On $`H=\ker\rho_{T_2A}`$ its image contains $`2^aT_2A`$ for some $`a`$. This remains true after intersecting $`H`$ with the kernel of any fixed finite Galois data.

*Proof.* On $`H`$ the cocycle is a homomorphism with compact image, hence a closed $`\mathbb{Z}_2`$‑submodule. Moreover $`c_Q(ghg^{-1})=\rho(g)c_Q(h)`$. The non-CM open-image theorem makes the rational Tate representation irreducible and supplies a scalar $`u\ne1`$ in its image. If $`c_Q(H)=0`$, the rational Kummer class factors through the Tate image. Comparison at $`ug`$ and $`gu`$ gives $`(u-1)c(g)=(\rho(g)-1)c(u)`$, making it a rational coboundary. This contradicts Kummer injectivity for the nontorsion point $`Q`$. Its nonzero rational span is therefore all of $`V_2A`$, so the closed image contains a full lattice. A finite-index subgroup of $`H`$ has translation image of finite index, proving the last assertion.

**Proposition E.4 (Finite-field detection).**

For arbitrarily large $`M`$ there are fresh good primes $`ℓ`$ with

```math
\rho_T(\mathrm{Fr}_ℓ)\equiv C\pmod{2^M},\qquad
 (D_w/ℓ)=1,\qquad(h_*/ℓ)=-1,
```

and integral Frobenius-invariant homomorphisms

```math
\lambda_M:E(\mathbb{F}_{ℓ^2})\longrightarrow\mathbb{Z}/2^M\mathbb{Z}
```

for which $`\lambda_M(\mathrm{red}_ℓ(LP_{D_w}))`$ has one fixed finite valuation. The primes may avoid any prescribed finite set.

*Proof.* Apply Lemma E.3 to $`A=E^{(D_w)}`$ and the rational point corresponding to $`LP_{D_w}`$. Since $`D_w\gt 0`$, conjugation acts by $`C`$ on its Tate module. Intersect the Tate kernel with the kernels of the fixed quadratic data. Choose $`v`$ in its translation image with $`b(v)=2^a`$, and $`h`$ in this kernel with $`c_Q(h)=v`$. For actual conjugation $`\tau`$ put $`g=\tau h`$. The relation $`\tau^2=1`$ gives $`(1+C)c_Q(\tau)=0`$, and hence

```math
c_Q(g^2)=(1+C)v,\qquad b(c_Q(g^2))=2^{a+1}.
```

The element $`g`$ fixes $`\sqrt{D_w}`$ and negates $`\sqrt{h_*}`$. For $`M\gt a+1`$ take the finite Galois quotient recording $`2^M`$‑torsion, $`2^M`$‑division of the point, and these characters. Chebotarev realizes its conjugacy class at infinitely many good primes; choose a place realizing the specified representative.

Lang’s theorem and finite-field Kummer theory give

```math
E(\mathbb{F}_{ℓ^2})/2^ME(\mathbb{F}_{ℓ^2})
 \simeq H^1(\mathbb{F}_{ℓ^2},E[2^M])
 \simeq T/(2^MT+(\mathrm{Fr}_ℓ^2-1)T)=T/2^MT.
```

This is evaluation at arithmetic Frobenius squared. Composition with $`b`$ defines $`\lambda_M`$; it is Frobenius-invariant because $`bC=b`$ and $`\mathrm{Fr}_ℓ\equiv C`$. Splitting of $`D_w`$ at $`ℓ`$ identifies the twisting isomorphism and the prescribed reduction of the division cocycle. Finally the Weil pairing gives $`ℓ\equiv\det C=-1\pmod{2^M}`$, so $`ℓ\equiv3\pmod4`$ when $`M\ge2`$. Choosing successively and excluding the previously chosen primes gives a detector sequence $`(ℓ_M)`$ with pairwise distinct entries.

### E.4. The integral theta bridge

For positive squarefree admissible $`D`$ put $`K_D=\mathbb{Q}(\sqrt{Dh_*})`$ and fix one Heegner orientation at each level prime. The unaveraged genus sum is

```math
P_D=\sum_{[\mathfrak{a}]\in\mathrm{Pic}(\mathcal{O}_{K_D})}
       \chi_{h_*}(N\mathfrak{a})\,\phi(x_D^{[\mathfrak{a}]}).
```

The support includes the primes of $`h_*`$, so they cannot cancel and $`\mathcal{O}_{K_D}^\times=\{\pm1\}`$.

**Proposition E.5 (Integral theta bridge).**

Let $`ℓ\nmid2Nh_*`$ be good, $`ℓ\equiv3\pmod4`$, and $`(h_*/ℓ)=-1`$. Let $`\lambda:E(\mathbb{F}_{ℓ^2})\to\mathbb{Z}/2^M\mathbb{Z}`$ be an integral Frobenius-invariant homomorphism. There is a holomorphic weight‑$`3/2`$ form $`g_M=\sum_{n\ge1}a_M(n)q^n`$ with integral coefficients in one fixed $`2`$‑power cyclotomic ring such that

**Equation (E.6).**

```math
a_M(D)\equiv c_0\,2^{\omega(N)}\zeta_M(D)
     \lambda(\mathrm{red}_ℓ(LP_D))\pmod{2^M}
```

at admissible squarefree $`D`$ with $`(D/ℓ)=1`$. Here $`c_0\gt 0`$ is independent of $`D,M,ℓ`$ and $`\zeta_M(D)`$ is a $`2`$‑power root of unity. Coefficients vanish off the support filter and unless $`(D/ℓ)=1`$. The level is supported on the fixed primes and $`ℓ`$; its good-prime recurrence is (E.2) modulo $`2^M`$, with $`\psi/\eta=\chi_{-4}`$.

*Proof.* We give the theta construction of OpenAI (2026) in the present local type. Its geometric input is the equivariant CM-reduction correspondence of Cornut and Jetchev (2013, Sections 3.2 and 4.9–4.10, Corollary 4.1), valid for arbitrary level prime to $`ℓ`$.

Let $`B/\mathbb{Q}`$ be ramified at $`ℓ`$ and infinity, $`R`$ an Eichler order of level $`N`$, and

```math
V=B^0,\quad Q(x)=-x^2,\quad
 X=B^\times\backslash\widehat B^\times/\widehat R^\times.
```

The set $`X`$ parametrizes supersingular pairs with cyclic level subgroup; all are defined over $`\mathbb{F}_{ℓ^2}`$. Choose arbitrary integer lifts of $`P(z)=\lambda(L\phi_ℓ(z))`$. Modulo $`2^M`$ this is a Brandt eigenfunction of eigenvalue $`a_p(E)`$ at $`p\nmid Nℓ`$: Hecke correspondences commute with the elliptic quotient and reduction, and the normalization at infinity removes the Hecke constant. Multiplication by $`L`$ removes the Atkin–Lehner cuspidal constants, so the operator at $`p^e\Vert N`$ acts by $`w_{p^e}`$. An $`ℓ`$‑uniformizer acts by $`+1`$, since it induces residue Frobenius.

Construct $`f=\prod_pf_p`$ on $`\widehat V`$ as follows. Away from $`2Nh_*ℓ`$ take $`\mathbf{1}_{R_p^0}`$. Impose extra fixed squareclass and coprimality conditions on $`Q(x)`$; they are conjugation-invariant and stable under unit-square scaling of the norm.

At $`p^e\Vert N`$, require an embedding of the split maximal quadratic algebra with $`x^2`$ a unit square. The cyclic level quotient selects one of its integral summands. Give the eigenvalue $`r`$ of $`x`$ there weight $`\alpha_p(r)`$, with $`\alpha_p`$ of $`2`$‑power order and

```math
\alpha_p(-1)=w_{p^e}\chi_{h_*}(p)^e=w_{p^e}.
```

At odd $`p`$, a character of the $`2`$‑primary quotient of $`\mathbb{F}_p^\times`$ realizes either sign at $`-1`$. At two use

```math
R_2=\left\{\begin{pmatrix}a&b\\ c&d\end{pmatrix}:
 a,b,d\in\mathbb{Z}_2,\ c\in16\mathbb{Z}_2\right\},
```

impose $`(1+x)/2\in R_2`$, and take $`\alpha_2=\chi_{-4}`$. If $`r^2=x^2`$, the eigenvalues of $`(1+x)/2`$ differ by the unit $`r`$. Its idempotent summands are therefore distinct even modulo two. For odd $`u`$ the identity $`(1+ux)/2=u(1+x)/2+(1-u)/2`$ leaves the selected summand unchanged and replaces $`r`$ by $`ur`$. This proves the required unit-scaling rule.

At $`p\mid h_*`$ require $`x\in M_2(\mathbb{Z}_p)^0`$ and $`v_p(Q(x))=1`$. Its reduction is a nonzero nilpotent. With $`X_0=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)`$ put

```math
\epsilon_p(gX_0g^{-1})=(\det g/p).
```

The centralizer has square determinant, making this well-defined, and

```math
\epsilon_p(uyu^{-1})=(\det u/p)\epsilon_p(y),\qquad
 \epsilon_p(ay)=(a/p)\epsilon_p(y).
```

Use $`\epsilon_p(\bar x)`$ as the weight. At $`ℓ`$, the maximal-order residue field is $`\mathbb{F}_{ℓ^2}`$. Choose a nonzero basis $`\beta`$ of its trace-zero line and set $`f_ℓ(x)=(t/ℓ)`$ if $`\bar x=t\beta\ne0`$, and zero otherwise. Order units conjugate trivially on the residue field; a uniformizer sends $`\beta`$ to $`-\beta`$ and changes the weight by $`-1`$. Both $`\beta^2`$ and $`-1`$ are nonsquares, so $`Q(x)=-t^2\beta^2`$ is a unit square. Since $`(\vert h_*\vert /ℓ)=1`$, the index $`\vert h_*\vert D`$ forces $`(D/ℓ)=1`$.

This compactly supported locally constant function satisfies

**Equation (E.7).**

```math
f(u^{-1}xu)=\chi_{h_*}(\mathrm{Nrd}u)^{-1}f(x)
 \quad(u\in\widehat R^\times).
```

Its total unit-scaling character is even: the level contribution at $`-1`$ is $`\prod w_{p^e}=+1`$, whereas the $`h_*`$ and $`ℓ`$ contributions are both $`-1`$. Its values belong to one fixed $`2`$‑power cyclotomic field, since the moving character at $`ℓ`$ is quadratic.

Scalar modularity can be checked from the Weil operators. For an additive character of conductor $`\mathbb{Z}_p`$ these are

```math
\omega(n(b))f_p(x)=e_p(bQ(x))f_p(x),\quad
 \omega(m(u))f_p(x)=\gamma_p(u)\vert u\vert _p^{3/2}f_p(ux),\quad
 \omega(w)f_p=\gamma_p\widehat f_p.
```

Integral upper unipotents fix $`f_p`$ because $`Q`$ is integral on its support. If $`f_p`$ is translation-invariant by $`L'_p`$, its Fourier transform is supported on $`(L'_p)^\vee`$. Choose $`A_p`$ with $`p^{A_p}Q((L'_p)^\vee)\subset\mathbb{Z}_p`$; Fourier conjugation gives deep lower-unipotent invariance. Relative to the ordinary theta multiplier cubed, the diagonal factor is $`(\det Q,u)_p`$. The presentation $`B=(-a,-b)`$ gives $`Q=aX^2+bY^2+abZ^2`$ with square determinant $`(ab)^2`$. Thus only the computed unit-scaling character remains. For a matrix with unit upper-left entry,

```math
\begin{pmatrix}a&b\\ c&d\end{pmatrix}=n_-(c/a)m(a)n(b/a).
```

This proves scalar transformation under a sufficiently deep $`\Gamma_0(p^{A_p})`$; at two include the metaplectic splitting depth. Denote the classical character by $`\eta_B`$. In the inverse finite adelic action the diagonal entry is the classical lower-right entry $`d`$, fixing the convention $`\eta_B(d)`$. The real Gaussian gives weight $`3/2`$. Positive definiteness gives nonnegative exponents at every cusp, also after finite Weil transforms.

Choose $`c_0`$ divisible by all possible orders $`\vert R_z^\times\vert `$, uniformly in $`ℓ`$. These finite groups act faithfully on the rank-four integral lattice $`R_z`$, so the finite-subgroup bound for $`\mathrm{GL}_4(\mathbb{Z})`$ supplies such an integer. Define

```math
H_M(n)=c_0\sum_{z\in X}
 \frac{P(z)\chi_{h_*}(\mathrm{Nrd}z)}{\vert R_z^\times\vert }
 \sum_{\substack{x\in B^0\\ Q(x)=n}}f(z^{-1}xz).
```

Equation (E.7) proves independence of right representatives. The norm character is trivial on positive rational norms, giving independence of left representatives. The Weil calculation proves modularity. Every $`c_0/\vert R_z^\times\vert `$ is integral, so the coefficients are integral and changing a lift of $`P`$ by $`2^M`$ changes them by multiples of $`2^M`$.

At good $`p`$, Brandt neighbors are the lines in $`\mathbb{F}_p^2`$. A nonzero nilpotent has one invariant line; a nonzero semisimple trace-zero matrix of norm $`n`$ has $`1+(-n/p)`$ invariant lines; zero reduction contributes $`p`$ extra lines. If a primitive $`y`$ has $`p^2\mid Q(y)`$, put its reduction in the form $`X_0`$. Its diagonal entry is divisible by $`p`$, its upper-right entry is a unit, and the norm condition makes its lower-left entry divisible by $`p^2`$. Exactly the neighbor of its invariant line makes $`y/p`$ integral. These cases, with the stabilizer weights, give

```math
\begin{aligned}
 H_M(p^2n)&+\eta_B(p)(-n/p)H_M(n)
             +p\eta_B(p)^2H_M(n/p^2)\\
 &\equiv\eta_B(p)\chi_{h_*}(p)a_p(E)H_M(n)\pmod{2^M}.
\end{aligned}
```

Here $`\eta_B(p)`$ comes from unit scaling at the other places and $`\chi_{h_*}(p)`$ from the reduced norm of a neighbor.

At $`n=\vert h_*\vert D`$, representations are exactly optimal embeddings $`\mathcal{O}_{K_D}\hookrightarrow R_z`$ sending $`\sqrt{Dh_*}`$ to $`x`$. The condition at two is integrality of $`(1+\sqrt{Dh_*})/2`$; fundamental discriminant implies optimality. There are two orientations at each level prime, two at $`ℓ`$, and one local orbit elsewhere. For a fixed tuple, embedding orbits are parametrized by $`\mathrm{Pic}(\mathcal{O}_{K_D})`$. Replacing $`z_0`$ by $`az_0`$ with $`a\in\widehat K_D^\times`$ leaves $`z_0^{-1}xz_0`$ unchanged, and its relative norm character is $`\chi_{h_*}(N_{K_D/\mathbb{Q}}a)`$. The equivariant reduction correspondence identifies these projected pairs with reductions of the CM class orbit.

An embedding stabilizer is $`\{\pm1\}`$, so an orbit contributes $`c_0/2`$ times the unaveraged genus sum. Reversing a level orientation changes the Schwartz weight and the norm-weighted parametrization by the same sign $`w_{p^e}\chi_{h_*}(p)^e`$; reversing the $`ℓ`$‑orientation changes both by $`-1`$. All $`2^{\omega(N)+1}`$ tuples consequently contribute equally, with one initial root-of-unity factor. The conjugate-pair formulation of the reduction correspondence keeps the factor two at $`ℓ`$, which cancels the stabilizer denominator. This gives

```math
H_M(\vert h_*\vert D)\equiv c_0\,2^{\omega(N)}\zeta_M(D)
       \lambda(\mathrm{red}_ℓ(LP_D))\pmod{2^M}.
```

Finally put $`a_M(n)=H_M(\vert h_*\vert n)`$. The operator $`U_{\vert h_*\vert }`$ preserves modularity and changes the character to $`\psi=\eta_B(\vert h_*\vert /\,\cdot\,)`$. The recurrence has $`\eta=\eta_B\chi_{h_*}`$, hence $`\psi/\eta=\chi_{-4}`$. Every normalization factor is independent of the number of varying primes.

---

[← Appendix D, sections D.5–D.8](appendix-d-continued.md) · [Main article](README.md) · [Appendices F–H →](appendices-f-h.md)
