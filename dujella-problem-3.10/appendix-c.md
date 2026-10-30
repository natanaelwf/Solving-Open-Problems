[← Main article and Appendices A–B](README.md) · [Main article](README.md) · [Appendix D, sections D.1–D.4 →](appendix-d.md)

---

## Appendix C. Cyclotomic comparison for the auxiliary curve

Throughout this section, $`E=F`$ is the auxiliary curve of Lemma A.1. In particular, $`E`$ is non-CM, $`E[2]\subset E(\mathbb{Q})`$, $`E`$ has potentially good reduction at $`2`$, and every odd prime of bad reduction is multiplicative. Write $`N=N_E`$, $`T=T_2E`$, and $`V=T\otimes_{\mathbb{Z}_2}\mathbb{Q}_2`$. The positive determinant construction and its binary interpolation are adapted from OpenAI (2026, section on cyclotomic interpolation). We give the specialized construction, including its coefficient maps and integral central comparison.

An allowed discriminant $`h`$ is an odd fundamental discriminant, with $`h\in\mathbb{Q}_q^{\times 2}`$ for every $`q\mid 2N`$; the trivial character $`h=1`$ is included. Thus $`(h,2N)=1`$ and $`h\equiv1\pmod8`$. All discriminants in a binary family have the same sign. Fix nonzero periods $`\Omega_E^+`$ and $`\Omega_E^-`$ in the two rational Betti period lines, and a compatible embedding of algebraic numbers into $`\overline{\mathbb{Q}}_2`$. Put

```math
L_*(h)=\frac{\sqrt{\vert h\vert }\,L(E^{(h)},1)}{\Omega_E^{\mathrm{sgn}(h)}}.
```

Changing either fixed period changes the valuations below by a fixed constant. The value is algebraic; a purely imaginary choice of the minus period only introduces a root of unity into comparisons with a real period convention. If $`s_2(E^{(h)})=0`$, then both the Mordell–Weil rank and the divisible corank of its $`2`$‑primary Shafarevich–Tate group vanish. Consequently that group is finite, and we set

```math
s(h)=\mathrm{length}_{\mathbb{Z}_2}
       \mathrm{Sha}(E^{(h)}/\mathbb{Q})[2^\infty].
```

When also $`L(E^{(h)},1)\ne0`$, define

```math
D(h)=v_2(L_*(h))-2\omega(\vert h\vert )-s(h).
```

**Theorem C.1 (Cyclotomic lower bound).** There is a constant $`C_E`$ such that every allowed $`h`$ with $`L(E^{(h)},1)\ne0`$ satisfies

```math
v_2(L_*(h))\ge 2\omega(\vert h\vert )+s(h)-C_E.
```

The constant is independent of the number and sizes of the primes of $`h`$.

**Theorem C.2 (Cyclotomic transfer to the missing vertex).**

Let $`h_0`$ be allowed and satisfy $`s_2(E^{(h_0)})=0`$. Suppose that for arbitrarily large $`b`$ there are a finite set $`Q`$ of primes not dividing $`2Nh_0`$ and linear forms $`\lambda_q:\mathbb{F}_2^b\to\mathbb{F}_2`$ such that

```math
h_x=h_0\prod_{q\in Q}(q^*)^{\lambda_q(x)},\qquad
 q^*=(-1)^{(q-1)/2}q,
```

are allowed and have the same sign. Suppose that a constant $`B`$, independent of the family, satisfies

```math
L(E^{(h_x)},1)\ne0,\qquad D(h_x)\le B\qquad(x\ne0).
```

Then $`L(E^{(h_0)},1)\ne0`$ and $`D(h_0)\le B+C_E`$. The constant $`C_E`$ is independent of $`h_0`$, $`Q`$, and $`b`$.

### C.1. Positive cochains and derived coefficient change

Let $`S`$ be finite and contain $`2`$, the real place, and the ramification of the coefficients. For a finite $`2`$‑primary $`G_{\mathbb{Q},S}`$‑module $`M`$, define

```math
\mathcal{F}_S(M)=
 \mathrm{Cone}\bigl(
 C^\bullet(G_{\mathbb{Q},S},M)\longrightarrow
 C^\bullet(\mathrm{Gal}(\mathbb{C}/\mathbb{R}),M)
 \bigr)[-1].
```

The real cochains in this definition are ordinary cochains in nonnegative degrees. Complete real Tate cochains will instead occur in Poitou–Tate duality.

**Lemma C.3.** The cohomology of $`\mathcal{F}_S(M)`$ is finite and is concentrated in degrees $`1`$ and $`2`$. The same degree bounds hold for finite-type compact coefficient modules by passage to inverse limits.

*Proof.* The map on degree-zero cohomology is injective. We also need surjectivity of global restriction in degree two. If $`2^aM=0`$, put $`M^D=\mathrm{Hom}(M,\mu_{2^a})`$. Restriction

```math
H^0(G_{\mathbb{Q},S},M^D)\longrightarrow H^0(\mathbb{Q}_2,M^D)
```

is injective. Its dual, under local Tate duality, is a surjection

```math
H^2(\mathbb{Q}_2,M)\longrightarrow
 H^0(G_{\mathbb{Q},S},M^D)^\vee.
```

Given a prescribed real degree-two class, choose a class at $`2`$ that cancels its obstruction in this last group and set the other finite local classes to zero. The finite Poitou–Tate sequence then supplies a global class with the prescribed real restriction. In every degree strictly greater than two, restriction from global cohomology to real cohomology is an isomorphism. These are precisely the real-place clauses of Milne (2006, I, Theorem 4.10) and Nekovář (2006, 5.7.1.4–5.7.1.7). The cone sequence proves the assertion for $`M`$.

For a compact coefficient module, take its finite coefficient quotients. Continuous cochains are their inverse limit. The cohomology groups at each finite quotient are finite, so their inverse systems satisfy the Mittag–Leffler condition. The inverse-limit cohomology sequence therefore preserves the degree bounds.

