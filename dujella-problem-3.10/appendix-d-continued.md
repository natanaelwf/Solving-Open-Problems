[← Appendix D, sections D.1–D.4](appendix-d.md) · [Main article](README.md) · [Appendix E →](appendix-e.md)

---

## Appendix D. Ring-class determinants (continued)

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

Denote its coordinate in an integral determinant basis by $`u_I`$. Changing that basis multiplies $`u_I`$ by a unit. For a generically acyclic constituent set this class-dual coordinate to zero. For $`I=\emptyset`$ write $`u_h`$.

**Lemma D.13 (Exact integral switch).** At a derivative prime let the integral localization and duality triangles be those of Lemma D.6, over a DVR $`O`$. Suppose the finite-condition complex has generic $`H^1`$ spanned by $`A`$, and the derivative class $`B`$ has

```math
f(A)=v\ne0,\qquad f(B)=0,\qquad s(B)=Jv.
```

The singular-condition complex has generic rank one, spanned by $`B`$, and the two actual class-dual determinant coordinates satisfy

```math
v_O(u_F)=v_O(u_S).
```

Neither localization is required to be primitive.

*Proof.* Work first over the fraction field. Nonzero localization of $`A`$ makes strict $`H^1`$ zero. The relaxed localization image is self-annihilating in $`F\oplus S`$, hence has dimension two. It contains $`(v,0)`$ and $`(0,Jv)`$, so its intersections with the two planes are precisely these lines. This proves the rank assertion.

Let $`V=H^1(C_{\mathrm{rel}})`$ have basis $`A,B`$. Duality identifies $`H^2(C_{\mathrm{str}})`$ with $`V^*`$; let $`A^*,B^*`$ be the dual basis. The integral triangles

```math
C_{\mathrm{str}}\longrightarrow C_F\longrightarrow F[-1],\qquad
 C_{\mathrm{str}}\longrightarrow C_S\longrightarrow S[-1]
```

have boundaries dual to relaxed localization. In the first,

```math
\delta_F(x)=\epsilon\langle x,v\rangle B^*,\qquad
                                  \epsilon\in O^\times.
```

Choose a fractional $`x`$ with $`\delta_F(x)=B^*`$. The exterior product $`v\wedge x`$ has unit volume in $`\det_O F`$ because the alternating form is unimodular. Similarly choose $`y`$ in the singular plane mapping to $`A^*`$; $`Jv\wedge y`$ has unit volume. The determinant isomorphisms carry the two class-dual tensors to

```math
(A^*\wedge B^*)^*\otimes(v\wedge x),\qquad
 (A^*\wedge B^*)^*\otimes(Jv\wedge y),
```

up to units and signs. The plane determinant lattices are unimodularly identified, so their valuations agree. These are the integral triangles, including their torsion elementary divisors. For example, $`v=2^de_1`$ is paired with $`2^{-d}e_2`$; their exterior product is a unit. No factor $`2^d`$ is discarded or charged anew at the switch.

**Lemma D.14 (Rank-two evaluation).** At an inner characteristic-zero test with $`\Psi^2\ne1`$, and at every outer characteristic-zero test, the rank-four induced representation $`W`$ is absolutely irreducible. For two independent Selmer classes their joint evaluations on the exact kernel span $`W\oplus W`$. Some actual kernel element has rank-two finite localization. One of the classes may be any prescribed nonzero class.

*Proof.* Moving inertia distinguishes $`\Psi`$ and $`\Psi^{-1}`$. The Tate representation over $`K`$ is absolutely irreducible by open image, and multiplication of its matrices by character scalars does not change invariant subspaces. These facts prove irreducibility of the induction. In the outer case a uniform finite witness is needed. The images of the quadratic subgroups have index at most two in the fixed compact Tate image; there are finitely many such subgroups. On a large set choose one and finitely many of its matrices spanning $`M_2(\mathbb{Q}_2)`$. Their spanning determinant is a fixed nonzero $`2`$‑adic number. Character scalars are units, so this determinant remains nonzero in the outer fraction field. Moving inertia separates the two blocks, and conjugation interchanges them. Moreover $`1+t`$ has infinite order already in each $`\Omega`$: for a nonzero integer $`n`$, $`(1+t)^n-1`$ is a nonzero Laurent-series unit. It remains nonzero in the outer quotient.

Restriction to the exact kernel is injective by Lemmas D.10 and D.12. There the cocycles are additive homomorphisms with equivariant image. A proper submodule of $`W\oplus W`$ projecting onto both factors would impose a scalar relation, since $`W`$ is absolutely simple. That relation would contradict independence after restriction. Thus the joint span is the whole direct sum. Projection by $`1+\tau`$ gives all pairs in the finite plane. If their determinant quadratic vanished on the additive image, its polar form would vanish on every pair in that image, hence the quadratic would vanish on its entire field span. This is impossible. An actual rank-two evaluation therefore exists and is realized by Lemma D.10.

