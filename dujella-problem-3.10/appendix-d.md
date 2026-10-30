[← Appendix C](appendix-c.md) · [Main article](README.md) · [Appendix D, sections D.5–D.8 →](appendix-d-continued.md)

---

## Appendix D. Ring-class determinants

Throughout this section $`E=F`$ is the auxiliary curve, $`N`$ is its conductor, and $`T=T_2E`$. In particular, $`E`$ is non-CM and $`E[2]\subset E(\mathbb{Q})`$. Put

```math
\Lambda=\mathbb{Z}_2[[t]],\qquad
 \mathcal{O}=\widehat{\Lambda_{(2)}},\qquad
 \Omega=\mathbb{F}_2((t)),\qquad v_2(2)=1.
```

We use the ring-class deformation, determinant switch, and binary transfer construction of OpenAI (2026), with the integral local conditions and finite descent specified below.

Let $`K=\mathbb{Q}(\sqrt{k})`$ be imaginary quadratic, split at every prime dividing $`2N`$, with $`\mathcal{O}_K^\times=\{1,-1\}`$. Let $`h`$ be a product of distinct signed good odd primes, all split in $`K`$, with $`(h,k)=1`$. For a fixed modular parametrization $`\pi:X_0(N)\to E`$ normalized by $`\pi(\infty)=0`$, choose coherently oriented CM points $`y_c\in E(H_c)`$, where $`H_c`$ is the ring-class field of conductor $`c`$. The primitive, unaveraged sum is

```math
P_h(K)=\sum_{\sigma\in\mathrm{Gal}(H_{\vert h\vert }/K)}
                   \chi_h(\sigma)\,\sigma(y_{\vert h\vert })
              \in E^{(h)}(K).
```

Here the last inclusion uses the quadratic-twist identification. When $`L(E^{(h)},s)L(E^{(hk)},s)`$ has a simple zero at $`s=1`$, the Gross–Zagier–Kolyvagin theorem makes $`P_h(K)`$ nontorsion and $`E^{(h)}(K)`$ of rank one. Write $`j_h(k)`$ for the $`2`$‑adic valuation of its index in the free completed Mordell–Weil lattice. In this situation write

```math
s(h)=v_2\#\mathrm{Sha}(E^{(h)}/\mathbb{Q})[2^\infty],
 \qquad w(h)=\omega(\vert h\vert ).
```

These Shafarevich–Tate groups are finite by the same forward theorem.

**Theorem D.1 (Ring-class lower bound).** For every $`A\geq0`$ there is a constant $`C(E,A)`$ such that every such simple-zero instance with $`\omega(\vert k\vert )\leq A`$ satisfies

```math
2j_h(k)\geq 4w(h)+s(h)+s(hk)-C(E,A).
```

**Theorem D.2 (Ring-class missing vertex).** Fix $`K`$ as above and suppose

```math
\mathrm{corank}_{\mathbb{Z}_2}
       \mathrm{Sel}_{2^\infty}(E/K)=1.
```

Suppose there are binary families of arbitrarily large dimension $`b`$,

```math
h_x=\prod_{q\in Q}(q^*)^{\lambda_q(x)},\qquad
 x\in\mathbb{F}_2^b,\qquad
 \lambda_q:\mathbb{F}_2^b\longrightarrow\mathbb{F}_2\text{ linear},
```

where the primes in $`Q`$ are good, odd, split in $`K`$, and outside the fixed support. Assume all vertices have the same local squareclasses at $`2N`$ and the same real sign as $`h_0=1`$. Suppose every $`x\ne0`$ has a simple zero of $`L(E^{(h_x)},s)L(E^{(h_xk)},s)`$ and

```math
2j_{h_x}(k)-4w(h_x)-s(h_x)-s(h_xk)\leq B
```

with one constant $`B`$ for all families. Then

```math
\mathrm{ord}_{s=1}\bigl(L(E,s)L(E^{(k)},s)\bigr)=1.
```

No finiteness assumption on $`\mathrm{Sha}(E/K)`$ is made.

### D.1. Moving scalar characters

**Lemma D.3.** There is a constant $`c_E`$ with the following property. For any finite list of oriented split odd primes outside $`2N`$ and any integers $`n_i\to\infty`$, there are distinct split primes $`r_i`$ and characters

```math
\xi_i:\mathrm{Gal}(H_{r_i}/K)\longrightarrow\mathbb{Z}/2^{n_i}
```