**Proposition C.4.** Let $`R`$ be a complete Noetherian local $`\mathbb{Z}_2`$‑algebra with finite residue field, and let $`\mathcal{T}`$ be finite free over $`R`$ with continuous $`G_{\mathbb{Q},S}`$‑action. Then $`\mathcal{F}_S(\mathcal{T})`$ is represented by a finite free complex in degrees $`1`$ and $`2`$. For a coefficient quotient $`R\to B`$ there is a natural isomorphism

```math
\mathcal{F}_S(\mathcal{T})\otimes_R^{\mathbf{L}}B
 \simeq \mathcal{F}_S(\mathcal{T}\otimes_R B).
```

The maps commute with restriction and with Shapiro’s maps. At a nonarchimedean place, or over a totally imaginary number field, the ordinary complex has perfect amplitude $`[0,2]`$ under the same finite-free coefficient hypotheses. The compact-support cone over a totally imaginary number field has perfect amplitude $`[0,3]`$.

*Proof.* Continuous cochains on admissible modules are exact on short exact sequences, commute with filtered direct limits, and satisfy the projection formula for complexes of flat modules Nekovář (2006, 3.4.2–3.4.4). The same statements hold for the positive cone with its actual restriction map. Global and real Galois groups satisfy the finite-cohomology condition Nekovář (2006, 5.7.1.1); hence the complete-local finiteness argument Nekovář (2006, 4.2.3–4.2.5) gives finite-type cohomology. It is bounded by Lemma C.3.

For completeness, derived coefficient change does not require $`B`$ to be flat. Take a resolution of a finite-type $`R`$‑module $`B`$ by finite free modules and let $`P_n`$ be its brutal truncation in degrees $`[-n,0]`$. If $`K_n`$ is the leftmost resolution syzygy, there is a triangle

```math
K_n[n]\longrightarrow P_n\longrightarrow B\longrightarrow K_n[n+1].
```

The projection formula holds for $`P_n`$ on the level of cochains. Applying the positive functor to the last term gives cohomology only in degrees $`[-n,1-n]`$, by Lemma C.3. It cannot change any fixed cohomological degree for sufficiently large $`n`$. The same truncation argument on the tensor side proves the derived projection formula and gives Tor amplitude $`[1,2]`$. Filtered direct limits extend the Tor bound to arbitrary $`R`$‑modules. The perfectness criterion Nekovář (2006, 4.2.8 and the proof of 4.2.9) now applies. A minimal finite free model over $`R`$ has zero differential after reduction to the residue field. Its residual cohomology is concentrated in degrees $`1,2`$, so its terms outside those degrees vanish.

All comparisons came from cochain maps. In particular, quotienting a cyclotomic coefficient module by $`\gamma^{2^n}-1`$ uses its two-term Koszul resolution and the same coefficient exact sequence on the global and ordinary real cochains. Shapiro’s maps commute with these restriction maps; see also Nekovář (2006, 8.4.8.1).

For a nonarchimedean local field of characteristic zero and for a totally imaginary number field, the relevant $`2`$‑cohomological dimension is two. The same finite-Tor argument applies to ordinary cochains, or directly Nekovář (2006, 4.2.9 and 5.1.1–5.1.2). Forming the actual compact-support cone adds at most one degree.

### C.2. Residual concentration at the height-one prime

Let $`\Gamma=\mathrm{Gal}(\mathbb{Q}_\infty/\mathbb{Q})`$ be the real cyclotomic $`\mathbb{Z}_2`$‑group, choose $`\gamma\in\Gamma`$, and write

```math
\Lambda=\mathbb{Z}_2[[\Gamma]]=\mathbb{Z}_2[[t]],\qquad
 \gamma=1+t,\qquad
 \mathcal{O}=\widehat{\Lambda_{(2)}},\qquad
 \Omega=\mathbb{F}_2((t)).
```

For a binary family, put $`G=(\mathbb{Z}/2\mathbb{Z})^b`$ and $`R=\Lambda[G]`$. Let $`\psi:G_{\mathbb{Q}}\to G`$ be the universal quadratic character, so its character at $`x`$ is $`\chi_{h_x/h_0}`$. The action on $`\mathbf{T}=T\otimes_{\mathbb{Z}_2}R`$ is

```math
\rho_T\chi_{h_0}\psi\kappa_\Gamma^{-1},
```

where $`\kappa_\Gamma:G_{\mathbb{Q}}\to\Gamma`$ is the group-valued cyclotomic quotient. Put

```math
\mathcal{C}_S^+=\mathcal{F}_S(\mathbf{T}),
```

where $`S`$ contains $`2N`$ and the prime factors of all the $`h_x`$. Since the signs are fixed, both $`\psi`$ and $`\kappa_\Gamma`$ are trivial at the real place. In the zeta-class construction we take $`S`$ to be exactly the real place together with the primes dividing $`2N`$ or one of the $`h_x`$.

**Lemma C.5.** Every layer $`K_n`$ of degree $`2^n`$ in the real cyclotomic $`\mathbb{Z}_2`$‑extension has odd ordinary class number.

*Proof.* The assertion holds for $`K_0=\mathbb{Q}`$. Suppose it holds for $`K_n`$. If the $`2`$‑primary part $`P`$ of the ordinary class group of $`K_{n+1}`$ were nonzero, the involution of $`K_{n+1}/K_n`$ would act on the nonzero space $`\mathrm{Hom}(P,\mathbb{F}_2)`$ with a nonzero fixed vector: in characteristic two, the square of its difference from the identity is zero. Class field theory would then give an everywhere-unramified quadratic extension $`L/K_{n+1}`$, invariant under that involution. Here “everywhere-unramified” includes splitting at real places, as appropriate to the ordinary Hilbert class field. Thus $`L/K_n`$ is Galois of degree four and its Galois group is abelian.