**Proposition D.15 (Power-series regularity and uniform bound).**

For a primitive constituent whose generic cohomology is acyclic or has the rank-one pattern above, its coordinate lies in $`\Lambda[1/2]`$. For the simple-zero instances,

```math
v_{(2)}(u_h)\geq-C(E,A),\qquad \omega(\vert k\vert )\leq A.
```

*Proof.* The zero coordinate needs no argument. Otherwise the arithmetic class spans generic $`H^1`$. At a height-one prime $`\mathfrak{p}\ne(2)`$, use the DVR $`\Lambda_{\mathfrak{p}}`$ and its characteristic-zero residue field. The full active local complexes are acyclic because ramified quadratic inertia minus one is $`-2`$. At $`r`$ the same holds unless the scalar inertia is one; that case is $`t=0`$, where the bounded nonzero Frobenius determinant from Lemma D.3 suffices. Degree-zero evaluation and global duality exclude degrees zero and three, so unit cancellation leaves a square two-term model. Its generic kernel is saturated; a primitive kernel vector has nonzero $`\mathfrak{p}`$‑fiber.

If the fiber dimension is $`s\gt 1`$ and $`\Psi^2\ne1`$, choose a rank-two finite localization by Lemma D.14, including that primitive vector. The relaxed localization image is self-annihilating and contains the entire finite plane, so equals that plane. The strict kernel has dimension $`s-2`$, and the singular condition adds no class. The fiber rank drops by two. Generic localization is nonzero, so Lemmas D.8 and D.13 preserve generic rank one, a nonzero arithmetic class, and the determinant valuation.

If $`\Psi^2=1`$, the induced representation splits into two inequivalent absolutely irreducible quadratic twists. They are inequivalent because a nontrivial quadratic self-twist would contradict the open Tate image. Conjugation splits the Selmer fiber into these two signs. Each sign has a finite and a singular line, with a symmetric hyperbolic local pairing. Since the residue characteristic is zero, its only isotropic lines are the two axes. If both signs occur globally, independent evaluations in the two signs give rank two, nonzero on a prescribed nonzero component of the primitive vector. If only one sign occurs and $`s\gt 1`$, first choose a nonzero rank-one localization on that vector. The relaxed image is the finite line in that sign and the singular line in the other sign. A switch retains the old strict kernel of dimension $`s-1`$ and introduces the other sign. The next rank-two switch reduces the dimension by two. Repetition terminates at dimension one; it cannot pass below one because a primitive generic-kernel vector survives every switch. The terminal minimal DVR model is one-by-one with zero differential. The class and functional are integral there, so its determinant coordinate is integral. Reversing the exact switches proves nonnegative valuation at $`\mathfrak{p}`$. Intersecting all such height-one valuation rings in the normal ring $`\Lambda`$ proves $`u_h\in\Lambda[1/2]`$.

For the uniform bound at $`(2)`$, suppose instead that a sequence of simple-zero coordinates has valuations tending to $`-\infty`$. By Lemma D.11 the minimal models have bounded size and one common functional clearing exponent $`a`$. Fix their size on a large set and write

```math
C_j=[\,\mathcal{O}_j^n\xrightarrow{D_j}\mathcal{O}_j^n\,].
```

Apply Lemma D.12. The outer kernel may contain new classes represented only by approximate inner cycles; the retained degree-two identities make them valid classes for evaluation. Primitive vectors in the inner generic kernels supply a nonzero outer class. If the outer dimension is $`s\gt 1`$, use Lemma D.14 with that class and a second one, and realize the evaluation at the original finite stages. The outer rank drops by two as above. The primitive inner vector localizes nontrivially on a large set, hence so does its nonzero arithmetic multiple. The exact switch preserves each inner determinant valuation, even if that multiple is highly divisible.

Only boundedly many switches are needed, because the initial outer size is bounded. At terminal outer rank one an $`(n-1)`$‑minor has nonzero image, so its inner determinants have one finite valuation $`b`$ on a large set. Put it in the upper left block $`A_j`$ of $`D_j`$. Fraction-field triangular operations of determinant one leave $`A_j`$ and a zero one-by-one block. If $`\alpha_j`$ is the last coordinate of the integral class and $`\beta_j`$ the value of the functional on the last target basis vector, the determinant formula is

```math
u_j=\pm\frac{\alpha_j\beta_j}{\det A_j},\qquad
 \alpha_j\in\mathcal{O}_j,\quad
 \beta_j\in2^{-a}\mathcal{O}_j.
```