surjective on inertia at $`r_i`$, trivial at the primes over $`2N`$, and odd on the prescribed oriented Frobenii. One may require $`r_i\to1`$ in $`\mathbb{Z}_2`$ and

```math
v_2(2-a_{r_i}),\quad v_2(2+a_{r_i}),\quad
 v_2\det(1-\mathrm{Fr}_{r_i}\vert T),\quad
 v_2\det(1+\mathrm{Fr}_{r_i}\vert T)\leq c_E.
```

The constant is independent of $`K`$ and of the list.

*Proof.* Choose split prime ideals $`\mathfrak{p}_j`$, with disjoint conjugate pairs, containing the prescribed ideals and ideals over $`2N`$, and enlarge the list to generate $`\mathrm{Cl}(K)`$. Assign weight $`1`$ to prescribed odd ideals, weight $`0`$ to the others, and opposite weights to conjugates. For a basis $`m^{(a)}`$ of the relation lattice choose

```math
(\beta_a)=\prod_j\mathfrak{p}_j^{m_j^{(a)}}.
```

Over $`K(\mu_{2^\infty})`$, prescribe the action on the $`2^n`$th roots of $`\beta_a/\overline\beta_a`$ by $`\zeta_{2^n}^{-\sum_jm_j^{(a)}w_j}`$. These prescriptions respect every Kummer relation: at an odd ideal with nonzero weight the cyclotomic extension is unramified, so a $`2^n`$th-power relation has each relevant valuation divisible by $`2^n`$. Weights over $`2`$ are zero. Kummer duality therefore supplies the prescribed automorphism.

For a split prime $`r`$, the ring-class exact sequence is

```math
1\longrightarrow\mathbb{F}_r^\times
 \longrightarrow\mathrm{Pic}(\mathbb{Z}+r\mathcal{O}_K)
 \longrightarrow\mathrm{Cl}(K)\longrightarrow1.
```

The units $`\pm1`$ are diagonal in the split residue quotient. The displayed principal relations say exactly that a primitive residue character of order $`2^n`$ extends with the prescribed values on the $`\mathfrak{p}_j`$. Conjugation inverts this character.

For compatibility with the Tate representation, let $`H_E`$ be its image over $`\mathbb{Q}(\mu_{2^\infty})`$. It is open in $`\mathrm{SL}_2(\mathbb{Z}_2)`$ by the open-image theorem Serre (1972). The image over $`K(\mu_{2^\infty})`$ has index at most two in $`H_E`$. Every such subgroup contains $`[H_E,H_E]`$, and its commutator contains $`[[H_E,H_E],[H_E,H_E]]`$. The latter contains a fixed open subgroup $`U_E`$: the Lie algebra $`\mathfrak{sl}_2(\mathbb{Q}_2)`$ is perfect. Lifted commutators fix the radical extension, which is abelian over the cyclotomic field. Thus a permitted Tate image can be varied throughout its $`U_E`$‑coset without changing the Kummer prescriptions.

There are finitely many such cosets. In each choose a matrix $`g_C`$ with trace different from $`2`$ and $`-2`$. This is possible because neither trace equation contains an analytic open subset of $`\mathrm{SL}_2`$. The maximum of $`v_2(2\pm\mathrm{tr}g_C)`$ is a fixed $`c_E`$. Restrict a lift with this Tate image to a finite extension containing the required radical roots, roots of unity, and sufficiently much $`2`$‑power torsion. Chebotarev supplies infinitely many primes realizing this finite condition, with a chosen place realizing its representative. Requiring $`r\equiv1\pmod{2^M}`$ for $`M\gt c_E`$ gives the two determinant bounds from $`\det\mathrm{Fr}_r=r`$. Finite avoidance gives distinct $`r_i`$ outside the previous support.

Put $`A_i=(\mathbb{Z}/2^i)[t]/(t^i)`$ and choose $`n_i\geq2i`$. Then $`\Psi_i=(1+t)^{\xi_i}`$ is well defined: the coefficients of $`(1+t)^{2^{n_i}}-1`$ below degree $`i`$ are divisible by $`2^i`$. These are finite characters. No prime is required to split in an infinite extension, and no compatibility of the chosen moving primes is assumed before the limiting construction.

### D.2. Integral local conditions and finite diagrams

**Lemma D.4 (Finite free models).** Let $`(A,\mathfrak{m},\kappa)`$ be an Artin local ring and let $`D`$ be a complex of flat $`A`$‑modules with finite-dimensional residual cohomology in a bounded interval. There is a bounded finite free complex $`C`$ and maps $`i,p,h`$ with