Only the unique prime above $`2`$ can ramify in $`L/K_n`$, and its inertia group has order two: the ramification index in $`K_{n+1}/K_n`$ is two and $`L/K_{n+1}`$ is unramified. The fixed field of this inertia group is consequently an everywhere-unramified quadratic extension of $`K_n`$. This contradicts the odd class number of $`K_n`$.

**Lemma C.6.** There is an isomorphism

```math
\mathcal{C}_S^+\otimes_R^{\mathbf{L}}\mathcal{O}[G]
       \simeq \mathcal{O}[G]^2[-1].
```

It introduces no denominator depending on $`S`$ or on $`G`$.

*Proof.* The ring $`\mathcal{O}[G]`$ is local with residue field $`\Omega`$; its residue map sends $`2`$ to zero and every element of $`G`$ to one. Every quadratic character therefore disappears. Full rational $`2`$‑torsion makes $`T/2T`$ a direct sum of two trivial modules. It suffices to compute one trivial summand.

Let $`d_n=[K_n:\mathbb{Q}]=2^n`$ and let $`s_n`$ be the number of finite places of $`K_n`$ above $`S`$. The numbers $`s_n`$ are bounded in $`n`$. The prime $`2`$ is totally ramified, and the Frobenius of each fixed odd prime has nonzero image in $`\Gamma`$: an odd positive rational prime cannot equal $`1`$ or $`-1`$ in $`\mathbb{Z}_2^\times`$. By Lemma C.5, the $`S`$‑class group has no $`2`$‑primary part.

The unit signature map is surjective. For $`n\ge1`$, take a primitive $`2^{n+2}`$th root $`\zeta`$ and put $`\varepsilon=1+\zeta+\zeta^{-1}`$. The minimal polynomials of $`\zeta+\zeta^{-1}`$ satisfy

```math
f_1(X)=X^2-2,\qquad f_{n+1}(X)=f_n(X^2-2),\qquad f_n(-1)=-1.
```

Thus $`\varepsilon`$ is a unit of norm $`-1`$. Its signature has odd augmentation in the regular $`\mathbb{F}_2[\mathrm{Gal}(K_n/\mathbb{Q})]`$‑module. The group algebra of a cyclic $`2`$‑group over $`\mathbb{F}_2`$ is local, so that signature is a unit and its conjugates span every signature. For $`n=0`$, use $`-1`$.

Kummer theory and the Brauer invariant sequence now give

```math
\dim_{\mathbb{F}_2}H^1(G_{K_n,S},\mu_2)=d_n+s_n.
```

Restriction in degree one to the $`d_n`$ real places is surjective. Degree-zero restriction has cokernel of dimension $`d_n-1`$. In degree two, restriction to the real places is also surjective; its kernel has dimension $`s_n-1`$, because the finite and real Brauer invariants have one sum relation and a finite place above $`2`$ is present. The positive complex therefore has dimensions

```math
d_n+s_n-1\quad\text{in degree }1,\qquad
 s_n-1\quad\text{in degree }2,
```

and zero cohomology elsewhere.

By Proposition C.4, reduction to $`K_n`$ is derived reduction modulo $`t^{2^n}`$ of a perfect complex over $`\mathbb{F}_2[[t]]`$. For such a complex, the universal-coefficient sequence and the structure theorem over $`\mathbb{F}_2[[t]]`$ show that its degree‑$`i`$ dimension modulo $`t^{2^n}`$ is $`2^n\mathrm{rank}H^i+O(1)`$. Its torsion modules contribute only a bounded term. After inverting $`t`$, the trivial summand therefore has dimension one in degree one and is zero otherwise. The two trivial summands have dimension two in degree one. A minimal finite free model over $`\mathcal{O}[G]`$ has zero residual differentials. This residual concentration forces exactly one term, free of rank two in degree one.

The fixed integral invariant line of $`T\chi_{h_0}`$ at the real place has a primitive generator. Its connecting image defines $`a\in H^1(\mathcal{C}_S^+)`$. Global rational invariants vanish: the non-CM image on the kernel of the cyclotomic character and the finitely many quadratic characters contains an open subgroup of $`\mathrm{SL}_2(\mathbb{Z}_2)`$ and fixes no nonzero vector. Thus $`a`$ spans the real-place summand. Its normalization depends only on $`E`$ and the fixed real sign. Since $`H^1(\mathbb{R},\mathbf{T})`$ is killed by $`2`$, twice an ordinary global class lifts to positive cohomology. Two lifts have the same wedge with $`a`$.

### C.3. A fixed-form integral zeta class

Let $`f=f_E`$ be the fixed weight-two newform. We use Kato’s integral classes at this form, followed by the fixed comparison of its rational representation with $`V`$. Kato (2004, 8.9–8.12) gives an integral trace to

```math
\mathbb{Z}_2[\mathrm{Gal}(\mathbb{Q}(\mu_m)/\mathbb{Q})]
 \otimes_{\mathbb{Z}_2}V_{2,\mathbb{Z}_2}(Y_1(N))(1),
```

then an integral projection to the lattice of $`f`$. One fixed power $`2^{c_E}`$ sends that lattice into $`T`$. Choose fixed symbols in $`\mathrm{SL}_2(\mathbb{Z})`$ with nonzero projections in both required period lines; their existence follows from Kato (2004, 13.6 and 13.9). The two sign choices cost only a fixed lattice constant.

Let $`m`$ be odd and divisible by all the tame conductors in the family. Write $`\Gamma_n=\Gamma/\Gamma^{2^n}`$ and use the field $`\mathbb{Q}(\mu_{m2^{n+2}})`$, so that its real cyclotomic quotient is exactly $`\Gamma_n`$. Shapiro’s isomorphism and the coefficient map

```math
\begin{aligned}
 \mathbb{Z}_2[\mathrm{Gal}(\mathbb{Q}(\mu_{m2^{n+2}})/\mathbb{Q})]
   &\longrightarrow \mathbb{Z}_2[\Gamma_n\times G],\\
 [\sigma]&\longmapsto
 \chi_{h_0}(\sigma)[\sigma\vert _{\Gamma_n}][\psi(\sigma)]
 \end{aligned}
```