Thus $`v_2(u_j)\geq-a-b`$, contradicting the assumed losses. All new diagrams were adjoined to the same finite stages and ultrafilters as in Lemma D.12; the common clearing exponent remains valid through every switch.

### D.6. Central specialization

**Lemma D.16 (The integral central complex).** Let $`C`$ be a perfect $`\Lambda`$‑complex and $`C_0=C\otimes_\Lambda^{\mathbf{L}}\mathbb{Z}_2`$. If generic and central rational cohomology both have dimension one in degrees one and two and vanish elsewhere, a class-dual tensor represented over $`\Lambda_{(t)}`$ specializes to its actual central class-dual tensor. The determinant comparison retains all torsion cohomology of $`C_0`$. For the ordinary integral Kummer Selmer complex, its degree-two torsion has the length of the quotient of $`\mathrm{Sel}_{2^\infty}`$ by its maximal divisible subgroup.

*Proof.* Derived reduction is termwise reduction of a free model, so its determinant line commutes with base change. The cohomology sequences are

```math
0\longrightarrow H^j(C)/tH^j(C)
 \longrightarrow H^j(C_0)
 \longrightarrow H^{j+1}(C)[t]\longrightarrow0.
```

Over the DVR $`\Lambda_{(t)}`$, a nonunit differential pivot would create extra central cohomology in adjacent degrees. The equal generic and central dimensions exclude such pivots. Only invertible disks and the two free lines remain, proving specialization of the tensor. The determinant isomorphism over $`\mathbb{Z}_2`$ still contains every elementary divisor, including those arising from the displayed base-change terms.

For the Kummer complex, derived tensor with $`\mathbb{Q}_2/\mathbb{Z}_2`$ gives the discrete Selmer group in degree one. Its universal-coefficient sequence has divisible image $`H^1(C_0)\otimes\mathbb{Q}_2/\mathbb{Z}_2`$ and finite quotient $`\mathrm{Tor}_1(H^2(C_0),\mathbb{Q}_2/\mathbb{Z}_2)`$. The image is the maximal divisible subgroup: any divisible subgroup maps trivially to the finite quotient. The latter is canonically the torsion of $`H^2(C_0)`$, proving the length statement. This argument allows a divisible part in the Shafarevich–Tate group.

**Lemma D.17 (Active local contribution).** At a good odd prime ramified in a quadratic twist of $`E`$, the quotient of the full integral local complex by the Kummer condition has only degree-two cohomology, of length two. Thus an active prime split in $`K`$ contributes exactly four to this quotient length.

*Proof.* The pro‑$`2`$ tame inertia generator acts by $`-1`$, so its integral complex has differential $`-2`$ and only $`H^1=T/2T`$. Taking residue-field cohomology gives

```math
H^1(K_v,T\chi_h)=E[2]^{\mathrm{Fr}_v},\qquad
 H^2(K_v,T\chi_h)=E[2]/(\mathrm{Fr}_v-1)E[2].
```

Both have length two because $`E[2]`$ is rational. The local integral Kummer sequence identifies $`H^1`$ with the completed point group: the residual local Weil–Châtelet group has finite $`2`$‑primary part and hence zero Tate module. The full/Kummer quotient therefore has exactly the asserted $`H^2`$. There are two places over every split active prime.

**Proposition D.18 (Central determinant formula).** At every known simple-zero instance,

```math
v_2(u_h(0))
   =2j_h(k)-s(h)-s(hk)-4w(h)+O_{E,A}(1),
       \qquad \omega(\vert k\vert )\leq A.
```

The error is independent of the number of primes dividing $`h`$. At a base of Selmer corank one, generic cohomology has rank at most one. If its central Heegner point is torsion, its primitive class-dual coordinate satisfies $`u_0(0)=0`$.

*Proof.* At a known simple zero, the forward Gross–Zagier–Kolyvagin theorem gives rank one over $`K`$ and finite Shafarevich–Tate group. At the split auxiliary prime the point norm relation is

```math
\mathrm{Tr}_{H_{\vert h\vert r_i}/H_{\vert h\vert }}y_{\vert h\vert r_i}
   =(a_{r_i}-\sigma_{r_i}-\sigma_{\bar r_i})y_{\vert h\vert }.
```

At $`t=0`$ the scalar character is trivial and both Artin symbols have quadratic value $`\chi_h(r_i)`$. The completed weighted class therefore specializes to the Kummer class of $`Lm_iP_h(K)`$, where $`m_i=a_{r_i}-2\chi_h(r_i)`$ and $`v_2(m_i)\leq c_E`$.