```math
pi=1,\qquad 1-ip=dh+hd,\qquad
 \mathrm{rank}C^j=\dim_\kappa H^j(D\otimes_A\kappa).
```

Every specified finite collection of chain maps, homotopies, pairings, and triangles can be transported through these contractions.

*Proof.* A flat module over an Artin local ring is free. Indeed, lift a basis modulo $`\mathfrak{m}`$; nilpotence kills the cokernel, and flatness and nilpotence kill the kernel. Split the residual complex into its cohomology and contractible disks, and lift the graded bases. If $`d_0`$ is the lifted disk differential, write $`d=d_0+\epsilon`$. For the disk contraction $`(i_0,p_0,h_0)`$, the inverses of $`1+h_0\epsilon`$ and $`1+\epsilon h_0`$ are finite geometric sums. The formulas

```math
\begin{aligned}
 d_C&=p_0\epsilon(1+h_0\epsilon)^{-1}i_0,\qquad
 i=(1+h_0\epsilon)^{-1}i_0,\\
 p&=p_0(1+\epsilon h_0)^{-1},\qquad
 h=h_0(1+\epsilon h_0)^{-1}
 \end{aligned}
```

give the asserted identities by substitution. They apply to infinite disk sums because every geometric sum terminates. Transport a map $`f`$ as $`p'fi`$ and retain the induced composition homotopies. A quasi-isomorphism between bounded free complexes has a contractible cone, which supplies its homotopy inverse.

Continuous cochains with finite free Artin coefficients are flat: the locally constant functions are filtered unions of finite free modules over finite clopen partitions. Reduction gives the actual reduced cochains. We apply Lemma D.4 to these cochains and their Selmer cones, keeping maps back to the original cochains.

**Lemma D.5 (Kummer conditions and coefficient duality).**

For a finite extension $`L`$ of a nonarchimedean local field of characteristic zero and an elliptic curve $`B/L`$, the condition

```math
U_L=B(L)^\wedge_2[-1]\longrightarrow R\Gamma(L,T_2B)
```

is perfect and exactly self-orthogonal under local Tate duality. Its derived reduction modulo $`2^a`$ has

```math
H^0=B(L)[2^a],\qquad H^1=B(L)/2^aB(L),
```

with the invariant isomorphism and Kummer injection as its maps to local cohomology. The local and totally imaginary global duality diagrams are natural under arbitrary, including nonflat, coefficient quotients.

*Proof.* The completed point group is finitely generated over $`\mathbb{Z}_2`$ and has a free resolution of length one. Its integral Kummer map defines the indicated derived morphism; the Kummer exact sequences give the asserted maps after reduction. The cup product on $`U_L\otimes^{\mathbf{L}}U_L`$ followed by the invariant map to $`\mathbb{Z}_2[-2]`$ is zero. Indeed, this source has amplitude $`[0,2]`$, and its morphisms to $`\mathbb{Z}_2[-2]`$ are determined by the map on degree-two cohomology; the possible $`\mathrm{Ext}^1(H^3,-)`$ term is zero. That map vanishes at every finite exponent by finite Kummer isotropy and hence vanishes integrally. Choose one nullhomotopy on free models. The resulting quotient-to-dual map is a quasi-isomorphism modulo $`2`$, by the perfect finite Kummer pairing, and therefore integrally by derived Nakayama. This proves exact orthogonality for every reduction type, also at $`2`$ Milne (2006, I, Theorem 3.2 and Corollary 3.4).

Start the invariant morphisms with $`R\Gamma(L,\mathbb{Z}_2(1))\to\mathbb{Z}_2[-2]`$ and, globally, the compact-support morphism to $`\mathbb{Z}_2[-3]`$. Define their $`A`$‑valued versions by derived tensor. Associativity gives naturality for every $`A\to B`$. The Weil pairing between $`T\chi_h\Psi\otimes A`$ and $`T\chi_h\Psi^{-1}\otimes A`$ is $`A`$‑bilinear; the character factors cancel before the invariant map. For a bounded free complex,

```math
R\mathrm{Hom}_A(C,A)\otimes_A^{\mathbf{L}}B
 \simeq R\mathrm{Hom}_B(C\otimes_A^{\mathbf{L}}B,B).
```