push the actual class into the required coefficient module. We use the inverse group actions on both sides when identifying this module with $`\mathbf{T}`$. This is an integral homomorphism of coefficient modules, not division by an idempotent. In particular it introduces no factor $`\vert G\vert ^{-1}`$ and uses no surjectivity assertion for cohomological specialization. Since $`2\in S`$, Kato’s norm relation has no new Euler factor as $`n`$ increases. The inverse limit is an integral smoothed class, up to $`2^{c_E}`$.

**Lemma C.7.** The weight-two smoothing factors can be removed over $`\mathcal{O}[G]`$ without any additional $`2`$‑denominator. Their central values have bounded, fixed valuations as the tame support varies.

*Proof.* For $`k=2`$ and $`r=r'=1`$, the factors are $`(c^2-c\sigma_c)(d^2-d\sigma_d)`$ Kato (2004, Theorem 6.6). Fix $`e\ge\max(2,v_2(N))`$ and choose $`c,d\gt 1`$ with

```math
c,d\equiv1\pmod{3N_{\mathrm{odd}}m},\qquad
 c,d\equiv1+2^e\pmod{2^{e+1}}.
```

They satisfy the required coprimality conditions and act trivially on all tame characters. Taking $`5`$ as a generator of $`1+4\mathbb{Z}_2`$, the exponent $`\kappa(c)=\log(c)/\log(5)`$ has valuation $`e-2`$. Thus the reduction of $`c^2-c\sigma_c`$ to $`\Omega`$ is

```math
1-(1+t)^{\kappa(c)}\ne0.
```

Indeed its first nonzero term has degree $`2^{e-2}`$. It is consequently a unit in the local ring $`\mathcal{O}[G]`$. At $`t=0`$ its value is $`c(c-1)`$, of valuation $`e`$. The same argument applies to $`d`$ and to inverse group actions.

Denote the unsmoothed ordinary class by $`z_S^{(0)}`$. Before the comparison below, its character components are regarded as elements of $`\mathrm{Frac}(A)\otimes_A H^1(C_{S,h})`$, where $`A=\Lambda[1/2]`$. Their smoothing denominators are nonzero power series with nonzero central values. The following normalization makes the roles of Betti and de Rham vectors explicit. Choose a rational Betti generator $`b^\epsilon`$ in the required sign line and a de Rham generator $`\omega_f`$ such that

```math
\mathrm{per}_f(\omega_f)^\epsilon
     =\Omega_f^\epsilon b^\epsilon,\qquad
 \delta(f,1,\xi)^\epsilon=d_\xi^\epsilon b^\epsilon,
 \qquad d_\xi^\epsilon\in\mathbb{Q}^\times.
```

The periods $`\Omega_f^\epsilon`$ and $`\Omega_E^\epsilon`$ differ by fixed nonzero rational comparison factors. Kato’s unnormalized character-sum formula, followed by explicit reciprocity, Kato (2004, Theorems 6.6 and 9.7), therefore has de Rham coefficient $`d_\xi^\epsilon L_S(E^{(h)},1)/\Omega_f^\epsilon`$ before identifying the quadratic twisting line.

For a primitive quadratic character of odd conductor $`\vert h\vert `$, choose its Gauss sum $`\tau_h`$ with $`\tau_h^2=h`$. The character eigenline in $`\mathbb{Q}(\mu_{\vert h\vert })`$ is generated by $`\tau_h`$, which is a $`2`$‑adic unit. Since $`h`$ is a square in $`\mathbb{Q}_2`$, its image under the chosen embedding belongs to $`\mathbb{Q}_2^\times`$. The de Rham basis of the twisted representation can thus be taken to $`\tau_h\omega_f`$. Dividing the preceding coefficient by $`\tau_h`$ gives

```math
\frac{d_\xi^\epsilon L_S(E^{(h)},1)}
      {\tau_h\Omega_f^\epsilon}.
```

The ratio between $`1/\tau_h`$ and $`\sqrt{\vert h\vert }`$ is a root of unity times $`1/h`$, and has valuation zero. Comparing with a minimal differential at $`2`$ contributes a bounded index, because all the allowed $`h`$ are local squares there.

There is no growing trace factor in this computation. With the left-coset Shapiro convention, restriction of the pushed class is the unnormalized sum $`\sum_\sigma\chi_h(\sigma)\sigma z`$; this is also the sum in Kato’s Theorem 6.6. If a character is imprimitive at a larger tame level, first taking the trace to its conductor gives the same sum and Kato’s norm relation supplies exactly the omitted Euler factors. Projection from the full cyclotomic group to its real component has order two and changes only a fixed normalization. Consequently

**Equation (C.1).**

```math
v_2\bigl(\exp_2^*z_{S,h}^{(0)}(0)\bigr)
 =v_2(L_*(h))+
 \sum_{\substack{q\in S\ \mathrm{finite}\\ q\nmid2Nh}}
       v_2\bigl(\#E^{(h)}(\mathbb{F}_q)\bigr)+O_E(1)
```

when the value is nonzero. A zero central value gives zero dual exponential. The error in (C.1) is bounded in absolute value independently of the varying support. At a good unused prime the omitted factor is $`\#E^{(h)}(\mathbb{F}_q)/q`$; at a good ramified prime it is $`1`$. Factors at primes of $`N`$ are fixed because the local twists there are fixed.

### C.4. Rational divisibility and the local Euler factors