This equality is retained as an equality in the actual target diagram. Choose a free model of the ordinary Kummer Selmer complex and a representative $`b_h`$ of $`P_h(K)`$. The central comparison $`j_i`$ to the relaxed target has, after contraction, a degree-zero witness $`v_i`$ with

```math
z_i(0)-Lm_i j_i(b_h)=dv_i.
```

The equality follows from Kummer naturality, the point norm, and the injection of Selmer $`H^1`$ into global cohomology. Retain this witness, its local comparison triangles, and their matrices. The limit $`m`$ is nonzero and has bounded valuation because the same bound holds at every stage.

The paired functional has a representative over $`\Lambda_{(t)}`$. There, active inertia minus one is $`-2`$, a unit, and the central auxiliary Frobenius determinants are nonzero by Lemma D.3. Contract those local complexes and apply the retained global duality. This is the same generic functional as the integral representative over $`\mathcal{O}`$, and its specialization is rational Kummer duality. Over $`\Lambda_{(t)}`$, unit cancellation leaves one term in each of degrees one and two, since these are the central rational dimensions. The retained cycle has nonzero central image, so the remaining one-by-one differential must be zero. Generic and central rational ranks are therefore both one, and Lemma D.16 applies.

In the ordinary integral Kummer complex, free degrees one and two are paired unimodularly. The point and its functional each contribute $`j_h(k)`$. The degree-two torsion subtracts $`v_2\#\mathrm{Sha}(E^{(h)}/K)[2^\infty]`$ from the inverse determinant coordinate. Torsion in degrees one and three is bounded by the fixed scalar annihilator. More generally an elementary divisor of valuation $`d`$ with cokernel in degree $`j`$ contributes $`(-1)^{j+1}d`$. Lemma D.17 therefore subtracts exactly $`4w(h)`$. At $`r`$, the two local determinants have valuations $`v_2(r+1-a_r\chi_h(r))\leq c_E`$; the point multiplier also has bounded valuation. The unchanged Kummer conditions at $`2N`$ range through finitely many fixed local types. Consequently

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

whose composites are multiplication by $`2`$. The Cassels–Tate isogeny identity, with the finite Shafarevich–Tate groups just established, identifies

```math
\frac{\#\mathrm{Sha}(A_h)\mathrm{Reg}(A_h)
                 \mathrm{Per}(A_h)\prod_p c_p(A_h)}
      {\#A_h(\mathbb{Q})_{\mathrm{tors}}\,
       \#A_h^\vee(\mathbb{Q})_{\mathrm{tors}}}
```

with the analogous expression for $`B_h`$ Milne (2006, I, proof of Theorem 7.3, especially (7.3.1)). This is an isogeny theorem, and does not assume the Birch–Swinnerton-Dyer conjecture. The fixed-degree composites bound the rank-one regulator, period, differential, and torsion ratios by fixed powers of $`2`$. At split primes the component factors agree exactly; this cancels every prime dividing $`h`$. At an odd prime dividing $`k`$ outside $`2N`$, the Weil restriction of the good curve has connected special fiber, whereas the ramified rational twist has component $`2`$‑part at most $`4`$. At other good nonsplit primes both factors are one. The comparisons at $`2N`$ are fixed. Hence

```math
v_2\#\mathrm{Sha}(E^{(h)}/K)[2^\infty]
       =s(h)+s(hk)+O_{E,A}(1).
```

This proves the formula without any error accumulating with $`w(h)`$.

At the unknown base, the central Kummer complex has rational dimensions one in degrees one and two by Selmer corank one; relaxation changes only rationally acyclic local terms. Generic dimensions are therefore at most one. If the generic complex is acyclic its coordinate is zero by definition. Otherwise the generic and central ranks agree, and Lemma D.16 specializes its tensor to the actual rational Kummer class-dual tensor. A torsion central point has zero rational Kummer class, so $`u_0(0)=0`$. No identification of Selmer corank with Mordell–Weil rank is used.

*Proof of Theorem D.1.* At a known simple zero, Proposition D.18 verifies the generic rank-one pattern. Proposition D.15 gives $`u_h\in\Lambda[1/2]`$ and a uniform lower bound for its $`(2)`$‑valuation. Thus $`2^{C(E,A)}u_h\in\Lambda`$, and its constant coefficient has the same lower bound. Substitute the central formula and enlarge the constant.

### D.7. Universal families and bounded clearing

Fix $`K`$ and one binary family from Theorem D.2. Put $`G=(\mathbb{Z}/2)^b`$ and $`R=\Lambda[G]`$, and write a subscript $`0`$ for augmentation. At every finite stage form the weighted transfer over $`A_i[G]`$, using the coefficient map