In bases this is transpose followed by reduction. Cone formation, restrictions, and the chosen isotropy homotopies commute with these operations. The usual local and Poitou–Tate duality morphisms therefore give coefficient-natural relative dualities Nekovář (2006, Proposition 5.2.4 and Theorem 6.3.4). A finite Frobenius-ring trace may check perfectness at an Artin stage; it is not used as a transition morphism.

For $`M_i=T\otimes\chi_h\Psi_i\otimes A_i`$ the Selmer complex is the actual mapping cone

```math
C_i=\mathrm{Cone}\left(
 R\Gamma(G_{K,S_i},M_i)\oplus\bigoplus_{v\in S_i}U_v
 \longrightarrow\bigoplus_{v\in S_i}R\Gamma(K_v,M_i)
 \right)[-1].
```

Use the integral Kummer condition at $`2N`$, the full condition at primes dividing $`h`$ and at $`r_i`$, and the unramified condition at other good places. The full condition has orthogonal condition zero. At a derivative prime we instead use the following truncations.

**Lemma D.6 (The derivative local complex).** Choose inert derivative primes $`ℓ`$ with rational Frobenius tending on $`T`$ to a fixed complex conjugation $`J`$. At retained precision $`2^a`$, impose $`ℓ^2\equiv1\pmod{2^{a+1}}`$ as well. The local complex has the split form

```math
M\oplus(F\oplus S)[-1]\oplus M[-2],\qquad F=S=M,
```

with zero differential and coordinates $`f(c)=c(\gamma^2)`$, $`s(c)=c(\sigma)`$, where $`\gamma`$ is rational Frobenius and $`\sigma`$ is oriented tame inertia. The conditions

```math
U_F=M\oplus F[-1],\quad U_S=M\oplus S[-1],\quad
 U_{\mathrm{str}}=M,\quad U_{\mathrm{rel}}=M\oplus(F\oplus S)[-1]
```

have compatible integral duality triangles; the first two are self-orthogonal and the last two are orthogonal complements. The mixed pairing is a unit multiple of $`\langle x,Jy\rangle`$.

*Proof.* The tame presentation is $`\phi\sigma\phi^{-1}\sigma^{-q}=1`$, $`q=ℓ^2`$. After trivial coefficient action its Fox complex has ranks $`(1,2,1)`$, differential $`d^0=0`$, $`d^1=(0,1-q)`$. Its cup diagonal has zero pure-finite term, unit mixed terms, and pure-tame coefficient $`\pm\binom q2`$. Both $`1-q`$ and $`\binom q2`$ vanish modulo $`2^a`$ under the imposed congruence. Equivalently, the field contains the $`2^{a+1}`$st roots of unity, so the norm-residue identity $`(x,x)=(x,-1)`$ makes the scalar square terms zero. Local Tate duality makes the mixed term a unit. This computation is coefficientwise and applies to the free Artin module, including its nilpotent variables. The pure-plane cup maps are zero already on these finite complexes; choose their zero homotopies. Conjugation acts by $`J`$ on the finite coordinate and by $`-J`$ on the singular coordinate, giving the displayed mixed pairing. The stated orthogonal complements and duality triangles follow directly.

### D.3. Integral derivative classes at two

**Lemma D.7 (Uniform direct descent).** There is an integer $`e`$ depending only on $`E`$ such that $`2^e`$ kills the $`2`$‑primary torsion over every compositum of ring-class fields of any imaginary quadratic $`K`$. If $`L/F`$ is such a finite Galois extension, $`m=2^a`$, and $`R\in E(L)`$ has invariant image in $`E(L)/mE(L)`$, the formula

```math
b_R(\sigma)=2^e\bigl((\sigma-1)Q-B_{\bar\sigma}\bigr),
 \quad mQ=R,\quad mB_\delta=(\delta-1)R,\quad B_1=0
```

defines a canonical class $`d_m(R)\in H^1(F,E[m])`$. It restricts to the Kummer class of $`2^eR`$, is additive in the invariant Kummer class, and commutes with embeddings and conductor corestrictions.

*Proof.* By open image choose $`g`$ acting on $`T`$ by $`u\mathrm{Id}`$, $`u\in1+4\mathbb{Z}_2`$, $`u\ne1`$. For complex conjugation $`\tau`$, $`g^2\tau g^2\tau^{-1}`$ fixes every ring-class field of $`K`$: $`g^2`$ belongs to $`G_K`$ and $`\tau`$ inverts the abelian ring-class action. Its Tate action is $`u^4`$. Thus $`e=v_2(u^4-1)`$ works uniformly.