Put $`A=\Lambda[1/2]`$. After a quadratic twist and the Tate twist identifying Kato’s representation with $`V_h=V\chi_h`$, Kato’s Theorems 12.4 and 12.5(3) apply over $`A`$. The Tate twist acts on the Iwasawa algebra by its usual automorphism and preserves all height-one length statements. The non-CM open-image theorem Serre (1972), in the form recorded in Kato (2004, 12.8.2 and 13.4), supplies the characteristic-zero irreducibility and a nonidentity unipotent with a one-dimensional fixed space. Intersecting the image with the kernel of a quadratic character preserves an open subgroup. No residual irreducibility or integral $`p\ne2`$ assertion is used.

**Lemma C.8.** For every allowed $`h`$, the local correction in Kato’s rational height-one inequality vanishes. Thus the multiplier at $`2`$ can be taken to be $`F_2=1`$.

*Proof.* Potential good reduction is preserved by quadratic twisting. Kato (2004, 12.5(3), including (12.5.1), and 12.7) states that a nonzero local degree-two term at a rational height-one prime can occur, in weight two, only for a form which is not potentially of good reduction at the coefficient prime. The hypothesis of Lemma A.1 excludes this case.

Write $`C_{j_*}`$ for Kato’s rational global complex, and $`C_{S,h}`$ for ordinary rational global Iwasawa cohomology with the primes of $`S`$ removed. At an odd prime put $`W_q=H^1(I_q,V_h)`$. The localization cone is

**Equation (C.2).**

```math
Q_q=\left[W_q\otimes_{\mathbb{Q}_2}A
    \xrightarrow{\,1-\gamma_q\mathrm{Fr}_{W_q}\,}
    W_q\otimes_{\mathbb{Q}_2}A\right]
```

in degrees one and two. Here $`\gamma_q`$ is the scalar arithmetic Frobenius action in the inverse cyclotomic coefficient module. Its exponent in $`\Gamma`$ is nonzero. Hence $`D_q=\det(1-\gamma_q\mathrm{Fr}_{W_q})`$ is nonzero, and

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

The determinants can all be written explicitly in the present case. At a good unused prime, $`W_q=V_h(-1)`$ and

```math
D_q=P_q(\chi_h(q)\gamma_q),\qquad
 P_q(Z)=1-\frac{a_q(E)}qZ+\frac1q Z^2.
```

At a good active prime, inertia acts by $`-1`$ rationally, so $`W_q=0`$ and $`D_q=1`$. At a multiplicative prime of $`E`$, the local twist is trivial and

```math
W_q=\mathbb{Q}_2(-1)\otimes\mathrm{unr}(a_q(E)),\qquad
 D_q=1-\frac{a_q(E)}q\gamma_q,
 \qquad a_q(E)\in\{1,-1\}.
```

This follows from the Tate-curve extension and its nonsplit unramified twist. In particular, $`W_q`$ is the actual inertia cohomology; it is not replaced by $`V_h^{I_q}(-1)`$. These bad-prime determinants are exactly the omitted multiplicative $`L`$‑factors and have nonzero central values.

**Lemma C.9.** Let $`Z_h`$ be Kato’s rational zeta submodule for the form of $`E^{(h)}`$ in the corresponding real cyclotomic component. With consistent Frobenius conventions, the fixed-form class satisfies

```math
A z_{S,h}^{(0)}=
 \left(\prod_{q\in S\setminus\{2,\infty\}}D_q\right) Z_h
 \quad\text{inside }H^1(C_{S,h}).
```

Consequently, for every height-one prime $`\mathfrak{p}`$ of $`A`$,

**Equation (C.3).**

```math
\mathrm{length}_{A_{\mathfrak{p}}}H^2(C_{S,h})_{\mathfrak{p}}
 \le
 \mathrm{length}_{A_{\mathfrak{p}}}
 \bigl(H^1(C_{S,h})/Az_{S,h}^{(0)}\bigr)_{\mathfrak{p}}.
```

*Proof.* The rational global cohomology is free of rank one over $`A`$, by Kato (2004, Theorem 12.4). A rational generator $`z_{{\mathrm{BK}},h}`$ of $`Z_h`$ can be chosen using one fixed nonzero Betti vector for the form of $`E^{(h)}`$ in the required sign. Compare its explicit reciprocity formula with that of the fixed-form trace at finite-order cyclotomic characters $`ν`$.

The omitted Euler factors in the two formulas have ratio exactly $`\prod_qD_q(ν)`$, by the preceding local calculation. The comparison of the two fixed period vectors, for this one $`h`$, is a nonzero scalar; no bound for its valuation is needed here. The remaining character dependence in the twisting identifications is group-like. More explicitly, for $`ν`$ of conductor $`2^n`$, coprime Gauss-sum factorization gives

```math
\tau(\chi_hν)=\chi_h(2)^nν(\vert h\vert )\tau(\chi_h)\tau(ν).
```

Here $`\chi_h(2)=1`$. Thus the factor depending on $`n`$ disappears, and the remaining factor $`ν(\vert h\vert )`$ is the value of the group-like unit $`[\vert h\vert ]\in\Lambda^\times`$. Reversing the action convention inverts this unit. Using product Gauss bases instead simply absorbs it into the chosen generator of the same $`A`$‑module $`Z_h`$. The common cyclotomic Gauss factors cancel. Hence the reciprocity formulas differ by the displayed Euler product, a scalar in $`\mathbb{Q}_2^\times`$, and a group-like unit. This calculation uses Kato (2004, Theorems 6.6, 9.7, 12.5(1), and Lemma 13.10(2)) with the unnormalized trace convention already specified.

Fix an $`A`$‑basis $`b_h`$ of $`H^1(C_{S,h})`$. The unsmoothed fixed-form trace initially has a coefficient in $`\mathrm{Frac}(A)`$ relative to $`b_h`$: its smoothing factors need not be units of $`A`$. Subtract the comparison class just described, and multiply the difference by a nonzero power-series denominator and a power of $`2`$. The result is $`F(t)b_h`$ with $`F(t)\in\mathbb{Z}_2[[t]]`$.