```math
A_i[\mathrm{Gal}(H_{r_i\prod_{q\in Q}q}/K)]
 \longrightarrow A_i[G],\qquad
 [\sigma]\longmapsto\Psi_i(\sigma)[\varepsilon(\sigma)].
```

Here $`\varepsilon`$ is the universal quadratic character; the same inverse-action convention is used on both sides. Complete this actual coset sum, its local lifts and boundary witnesses, before taking the finite target models and their limit. Character evaluation commutes with every finite identity. Lemma D.11 constructs the paired functional over $`\mathcal{O}[G]`$ itself. All comparisons with the ordinary central Kummer complex, including the multiplier $`a_{r_i}-2[\varepsilon(\mathrm{Fr}_{\mathfrak{r}_i})]`$, are retained in this same diagram.

**Lemma D.19 (Lifting a localization filtration).** Let $`G`$ be a finite abelian $`2`$‑group, put $`R=\mathbb{Z}_2[[t]][G]`$, and let $`\epsilon:R\to\Lambda=\mathbb{Z}_2[[t]]`$ be augmentation. Let $`C`$ be a perfect $`R`$‑complex. Suppose the actual augmentation localization triangle identifies $`C\otimes_R^{\mathbf{L}}\Lambda`$ with a bounded finite free complex

```math
T_0^\bullet=C_{\mathrm{old}}^\bullet\oplus Q^\bullet,\qquad
 d_{T_0}=\begin{pmatrix}d_{\mathrm{old}}&U_0\\0&A\end{pmatrix},
```

where $`Q^\bullet`$ is a direct sum of two-term local complexes in degrees one and two. There is a bounded finite free model of $`C`$, obtained by homotopy equivalences and addition of contractible free disks, whose underlying graded module lifts this displayed decomposition and whose differential has blocks

```math
d_C=\begin{pmatrix}D&U\\ S&B\end{pmatrix},\qquad
 D_0=d_{\mathrm{old}},\quad S_0=0,\quad B_0=A.
```

All entries belong to $`R`$. Every specified morphism and homotopy in the localization triangle can be transported through these equivalences. In particular, the assertion does not require the old summand to be a subcomplex before augmentation.

*Proof.* The ring $`R`$ is local, with maximal ideal generated by $`2,t`$, and the augmentation ideal. Repeatedly cancel a unit differential entry in a bounded finite free model of $`C`$. Each cancellation splits off a contractible free disk and retains explicit inclusion, projection, and contraction maps. The resulting model $`C_{\min}`$ is minimal over $`R`$; its augmentation is minimal over $`\Lambda`$.

Perform the same cancellations on $`T_0`$, obtaining $`T_0\simeq T_{\min}\oplus E_0`$, where $`E_0`$ is a finite direct sum of contractible disks. The given augmentation comparison induces a homotopy equivalence between $`C_{\min}\otimes_R\Lambda`$ and $`T_{\min}`$. A homotopy equivalence between bounded minimal free complexes over a local ring is a chain isomorphism: modulo the maximal ideal its differential is zero and its homotopy-inverse identities are degreewise inverse identities; Nakayama’s lemma then makes every degreewise matrix invertible. Hence

```math
(C_{\min}\otimes_R\Lambda)\oplus E_0\cong T_0
```

as based complexes. Lift $`E_0`$ to the same identity disks over $`R`$ and lift each matrix of this graded isomorphism to $`R`$. These lifted matrices are invertible because their augmented determinants are $`\Lambda`$‑units. Conjugating the actual differential on $`C_{\min}\oplus E_0\otimes_\Lambda R`$ by these matrices gives the asserted blocks and their exact augmentation identities. Transport of the specified maps and homotopies uses the retained contractions and these chain isomorphisms.

**Lemma D.20 (Simultaneous elimination).** Write $`\mathcal{O}=\widehat{\Lambda_{(2)}}`$. Suppose $`A=\mathrm{diag}(A_1,\ldots,A_m)`$ has entries in $`\Lambda`$, with $`\det\overline A_j\ne0`$ and $`\mathrm{ord}_t(\det\overline A_j)\le h`$. If $`B=A+2E`$ and $`E`$ has power-series entries, then $`B`$ is invertible over $`\mathcal{O}`$, and every entry of $`B^{-1}`$ modulo $`2^M`$ has no Laurent term of degree below $`-Mh`$. The same lower bound holds for the entries of $`P-UB^{-1}S`$ when $`P,U,S`$ have power-series entries. These bounds do not depend on $`m`$.