The expression in parentheses belongs to $`E[m]`$. Moreover $`db_R=-2^e dB=0`$, since $`dB\in E(L)[m]`$. Changing $`B`$ has no effect, changing $`Q`$ gives a coboundary, and replacing $`R`$ by $`R+mW`$ is absorbed by $`Q+W`$ and $`B_\delta+(\delta-1)W`$. These observations also prove additivity and naturality. For a conductor corestriction, write $`\sigma r=r'h`$ for coset representatives and set

```math
Q_{\mathrm{norm}}=\sum_r rQ,\qquad
 B_{\mathrm{norm}}(\sigma)=\sum_r r'B_{\bar h}.
```

The coset permutation gives the required multiples for the norm point, and the corestricted cocycle is exactly the displayed direct descent formula. Choices in a smaller field differ by torsion in the larger ring-class field and are killed by the same $`2^e`$.

**Lemma D.8 (Finite derivative identities).** One fixed integer $`L\ne0`$ gives, for every finite set $`I`$ of derivative slots, classes $`z_I`$ in the corresponding Selmer complex with singular conditions at $`I`$. At a new derivative prime $`ℓ`$ their coordinates satisfy

```math
f(z_{I\cup\{ℓ\}})=0,\qquad
 s(z_{I\cup\{ℓ\}})=Jf(z_I).
```

The same $`L`$ works for every active and derivative support, and the identities survive integral weighted transfer and coefficient reduction.

*Proof.* A fixed multiple of the parametrization kills its cusp differences by Manin–Manin (1972) and Drinfeld (1973). For $`c=\vert h\vert r`$ and inert good $`ℓ\nmid c`$, the CM point relations are

```math
\mathrm{Tr}_{H_{cℓ}/H_c}y_{cℓ}=a_ℓ y_c,
 \qquad \widetilde y_{cℓ}
                  =F_ℓ\widetilde y_c.
```

These are the norm and reduction relations from the CM Hecke correspondence Kolyvagin (1990). For squarefree $`n=\prod_{ℓ\in I}ℓ`$, the relative ring-class group is the product of cyclic groups of orders $`ℓ+1`$. Put

```math
D_ℓ=\sum_{j=1}^{ℓ}j\sigma_ℓ^j,\qquad
 D_I=\prod_{ℓ\in I}D_ℓ.
```

The exact identity $`(\sigma_ℓ-1)D_ℓ=(ℓ+1)-\mathrm{Tr}`$ makes the Kummer class of $`D_Iy_{cn}`$ invariant modulo $`m`$ when $`m`$ divides $`a_ℓ`$ and $`ℓ+1`$ for every $`ℓ\in I`$. Apply Lemma D.7 once to this full extension.

Fix $`ℓ\in I`$ and write $`X=D_{I\setminus\{ℓ\}}y_{cn/ℓ}`$, $`Y=D_{I\setminus\{ℓ\}}y_{cn}`$. Choose in the direct descent

```math
B_{\sigma_ℓ}=[(ℓ+1)/m]Y-[a_ℓ/m]X.
```

The prime $`(ℓ)`$ is principal in $`K`$ and splits in the lower ring-class field; hence $`F_ℓ^2\widetilde X=\widetilde X`$. For $`mQ_X=X`$, the lower finite coordinate and upper singular coordinate are

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

Therefore $`s=(F_ℓ-a_ℓ)f=Jf`$ at the retained precision. For the upper finite coordinate,

```math
\widetilde{D_ℓ Y}
       =[ℓ(ℓ+1)/2]F_ℓ\widetilde X.
```

Require $`v_2(ℓ+1)\geq a+1`$. Its displayed division by $`m`$ is an $`\mathbb{F}_{ℓ^2}`$‑point. Lift it to the unramified lower local field; multiplication by $`m`$ is an automorphism on the formal group at odd $`ℓ`$. An $`m`$‑division point of $`D_ℓ Y`$ thus exists in the upper local field with that reduction. A Frobenius-square lift fixing this field has zero Kummer value, and its $`B_1`$ is zero. This proves the upper finite identity. The calculation applies at each retained derivative prime, preserving the earlier singular conditions.

At a place over $`2N`$ the descent extensions are unramified. The first cohomology of the identity-component point group under an unramified extension vanishes by Lang’s theorem, smooth lifting, and the formal-group trace calculation. The remaining obstruction is killed by the exponent of the geometric component group. The finitely many permitted local quadratic types have a common such multiple. Include it, the cusp multiple, and $`2^e`$ in $`L`$.