For this fixed $`h`$, cyclotomic nonvanishing Kato (2004, Theorem 13.5(2)) supplies infinitely many finite-order characters at which the common $`L`$‑value is nonzero. A nonzero power series in $`\Lambda`$ has only finitely many finite-order character zeros, by Weierstrass preparation. Exclude these zeros for the denominator just cleared and for the finitely many interpolation factors. At every remaining character $`ν`$, the explicit reciprocity formula for $`z_{{\mathrm{BK}},h}`$ has nonzero dual exponential. Since $`z_{{\mathrm{BK}},h}`$ is an $`A`$‑multiple of $`b_h`$, the specialization of $`b_h`$ also has nonzero dual exponential. The difference of the two reciprocity formulas is zero, so

```math
F(ν)\,\exp_ν^*(b_h(ν))=0
```

implies $`F(ν)=0`$. These are infinitely many distinct characters. Weierstrass preparation now gives $`F=0`$. Thus the fixed-form trace equals a unit of $`A`$ times the Euler product times $`z_{{\mathrm{BK}},h}`$. In particular it belongs to $`H^1(C_{S,h})`$, and the asserted submodule equality follows. This comparison makes no claim about uniform lattices of the varying newforms.

Kato’s rational inequality bounds $`H^2(C_{j_*})`$ by the index of $`Z_h`$; its local correction is zero by Lemma C.8. The localization sequence adds at most $`\sum_qv_{\mathfrak{p}}(D_q)`$ to the degree-two length. Multiplication of a rank-one submodule by $`\prod_qD_q`$ adds exactly that amount to its index. This proves (C.3). No additional fixed multiplier is needed: here one can take $`F_E=1`$.

We henceforth write $`z_S=z_S^{(0)}`$. The inverse cyclotomic action in (C.2) is also the action used in Kato’s norm relation Kato (2004, Theorem 8.12); thus the displayed Euler factors agree before character evaluation.

### C.5. The integral determinant coordinate

Choose an $`R`$‑basis $`\mathbf{e}`$ of the invertible module $`\det_R^{-1}\mathcal{C}_S^+`$. In generic cohomology put

```math
a\wedge\widetilde{2z_S}=u\mathbf{e}.
```

The generic positive degree-one cohomology has rank two: ordinary rational cohomology has rank one and the real invariant line contributes one more. Its degree-two cohomology is torsion. Over $`\mathcal{O}[G]`$, Lemma C.6 identifies the determinant with the exterior square of an integral free degree-one module. The fixed-form lattice comparison, integral coefficient map, and unsmoothing therefore give

```math
2^{C_{\mathrm{int}}}u\in\mathcal{O}[G]
```

with one $`C_{\mathrm{int}}`$ independent of $`S`$, $`h_0`$, and $`G`$.

On the other hand, (C.3) implies $`u_x\in A`$ for every character $`x`$. Indeed, after inverting $`2`$, the real invariant line is primitive and contributes no height-one torsion. The inverse-determinant valuation at a height-one prime is the index of the zeta vector minus the length of degree-two torsion. It is nonnegative by (C.3). Normality of $`\Lambda`$ therefore excludes every pole except possibly at $`(2)`$.

**Lemma C.10 (Integral Fourier intersection).** If every $`u_x`$ belongs to $`\Lambda[1/2]`$ and $`2^C u\in\mathcal{O}[G]`$, then $`2^C u\in\Lambda[G]`$.

*Proof.* Fourier inversion expresses each group-basis coefficient of $`u`$ as a sum of its character values divided by $`\vert G\vert `$. As $`\vert G\vert `$ is a power of two, that coefficient belongs to $`\Lambda[1/2]`$. The corresponding coefficient of $`2^Cu`$ belongs also to $`\mathcal{O}`$. For a power series with bounded $`2`$‑denominator, nonnegative valuation in $`\mathcal{O}`$ means that all its coefficients are integral. Thus $`\mathcal{O}\cap\Lambda[1/2]=\Lambda`$.

We have consequently proved the uniform assertion

**Equation (C.4).**

```math
2^{C_{\mathrm{int}}}u\in\Lambda[G].
```

This argument introduces no loss depending on the size of the quadratic group.

### C.6. The integral central comparison

**Lemma C.11 (Derived Kummer reduction).** Let $`K/\mathbb{Q}_2`$ be finite, put $`T_h=T_2E^{(h)}`$, and put $`M=E^{(h)}(K)^{\wedge}_2`$. The Kummer condition is represented by the perfect complex $`M[-1]\to R\Gamma(K,T_h)`$. Its derived reduction modulo $`2^n`$ has degree-zero group $`M[2^n]`$ and degree-one group $`M/2^nM`$; the induced maps are respectively the local invariant map and the finite Kummer map.

*Proof.* The compact point group $`M`$ is a finite-rank free $`\mathbb{Z}_2`$‑module plus a finite group, so it has a free resolution of length one. After the shift by $`-1`$, tensoring this resolution with $`\mathbb{Z}/2^n\mathbb{Z}`$ gives the two displayed groups. The actual Kummer map is obtained from the inverse system of the multiplication-by‑$`2^n`$ sequences. Its compatibility with reduction follows from these same sequences. In degree zero this can also be read from the Bockstein sequence: $`H^0(K,T_h)=0`$, and $`H^1(K,T_h)_{\mathrm{tors}}=E^{(h)}(K)[2^\infty]`$. Consequently the reduction retains precisely the torsion invariants $`E^{(h)}(K)[2^n]`$, as well as the usual degree-one Kummer image. The statement is about derived reduction, so it does not require flatness of the coefficient quotient.

**Proposition C.12.** There is a constant $`C_{\mathrm{loc}}`$, depending only on $`E`$ and the fixed period choices, such that the following holds. If $`s_2(E^{(h)})=0`$, then

```math
u_h(0)=0\quad\Longleftrightarrow\quad L(E^{(h)},1)=0.
```

If these values are nonzero, then

**Equation (C.5).**