Consequently, if $`G`$ is elementary abelian and $`B`$ is the lifted block in Lemma D.19, it is invertible over $`\mathcal{O}[G]`$. Eliminating this block leaves a complex of the old graded size. Its augmentation is exactly $`C_{\mathrm{old}}`$, and all its sign constituents satisfy the preceding Laurent bound.

*Proof.* The natural coefficient description is

```math
\mathcal{O}/2^M\mathcal{O}
       =(\mathbb{Z}/2^M\mathbb{Z})((t)).
```

Indeed, if $`s\notin(2)`$, write $`s=t^dv+2w`$ with $`v\in\Lambda^\times`$; the finite geometric expansion of $`s^{-1}`$ modulo $`2^M`$ is a Laurent series with finite negative support. Conversely every such series is obtained by inverting $`t`$.

Write $`\det A_j=t^{d_j}v_j+2w_j`$, with $`d_j\le h`$ and $`v_j\in\Lambda^\times`$, and set

```math
C_j=\frac{\mathrm{adj}(A_j)}{t^{d_j}v_j},\qquad
 C=\mathrm{diag}(C_j).
```

The entries of $`C`$ have pole at most $`h`$, and $`BC=1+2F`$, where the entries of $`F`$ have the same bound. Thus

```math
B^{-1}\equiv C\sum_{j=0}^{M-1}(-2F)^j\pmod{2^M}.
```

The $`j`$th summand has pole at most $`(j+1)h`$. Matrix addition and multiplication by power-series matrices cannot worsen the asserted bound, regardless of the number of blocks.

The group ring $`\mathcal{O}[G]`$ is local. The residual determinant of the universal $`B`$ equals $`\prod_j\det\overline A_j`$, which is nonzero in $`\mathbb{F}_2((t))`$, so $`B`$ is invertible. A sign character sends the augmentation ideal to $`2\Lambda`$. Consequently $`B_x=A+2E_x`$ with power-series $`E_x`$. The usual contractible-pair elimination leaves the Schur differential $`D-UB^{-1}S`$. Its augmentation is $`d_{\mathrm{old}}`$ because $`S_0=0`$. The preceding calculation gives the uniform bound at every sign character.

For the ring-class complexes of $`E`$ with full rational $`2`$‑torsion, the augmentation block at a split conductor prime has residual Frobenius scalar $`z=(1+t)^a`$ with $`a`$ odd. At each of the two split places its singular determinant has residual $`t`$‑order two; hence one may take $`h=4`$ for the combined block. This proves the uniform elimination assertion in the group-ring construction of OpenAI (2026) while retaining the actual localization triangle.

**Lemma D.21 (Primitive correction).** There is a multiplier $`\eta\in\mathcal{O}[G]`$ such that the character coordinates of $`\eta u_{\mathrm{rel}}`$ are the primitive coordinates $`u_{h_x}`$, up to $`\Lambda`$‑units. This correction has no denominator depending on the number of conductor primes.

*Proof.* At an unused split prime $`q`$, let $`z`$ be the full scalar Frobenius at one orientation; the other has $`z^{-1}`$. The point norm and the singular local determinant are

```math
e_q=a_q-z-z^{-1},\qquad
 l_q=\det(1-q^{-1}z\mathrm{Fr}_q\vert T)
             \det(1-q^{-1}z^{-1}\mathrm{Fr}_q\vert T).
```

Conductor norms commute with direct descent and weighted transfer, so $`e_q`$ multiplies the actual class. It is symmetric under conjugation and therefore multiplies its actual paired functional as well. The localization triangle gives

```math
u_{\mathrm{rel}}=e_q^2u_{\mathrm{prim}}/l_q.
```

Both $`e_q`$ and $`l_q`$ are units in $`\mathcal{O}[G]`$: modulo its maximal ideal the scalar is $`(1+t)^a`$ with $`a`$ odd. Before character evaluation, their reductions satisfy

```math
(1+a_qz+z^2)(1+a_qz^{-1}+z^{-2})
       =a_q^2+z^2+z^{-2}=(a_q+z+z^{-1})^2.
```

Hence $`l_q/e_q^2-1\in2\mathcal{O}[G]`$. If $`g_q\in G`$ is the inertia bit, so $`g_q(x)=(-1)^{\lambda_q(x)}`$, then

```math
\eta=\prod_{q\in Q}
       \left(1+\frac{l_q/e_q^2-1}{2}(1+g_q)\right)
          \in\mathcal{O}[G].
```

Its $`q`$‑factor equals $`l_q/e_q^2`$ at an unused character and $`1`$ at an active character. Primitive central values are compared through the primitive point and its Selmer complex in Proposition D.18; no evaluation of an arbitrary element of $`\mathcal{O}`$ at $`t=0`$ is used.