Finally use the actual weighted coset sum. If $`F/K`$ is Galois and $`gr=r'h(g,r)`$, a cocycle $`b`$ on $`G_F`$ gives

```math
\mathrm{Cor}_\theta(b)(g)
       =\sum_r r'\cdot b(h(g,r)),
```

where the action includes the scalar and quadratic character $`\theta`$. The crossed identity follows termwise; changing representatives gives a coboundary. There is no division by the degree. At derivative primes the lower ring-class character is locally trivial because $`(ℓ)`$ is principal. Transporting the place and Frobenius in each summand preserves both displayed identities with the same scalar weight. The calculation in Lemma D.7 also proves compatibility with split conductor norms. Local lifts and degree-zero boundary witnesses are then included in the actual Selmer cone. Coefficient change uses the derived Kummer complexes, retaining their degree-zero torsion invariants.

### D.4. Limits with retained evaluations

At each finite stage, complete descent, all weighted coset sums, and their local lifts before applying Lemma D.4. Only the target complexes over $`K`$ enter the limit; no bound on the degrees of the ring-class source fields is needed. For fixed $`K`$, active support, derivative slots, and finite group $`G`$, their residual dimensions are bounded. Indeed, the residual representation is the trivial $`E[2]`$, and Kummer theory bounds global $`H^1`$ by the ranks of the relevant $`S`$‑unit groups and the fixed $`2`$‑class group of $`K`$. There are only boundedly many moving primes. Global duality and local Euler characteristics bound the other dimensions. The same argument applies over $`A_i[G]`$, whose residue field is $`\mathbb{F}_2`$.

Fix one nonprincipal ultrafilter for this inner construction. After fixing the finitely many graded ranks on a large set, every matrix has a unique coefficientwise limit modulo each $`(2^j,t^j)`$; these compatible limits define matrices over $`\Lambda`$ or $`\Lambda[G]`$. All specified maps, cycles, boundary witnesses, homotopies, inverses, and duality identities survive, since each is a finite polynomial matrix identity. When adjoining another derivative slot, extend the same finite-stage diagrams and retain their old contractions and this same ultrafilter. Passing to a slower cofinal precision preserves all old limits.

**Lemma D.9 (Evaluation on arbitrary sequences).** Let $`C`$ be one of the resulting global complexes or Selmer complexes whose local maps are isomorphisms on $`H^0`$ and injections on $`H^1`$. Put $`\Sigma=\prod_iG_K`$ and $`\Gamma=\Sigma\rtimes\langle\tau\rangle`$, with simultaneous complex conjugation. For every field $`L`$ receiving a map from $`\Lambda`$, retained evaluation gives injections

```math
H^1(C\otimes_\Lambda L)\hookrightarrow H^1_{\mathrm{abs}}(\Sigma,L^2),
 \qquad H^0(C\otimes_\Lambda L)\hookrightarrow(L^2)^\Sigma.
```

The analogous assertion holds for the rank-four representation induced to $`\Gamma`$. The degree-two crossed-cocycle identities are retained for all sequences, not only a finite detecting list.

*Proof.* Compose the maps from finite models to original cochains with evaluation in degrees zero, one, and two. For sequences $`g=(g_i)`$ and $`h=(h_i)`$, their coefficientwise limits satisfy

```math
e_g^1d=(\rho(g)-1)e^0,\qquad
 e_{g,h}^2d=\rho(g)e_h^1-e_{gh}^1+e_g^1.
```

One fixed ultrafilter defines these limits for every sequence. The second identity makes the evaluation of a cycle an actual abstract crossed homomorphism; the first sends boundaries to coboundaries.

For injectivity, choose representatives for residual $`H^1`$ and evaluate pairs $`(c,m)`$ by $`b_c(g)-(\rho(g)-1)m`$. Their common kernel consists of $`(0,m)`$ with $`m`$ invariant. A list of at most $`\dim H^1+\mathrm{rank}M`$ elements already detects this kernel. Evaluation on it gives a map to the two-term complex

```math
V_i=[\,A_i^d\xrightarrow{((\rho_i(g_j)-1))_j}
                         (A_i^d)^r\,],\qquad d=2\text{ or }4.
```