```math
\bigl\vert v_2(u_h(0))-D(h)\bigr\vert \le C_{\mathrm{loc}}.
```

The estimate is independent of all varying tame primes.

*Proof.* Write $`T_h=T_2E^{(h)}`$, $`A_h=E^{(h)}[2^\infty]`$, and

```math
H=H^1(G_{\mathbb{Q},S},T_h),\qquad
 H_2=H^2(G_{\mathbb{Q},S},T_h).
```

For a finite or real place $`v`$, let $`K_v`$ be the inverse-limit Kummer image of $`E^{(h)}(\mathbb{Q}_v)^{\wedge}_2`$ in $`H^1(\mathbb{Q}_v,T_h)`$. The inverse-limit Kummer sequence and local duality Milne (2006, I, Theorem 3.2) identify its quotient with $`T_2H^1(\mathbb{Q}_v,E^{(h)})`$. At an odd finite place the $`2`$‑completion of the local point group is finite, so this Tate module is zero. It is also zero at the real place. At $`2`$, the local point group has a free $`\mathbb{Z}_2`$‑part of rank one, and

```math
L_2=H^1(\mathbb{Q}_2,T_h)/K_2
```

is free of rank one. These assertions use the full Kummer condition, including at the bad primes.

The dual exponential induces an isomorphism from $`L_2\otimes\mathbb{Q}_2`$ to its one-dimensional de Rham target. For an elliptic curve, compatibility of the Kummer map with the exponential and formal logarithm, together with their local-duality adjunction, is given by Bloch–Bloch and Kato (1990, Proposition 3.8 and Example 3.11). It is valid for every reduction type. Choose a generator $`ℓ_h`$ of $`L_2`$ and use a minimal differential in the target. Define

```math
\delta_{2,h}=v_2(\exp_2^*ℓ_h).
```

The integer $`\delta_{2,h}`$ is bounded independently of $`h`$: the local curve is fixed up to isomorphism and a minimal differential is fixed up to a unit. Equivalently, the formal logarithm is an integral isomorphism on a fixed sufficiently small formal subgroup, and its adjoint gives the asserted fixed lattice index.

Here is the integral Poitou–Tate calculation, including its real term. At each finite level $`E^{(h)}[2^n]`$, the two Kummer images are exact annihilators under the Weil pairing and local Tate duality. The finite Poitou–Tate sequence therefore gives the Selmer comparison sequence. Explicitly, a character of the finite Selmer subgroup extends to global degree-one cohomology because $`\mathbb{Q}/\mathbb{Z}`$ is injective. Its Poitou–Tate connecting image in global degree two is independent of that extension: the difference comes from a local Kummer image, by the exact-annihilator relation. The same relation identifies the kernel with the image of the singular local quotient. Taking inverse limits on the compact side and direct limits on its dual side is exact: all the finite-level groups are finite and the inverse systems satisfy Mittag–Leffler. The real terms are complete Tate cohomology, agreeing with ordinary cohomology in the positive degrees used below; see Milne (2006, I, Theorem 4.10) and Nekovář (2006, 5.7.1.6). Since all singular compact local quotients except $`L_2`$ vanish, the resulting tail is

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

where $`J`$ is the image of $`H`$ in $`L_2`$.

The assumption $`s_2(E^{(h)})=0`$ makes the discrete Selmer group finite of length $`s(h)`$ and the compact Selmer group torsion. Tensoring the same comparison sequence with $`\mathbb{Q}_2`$ identifies $`H\otimes\mathbb{Q}_2`$ with $`L_2\otimes\mathbb{Q}_2`$ and makes $`H_2\otimes\mathbb{Q}_2=0`$. Thus $`J`$ has finite index, say $`i=\mathrm{length}(L_2/J)`$, and $`H_2`$ is finite. Put

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

Also $`H_{\mathrm{tors}}=H^0(\mathbb{Q},A_h)`$, by the cohomology sequence of $`0\to T_h\to V_h\to A_h\to0`$ and the vanishing of rational invariants.

We next compute the determinant coordinate without suppressing any finite index. Put $`K=\ker(H\to H^1(\mathbb{R},T_h))`$, let $`k_0=\mathrm{length}K_{\mathrm{tors}}`$, and let $`k`$ be the index length of $`K/K_{\mathrm{tors}}`$ in $`H/H_{\mathrm{tors}}`$. The positive cone sequence gives

```math
0\longrightarrow\mathbb{Z}_2a\longrightarrow H^1(\mathcal{C}_{S,h}^+(0))
 \longrightarrow K\longrightarrow0.
```

This positive degree-one group is free, since its complex has a finite free model in degrees $`1,2`$. The index of $`a`$ in its saturated real line is therefore $`2^{k_0}`$. If $`\alpha`$ is the coordinate of $`z_{S,h}(0)`$ in a generator of $`H/H_{\mathrm{tors}}`$, then the valuation of $`a\wedge\widetilde{2z_{S,h}(0)}`$ in the exterior square of the positive degree-one lattice is

```math
k_0+1+v_2(\alpha)-k.
```

The image of $`H`$ in $`H^1(\mathbb{R},T_h)`$ has length $`g-k_0+k`$. Surjectivity onto $`H^2(\mathbb{R},T_h)`$, proved in Lemma C.3, consequently gives

```math
\mathrm{length}H^2(\mathcal{C}_{S,h}^+(0))
   =\mathrm{length}H_2+r_1-g+k_0-k-r_2.
```

For a perfect complex with free degree-one cohomology and finite degree-two cohomology, its inverse determinant lattice maps to $`2^{\mathrm{length}H^2}`$ times the exterior power of the free degree-one lattice. This follows directly from Smith normal form, or from the block $`[\mathbb{Z}_2\xrightarrow{2^a}\mathbb{Z}_2]`$ in degrees one and two. A vector’s determinant coordinate therefore subtracts that length. The preceding two identities give

**Equation (C.8).**