**Lemma D.22 (Clearing a bounded complex).** Let $`D`$ be a based finite free $`\mathcal{O}[G]`$‑complex of total rank at most $`r_0`$, with augmentation $`D_0`$ defined over $`\Lambda`$. Suppose its central integral complex has rational dimensions one in degrees one and two, zero elsewhere, and total torsion length at most $`h_1`$. Let $`z`$ be an integral cycle and let $`\lambda\in2^{-a_0}(D^2)^*`$ be closed. Assume each character constituent is generically acyclic or has the rank-one pattern. An arbitrary multiplier $`\eta\in\mathcal{O}[G]`$ is allowed in its determinant coordinates. There are $`f,d\in\mathcal{O}[G]`$ with

```math
f_xu_x=d_x,\qquad f_0\in\Lambda,\qquad
 v_2(f_0(0))\leq C(r_0,h_1,a_0)\lt \infty.
```

If the character evaluations of the differential have uniformly bounded negative Laurent support modulo each $`2^M`$, the same holds for $`f_x`$.

*Proof.* Put the central integral complex in elementary-divisor bases over $`\mathbb{Z}_2`$ and lift those constant integral basis changes. Its positive pivot valuations sum to at most $`h_1`$. Formally cancel the same pivot positions upstairs, recording numerators and denominators in the rational basis changes and determinant comparison. There are at most $`r_0`$ operations. A product $`P`$ of bounded powers of pivot numerators clears all denominators. It is a polynomial of bounded degree in the differential entries, its augmentation belongs to $`\Lambda`$, and $`v_2(P_0(0))`$ is bounded in terms of $`r_0,h_1`$.

Where $`P_x\ne0`$, the remaining complex is one-by-one in degrees one and two. A nonzero differential forces the projected cycle to vanish, giving the stipulated zero coordinate. Otherwise the coordinate is the product of the projected class and functional with the canceled-pivot determinant factor. Thus

```math
u_x=2^{-a_0}\eta_xQ_x/P_x,\qquad Q\in\mathcal{O}[G].
```

Take $`f=2^{a_0}P^2`$ and $`d=\eta P Q`$. The equality holds also where $`P_x=0`$, since both sides are then zero. The central valuation and Laurent assertions follow because $`f`$ is a bounded-degree polynomial in the differential entries. No Laurent bound is required for $`z,\lambda,\eta`$, or $`d`$.

**Proposition D.23 (Uniform family clearing).** Under the hypotheses of Theorem D.2, the corrected universal coordinates satisfy Lemma D.22, with common central-valuation and fixed-precision negative Laurent bounds independent of $`b`$ and $`\#Q`$.

*Proof.* At augmentation the actual localization triangle has old complex equal to the base complex with only the auxiliary prime relaxed, and quotient the sum of singular complexes at the new split primes. Choose a finite free cone model for this triangle. Lemma D.19 lifts its graded filtration to the actual universal complex. Lemma D.20, with $`h=4`$, eliminates all new blocks at once. The remaining core has the bounded old size, its augmentation equals the old complex, and its sign constituents have uniform Laurent bounds. Its class and functional have the fixed clearing exponent of Lemma D.11.

The old central rational dimensions are one by the base Selmer corank. The quotient of the fixed base discrete Selmer group by its maximal divisible subgroup is finite, since its Pontryagin dual is finitely generated over $`\mathbb{Z}_2`$. Lemma D.16 bounds degree-two torsion by this fixed length; the scalar torsion bound handles the other degrees. The auxiliary terms are bounded by Lemma D.3. Thus total central torsion has a bound independent of the family, without finite base Shafarevich–Tate group.

Nonzero vertices have generic rank one by the simple-zero theorem; the zero vertex has rank at most one by Selmer corank. Generic invariants vanish, duality pairs degrees one and two, and unused local blocks are generically acyclic. The hypotheses of Lemma D.22 therefore hold. The determinant of the eliminated block is an $`\mathcal{O}[G]`$‑unit. Put its inverse and the correction $`\eta`$ from Lemma D.21 in the permitted numerator multiplier; neither enters $`f`$. The clearing lemma now proves both uniform bounds.

### D.8. Coefficient comparison and the missing vertex

**Lemma D.24 (Binary coefficient tests).** For $`q`$ specified Laurent coefficients of sign evaluations of elements of $`\mathcal{O}[G]`$, and $`M\geq1`$, there is a nonzero address agreeing with zero modulo $`2^M`$ on all tests whenever

```math
b\gt q(2^M-1).
```

*Proof.* Coefficient extraction gives $`q`$ elements of $`\mathbb{Z}_2[G]`$; it commutes with sign evaluation because $`G`$ is finite. For one of these elements the value function has a Boolean expansion