The Selmer-cone sequence supplies the asserted residual injection into global cohomology, because all its local $`H^0`$ maps are isomorphisms. The evaluation cone has no residual cohomology in degrees at most zero. Cancel its unit disks and retain the contraction. Its finite free model then starts in degree one and continues to do so after every field base change. The long exact sequence proves injection on $`H^1`$ and the asserted statement on $`H^0`$. A crossed cocycle that is a coboundary on every sequence is in particular a coboundary on this detecting list.

**Lemma D.10 (Exact kernels and finite realization).** Let $`H\subset\Sigma`$ consist of sequences whose entries act trivially on the full Tate module, all ring-class fields of $`K`$, and the quadratic characters in use. Restriction of the classes in Lemma D.9 to $`H`$ is injective at every characteristic-zero test and at the residual $`\Omega`$‑test. An actual element $`u\in H`$ can be realized at successively increasing finite precision by derivative Frobenii $`\tau u`$, without changing any previous finite diagram. Their finite localization is evaluation on $`(\tau u)^2`$.

*Proof.* Use $`z=g^2\tau g^2\tau^{-1}`$ from Lemma D.7. It is central modulo $`H`$ and acts on coefficients by the fixed scalar $`u_0^4\ne1`$. For a cocycle on $`\Sigma/H`$, comparison of $`b(zg)`$ and $`b(gz)`$ gives

```math
(u_0^4-1)b(g)=(g-1)b(z).
```

Thus this cocycle is a coboundary in characteristic zero; inflation–restriction gives injectivity on $`H`$. The valuation of $`u_0^4-1`$ is fixed as $`K`$ varies. At the residual test replace $`z`$ by moving inertia, whose Tate action is trivial and scalar action is $`1+t`$. It is central modulo the exact kernel, and $`t`$ is a unit in $`\Omega`$.

At one Artin stage, every coordinate cochain in the finite model is locally constant through a finite quotient. Enlarge that quotient by the finite ring-class data, all previous data, and a sufficiently deep Tate quotient. Chebotarev realizes the conjugacy class of the actual element $`\tau u`$, with a place realizing its chosen representative. It gives an inert prime outside the old support. Exact Tate triviality of $`u`$ permits arbitrary extra precision in $`a_ℓ\equiv0`$ and $`ℓ\equiv-1`$; exact ring-class triviality makes its square trivial on the lower ring-class fields. These are finite conditions at every stage. For a crossed cocycle in the induced representation,

```math
b((\tau u)^2)=(1+\tau)b(u),
```

since $`u`$ acts trivially and $`\tau^2=1`$. Projection to either induced summand identifies this image with the rank-two finite plane.

**Lemma D.11 (Uniform functional and residual size).** After the inner limit, the class $`z_I`$ has a closed degree-two functional $`\lambda_I`$ obtained from the same integral duality diagram. In finite free models over $`\mathcal{O}`$, both are integral up to one fixed power of $`2`$, independently of the active support and the number of switches. The same assertion holds over $`\mathcal{O}[G]`$ for a whole fixed binary family. After any fixed number of switches, minimal $`\mathcal{O}`$‑models have size bounded in terms of $`E`$, a bound on $`\omega(\vert k\vert )`$, and that number of switches.

*Proof.* At an active prime, residual Frobenius is the nonconstant scalar $`z=(1+t)^a`$, with $`a`$ odd. The determinant of $`z-1`$ on the trivial rank-two residual Tate module is nonzero in $`\Omega`$. At $`r`$, inertia minus one is $`t`$, also a unit. The full local complexes are therefore acyclic over $`\mathcal{O}`$ and have contractions using only unit pivots. Over $`\mathcal{O}[G]`$ the same conclusion follows after reduction modulo $`(2,I_G)`$, whose residue field is $`\Omega`$.

The actual comparison $`q:C_I^\perp\to C_I`$ has cone equal to the sum of these full local complexes; at derivative places the chosen planes are already exactly self-orthogonal. Thus $`q`$ has an integral homotopy inverse. Conjugation transports $`z_I`$ linearly to the separate inverse-character complex. Lift it through that comparison and apply the integral Poitou–Tate morphism

```math
C_I^{\perp,\vee}\longrightarrow
                 R\mathrm{Hom}(C_I,\mathcal{O})[-3].
```

Its degree-one image is a closed degree-two functional. Every map used is integral, and any fixed normalization at the old support requires only one fixed exponent. Contracting arbitrarily many acyclic summands introduces no inverse of $`2`$. Later switches and minimal-model contractions likewise use integral maps. This proves the asserted uniformity, also over the group ring. Inverses of the same derived isomorphism agree; representatives at other localizations therefore define this same generic functional.