```math
v_2(u_h(0))
  =v_2(\alpha)-\mathrm{length}H_2+g+1+r_2-r_1.
```

Since the image of a free generator of $`H`$ generates $`J`$,

```math
v_2(\alpha)=v_2(\exp_2^*z_{S,h}(0))-i-\delta_{2,h}.
```

Substitution of (C.7) into (C.8) cancels $`i`$ and yields

**Equation (C.9).**

```math
v_2(u_h(0))=
 v_2(\exp_2^*z_{S,h}(0))-s(h)
 -\sum_{\substack{q\in S\\ q\ \mathrm{finite}}}a_q
 +2g+1-\delta_{2,h}-r_1.
```

Full rational $`2`$‑torsion makes complex conjugation congruent to the identity modulo $`2`$. Thus $`(1+c)/2`$ and $`(1-c)/2`$ are integral projectors, each of rank one. In particular $`r_1=r_2=1`$.

At a good active prime, inertia acts by $`-1`$ on $`A_h`$; its invariants are exactly $`E[2]`$, all fixed by Frobenius, so $`a_q=2`$. At a good unused prime, reduction identifies the local $`2`$‑primary torsion with $`E^{(h)}(\mathbb{F}_q)[2^\infty]`$, so $`a_q=v_2(\#E^{(h)}(\mathbb{F}_q))`$. These unused terms cancel precisely the Euler terms in (C.1), and the active terms sum to $`2\omega(\vert h\vert )`$. The terms at $`2N`$ are fixed. Finally, $`g\le a_2`$, because global torsion injects into local torsion at $`2`$, and $`a_2`$ is fixed. Formula (C.9) proves the *two-sided* bound (C.5). It is a central lattice computation; it makes no equality assertion for Iwasawa characteristic ideals.

The same rational comparison sequence showed that the central positive complex has only degree-one rational cohomology, of dimension two. This equals its generic rank, so the determinant and its wedge specialize under derived coefficient change without a rank change. If $`L(E^{(h)},1)=0`$, explicit reciprocity gives zero dual exponential. The ordinary rational class then satisfies the Kummer condition at $`2`$ and, automatically, at every other place. Its rational finite Selmer group is zero, so the class is zero and its wedge with $`a`$ vanishes. Conversely, a nonzero central value has nonzero dual exponential, hence a nonzero ordinary free-line coordinate and a nonzero wedge. This proves the asserted equivalence.

### C.7. Binary congruences and the two consequences

**Lemma C.13.** Let $`z_1,\ldots,z_r\in\mathbb{Z}_2[G]`$. If $`b\gt r(2^M-1)`$, then there is $`x\ne0`$ such that

```math
(z_j)_x\equiv(z_j)_0\pmod{2^M}\qquad(1\le j\le r).
```

*Proof.* Expanding sign characters as products of $`1-2x_i`$ gives

```math
z(x)=a_\emptyset+
 \sum_{\emptyset\ne I\subseteq\{1,\ldots,b\}}
       2^{\vert I\vert }a_I\prod_{i\in I}x_i,
 \qquad a_I\in\mathbb{Z}_2.
```

The $`j`$th binary digit of a $`2`$‑adic integer $`a`$ is the coefficient of $`Y^{2^j}`$ in $`(1+Y)^a`$ over $`\mathbb{F}_2`$. On the Boolean cube, a monomial $`x_I=\prod_{i\in I}x_i`$ contributes

```math
1+x_I\bigl((1+Y)^{2^{\vert I\vert }a_I}-1\bigr).
```

Its nonconstant terms start in degree at least $`2^{\vert I\vert }`$ in $`Y`$. Since $`\vert I\vert \le2^{\vert I\vert }`$, the coefficient of $`Y^{2^j}`$ has Boolean degree at most $`2^j`$. The formulas extend to all $`2`$‑adic coefficients by continuity in each finite coefficient quotient.

The $`rM`$ digit equalities are therefore Boolean equations of total degree at most $`r(2^M-1)`$. Their common-zero indicator is the product of one plus each equation. A Boolean polynomial of degree less than $`b`$ has even sum over $`\mathbb{F}_2^b`$, since every monomial omits at least one variable. Thus the number of common zeros is even. It already contains $`0`$, so it contains a nonzero point.

*Proof of Theorem C.1.* For $`L(E^{(h)},1)\ne0`$, the forward analytic-rank-zero theorem Kolyvagin (1990) gives $`s_2(E^{(h)})=0`$ and finiteness of its Shafarevich–Tate group. Apply the construction to this single character. Equation (C.4) gives $`v_2(u_h(0))\ge-C_{\mathrm{int}}`$, and the central comparison gives $`D(h)\ge-C_{\mathrm{int}}-C_{\mathrm{loc}}`$.

*Proof of Theorem C.2.* Choose an integer $`M`$ with

```math
M-C_{\mathrm{int}}\gt B+C_{\mathrm{loc}}.
```

For a family with $`b\gt 2^M-1`$, apply Lemma C.13 to the constant coefficient of the element $`2^{C_{\mathrm{int}}}u\in\Lambda[G]`$. It gives $`x\ne0`$ with

```math
v_2(u_x(0)-u_0(0))\ge M-C_{\mathrm{int}}.
```

The hypotheses at $`x`$, the forward theorem, and Proposition C.12 give $`v_2(u_x(0))\le B+C_{\mathrm{loc}}`$. The ultrametric inequality now implies

```math
u_0(0)\ne0,\qquad
 v_2(u_0(0))=v_2(u_x(0))\le B+C_{\mathrm{loc}}.
```

Since the base has Selmer corank zero, Proposition C.12 gives $`L(E^{(h_0)},1)\ne0`$ and $`D(h_0)\le B+2C_{\mathrm{loc}}`$. One constant $`C_E`$ can cover both stated theorems and the two fixed real signs.

---

[← Main article and Appendices A–B](README.md) · [Main article](README.md) · [Appendix D, sections D.1–D.4 →](appendix-d.md)