```math
a_\emptyset+\sum_{\emptyset\ne I\subseteq\{1,\ldots,b\}}
                 2^{\vert I\vert }a_I\prod_{i\in I}x_i,
       \qquad a_I\in\mathbb{Z}_2,
```

obtained by expanding products of $`1-2x_i`$. Its $`j`$th binary digit is a Boolean polynomial of degree at most $`2^j`$. Indeed, the digit is the coefficient of $`Y^{2^j}`$ in $`(1+Y)^a`$ modulo $`2`$; a monomial $`x_I`$ contributes the factor $`1+x_I((1+Y)^{2^{\vert I\vert }a_I}-1)`$. Its nonconstant terms start in $`Y`$‑degree $`2^{\vert I\vert }`$, and $`\vert I\vert \leq2^{\vert I\vert }`$. Thus all digit equalities for the $`q`$ tests have total degree at most $`q(2^M-1)`$. Their common-zero indicator is the product of $`1+`$ each equality polynomial. A Boolean polynomial of degree less than $`b`$ has even sum over $`\mathbb{F}_2^b`$, since every monomial omits a variable. Hence the number of common zeros is even. Zero is one, so another exists. This is the binary Chevalley–Warning argument used in OpenAI (2026).

**Lemma D.25 (Transfer through a bounded factor).** Suppose $`f,d\in\mathcal{O}[G]`$, $`u_x\in\Lambda[1/2]`$, and $`f_xu_x=d_x`$ for every character. Suppose $`f_0\in\Lambda`$ and $`c=v_2(f_0(0))\lt \infty`$. If every $`f_x`$ modulo $`2^M`$ has no powers below $`-L(M)`$, then for

```math
M\gt c,\qquad b\gt (L(M)+2)(2^M-1)
```

there is $`x\ne0`$ with

```math
v_2(u_x(0)-u_0(0))\geq M-2c.
```

*Proof.* Apply Lemma D.24 to the coefficients of $`f_x`$ in degrees $`-L(M),\ldots,0`$ and to the constant coefficient of $`d_x`$. At the resulting nonzero address all negative coefficients of $`f_x`$ are divisible by $`2^M`$, while its constant coefficient is congruent to $`f_0(0)`$ and has valuation $`c`$. Consequently $`v_{\mathcal{O}}(f_x)\leq c`$. Since $`d_x`$ is integral, $`v_{\mathcal{O}}(u_x)\geq-c`$, and the same holds for $`u_0`$. Their power-series coefficients therefore belong to $`2^{-c}\mathbb{Z}_2`$. They have no negative powers because they lie in $`\Lambda[1/2]`$.

The Laurent expansion of an element of $`\mathcal{O}`$ has coefficients tending $`2`$‑adically to zero in negative degrees, so the constant-term convolution converges and gives

```math
[t^0]d_x\equiv[t^0]f_x\,u_x(0)\pmod{2^{M-c}},\qquad
 [t^0]d_0=f_0(0)u_0(0).
```

Use the chosen coefficient congruences and divide by $`f_0(0)`$. This gives the claimed precision. Only one coefficient of $`d`$ was tested; its negative support need not be bounded.

*Proof of Theorem D.2.* The universal family is constructed before character evaluation, with the actual integral class and functional. Its primitive constituents belong to $`\Lambda[1/2]`$ by Propositions D.15 and D.18, and Lemma D.21 identifies them with the corrected universal coordinates, up to $`\Lambda`$‑units. The assumed nonzero-vertex bound and Proposition D.18 give

```math
v_2(u_x(0))\leq B_1\qquad(x\ne0)
```

for one constant depending only on the fixed data and $`B`$.

If the derivative of $`L(E,s)L(E^{(k)},s)`$ at one vanished, the Gross–Zagier formula for the conductor-one primitive Heegner sum would give height zero, hence a torsion point Gross and Zagier (1986). Proposition D.18 then gives $`u_0(0)=0`$, using only the base Selmer corank. By Proposition D.23 the clearing factors have a common bound $`c_*`$ for $`v_2(f_0(0))`$ and common bounds $`L(M)`$. Choose

```math
M\gt \max\{c_*,B_1+2c_*\}
```

and then a family whose dimension exceeds the threshold in Lemma D.25. It supplies a nonzero vertex with $`v_2(u_x(0))\geq M-2c_*\gt B_1`$, a contradiction. Thus the derivative is nonzero. The split Heegner functional-equation sign is negative, so the product has a simple zero.

---

[← Appendix D, sections D.1–D.4](appendix-d.md) · [Main article](README.md) · [Appendix E →](appendix-e.md)