For the size bound first work with the genuine finite cochains over $`\overline A_i=\mathbb{F}_2[t]/(t^i)`$. The quadratic character $`\chi_h`$ disappears modulo $`2`$. Thus the reduced representation descends to the smaller permitted support containing only $`2N`$, the auxiliary prime, and the fixed derivative slots. Construct its smaller-support Selmer complex and its actual inflation and localization triangle to the original reduced complex. The quotient is the sum of the active singular local complexes.

Modulo $`t`$, the smaller-support representation is the trivial rank-two $`E[2]`$. The maximal pro‑$`2`$ Galois group over $`\mathbb{Q}`$ allowing also the ramification of $`K`$ has a generator bound from Kummer theory, depending only on the number of these primes. Its subgroup over $`K`$ has index at most two and satisfies Schreier’s bound. Every finite $`2`$‑extension over $`K`$ with this support lies in the same maximal pro‑$`2`$ extension: adjoining its quadratic conjugate still gives a $`2`$‑extension over $`\mathbb{Q}`$. This bounds the continuous residual $`H^1`$ of these genuine finite cochains, and duality bounds the other residual dimensions. Lemma D.4 therefore gives smaller-support free models over $`\overline A_i`$ of uniformly bounded ranks. Retain these models and their localization triangle in the same inner limit. Only then invert $`t`$. The active singular blocks become acyclic by the nonconstant residual Frobenius computation above, so the original $`\Omega`$‑complex is equivalent to this bounded smaller-support model. Moving inertia excludes invariants and duality excludes degree three. Minimal $`\mathcal{O}`$‑models therefore have two equal bounded terms in degrees one and two. This bound is proved on continuous finite arithmetic cochains; no generator bound on abstract sequence-group cohomology is used.

**Lemma D.12 (Outer characteristic-zero evaluation).** For any family of these bounded $`\mathcal{O}_j`$‑models, keep the integral evaluation and duality diagrams and a nonprincipal ultrafilter $`\mathcal{U}`$. The ring

```math
\mathcal{O}_\infty=
 \left(\prod_{\mathcal{U}}\mathcal{O}_j\right)\Big/
 \{(a_j):v_2(a_j)\to_{\mathcal{U}}\infty\}
```

is a DVR with uniformizer $`2`$ and characteristic-zero fraction field. The outer $`H^1`$ injects into crossed-homomorphism classes on the product of the inner sequence groups and remains injective on the product of their exact kernels. All degree-two evaluation identities and every retained finite integral diagram survive.

*Proof.* A nonzero element has bounded valuations on a large set. A finite partition then makes that valuation one integer $`n`$, so the element is $`2^n`$ times a unit. Products add these finite valuations, and every nonzero ideal has a least valuation. This proves the DVR assertion. No fixed $`2^n`$ vanishes, so its fraction field has characteristic zero.

Evaluation matrices remain integral through the contractions of Lemma D.11. Hence the identities of Lemma D.9 pass to this quotient. In particular, an outer cycle represented by $`x_j`$ with $`v_2(d_jx_j)\to\infty`$ satisfies the crossed identity: the integral degree-two evaluation of $`d_jx_j`$ also tends to zero. No exact inner lift of this new cycle is required. Choose bounded detecting lists over the residue fields and retain their cones contracted to degrees at least one. These contractions use unit pivots and survive the outer quotient, proving injectivity as before. The fixed scalar $`u_0^4-1`$ from Lemma D.10 remains nonzero, giving restriction injectivity on the product of exact kernels.

To express a localization test in the original finite models, first fix its $`2`$‑adic precision, below the vanishing order of any approximate coboundaries. Each of its finitely many $`\mathcal{O}`$‑coefficients then has a Laurent expansion with finite negative support. Multiply the test by a common power of $`t`$ and retain the finitely many coefficients needed to detect its nonzero value. These are evaluations of the original Artin cochains at sufficiently large stages, and hence factor through a finite Galois quotient. Apply Chebotarev to that quotient together with the old data and the additional Tate precision. Multiplication by $`t`$ affects only this finite realization test; it is a unit after localization and does not alter any arithmetic class or central normalization. Let the retained precision grow cofinally, preserving the inner and outer ultrafilters and all old diagrams and contractions. This retains both the new evaluations and the earlier arithmetic identities.

---

[← Appendix C](appendix-c.md) · [Main article](README.md) · [Appendix D, sections D.5–D.8 →](appendix-d-continued.md)
