# Reconstructed proof chain

The following blocks formalize the supplied continuous proof. All estimates are asserted with their quantifiers and their proof blocks record the exact interfaces used by the argument.


## Definition 1: Admissible simple polygon {#def-admissible-polygon}

An admissible polygon is a bounded simple planar polygonal domain whose boundary is a simple cyclic union of finitely many nonzero straight segments, with no self-contact. A genuine corner is a boundary vertex at which the two incident directed segments are not collinear; its interior angle is required to lie strictly between $0$ and $2\pi$. Starting from any polygonal presentation, delete adjacent collinear redundant vertices cyclically until no such vertex remains; the resulting effective-edge count is the invariant number $N$, and $A(P)$ is the Euclidean area. The cyclic deletion is independent of deletion order because it removes exactly the vertices at which the incoming and outgoing segment directions agree.



## Definition 2: Area-eigenvalue functional {#def-j-functional}

For an admissible polygon $P$ in [Definition 1](#def-admissible-polygon), let $\lambda_1(P)$ be the first Dirichlet eigenvalue of $-\Delta$ on the bounded nondegenerate polygonal domain $P$ and define
$$
J(P)=A(P)\lambda_1(P),\qquad
m_k=\inf\{J(Q):Q\text{ is admissible and has at most }k\text{ effective edges}\}.
$$
Here $k\ge3$ is an integer, and $R_k$ denotes the unit-area regular $k$-gon (its position is irrelevant because $J$ is similarity invariant). The first eigenvalue is defined by the Dirichlet Rayleigh quotient on $H_0^1(P)$.



## Definition 3: Vertex stationary polygon {#def-stationary-polygon}

An admissible polygon in [Definition 1](#def-admissible-polygon), with $J$ as defined in [Definition 2](#def-j-functional), is stationary when, in a differentiable local chart of its effective vertex coordinates, $DJ(P)[V]=0$ for every vertex variation $V$. On the same chart this is equivalent to $D\lambda_1(P)[V]=0$ for every variation with $DA(P)[V]=0$: the forward implication follows from $DJ=A\,D\lambda_1+\lambda_1\,DA$, and the converse follows by applying the scaling identities $D\lambda_1[X]=-2\lambda_1$ and $DA[X]=2A$ to the radial variation and then using the Lagrange-multiplier decomposition.



## Definition 4: Normalized conformal data {#def-conformal-data}

For a polygon $P$ in [Definition 1](#def-admissible-polygon), let $r_P$ be its maximal conformal radius and choose a Riemann map $F:\mathbb D\to P$ centered at a maximizing point, with $F'(0)=r_P>0$ and $F''(0)=0$. The equality $F''(0)=0$ is the first-order condition for the maximum of $(1-|a|^2)|F'(a)|$. Replace $P$ by the similarity-normalized polygon $\widetilde P=r_P^{-1}(P-F(0))$ and write $\widetilde F=r_P^{-1}(F-F(0))$; by the similarity invariance of $J$ in [Definition 2](#def-j-functional), this leaves $J$ and the effective-edge count unchanged and gives $\widetilde F'(0)=1$. In the normalized notation,
$$
\widetilde F'(z)=1+g(z),\qquad g(z)=\sum_{n\ge2}g_nz^n.
$$
Set
$$
S=\|g\|_{A^2}^2=\sum_{n\ge2}\frac{|g_n|^2}{n+1},\qquad
T=\|(\widetilde F')^{-1}-1\|_{A^2}^2,\qquad \|h\|_{A^2}^2=\pi^{-1}\int_{\mathbb D}|h|^2dA.
$$
The area identity is $A(\widetilde P)=\pi(1+S)$; all later uses of $P,F,A,\lambda_1$ are understood in this similarity-normalized representative. Write $k=(\widetilde F')^{-1}-1$, so $T=\|k\|_{A^2}^2$ and $g+k=-gk$. The inverse derivative is in $A^2$: at a prevertex with interior angle $\omega\in(0,2\pi)$, the Schwarz--Christoffel exponent is $\alpha=\omega/\pi-1<1$, so $|(\widetilde F')^{-1}|^2=O(r^{-2\alpha})$ and its area integral is bounded by $C\int_0^\varepsilon r^{1-2\alpha}\,dr<\infty$.



## Definition 5: Signed Schwarz-Christoffel turn measure {#def-turn-measure}

At the prevertices $e^{i\theta_i}$ of an admissible polygon in [Definition 1](#def-admissible-polygon), with normalized conformal map from [Definition 4](#def-conformal-data), put
$$
w_i=\frac{\pi-\omega_i}{2\pi},\qquad
\mu=\sum_iw_i\delta_{\theta_i},\qquad \widehat\mu(n)=\int e^{-in\theta}d\mu(\theta).
$$
Then $\sum_iw_i=1$ and $\widehat\mu(1)=0$ in the chosen $F''(0)=0$ normalization. The Schwarz--Christoffel derivative has logarithm
$$
L(z)=\log F'(z)=2\sum_{n\ge1}\frac{\widehat\mu(n)}n z^n,
$$
so $L_n=2\widehat\mu(n)/n$. This definition applies to finite real atomic measures induced by such polygons; all Fourier series below are interpreted in that class.



## Definition 6: Positive comparison kernel {#def-positive-kernel}

Let $j=j_{0,1}$ be the first positive zero of the Bessel function $J_0$, let $\kappa=j^2/2-1>0$, and define for $n\ge1$
$$
b_n=\frac1{n(n^2+\kappa)},\qquad
E_b(\mu)=\sum_{n\ge1}b_n|\widehat\mu(n)|^2,
$$
for a finite real atomic measure $\mu$ of total mass $1$ as in [Definition 5](#def-turn-measure). For every positive integer $p$, set
$$
B_p=\sum_{\ell\ge1}\frac1{\ell p((\ell p)^2+\kappa)}.
$$
The series defining $E_b$ and $B_p$ converge absolutely because $b_n=O(n^{-3})$ and finite atomic measures have bounded Fourier coefficients.



## Lemma 1: Stationary edge moments {#lem-edge-moments}

Let $P$ be admissible and stationary in the sense of [Definition 3](#def-stationary-polygon). If $u>0$ is the $L^2$-normalized first eigenfunction, $\lambda=\lambda_1(P)$, $c=\lambda/A(P)$, and $q=|\partial_\nu u|^2$, then every effective edge $E$, parametrized by physical arclength $s\in[0,\ell_E]$, satisfies
$$
\int_E(q-c)\,ds=0,\qquad \int_Es(q-c)\,ds=0.
$$



### Proof of Lemma 1 {#proof-lem-edge-moments}

By [Definition 3](#def-stationary-polygon), the derivative of $J=A\lambda$ vanishes for every vertex displacement. Hadamard's formula is
$$
DJ[V]=A\int_{\partial P}(c-q)V\cdot\nu\,ds.
$$
Moving one endpoint of an effective edge while keeping the other fixed produces an affine normal velocity on that edge, and the two endpoint velocities give the independent functions $1$ and $s/\ell_E$. Since adjacent effective edge normals are linearly independent at a genuine corner, stationarity forces both coefficients of these two affine test functions to vanish. Rescaling $s/\ell_E$ gives the displayed moments.



## Lemma 2: Airy fourth-power identity {#lem-airy-identity}

Let $P$ be an admissible polygon whose boundary segments are all effective edges, and assume the edge moments in [Lemma 1](#lem-edge-moments). Then its first eigenfunction satisfies
$$
\int_P|\nabla u|^4=\lambda^2\left(\int_Pu^4-A(P)^{-1}\right).
$$



### Proof of Lemma 2 {#proof-lem-airy-identity}

Define the divergence-free stress tensor
$$
T=\nabla u\otimes\nabla u-\tfrac12(|\nabla u|^2-\lambda u^2)I.
$$
An Airy potential $\psi$ with $D^2\psi=R^TTR$ exists locally and, after setting $\Phi=\psi-c|x|^2/4$, satisfies
$$
D^2\Phi=\tfrac12(|\nabla u|^2+\lambda u^2-c)I-\nabla u\otimes\nabla u.
$$
Every boundary segment is effective by [Definition 1](#def-admissible-polygon), so the identities in [Lemma 1](#lem-edge-moments) apply on each segment. The planar Airy-potential theorem for a symmetric divergence-free stress on the simply connected polygon supplies one global $\psi$, unique up to an affine function. The two moments imply that $\nabla\Phi$ has the same endpoint values on each segment. Propagating around the boundary and subtracting an affine function makes $\Phi=0$ at every vertex and $\partial_\nu\Phi=0$ on every segment; the mixed Hessian term vanishes there as well. At a corner of angle $\omega<2\pi$, the leading Dirichlet mode is $r^\alpha\sin(\alpha\theta)$ with $\alpha=\pi/\omega>1/2$, hence $|\nabla u|=O(r^{\alpha-1})$, $|\nabla\Phi|=O(r^{2\alpha-1}+r)$, and $|D^2\Phi|=O(r^{2\alpha-2}+1)$. These estimates make the circular boundary flux $O(\varepsilon^{4\alpha-2}+\varepsilon^{2\alpha})\to0$.

Apply the divergence identity
$$
\operatorname{div}\{\Delta\Phi\nabla\Phi-D^2\Phi\nabla\Phi\}=(\Delta\Phi)^2-|D^2\Phi|^2
$$
to $P$ with corner disks removed and let $\varepsilon\downarrow0$. The edge terms vanish by the preceding boundary conditions, hence $\int_P\det D^2\Phi=0$. The eigenvalues of $D^2\Phi$ are $(\lambda u^2-c\pm|\nabla u|^2)/2$, so expanding their product and using $\int_Pu^2=1$ gives the stated identity.



## Lemma 3: Uniform W1,4 bound {#lem-uniform-w14}

For every fixed area $A_0>0$ and eigenvalue bound $\Lambda<\infty$, there is $C=C(A_0,\Lambda)$ such that every admissible stationary polygon whose canonical boundary presentation consists entirely of effective edges, satisfying the edge-moment hypotheses of [Lemma 1](#lem-edge-moments), with $A(P)=A_0$ and $\lambda_1(P)\le\Lambda$, has its zero extension $\bar u$ of the $L^2(P)$-normalized positive first Dirichlet eigenfunction uniformly bounded in $W^{1,4}(\mathbb R^2)$ and hence in $C^{0,1/2}(\mathbb R^2)$.



### Proof of Lemma 3 {#proof-lem-uniform-w14}

The domain-independent Dirichlet heat-kernel estimate gives $\|u\|_\infty^2\le e^2\lambda/(8\pi)$ for the normalized first eigenfunction. Under the edge-moment hypotheses, [Lemma 2](#lem-airy-identity) applies, and $\int_Pu^4\le\|u\|_\infty^2\int_Pu^2=\|u\|_\infty^2$; combining these facts yields
$$
\int_P|\nabla u|^4\le \frac{e^2\lambda^3}{8\pi}.
$$
The same $L^\infty$ bound gives $\int_P|u|^4\le\|u\|_\infty^2$, so the $W^{1,4}(P)$ norm is bounded by a constant depending only on $A_0$ and $\Lambda$. Since $u\in H^1_0(P)$, its zero extension has no boundary distribution term in its weak gradient; the extension therefore lies in $W^{1,4}(\mathbb R^2)$ with the same gradient bound. Morrey's inequality in dimension two then gives a $C^{0,1/2}$ representative with the same parameter dependence.



## Lemma 4: Uniform C1 conformal perturbation {#lem-c1-perturbation}

Let
$$
X=\{\phi\in C^1(\overline{\mathbb D};\mathbb R):\phi|_{\partial\mathbb D}=0\},
\qquad \|\phi\|_X=\|\nabla\phi\|_{L^\infty}.
$$
For normalized conformal data from [Definition 4](#def-conformal-data) with $S=\|g\|_{A^2}^2$ sufficiently small, writing $g=t h$ with $t=\sqrt S$ and $\|h\|_{A^2}=1$, the pulled-back first eigenfunction has a uniform real-analytic expansion
$$
v=v_0+t v_1+v^{(2)}+R,
\qquad \|v_1\|_X\le C,
\qquad \|v^{(2)}\|_X\le CS,
\qquad \|R\|_X\le CS^{3/2},
$$
where $v_0(r)=J_0(jr)/(\sqrt\pi J_1(j))$, $v_1$ has no radial Fourier mode, and the corresponding eigenvalue branch is the positive first branch. More precisely, with $g=th$,
$$
(-\Delta-j^2)v_1=2j^2\operatorname{Re}(h)v_0\quad\text{in }\mathbb D,
\qquad v_1|_{\partial\mathbb D}=0.
$$
If $h(z)=\sum_{n\ge2}h_nz^n$, then
$$
v_1(r,\theta)=\sum_{n\ge2}w_n(r)\operatorname{Re}(h_ne^{in\theta}),
\quad
w_n(r)=\frac{r^{n+1}v_0'(r)+p_DJ_n(jr)/J_n(j)}{n+1},
$$
where $p_D=j/\sqrt\pi$ and $w_n'(1)=-p_D\rho_n/(n+1)$ with $\rho_n=jJ_{n+1}(j)/J_n(j)$.
The same branch has a real-analytic eigenvalue expansion
$$
\lambda(g)=j^2+\lambda^{(1)}(g)+\lambda^{(2)}(g)+O(\|g\|_{A^2}^3),
$$
where $\lambda^{(r)}$ is homogeneous of degree $r$.



### Proof of Lemma 4 {#proof-lem-c1-perturbation}

By [Definition 4](#def-conformal-data), $g$ is analytic, has no constant or linear coefficient, and satisfies $S=\|g\|_{A^2}^2$; its normalized conformal pullback is the weighted disk problem used below. Put $d(z)=1-|z|$. The Green kernel of the disk satisfies
$$
|\nabla_xG_D(x,z)|\le C|x-z|^{-1},
\qquad
|\nabla_xG_D(x,z)|\le C\frac{d(z)}{|x-z|^2}.
$$
The Bergman pointwise estimate gives $|g(z)|\le C\|g\|_{A^2}/d(z)$ for $g\in A^2$ with vanishing constant coefficient. If $h\in X$, then $|h(z)|\le d(z)\|h\|_X$. Splitting the Green integral into $|x-z|<d(x)/2$, the annulus $d(x)/2\le|x-z|<2d(x)$, and dyadic outer annuli, the two kernel bounds give
$$
\|G_D(gh)\|_X\le C\|g\|_{A^2}\|h\|_X,
\qquad
\|G_D(g_1\overline{g_2}h)\|_X\le C\|g_1\|_{A^2}\|g_2\|_{A^2}\|h\|_X.
$$
For example, in the near region $d(z)\simeq d(x)$ and the pointwise bounds leave an integrable $|x-z|^{-1}$ kernel; in the outer annuli $d(z)\le d(x)+|x-z|$ cancels one power of the second Green bound, and Cauchy--Schwarz gives $\|g_1g_2\|_{L^1}\le C\|g_1\|_{A^2}\|g_2\|_{A^2}$. Polynomial approximation extends these estimates to all $A^2$ data, and the Green potential has a continuous boundary derivative.

Define the real quadratic compact-operator family
$$
K_g h=G_D[|1+g|^2h]=G_D[h+2\operatorname{Re}(g)h+|g|^2h]
$$
onlinearly in $g$. The estimates give $\|K_g-K_0\|_{B(X)}\le C(\sqrt S+S)$. The operator $K_0$ is compact on $X$ by disk Poisson regularity and the compact embedding $C^{2,\alpha}(\overline{\mathbb D})\Subset C^1(\overline{\mathbb D})$. Its nonzero eigenvalues are the reciprocals of the Dirichlet eigenvalues; $1/j^2$ is an isolated simple eigenvalue.

Choose a fixed small contour $\Gamma$ enclosing only $1/j^2$. For $S$ small, the Neumann series uniformly bounds $(zI-K_g)^{-1}$ on $\Gamma$ and defines the rank-one Riesz projection
$$
\Pi_g=\frac1{2\pi i}\int_\Gamma(zI-K_g)^{-1}\,dz.
$$
The normalized vector
$$
\widetilde v(g)=\Pi_gv_0,
\qquad
v(g)=\frac{\widetilde v(g)}{\left(\int_{\mathbb D}\widetilde v(g)^2|1+g|^2\right)^{1/2}}
$$
therefore depends real-analytically on $g$ in a fixed $A^2$ neighborhood; the denominator stays uniformly away from zero. Writing $g=t h$, define $v_1=Dv(0)[h]$. Differentiating
$$
-\Delta v=\lambda|1+th|^2v,
\qquad \int_{\mathbb D}v^2|1+th|^2dA=1
$$
at $t=0$ gives
$$
(-\Delta-j^2)v_1=2j^2\operatorname{Re}(h)v_0+\lambda'(0)v_0,
\qquad
\lambda'(0)=-2j^2\int_{\mathbb D}\operatorname{Re}(h)v_0^2dA=0.
$$
The last equality uses that $v_0$ is radial and $h$ has no constant coefficient. Separating variables and imposing the zero boundary value yields
$$
v_1(r,\theta)=\sum_{n\ge2}w_n(r)\operatorname{Re}(h_ne^{in\theta}),
\qquad
w_n(r)=\frac{r^{n+1}v_0'(r)+p_DJ_n(jr)/J_n(j)}{n+1}.
$$
The Bessel recurrence gives $w_n'(1)=-p_D\rho_n/(n+1)$. The remaining Taylor terms give $v^{(2)}+R$, and Cauchy estimates on this fixed neighborhood give the displayed bounds; the same estimate applied to the isolated eigenvalue gives the displayed eigenvalue expansion, with constants independent of the direction of $g$.

The form identity
$$
\int_{\mathbb D}|g|^2|\phi|^2\,dA
\le C\|g\|_{A^2}^2\int_{\mathbb D}|\nabla\phi|^2\,dA,
\qquad \phi\in H^1_0(\mathbb D),
$$
which follows from Hardy's inequality, shows that the pulled-back eigenfunction belongs to the weighted Dirichlet space. The positive solution is the principal branch by the variational characterization of the weighted Dirichlet eigenvalue. Since $v_0(r)\ge c(1-r)$ and $\|v-v_0\|_X\le C\sqrt S$, the branch is strictly positive in $\mathbb D$. This proves the lemma.



## Lemma 5: Uniform disk perturbation expansion {#lem-disk-perturbation}

There are universal constants $S_0,C>0$ such that, for normalized conformal data from [Definition 4](#def-conformal-data) with $S\le S_0$, if $v$ is the positive first solution of
$$
-\Delta v=\lambda|1+g|^2v\quad\text{in }\mathbb D,qquad v|_{\partial\mathbb D}=0,qquad \int_{\mathbb D}v^2|1+g|^2=1,
$$
then, with $J$ as in [Definition 2](#def-j-functional),
$$
\frac{J(P)}{\pi j^2}=1+S-\sum_{n\ge2}\frac{\rho_n}{(n+1)^2}|g_n|^2+R(g),qquad |R(g)|\le CS^{3/2},
$$
where $j=j_{0,1}$ is the first positive zero of $J_0$, $\rho_n=jJ_{n+1}(j)/J_n(j)$, and $0<\rho_n<2$. In particular,
$$
\frac{J(P)}{\pi j^2}-1\ge S/6.
$$
Moreover, writing $g=t h$ with $t=\sqrt S$ and $\|h\|_{A^2}=1$, the corresponding normalized eigenpair satisfies
$$
\|v-v_0\|_{H^1_0(\mathbb D)}\le Ct,
\qquad |\lambda-j^2|\le Ct^2.
$$



### Proof of Lemma 5 {#proof-lem-disk-perturbation}

By [Definition 2](#def-j-functional), $J(P)=A(P)\lambda_1(P)$; after [Definition 4](#def-conformal-data) normalizes $A(P)=\pi(1+S)$, it remains to expand $\lambda_1(P)$. The fixed-space expansion in [Lemma 4](#lem-c1-perturbation) supplies the uniform eigenpair branch and remainder. For the quantitative rate, write the pulled-back eigenproblem as
$$
-\Delta v=\lambda|1+g|^2v,\qquad v|_{\partial\mathbb D}=0,
$$
with the weighted $L^2$ normalization. Put $d(z)=1-|z|$. For $g\in A^2$ with no constant or linear term, the Bergman pointwise estimate gives $|g(z)|\le C\|g\|_{A^2}/d(z)$. Consequently, Hardy's inequality gives, for all $\varphi,\psi\in H^1_0(\mathbb D)$,
$$
\left|\int_{\mathbb D}2\operatorname{Re}(g)\varphi\psi\right|\le C\sqrt S\,\|\varphi\|_{H^1_0}\|\psi\|_{H^1_0},\qquad
\left|\int_{\mathbb D}|g|^2\varphi\psi\right|\le CS\,\|\varphi\|_{H^1_0}\|\psi\|_{H^1_0}.
$$
Indeed $|g|^2\le CS/d^2$, $\int|\varphi|^2/d^2\le4\int|\nabla\varphi|^2$, and Cauchy--Schwarz handles the first integral. Therefore the closed forms
$$
q_t[\varphi]=\int|\nabla\varphi|^2,\qquad m_t[\varphi]=\int|1+t h|^2|\varphi|^2\quad(g=th)
$$
form a real-analytic type-(a) family on the fixed domain $H^1_0(\mathbb D)$ for real $|t|$ small (equivalently, a holomorphic two-parameter family in $(t,\bar t)$), with uniform form bounds. The simple disk eigenvalue is isolated by a fixed spectral gap, so the real-analytic form perturbation theorem applies uniformly to this family.

Write $g=t h$ with $t=\sqrt S$ and $\|h\|_{A^2}=1$. The simple disk eigenvalue is isolated by a fixed spectral gap. The form version of analytic simple-eigenvalue perturbation therefore gives, uniformly in such $h$,
$$
v=v_0+t v_1+t^2v_2+O_{H^1_0}(t^3),
\qquad
\lambda= j^2+t\lambda_1+t^2\lambda_2+O(t^3).
$$
The case $S=0$ is the disk and the assertion is immediate, so assume $S>0$. The first variation is $\lambda_1=-j^2\int_{\mathbb D}(h+\bar h)v_0^2=0$ because $v_0$ is radial and $h$ has no constant coefficient. Write $v_0(r)=J_0(jr)/(\sqrt\pi J_1(j))$ and $p_D=j/\sqrt\pi$. For the real mode $h=a z^n$, the first-order equation in the $n$th angular sector has the explicit solution
$$
v_1(r,\theta)=a w_n(r)\cos(n\theta),\qquad
w_n(r)=\frac{r^{n+1}v_0'(r)+p_DJ_n(jr)/J_n(j)}{n+1}.
$$
The Bessel equation verifies the radial equation and $w_n(1)=0$. The second-order solvability condition is
$$
\frac{\lambda_2}{j^2a^2}=-2\pi\int_0^1\left(r^{2n+1}v_0(r)^2+r^{n+1}v_0(r)w_n(r)\right)dr.
$$
Substitution of $w_n$ and one integration by parts reduce this to
$$
\frac{\lambda_2}{j^2a^2}=-\frac{\rho_n}{(n+1)^2},
\qquad \rho_n=j\frac{J_{n+1}(j)}{J_n(j)},\qquad 0<\rho_n<2.
$$
The only nontrivial radial integral is
$$
\int_0^1r^{n+1}v_0(r)J_n(jr)\,dr
=\frac{J_{n+1}(j)}{2\sqrt\pi(n+1)},
$$
which follows by one integration by parts from the Bessel equation. Orthogonality of distinct angular modes and density of analytic polynomials extend the formula to every $h\in A^2$. Since $A(P)=\pi(1+S)$ in [Definition 4](#def-conformal-data), this yields the uniform expansion
$$
\frac{J(P)}{\pi j^2}=1+S-\sum_{n\ge2}\frac{\rho_n}{(n+1)^2}|g_n|^2+O(S^{3/2}).
$$
The perturbed branch remains the first eigenvalue by the weighted min--max principle: the mass form $\int|1+g|^2|\varphi|^2$ is positive on nonzero $H^1_0$ functions, and the branch is the positive continuation of the disk ground state. The sine mode is obtained by a phase rotation, and polarization plus density of analytic polynomials extends the second-order form from real monomials to arbitrary complex $h\in A^2$. The Bessel interlacing inequalities $J_n(j)\ne0$ and $0<\rho_n<2$ hold for the first zero $j=j_{0,1}$. Thus
$$
\frac{\lambda}{j^2}=1-\sum_{n\ge2}\frac{\rho_n}{(n+1)^2}|g_n|^2+O(S^{3/2}).
$$
Multiplying by $A(P)/(\pi)=1+S$ from [Definition 4](#def-conformal-data) produces the displayed $J$ expansion; the cross term $S\sum\rho_n|g_n|^2/(n+1)^2$ is $O(S^2)$ and is absorbed in $O(S^{3/2})$. Since $0<\rho_n<2$ and $n+1\ge3$,
$$
\sum_{n\ge2}\frac{\rho_n}{(n+1)^2}|g_n|^2
\le2\sum_{n\ge2}\frac{|g_n|^2}{(n+1)^2}
\le\frac23\sum_{n\ge2}\frac{|g_n|^2}{n+1}=\frac23S.
$$
Therefore the quadratic part of the full expression is at least $S/3$; after shrinking the universal small neighborhood so that the $CS^{3/2}$ remainder is at most $S/6$, $J(P)/(\pi j^2)-1\ge S/6$. This proves the uniform perturbation expansion and coercivity.



## Lemma 6: Near-circle conformal deficit {#lem-near-circle-conformal}

For a sequence of admissible stationary $N$-gons in the sense of [Definition 3](#def-stationary-polygon) whose canonical boundary presentations consist entirely of effective edges, satisfying the edge moments of [Lemma 1](#lem-edge-moments) and with $J,R$ as in [Definition 2](#def-j-functional),
$$
J(P)\le J(R_{N-1}),
$$
with $N\to\infty$, the conformal data of [Definition 4](#def-conformal-data) satisfy $S\to0$ and, in fact, $S\le C N^{-3}$ with a universal $C$.



### Proof of Lemma 6 {#proof-lem-near-circle-conformal}

Use the similarity invariance in [Definition 2](#def-j-functional) to normalize $A(P)=\pi$ and translate so that the Fraenkel-optimal comparison disk is $D=B_1(0)$. The regular-polygon asymptotic is
$$
\frac{J(R_M)}{\pi j^2}=1+\frac{4\zeta(3)}{M^3}+O(M^{-5}).
$$
The upper bound and the displayed asymptotic give $\lambda_1(P)\le j^2(1+CN^{-3})$, while Faber--Krahn gives $\lambda_1(P)\ge j^2$. Quantitative Faber--Krahn therefore gives $|P\triangle D|\to0$. Let $u_N$ be the normalized positive eigenfunction and extend it by zero. By [Lemma 3](#lem-uniform-w14), the extensions are uniformly bounded in $W^{1,4}(\mathbb R^2)$ and hence equicontinuous and uniformly bounded. Arzelà--Ascoli gives a locally uniform limit along a subsequence. On every compact set outside $\overline D$, the limit must vanish: otherwise the uniform Hölder bound would force a fixed positive amount of area in $P_N\setminus D$, contradicting $|P_N\triangle D|\to0$. The same argument gives zero trace on $\partial D$. Since $\|u_N\|_\infty$ is uniformly bounded, the mass outside $D$ tends to zero; hence the limit has $L^2(D)$ norm one. Weak lower semicontinuity gives $\int_D|\nabla u|^2\le\liminf\lambda_1(P_N)=j^2$, while the disk Rayleigh inequality gives the reverse inequality. Thus the limit is the normalized positive disk eigenfunction $u_0$. Uniqueness of the limit upgrades the whole sequence to local uniform convergence, and the boundary Hölder bound upgrades it to uniform convergence on $\overline D$. Since $u_0>0$ on $B_{1-\eta}$, eventually $u_N>0$ there; because the zero extension vanishes off $P_N$, $B_{1-\eta}\subset P_N$.

The maximal conformal radius is at least $1-\eta$ by monotonicity under inclusion and at most $1$ by the conformal area inequality $A(P)\ge\pi r_P^2$. In the normalization of [Definition 4](#def-conformal-data), $1+S=r_P^{-2}\to1$.

By [Lemma 5](#lem-disk-perturbation), once $N$ is large enough that $S\le S_0$, the uniform expansion and coercivity give
$$
\frac{J(P)}{\pi j^2}-1\ge S/6.
$$
The regular-polygon upper bound is $O(N^{-3})$, hence $S\le CN^{-3}$ with a universal constant.



## Lemma 7: Gradient perturbation interface {#lem-gradient-perturbation}

For the normalized conformal data in [Definition 4](#def-conformal-data) in the regime of [Lemma 5](#lem-disk-perturbation), let $v$ be the positive weighted first eigenfunction and let $v_0(r)=J_0(jr)/(\sqrt\pi J_1(j))$. Writing $g=t h$ with $t=\sqrt S$ and $\|h\|_{A^2}=1$, there is a first-order response $v_1$ with no radial Fourier mode such that
$$
\|v-v_0-t v_1\|_{W^{1,4}(\mathbb D)}\le CS,
$$
and, with $b_1=4\,\nabla v_0\cdot\nabla v_1\,|\nabla v_0|^2$,
$$
\int_0^{2\pi}b_1(r,\theta)\,d\theta=0,
\qquad
\bigl\||\nabla v|^4-|\nabla v_0|^4-tb_1\bigr\|_{L^1(\mathbb D)}\le CS.
$$
Moreover, $\|b_1\|_{L^\infty(\mathbb D)}\le C$ and the remainder in this last display is bounded in $L^\infty(\mathbb D)$ by $CS$.
If $h(z)=\sum_{n\ge2}h_nz^n$, the response is diagonal:
$$
v_1(r,\theta)=\sum_{n\ge2}w_n(r)\operatorname{Re}(h_ne^{in\theta}),
\qquad
w_n(r)=\frac{r^{n+1}v_0'(r)+p_DJ_n(jr)/J_n(j)}{n+1},
$$
where $p_D=j/\sqrt\pi$ and $w_n'(1)=-p_D\rho_n/(n+1)$ with $\rho_n=jJ_{n+1}(j)/J_n(j)$.
In particular, if $M(h,k)=2\int_{\mathbb D}b_1(h)\operatorname{Re}k\,dA$, then
$$
M(h,k)=\sum_{n\ge2}m_n\operatorname{Re}(h_n\overline{k_n}),
\qquad |m_n|\le C(n+1)^{-3}.
$$
On the boundary, with $p=-\partial_rv|_{\partial\mathbb D}$,
$$
p(\theta)=p_D+p_D\sum_{n\ge2}\frac{\rho_n}{n+1}\operatorname{Re}(g_ne^{in\theta})+r_p(\theta),
\qquad \|r_p\|_{L^\infty}\le CS,
$$
and $|\rho_n|\le C/(n+1)$.
The constant is universal and independent of polygonal angles and vertex separation.



### Proof of Lemma 7 {#proof-lem-gradient-perturbation}

If $S=0$, then $g=0$ and the assertion is immediate. For $S>0$, [Lemma 4](#lem-c1-perturbation) and [Lemma 5](#lem-disk-perturbation) give the fixed-space expansion and the weighted equation
$$
-\Delta v=\lambda|1+th|^2v,
\qquad \int_{\mathbb D}v^2|1+th|^2dA=1.
$$
$$
v=v_0+t v_1+R_2,
\qquad \|v_1\|_X\le C,
\qquad \|R_2\|_X\le CS,
\qquad t=\sqrt S,
$$
where $R_2=v^{(2)}+R$.
with $v_1$ having no radial Fourier mode. Differentiating the weighted equation at $t=0$ gives
$$
-\Delta v_1-j^2v_1=2j^2\operatorname{Re}(h)v_0
$$
Here the first eigenvalue derivative is
$$
\lambda'(0)=-2j^2\int_{\mathbb D}\operatorname{Re}(h)v_0^2dA=0,
$$
because $v_0$ is radial and $h$ has no constant coefficient; the derivative of the normalization contributes no radial mode either. Imposing $v_1|_{\partial\mathbb D}=0$ gives the displayed Bessel solution $w_n$; the Bessel recurrence gives $w_n'(1)=-p_D\rho_n/(n+1)$. Since $X\hookrightarrow W^{1,4}(\mathbb D)$ for zero-boundary functions, the claimed $W^{1,4}$ estimate follows. Set $b_1=4\,\nabla v_0\cdot\nabla v_1\,|\nabla v_0|^2$; angular orthogonality gives its zero circular mean. The pointwise inequality
$$
\bigl||x+y|^4-|x|^4-4|x|^2x\cdot y\bigr|\le C(|x|^2|y|^2+|y|^4)
$$
with $x=\nabla v_0$ and $y=t\nabla v_1+\nabla R_2$ gives the stated remainder after separately bounding the omitted linear term $4|\nabla v_0|^2\nabla v_0\cdot\nabla R_2$ by $CS$ and using the $X$ bounds for the quadratic terms.
Because $\nabla v_0$ and $\nabla v_1$ are bounded and $\|\nabla R_2\|_{L^\infty}\le CS$, the same pointwise inequality gives the $L^\infty$ remainder bound in the statement; the definition of $b_1$ gives $\|b_1\|_{L^\infty}\le C$.
Finally angular orthogonality gives
$$
2\int_{\mathbb D}b_1(h)\operatorname{Re}k\,dA
=\sum_{n\ge2}m_n\operatorname{Re}(h_n\overline{k_n}),
\qquad
m_n=8\pi\int_0^1v_0'(r)^3w_n'(r)r^{n+1}\,dr.
$$
Writing $J_n(jr)/(r^nJ_n(j))$ as its Bessel power series, the denominator is at least $1-j^2/[4(n+1)]>1/2$ for $n\ge2$, and its derivative is $O((n+1)^{-1})$. Together with $w_n'(1)=O((n+1)^{-1})$ and $A_0'(1)=0$ for $A_0(r)=rv_0'(r)/p_D$, one obtains $|w_n'(r)|\le Cr^{n-1}((1-r)^2+(1-r)/(n+1)+(n+1)^{-2})$. Integrating the three Beta functions gives $|m_n|\le C(n+1)^{-3}$.
Evaluating the expansion at the boundary also gives
$$
p(\theta)=p_D+p_D\sum_{n\ge2}\frac{\rho_n}{n+1}\operatorname{Re}(g_ne^{in\theta})+r_p(\theta),
\qquad \|r_p\|_{L^\infty}\le CS,
$$
and the same Bessel series gives $|\rho_n|\le C/(n+1)$.



## Lemma 8: Weighted eigenenergy balance {#lem-weighted-eigen-balance}

For normalized conformal data in [Definition 4](#def-conformal-data) with $S$ sufficiently small, let $v$ and $\lambda$ be the positive weighted first eigenpair in [Lemma 5](#lem-disk-perturbation), and let $v_0(r)=J_0(jr)/(\sqrt\pi J_1(j))$. Then
$$
\left|\lambda^2\int_{\mathbb D}v^4|1+g|^2\,dA-
\frac{\lambda^2}{\pi(1+S)}-
\int_{\mathbb D}|\nabla v_0|^4\,dA\right|\le CS.
$$
The constant is universal.



### Proof of Lemma 8 {#proof-lem-weighted-eigen-balance}

By [Definition 4](#def-conformal-data), $g$ has no constant coefficient, so $h$ has no constant coefficient when $S>0$. Write $g=th$, $t=\sqrt S$, and $\|h\|_{A^2}=1$. By [Lemma 4](#lem-c1-perturbation),
$$
v=v_0+t v_1+e,
\qquad \|e\|_{L^\infty(\mathbb D)}\le CS,
\qquad \|v_1\|_{L^\infty(\mathbb D)}\le C,
$$
and $v_1$ has no radial Fourier mode. By [Lemma 5](#lem-disk-perturbation), $|\lambda-j^2|\le CS$. Since $v_0$ is radial and $h$ has no constant coefficient, angular orthogonality gives
$$
\int_{\mathbb D}v_0^3v_1\,dA=0,
\qquad
\int_{\mathbb D}v_0^4\operatorname{Re}h\,dA=0.
$$
The boundedness of $v_0,v_1,e$ and Cauchy--Schwarz imply
$$
v^4=v_0^4+4t v_0^3v_1+E,
\qquad \|E\|_{L^\infty(\mathbb D)}\le CS.
$$
Multiplying by $|1+th|^2=1+2t\operatorname{Re}h+t^2|h|^2$ and using $\|h\|_{L^1}\le C\|h\|_{A^2}$ gives
$$
\left|\int_{\mathbb D}v^4|1+g|^2\,dA-\int_{\mathbb D}v_0^4\,dA\right|\le CS.
$$
Indeed the only terms of order $t$ are the two displayed zero integrals; all remaining terms contain either $E$, $t^2|h|^2$, or the product $t^2v_0^3v_1\operatorname{Re}h$ and are $O(S)$. Therefore
$$
\lambda^2\int_{\mathbb D}v^4|1+g|^2\,dA
=j^4\int_{\mathbb D}v_0^4\,dA+O(S),
\qquad
\frac{\lambda^2}{\pi(1+S)}=\frac{j^4}{\pi}+O(S).
$$
The radial Bessel equation for $v_0$, integrated by parts using $v_0(1)=0$ and $\int_{\mathbb D}v_0^2dA=1$, gives
$$
\int_{\mathbb D}|\nabla v_0|^4\,dA
=j^4\left(\int_{\mathbb D}v_0^4\,dA-\frac1\pi\right).
$$
Combining these displays proves the claim.



## Lemma 9: Inverse-weighted gradient lower bound {#lem-inverse-left-bound}

Under the normalized conformal data of [Definition 4](#def-conformal-data), assume the hypotheses of [Lemma 7](#lem-gradient-perturbation) and let $k=(1+g)^{-1}-1$, $T=\|k\|_{A^2}^2$, and $a=|\nabla v_0|^4$. There are universal constants $c,C>0$ such that, for sufficiently small $S$,
$$
\int_{\mathbb D}|\nabla v|^4|1+k|^2\,dA
\ge \int_{\mathbb D}a\,dA+cT-C\bigl(S+\sqrt S\sqrt T+\sqrt S\,T+ST\bigr).
$$



### Proof of Lemma 9 {#proof-lem-inverse-left-bound}

If $S=0$ the assertion is immediate. Otherwise write $g=th$ with $t=\sqrt S$. By [Definition 4](#def-conformal-data), $k(0)=0$, so the constant coefficient of the analytic function $k$ is zero and
$$
\int_{\mathbb D}a\operatorname{Re}k\,dA=0
$$
because $a$ is radial. The function $a$ is bounded below on the fixed annulus $A_0=\{1/2\le|z|\le1\}$. The Bergman pointwise estimate on $|z|\le1/2$ gives $|g|\le C\sqrt S$ there, hence $|k|\le C\sqrt S$ for small $S$. Thus
$$
T\le CS+C\int_{A_0}|k|^2\,dA
\le CS+c^{-1}\int_{\mathbb D}a|k|^2\,dA.
$$
By [Lemma 7](#lem-gradient-perturbation), $\|b_1\|_{L^\infty}\le C$ and, from the $C^1$ remainder used in its proof, $\|R_1\|_{L^\infty}\le CS$ for $R_1=|\nabla v|^4-a-tb_1$. Expanding the weighted integral, using the vanishing radial pairing, and applying Cauchy--Schwarz gives
$$
\begin{aligned}
\int_{\mathbb D}|\nabla v|^4|1+k|^2\,dA
&\ge \int_{\mathbb D}a\,dA+\int_{\mathbb D}a|k|^2\,dA\\
&\quad-C\bigl(\sqrt S\sqrt T+\sqrt S\,T+S+S\sqrt T+ST\bigr).
\end{aligned}
$$
The first two errors come from $t b_1(2\operatorname{Re}k+|k|^2)$, and the remaining ones from $R_1(1+2\operatorname{Re}k+|k|^2)$. Since $S\sqrt T\le S+ST$, the preceding control of $T$ by the $a|k|^2$ term yields the stated inequality after adjusting $c,C$.



## Lemma 10: Inverse derivative energy {#lem-inverse-energy}

For the conformal data in [Definition 4](#def-conformal-data) of a stationary polygon whose canonical boundary presentation consists entirely of effective edges, satisfying [Lemma 1](#lem-edge-moments), [Lemma 5](#lem-disk-perturbation), and [Lemma 7](#lem-gradient-perturbation), and in the regime of [Lemma 6](#lem-near-circle-conformal), one has
$$
T\le CS.
$$
The constant is independent of the number and separation of the vertices and of the angle sizes.



### Proof of Lemma 10 {#proof-lem-inverse-energy}

Under the edge-moment hypotheses [Lemma 1](#lem-edge-moments), [Lemma 2](#lem-airy-identity) and the conformal change of variables in [Definition 4](#def-conformal-data) give
$$
\int_{\mathbb D}|\nabla v|^4|1+k|^2
=\lambda^2\int_{\mathbb D}v^4|1+g|^2-\frac{\lambda^2}{\pi(1+S)}.
$$
By [Lemma 9](#lem-inverse-left-bound), the left-hand side is at least
$$
\int_{\mathbb D}|\nabla v_0|^4+cT-C\{S+\sqrt S\sqrt T+\sqrt S\,T+ST\}.
$$
By [Lemma 8](#lem-weighted-eigen-balance), the right-hand side is at most
$$
\int_{\mathbb D}|\nabla v_0|^4+CS.
$$
Comparing these bounds in the identity yields
$$
T\le C\{S+\sqrt S\sqrt T+\sqrt S\,T+ST\}.
$$
Young's inequality absorbs the mixed term and, for sufficiently small $S$, the last two terms, proving $T\le CS$.



## Lemma 11: Frequency-decaying quadratic replacement {#lem-frequency-replacement}

Let $g,k,L$ be the normalized analytic data in [Definition 4](#def-conformal-data), with $L=\log(1+g)$, and suppose $S=\|g\|_{A^2}^2$ is sufficiently small and $T\le CS$. If $(m_n)_{n\ge2}$ is any real sequence with $|m_n|\le C_m(n+1)^{-2}$, then
$$
\left|\sum_{n\ge2}m_n\bigl(|k_n|^2-|g_n|^2\bigr)\right|
\le C C_m S^{3/2}\sqrt{\log(e/S)},
$$
and
$$
\left|\sum_{n\ge2}m_n\bigl(|L_n|^2-|g_n|^2\bigr)\right|
\le C C_m S^{3/2}\sqrt{\log(e/S)}.
$$
In addition, for $D=g+k$,
$$
\sum_{n\ge2}\frac{|D_n|^2}{(n+1)^3}
\le CS^2\log(e/S).
$$
The constant is independent of the polygonal angles and vertex separation.



### Proof of Lemma 11 {#proof-lem-frequency-replacement}

Put $D=g+k$. Since $g+k=-gk$ by [Definition 4](#def-conformal-data), Hölder gives
$$
\|D\|_{A^1}\le \|g\|_{A^2}\|k\|_{A^2}\le CS,
\qquad
\|D\|_{A^2}^2\le2(S+T)\le CS.
$$
The constant and linear coefficients of $D$ vanish. For every $n\ge2$, the coefficient formula and the two bounds imply
$$
|D_n|\le C(n+1)S,
\qquad
\sum_{n\ge2}\frac{|D_n|^2}{n+1}\le CS.
$$
With $K=\lceil S^{-1/2}\rceil$, splitting at $K$ gives
$$
\sum_{n\ge2}\frac{|D_n|^2}{(n+1)^3}
\le C S^2\sum_{n\le K}\frac1{n+1}
 +C(K+1)^{-2}\sum_{n>K}\frac{|D_n|^2}{n+1}
\le CS^2\log(e/S).
$$
Let $E=k-g$. Since $|k_n|^2-|g_n|^2=\operatorname{Re}(D_n\overline{E_n})$, Cauchy--Schwarz gives
$$
\left|\sum_{n\ge2}m_n(|k_n|^2-|g_n|^2)\right|
\le C C_m
\left(\sum_{n\ge2}\frac{|D_n|^2}{(n+1)^3}\right)^{1/2}
\left(\sum_{n\ge2}\frac{|E_n|^2}{n+1}\right)^{1/2}
\le C C_m S^{3/2}\sqrt{\log(e/S)}.
$$

Put $W=L-g$. The scalar estimate
$$
|e^z-1-z|\le C\bigl(|e^z-1|^2+|z|^2\bigr)
$$
and $e^L-1=g$ give $\|W\|_{A^1}\le CS$. Also
$$
\|L\|_{A^2}^2\le(S+T)/2
$$
because $|e^L|^2+|e^{-L}|^2-2\ge4(\operatorname{Re}L)^2$ pointwise and the real and imaginary parts of an analytic function with zero constant term have equal Bergman energy. Hence $\|W\|_{A^2}^2\le CS$. The same low/high frequency split gives
$$
\sum_{n\ge2}\frac{|W_n|^2}{(n+1)^3}\le CS^2\log(e/S).
$$
Finally $|L_n|^2-|g_n|^2=\operatorname{Re}(W_n\overline{(L_n+g_n)})$ and $\sum|L_n+g_n|^2/(n+1)\le CS$, so the second estimate follows by Cauchy--Schwarz.



## Lemma 12: Logarithmic Bergman energy bound {#lem-log-energy-bound}

For the normalized conformal data in [Definition 4](#def-conformal-data), with $L=\log(1+g)$,
$$
\|L\|_{A^2}^2\le\frac{S+T}{2}.
$$



### Proof of Lemma 12 {#proof-lem-log-energy-bound}

By [Definition 4](#def-conformal-data), $1+g$ is analytic and nonzero in $\mathbb D$ with value $1$ at the origin, so let $L$ be the analytic logarithm normalized by $L(0)=0$. Then $1+g=e^L$ and $(1+g)^{-1}=1+k=e^{-L}$, and the pointwise identity
$$
|1+g|^2+|1+k|^2-2
=2\cosh(2\operatorname{Re}L)-2
\ge4(\operatorname{Re}L)^2
$$
holds. Integrating and using the definitions of $S,T$ gives
$$
S+T\ge4\|\operatorname{Re}L\|_{A^2}^2.
$$
The constant coefficient of $L$ is zero because $(1+g)(0)=1$. For an analytic function with zero constant coefficient, Parseval gives equal Bergman energies for its real and imaginary parts, so $\|L\|_{A^2}^2=2\|\operatorname{Re}L\|_{A^2}^2$. The displayed inequality follows.



## Lemma 13: Bilinear mode replacement {#lem-bilinear-mode-replacement}

In the setting of [Lemma 11](#lem-frequency-replacement) and [Lemma 7](#lem-gradient-perturbation), let
$$
b_1(g)=4\,\nabla v_0\cdot\nabla v_1(g)\,|\nabla v_0|^2,
$$
and define $M(g,k)=2\int_{\mathbb D}b_1(g)\operatorname{Re}k\,dA$. Then
$$
|M(g,k)-M(g,-g)|\le C S^{3/2}\sqrt{\log(e/S)}.
$$
The constant is universal.



### Proof of Lemma 13 {#proof-lem-bilinear-mode-replacement}

By the diagonal representation in [Lemma 7](#lem-gradient-perturbation), with $D=g+k$,
$$
M(g,k)-M(g,-g)=M(g,D)=\sum_{n\ge2}m_n\operatorname{Re}(g_n\overline{D_n}),
\qquad |m_n|\le C(n+1)^{-3}.
$$
The coefficient splitting in [Lemma 11](#lem-frequency-replacement) gives
$$
\sum_{n\ge2}\frac{|D_n|^2}{(n+1)^3}\le CS^2\log(e/S),
\qquad \sum_{n\ge2}\frac{|g_n|^2}{n+1}=S.
$$
Cauchy--Schwarz with weights $(n+1)^{-3}$ and $(n+1)^{-1}$ proves the claim.



## Lemma 14: Airy boundary flux and area identity {#lem-airy-boundary-flux}

Let $\Omega$ be a simply connected smooth planar domain, $u$ its $L^2$-normalized first Dirichlet eigenfunction with eigenvalue $\lambda$, $A=|\Omega|$, $c=\lambda/A$, and $q=|\partial_\nu u|^2$. Put
$$
T=\nabla u\otimes\nabla u-\tfrac12(|\nabla u|^2-\lambda u^2)I.
$$
Let $\Phi=\psi-c|x|^2/4$, where $\psi$ is an Airy potential with $D^2\psi=R^TTR$ and $R$ is rotation by $\pi/2$. If $F(e^{i\theta})$ parametrizes $\partial\Omega$ counterclockwise and $\Gamma(\theta)=\nabla\Phi(F(e^{i\theta}))$ is identified with a complex vector, then
$$
\frac{d\Gamma}{d\theta}=\frac12(q-c)i e^{i\theta}F'(e^{i\theta}).
$$
Moreover, for
$$
\mathscr H=\int_\Omega|\nabla u|^4dA-\lambda^2\int_\Omega u^4dA+\frac{\lambda^2}{A},
$$
one has
$$
\mathscr H=-4\operatorname{Area}_{\rm signed}(\Gamma).
$$



### Proof of Lemma 14 {#proof-lem-airy-boundary-flux}

Set
$$
T=\nabla u\otimes\nabla u-\tfrac12(|\nabla u|^2-\lambda u^2)I.
$$
The equation $-\Delta u=\lambda u$ gives $\operatorname{div}T=0$. The planar Airy-potential theorem supplies a global $\psi$ on the simply connected smooth domain; set $\Phi=\psi-c|x|^2/4$. On $\partial\Omega$, $u=0$ and $\nabla u=-\partial_\nu u\,\nu$. The Hessian formula is
$$
D^2\Phi=\frac12(|\nabla u|^2+\lambda u^2-c)I-\nabla u\otimes\nabla u.
$$
If $\tau$ is the unit tangent, this gives $D^2\Phi\,\tau=(q-c)\tau/2$. Since $dF(e^{i\theta})/d\theta=i e^{i\theta}F'(e^{i\theta})$, the first identity follows.

The eigenvalues of $D^2\Phi$ are $(\lambda u^2-c\pm|\nabla u|^2)/2$, hence
$$
-4\det D^2\Phi=|\nabla u|^4-\lambda^2u^4+2\lambda c u^2-c^2.
$$
Integrating and using $\int u^2dA=1$ and $c=\lambda/A$ gives $\mathscr H=-4\int_\Omega\det D^2\Phi$. The gradient-map Stokes identity
$$
\int_\Omega\det D^2\Phi=\operatorname{Area}_{\rm signed}(\Gamma)
$$
proves the second formula.



## Lemma 15: Airy boundary quadratic calculation {#lem-airy-boundary-quadratic}

Let $g$ be an analytic polynomial with no constant or linear coefficient. Let $v(g),\lambda(g)$ be the positive weighted disk branch in [Lemma 4](#lem-c1-perturbation) and let $H_2$ be the second homogeneous term at $(g,k)=(0,0)$ of
$$
\mathscr H(g,k)=\int_{\mathbb D}|\nabla v(g)|^4|1+k|^2dA
-\lambda(g)^2\int_{\mathbb D}v(g)^4|1+g|^2dA
+\frac{\lambda(g)^2}{\pi(1+\|g\|_{A^2}^2)}.
$$
For the inverse path $k=-g$, the second homogeneous term is
$$
H_2(g,-g)=2\pi p_D^4\sum_{n\ge2}
\frac{\beta_n^2}{(n+1)^2(n^2-1)}|g_n|^2,
\qquad p_D=j/\sqrt\pi,
$$
where $\beta_n=n+1-jJ_{n+1}(j)/J_n(j)$.



### Proof of Lemma 15 {#proof-lem-airy-boundary-quadratic}

For one real monomial $g=az^n$, the first-order disk equation in [Lemma 7](#lem-gradient-perturbation) gives
$$
v_1(r,\theta)=a w_n(r)\cos(n\theta),
\qquad
w_n(r)=\frac{r^{n+1}v_0'(r)+p_DJ_n(jr)/J_n(j)}{n+1},
$$
and the Bessel recurrence gives $w_n'(1)=-p_D\rho_n/(n+1)$. The physical flux is $q=p^2/|1+g|^2$, so
$$
\delta(q-c)=-\frac{2p_D^2\beta_n}{n+1}\operatorname{Re}(ae^{in\theta}).
$$
By [Lemma 14](#lem-airy-boundary-flux), the calibrated Airy boundary gradient satisfies
$$
\frac{d\Gamma}{d\theta}=\frac12(q-c)i e^{i\theta}F'(e^{i\theta}).
$$
At the disk $\Gamma$ is constant. Integrating the first variation gives frequencies $n+1$ and $1-n$. If $d=-2p_D^2\beta_na/(n+1)$, the signed Fourier-area formula gives
$$
\operatorname{Area}_{\rm signed}(\dot\Gamma)=-\frac{\pi d^2}{8(n^2-1)}.
$$
For the conformal pullback $v=u\circ F$, the chain rule and $dA_x=|F'|^2dA_z$ give
$$
\int_\Omega|\nabla u|^4dA_x=\int_{\mathbb D}|\nabla v|^4|1+k|^2dA_z,
\quad
\int_\Omega u^4dA_x=\int_{\mathbb D}v^4|1+g|^2dA_z,
\quad
A(\Omega)=\pi(1+\|g\|_{A^2}^2).
$$
Thus the physical functional in [Lemma 14](#lem-airy-boundary-flux) is the disk functional $\mathscr H(g,k)$ on the inverse path $k=(1+g)^{-1}-1$. The second identity of [Lemma 14](#lem-airy-boundary-flux) therefore gives $H_2=-4$ times this signed area, hence
$$
H_2(az^n,-az^n)=2\pi p_D^4\frac{\beta_n^2}{(n+1)^2(n^2-1)}|a|^2.
$$
Rotation handles complex $a$, and angular orthogonality eliminates mixed modes. Summing over finite polynomials proves the formula.



## Lemma 16: Airy quadratic response {#lem-airy-quadratic-response}

Under the hypotheses of [Lemma 10](#lem-inverse-energy) and [Definition 4](#def-conformal-data), put
$$
\rho_n=j\frac{J_{n+1}(j)}{J_n(j)},
\qquad \beta_n=n+1-\rho_n,
\qquad d_n=\frac{\beta_n^2}{(n+1)^2(n^2-1)}.
$$
Then, for sufficiently small $S$,
$$
\left|S-T-2\sum_{n\ge2}d_n|g_n|^2\right|
\le C S^{3/2}\sqrt{\log(e/S)}.
$$
The constant is universal.



### Proof of Lemma 16 {#proof-lem-airy-quadratic-response}

By [Definition 4](#def-conformal-data), write $F'=1+g$, $k=(1+g)^{-1}-1$, $S=\|g\|_{A^2}^2$, and $T=\|k\|_{A^2}^2$. Let $v(g)$ and $\lambda(g)$ be the fixed-space positive branch from [Lemma 4](#lem-c1-perturbation) and [Lemma 5](#lem-disk-perturbation). Treat $g$ and $k$ temporarily as independent analytic variables and define
$$
\mathscr H(g,k)=\int_{\mathbb D}|\nabla v(g)|^4|1+k|^2dA
-\lambda(g)^2\int_{\mathbb D}v(g)^4|1+g|^2dA
 +\frac{\lambda(g)^2}{\pi(1+\|g\|_{A^2}^2)}.
$$
The fixed-space expansion in [Lemma 4](#lem-c1-perturbation) and the form expansion in [Lemma 5](#lem-disk-perturbation) imply a uniform Taylor formula
$$
\mathscr H(g,k)=H_2(g,k)+R_H(g,k),
\qquad |R_H(g,k)|\le C(\|g\|_{A^2}+\|k\|_{A^2})^3.
$$
Here the constant and linear Taylor coefficients vanish. At $(g,k)=(0,0)$ the radial Bessel equation gives
$$
\int_{\mathbb D}|\nabla v_0|^4dA-j^4\int_{\mathbb D}v_0^4dA+\frac{j^4}{\pi}=0.
$$
For a first variation $g=th$, the eigenvalue derivative is $\lambda'(0)=0$ by angular orthogonality, the area term has zero derivative, and every term involving $h$, $v_1$, or $k$ has zero angular mean because all these analytic perturbations have no constant coefficient. Thus $D\mathscr H(0,0)=0$. Multiplying the second-order Taylor polynomials supplied by [Lemma 4](#lem-c1-perturbation) (including its eigenvalue expansion) gives the displayed cubic remainder; products of two $A^2$ factors are controlled by Cauchy--Schwarz and the $C^1$ eigenfunction remainder is uniform.

For the quadratic part, put $a=|\nabla v_0|^4$, $p_D=j/\sqrt\pi$, and let $b_1$ be the first gradient variation in [Lemma 7](#lem-gradient-perturbation). Direct multiplication gives
$$
H_2(g,k)=\pi p_D^4(T-S)+Q_0(g)+A(k)+M(g,k),
$$
where $A(k)=\int(a-p_D^4)|k|^2dA$ and $M(g,k)=2\int b_1(g)\operatorname{Re}k\,dA$; $Q_0$ contains the remaining pure quadratic terms in $v(g)$, $\lambda(g)$ and $g$.

For the quadratic part, the radial term $A(k)$ has coefficients $O((n+1)^{-2})$ by $|a(r)-p_D^4|\le C(1-r)$. The phase-sensitive term is handled by [Lemma 13](#lem-bilinear-mode-replacement). The pure inverse-path quadratic form is exactly the Airy boundary calculation in [Lemma 15](#lem-airy-boundary-quadratic), and polynomial density extends it to all $A^2$ data because its multiplier is $O((n+1)^{-2})$. Thus
$$
H_2(g,-g)=2\pi p_D^4\sum_{n\ge2}d_n|g_n|^2.
$$
For the actual inverse relation, [Lemma 11](#lem-frequency-replacement) and [Lemma 13](#lem-bilinear-mode-replacement) replace $A(k)+M(g,k)$ by $A(-g)+M(g,-g)$ with error $O(S^{3/2}\sqrt{\log(e/S)})$. The same bound controls $R_H$ because [Lemma 10](#lem-inverse-energy) gives $T\le CS$. Indeed, with $v=u\circ F$, the chain rule and conformal Jacobian give
$$
\int_P|\nabla u|^4=\int_{\mathbb D}|\nabla v|^4|1+k|^2dA,
\quad
\int_Pu^4=\int_{\mathbb D}v^4|1+g|^2dA,
\quad
A(P)=\pi(1+S),
$$
so [Lemma 2](#lem-airy-identity) is exactly $\mathscr H(g,k)=0$. Dividing by $\pi p_D^4$ proves the formula.



## Lemma 17: Uniform nonlinear spectral lower bound {#lem-spectral-core}

There are universal constants $C$ and $S_0>0$ such that every stationary polygon whose canonical boundary presentation consists entirely of effective edges, satisfying [Lemma 1](#lem-edge-moments), [Lemma 5](#lem-disk-perturbation), and [Lemma 7](#lem-gradient-perturbation), and lying in the regime of [Lemma 6](#lem-near-circle-conformal), with $S\le S_0$, satisfies
$$
\frac{J(P)}{\pi j^2}\ge 1+4\sum_{n\ge2}a_n|\widehat\mu(n)|^2-C S^{3/2}\sqrt{\log(e/S)},
$$
where [Definition 5](#def-turn-measure) defines $\mu$ and
$$
a_n=\frac{\beta_n}{n^2(n+1)^2}\left(1+\frac{\beta_n}{n^2-1}\right),
\qquad \beta_n=n+1-j\frac{J_{n+1}(j)}{J_n(j)}.
$$



### Proof of Lemma 17 {#proof-lem-spectral-core}

The first-order perturbation and the second-order disk calculation from [Lemma 5](#lem-disk-perturbation) give
$$
\frac{J(P)}{\pi j^2}=1+S-\sum_{n\ge2}\frac{\rho_n}{(n+1)^2}|g_n|^2+O(S^{3/2}),
$$
with $\beta_n=n+1-\rho_n$. By [Lemma 7](#lem-gradient-perturbation), [Lemma 10](#lem-inverse-energy) and [Lemma 16](#lem-airy-quadratic-response),
$$
S-T=2\sum_{n\ge2}\frac{\beta_n^2}{(n+1)^2(n^2-1)}|g_n|^2+O\bigl(S^{3/2}\sqrt{\log(e/S)}\bigr).
$$
By [Lemma 12](#lem-log-energy-bound), $\|L\|_{A^2}^2\le(S+T)/2$, and by [Lemma 11](#lem-frequency-replacement) every quadratic form with multiplier $O((n+1)^{-2})$ may replace $g$ by $L$ at an error of order $S^{3/2}\sqrt{\log(e/S)}$. Combining these facts with the scalar expansion gives
Put $d_n=\beta_n^2/((n+1)^2(n^2-1))$, $r_n=\rho_n/(n+1)^2$, and $E=S^{3/2}\sqrt{\log(e/S)}$. The Airy response gives $T=S-2\sum d_n|g_n|^2+O(E)$, so the logarithmic bound gives
$$
S\ge \|L\|_{A^2}^2+\sum_{n\ge2}d_n|g_n|^2-O(E).
$$
The scalar disk expansion therefore yields
$$
\frac{J(P)}{\pi j^2}
\ge1+\|L\|_{A^2}^2+\sum_{n\ge2}(d_n-r_n)|g_n|^2-O(E).
$$
Since $0<\rho_n<2$ and $0<\beta_n<n+1$, one has
$$
|d_n-r_n|\le\frac{C}{(n+1)^2}.
$$
Thus [Lemma 11](#lem-frequency-replacement) changes the last quadratic form from $g$ to $L$ at cost $O(E)$. Since $L(0)=L_1=0$, Bergman Parseval gives $\|L\|_{A^2}^2=\sum_{n\ge2}|L_n|^2/(n+1)$, and
$$
\frac1{n+1}+d_n-r_n
=\frac{\beta_n}{(n+1)^2}\left(1+\frac{\beta_n}{n^2-1}\right).
$$
Finally, [Definition 5](#def-turn-measure) gives $L_n=2\widehat\mu(n)/n$, so the coefficient becomes $4a_n$ and the claimed inequality follows after shrinking $S_0$ to absorb the $O(S^{3/2})$ term into $O(E)$.
$$
\frac{J(P)}{\pi j^2}\ge1+\sum_{n\ge2}\frac{\beta_n}{(n+1)^2}\left(1+\frac{\beta_n}{n^2-1}\right)|L_n|^2-C S^{3/2}\sqrt{\log(e/S)}.
$$
Finally [Definition 5](#def-turn-measure) gives $L_n=2\widehat\mu(n)/n$, which is the claimed inequality.



## Lemma 18: Positive-atom Toeplitz bound {#lem-toeplitz-positive-atoms}

Let $\mu$ be a finite real atomic measure of total mass $1$ with exactly $p$ positive atoms, allowing arbitrary negative atoms. For $0<\tau<1$,
$$
\sum_{n\ge1}\tau^n|\widehat\mu(n)|^2\ge\frac{\tau^p}{1-\tau^p}.
$$



### Proof of Lemma 18 {#proof-lem-toeplitz-positive-atoms}

Define on $\ell^2(\mathbb N_0)$ the self-adjoint matrix
$$
A_{rs}=\tau^{(r+s)/2}\widehat\mu(r-s)=\sum_iw_i(v_i)_r\overline{(v_i)_s},
\qquad (v_i)_r=\tau^{r/2}e^{-ir\theta_i}.
$$
The Vandermonde vectors at distinct nodes are linearly independent, so $A$ has exactly $p$ positive eigenvalues $\alpha_1\ge\cdots\ge\alpha_p>0$. The trace is $(1-\tau)^{-1}$, and the negative eigenvalues can only decrease the trace, hence $Q:=\sum_i\alpha_i\ge(1-\tau)^{-1}$. The shift compression and the min--max principle give $\alpha_{i+1}\le\tau\alpha_i$. For fixed $Q$ and these ratio constraints, a finite exchange argument (move mass from an earlier coordinate to the latest coordinate until the active constraint is met) shows that the minimum of the strictly convex function $\sum_i\alpha_i^2$ is attained at
$$
\alpha_i=Q\frac{(1-\tau)\tau^{i-1}}{1-\tau^p},\qquad 1\le i\le p.
$$
Consequently
$$
\sum_i\alpha_i^2\ge Q^2\frac{1-\tau}{1+\tau}\frac{1+\tau^p}{1-\tau^p}
\ge\frac{1+\tau^p}{(1-\tau^2)(1-\tau^p)}.
$$
On the other hand,
$$
\|A\|_{HS}^2=\frac{1+2\sum_{n\ge1}\tau^n|\widehat\mu(n)|^2}{1-\tau^2}
$$
and the Hilbert--Schmidt norm dominates the squared positive eigenvalues. Rearranging gives
$$
1+2\sum_{n\ge1}\tau^n|\widehat\mu(n)|^2\ge\frac{1+\tau^p}{1-\tau^p},
$$
which is exactly the claimed bound.



## Lemma 19: Positive kernel comparison {#lem-kernel-comparison}

For every $n\ge2$, the coefficients in [Lemma 17](#lem-spectral-core) satisfy
$$
0<b_n\le a_n.
$$
Moreover,
$$
b_n=\int_0^\infty e^{-nt}\frac{1-\cos(\sqrt\kappa t)}\kappa\,dt,
$$
so for any signed atomic measure of total mass $1$ with $p$ positive atoms,
$$
E_b(\mu)\ge B_p.
$$



### Proof of Lemma 19 {#proof-lem-kernel-comparison}

By [Lemma 17](#lem-spectral-core) and [Definition 6](#def-positive-kernel), the coefficients $a_n$, $b_n$, $\rho_n$, $\kappa$, and the energy $E_b$ have the stated meanings. The Bessel bounds $5.78<j^2<5.8$ give $1.89<\kappa<1.9$. The recurrence for $J_n$ implies $0<\rho_n<2$ and, for $n\ge3$, $\rho_n<n\alpha/(n^2+\kappa)$ with $\alpha=\kappa+1$. Substitution into
$$
a_n=\frac{n-\rho_n+\rho_n^2/(n+1)^2}{n^2(n^2-1)}
$$
proves $a_n\ge b_n$; for $n=2$, the identity $J_0(j)=0$ reduces the inequality to $\kappa^3+7\kappa^2+12\kappa-54\ge0$, which holds for $\kappa\ge1.89$.

The Laplace representation follows from
$$
\int_0^\infty e^{-nt}(1-\cos(\sqrt\kappa t))\,dt=\frac{\kappa}{n(n^2+\kappa)}.
$$
Apply [Lemma 18](#lem-toeplitz-positive-atoms) with $\tau=e^{-t}$ and integrate against the nonnegative weight $(1-\cos(\sqrt\kappa t))/\kappa$. Tonelli's theorem gives $E_b(\mu)\ge B_p$.



## Lemma 20: Signed-turn spectral lower bound {#lem-signed-turn-lower-bound}

For a stationary polygon in the regime of [Lemma 17](#lem-spectral-core), if $p$ is its number of convex corners, then
$$
\frac{J(P)}{\pi j^2}\ge1+4B_p-C S^{3/2}\sqrt{\log(e/S)}.
$$



### Proof of Lemma 20 {#proof-lem-signed-turn-lower-bound}

By [Lemma 17](#lem-spectral-core) and [Lemma 19](#lem-kernel-comparison), $a_n\ge b_n$ for $n\ge2$. The missing $n=1$ term is harmless because [Definition 5](#def-turn-measure) gives $\widehat\mu(1)=0$. Hence
$$
\frac{J(P)}{\pi j^2}\ge 1+4E_b(\mu)-C S^{3/2}\sqrt{\log(e/S)}.
$$
The lower bound $E_b(\mu)\ge B_p$ is exactly [Lemma 19](#lem-kernel-comparison).



## Lemma 21: Discrete comparison energy asymptotic {#lem-bp-asymptotic}

For $B_p$ in [Definition 6](#def-positive-kernel),
$$
B_p=\frac{\zeta(3)}{p^3}-\frac{\kappa\zeta(5)}{p^5}+O(p^{-7})
\quad (p\to\infty),
$$
and $B_p$ is strictly decreasing in $p$.



### Proof of Lemma 21 {#proof-lem-bp-asymptotic}

By [Definition 6](#def-positive-kernel), $p\ge1$, $\kappa>0$, and
$$
B_p=\sum_{\ell\ge1}\frac1{\ell p((\ell p)^2+\kappa)}.
$$
For each $\ell\ge1$,
$$
\frac1{\ell p((\ell p)^2+\kappa)}
=\frac1{\ell^3p^3}-\frac{\kappa}{\ell^5p^5}+O\left(\frac{1}{\ell^7p^7}\right),
$$
uniformly for large $p$, by the geometric expansion of $(1+\kappa/(\ell p)^2)^{-1}$. Summing the absolutely convergent remainders gives the stated asymptotic. Each summand decreases strictly with $p$, so $B_p$ is decreasing.



## Lemma 22: Large-order Bessel ratio decay {#lem-bessel-ratio-decay}

For $j=j_{0,1}$ and $\rho_n=jJ_{n+1}(j)/J_n(j)$,
$$
0<\rho_n\le\frac{C}{n+1}\qquad(n\ge2).
$$



### Proof of Lemma 22 {#proof-lem-bessel-ratio-decay}

Write
$$
J_n(j)=\frac{(j/2)^n}{n!}H_n,
\qquad
H_n=\sum_{m\ge0}\frac{(-j^2/4)^m n!}{m!(n+m)!}.
$$
The alternating-series estimate gives $H_n\ge1-j^2/[4(n+1)]>1/2$ for $n\ge2$, while absolute summation gives $|H_{n+1}|\le C$. Hence
$$
\rho_n=\frac{j^2}{2(n+1)}\frac{H_{n+1}}{H_n},
$$
which proves the upper bound. Positivity follows from the standard interlacing of the first positive zeros, since $j_{0,1}<j_{n,1}$ and $J_n(j)>0$ for $n\ge1$.



## Lemma 23: Regular polygon center maximizes conformal radius {#lem-regular-center-maximizer}

For a regular $M$-gon $R_M$, the center is a point where the maximal conformal radius in [Definition 4](#def-conformal-data) is attained. Consequently the similarity-normalized Riemann map may be chosen centered at the center of $R_M$ and satisfies $F_M''(0)=0$.



### Proof of Lemma 23 {#proof-lem-regular-center-maximizer}

By [Definition 4](#def-conformal-data), $r_{R_M}$ denotes the conformal-radius function used in the normalization. We use the standard theorem that the conformal-radius function of a bounded convex planar domain is concave. The regular polygon is convex and invariant under the rotations $\sigma_k(z)=e^{2\pi ik/M}z$. For every $z$ in the polygon,
$$
0=\frac1M\sum_{k=0}^{M-1}\sigma_k(z).
$$
Concavity and rotational invariance give
$$
r_{R_M}(0)\ge\frac1M\sum_{k=0}^{M-1}r_{R_M}(\sigma_kz)=r_{R_M}(z).
$$
Thus the center is a maximizer. Uniqueness of the centered Riemann map after fixing $F_M'(0)>0$ and equivariance under the rotation group imply $F_M(e^{2\pi i/M}z)=e^{2\pi i/M}F_M(z)$; differentiating twice at $0$ gives $F_M''(0)=0$.



## Lemma 24: Regular polygon coefficient sum {#lem-regular-sc-coefficient-sum}

Let $M\ge4$, $\alpha=2/M$, and $c_q=(\alpha)_q/q!$. Then
$$
\sum_{q\ge1}\frac{c_q^2}{qM+1}
=\frac{4\zeta(3)}{M^3}+O(M^{-5}),
$$
with a universal implied constant.



### Proof of Lemma 24 {#proof-lem-regular-sc-coefficient-sum}

Write
$$
c_q=\frac\alpha qP_q,
\qquad P_q=\prod_{r=1}^{q-1}\left(1+\frac\alpha r\right),
\qquad H_q=\sum_{r=1}^q\frac1r.
$$
Set $Q=\lfloor e^{1/(4\alpha)}\rfloor$. For $q\le Q$, $\alpha H_{q-1}\le1/2$ and the product expansion with a positive remainder gives
$$
P_q=1+\alpha H_{q-1}+R_q,
\qquad |R_q|\le C\alpha^2(1+H_{q-1}^2).
$$
Also
$$
\frac1{qM+1}=\frac1{qM}-\frac1{q^2M^2}+O\left(\frac1{q^3M^3}\right).
$$
Substitution, using convergence of $\sum q^{-3}$, $\sum H_{q-1}q^{-3}$ and $\sum(1+H_{q-1}^2)q^{-3}$, gives
$$
\sum_{q\le Q}\frac{c_q^2}{qM+1}
=\frac{\alpha^2}{M}\zeta(3)
 +\frac{2\alpha^3}{M}\sum_{q\ge1}\frac{H_{q-1}}{q^3}
 -\frac{\alpha^2}{M^2}\zeta(4)+O(M^{-5}).
$$
The standard Euler sum $\sum_{q\ge1}H_{q-1}/q^3=\zeta(4)/4$ and $\alpha=2/M$ make the two $M^{-4}$ terms cancel, leaving $4\zeta(3)M^{-3}+O(M^{-5})$.

For $q>Q$, the Gamma-ratio estimate $P_q\le Cq^\alpha$ gives
$$
\sum_{q>Q}\frac{c_q^2}{qM+1}
\le\frac{C\alpha^2}{M}\sum_{q>Q}q^{-3+2\alpha}
\le C M^{-3}e^{-1/(2\alpha)}=O(M^{-5}).
$$
This proves the claim.



## Lemma 25: Regular polygon spectral asymptotic {#lem-regular-polygon-asymptotic}

For the unit-area regular $M$-gon in [Definition 2](#def-j-functional),
$$
\frac{J(R_M)}{\pi j^2}=1+\frac{4\zeta(3)}{M^3}+O(M^{-9/2})
\quad (M\to\infty).
$$



### Proof of Lemma 25 {#proof-lem-regular-polygon-asymptotic}

By [Lemma 23](#lem-regular-center-maximizer), the centered map below is the normalized map required by [Definition 4](#def-conformal-data). The regular $M$-gon is invariant under rotations about its center, and its Schwarz--Christoffel derivative is
$$
F_M'(z)=(1-z^M)^{-2/M}=1+g_M(z),qquad
g_M(z)=\sum_{q\ge1}c_qz^{qM},qquad
c_q=\frac{(2/M)_q}{q!}.
$$
By [Lemma 24](#lem-regular-sc-coefficient-sum) and [Definition 4](#def-conformal-data),
$$
S_M=\sum_{q\ge1}\frac{c_q^2}{qM+1}
=\frac{4\zeta(3)}{M^3}+O(M^{-5}).
$$

Apply [Lemma 5](#lem-disk-perturbation) to $g_M$. The quadratic correction satisfies
$$
\left|\sum_{q\ge1}\frac{\rho_{qM}}{(qM+1)^2}c_q^2\right|
\le \frac{C}{M^2}\sum_{q\ge1}\frac{c_q^2}{qM+1}=O(M^{-5}),
$$
using [Lemma 22](#lem-bessel-ratio-decay). Since $S_M=O(M^{-3})$, it is below the fixed perturbation threshold for all sufficiently large $M$, and $S_M^{3/2}=O(M^{-9/2})$. The perturbation expansion yields
$$
\frac{J(R_M)}{\pi j^2}=1+\frac{4\zeta(3)}{M^3}+O(M^{-9/2}).
$$



## Lemma 26: At least two reflex corners are excluded {#lem-two-reflex-exclusion}

There is $N_1$ such that no stationary admissible $N$-gon in the sense of [Definition 3](#def-stationary-polygon), with at least two reflex corners, satisfying [Lemma 1](#lem-edge-moments), [Lemma 17](#lem-spectral-core), and the regime of [Lemma 6](#lem-near-circle-conformal), and with $J$ as in [Definition 2](#def-j-functional), satisfies
$$
J(P)\le J(R_{N-1})
$$
for $N\ge N_1$.



### Proof of Lemma 26 {#proof-lem-two-reflex-exclusion}

Assume for contradiction that there is a sequence of such polygons with $N\to\infty$ and $J(P)\le J(R_{N-1})$. If there are at least two reflex corners, the number $p$ of convex corners is at most $N-2$. By [Lemma 6](#lem-near-circle-conformal), $S\le CN^{-3}$, and [Lemma 20](#lem-signed-turn-lower-bound) gives
$$
\frac{J(P)}{\pi j^2}\ge1+4B_p-C S^{3/2}\sqrt{\log(e/S)}.
$$
By [Lemma 21](#lem-bp-asymptotic), $B_p\ge B_{N-2}$ and
$$
B_{N-2}=\zeta(3)(N-2)^{-3}+O(N^{-5}).
$$
The conformal estimate makes the error $o(N^{-4})$. By [Lemma 25](#lem-regular-polygon-asymptotic),
$$
4B_{N-2}-\frac{4\zeta(3)}{(N-1)^3}=12\zeta(3)N^{-4}+O(N^{-5})>0
$$
for large $N$, so the lower bound is strictly larger than $J(R_{N-1})/(\pi j^2)$, contradicting the assumed upper bound.



## Lemma 27: Straight-edge prevertex gap bound {#lem-prevertex-gap}

For normalized conformal data in [Definition 4](#def-conformal-data), let $I$ be the prevertex arc corresponding to a straight effective edge and let $\varepsilon=|I|$. Then
$$
\varepsilon^4\le CS.
$$
The constant is universal.



### Proof of Lemma 27 {#proof-lem-prevertex-gap}

By [Definition 4](#def-conformal-data), put $H(z)=F(z)-F(0)-z$. The homogeneous boundary $H^{1/2}$ seminorm satisfies
$$
\int_0^{2\pi}\!\int_0^{2\pi}
\frac{|H(e^{i\theta})-H(e^{i\varphi})|^2}{|e^{i\theta}-e^{i\varphi}|^2},d\theta d\varphi
=4\pi^2S.
$$
On a straight edge, a fixed unit normal $\nu$ makes $\nu\cdot F(e^{i\theta})$ constant. Restricting the double integral to the edge arc and projecting onto $\nu$ gives the quotient of the difference of $\nu\cdot e^{i\theta}$ by $e^{i\theta}-e^{i\varphi}$. After centering the arc, the sine part contributes $c\varepsilon^2$ and the cosine part contributes $c\varepsilon^4$; the mixed term vanishes by $(\theta,\varphi)\mapsto(-\theta,-\varphi)$. Thus the restricted integral is at least $c\varepsilon^4$, proving the claim.



## Lemma 28: Uniform disk pressure oscillation {#lem-edge-pressure-oscillation}

In the regime of [Lemma 5](#lem-disk-perturbation), for every prevertex arc $I$ corresponding to a straight effective edge, the disk normal derivative $p=-\partial_rv|_{\partial\mathbb D}$ satisfies
$$
\operatorname{osc}_I p
\le C S^{3/4}\sqrt{\log(e/S)}.
$$
Moreover $p\ge p_D/2$ on the boundary for sufficiently small $S$.
Also, for sufficiently small $S$,
$$
\|p-p_D\|_{L^\infty(\partial\mathbb D)}\le C\sqrt S+CS,
$$
so $p\le2p_D$.



### Proof of Lemma 28 {#proof-lem-edge-pressure-oscillation}

By [Lemma 7](#lem-gradient-perturbation), write $g=th$ and use the boundary expansion
$$
p(\theta)=p_D+p_D\sum_{n\ge2}\frac{\rho_n}{n+1}\operatorname{Re}(g_ne^{in\theta})+O(S)
$$
uniformly. The pointwise sum is $O(\sqrt S)$ by Cauchy--Schwarz. For $|t|\le\varepsilon\le1$,
$$
|p(\theta+t)-p(\theta)|
\le C\sqrt S\left(\sum_{n\ge2}\frac{\min(n^2t^2,4)}{(n+1)^3}\right)^{1/2}+CS
\le C\sqrt S\,\varepsilon\sqrt{\log(e/\varepsilon)}+CS.
$$
By [Lemma 27](#lem-prevertex-gap), $\varepsilon\le CS^{1/4}$, and the displayed bound follows after enlarging the constant. The same pointwise estimate gives $\|p-p_D\|_\infty\le C\sqrt S+CS$; choosing $S$ small gives both $p\ge p_D/2$ and $p\le2p_D$.



## Lemma 29: Monotone edge next to the unique reflex corner {#lem-reflex-monotone-edge}

Suppose the turn measure in [Definition 5](#def-turn-measure) has exactly one negative atom $-b$ at $0$, with $0<b<1/2$, and let $a$ be the turn weight at one of the two adjacent positive vertices. There is a choice of one adjacent edge on which $h=|F'|$ is monotone and, after orienting it decreasingly,
$$
\log h(\theta_-)-\log h(\theta_+)\ge c(a+b)
$$
on a central half of the edge.



### Proof of Lemma 29 {#proof-lem-reflex-monotone-edge}

By [Definition 5](#def-turn-measure), the normalized map has prevertices $0=\theta_0<\theta_1<\cdots<\theta_p<2\pi$, weights $-b$ at $0$ and $a_j>0$ at the other prevertices, and
$$
\log F'(z)=\mathrm{const}+2b\log(1-z)-2\sum_j a_j\log(1-e^{-i\theta_j}z).
$$
On the boundary, write $x=\cot(\theta/2)$ and $x_j=\cot(\theta_j/2)$. Differentiating the real part of this formula gives
$$
(\log h)'=bx+C_*+\sum_j\frac{a_j(1+x_j^2)}{x-x_j},
\qquad C_*:=\sum_ja_jx_j.
$$
If $C_*\ge0$, choose the first edge to the right of $0$; its parameter interval lies in $(0,\theta_1)$, so $x>0$ and $x>x_j$ for every positive prevertex. If $C_*<0$, choose the last edge to the left; its interval lies in $(\theta_p,2\pi)$, so $x<0$ and $x<x_j$ for every positive prevertex. Thus all terms have one sign. Reverse orientation if needed so $h$ decreases. If the selected edge has parameter length $\varepsilon$, its positive endpoint has weight $a$. On its central subarc $[\varepsilon/4,3\varepsilon/4]$, the endpoint term is
$$
\frac{1+\cot^2(\varepsilon/2)}{\cot(\theta/2)-\cot(\varepsilon/2)}
=\frac{\sin(\theta/2)}{\sin(\varepsilon/2)\sin((\varepsilon-\theta)/2)}\ge c/\varepsilon.
$$
The negative atom contributes the same lower bound with $b$; integrating over the central half gives the stated logarithmic drop.



## Lemma 30: Conformal pressure moment identity {#lem-physical-pressure-moment}

Let $P$ be admissible and stationary in the senses of [Definition 1](#def-admissible-polygon) and [Definition 3](#def-stationary-polygon), let $E$ be an effective edge, and use the normalized conformal data in [Definition 4](#def-conformal-data). Under [Lemma 1](#lem-edge-moments), let $p=-\partial_rv|_{\partial\mathbb D}$, $h=|F'|$, and normalize $E$ by physical arclength $x\in[0,1]$. Then
$$
q(x)=p(\theta(x))^2h(\theta(x))^{-2},
$$
and, with $k_0=h^{-2}$,
$$
\int_0^1(x-1/2)p(\theta(x))^2k_0(x)\,dx=0.
$$



### Proof of Lemma 30 {#proof-lem-physical-pressure-moment}

By [Definition 1](#def-admissible-polygon), [Definition 3](#def-stationary-polygon), and [Definition 4](#def-conformal-data), $E$ is an effective edge and $v=u\circ F$, $h=|F'|$. The conformal chain rule gives $|\nabla u(F(z))|=|\nabla v(z)|/|F'(z)|$ on the relative interior of $E$; since both functions vanish there, their gradients are normal, hence $q=p^2/h^2$. If $L_E=\int h(\theta)d\theta$ and $x=L_E^{-1}\int_0^\theta h(s)ds$, then $dx=h(\theta)d\theta/L_E$ and the two edge moments in [Lemma 1](#lem-edge-moments) become
$$
\int_0^1(q-c)dx=0,
\qquad \int_0^1x(q-c)dx=0.
$$
Subtracting one half of the first equation from the second gives the displayed centered identity.



## Lemma 31: Monotone weight double-integral comparison {#lem-monotone-weight-comparison}

Let $h>0$ be monotone on $[0,\varepsilon]$. Define the normalized physical coordinate
$$
x(s)=\frac{\int_0^s h(t)dt}{\int_0^\varepsilon h(t)dt},
\qquad \widetilde k_0(x)=h(s(x))^{-2}.
$$
Suppose $p_0>0$ and $p_0\le p(s(x))\le C_0p_0$ for a fixed $C_0$ and
$$
\int_0^1(x-1/2)p(s(x))^2\widetilde k_0(x)dx=0.
$$
Then
$$
D:=\frac{\int_{s<t}(h(s)/h(t)-h(t)/h(s))dsdt}
{\int_{s<t}(h(s)/h(t)+h(t)/h(s))dsdt}
\le C\frac{\operatorname{osc}p}{p_0}.
$$



### Proof of Lemma 31 {#proof-lem-monotone-weight-comparison}

After reversing the interval assume $h$ decreases. Put $H=\int_0^\varepsilon h(s)ds$ and use the coordinate $x(s)$ and transformed weight $\widetilde k_0$ from the statement. A direct change of variables in the two ordered double integrals gives
$$
\int_{s<t}\frac{h(s)}{h(t)}dsdt=H^2\int_0^1x\widetilde k_0(x)dx,
\qquad
\int_{s<t}\left(\frac{h(s)}{h(t)}+\frac{h(t)}{h(s)}\right)dsdt=H^2\int_0^1\widetilde k_0(x)dx.
$$
Consequently,
$$
D=\frac{2\int_0^1(x-1/2)\widetilde k_0(x)dx}{\int_0^1\widetilde k_0(x)dx}.
$$
Let $m=\min_{[0,1]}p(s(x))^2$. The centered condition gives
$$
\left|\int_0^1(x-1/2)\widetilde k_0dx\right|
=\frac1m\left|\int_0^1(x-1/2)(m-p(s(x))^2)\widetilde k_0dx\right|
\le \frac{\operatorname{osc}(p^2)}{2m}\int_0^1\widetilde k_0dx.
$$
Since $m\ge p_0^2$ and $p\le C_0p_0$, $\operatorname{osc}(p^2)\le(C_0+1)p_0\operatorname{osc}p$, and the identity gives the claimed bound with a constant depending only on $C_0$.



## Lemma 32: One-reflex edge pressure comparison {#lem-reflex-edge-pressure-comparison}

Let $P$ be an admissible stationary polygon with normalized conformal data in the small-$S$ regime of [Lemma 5](#lem-disk-perturbation), satisfying [Lemma 1](#lem-edge-moments). Suppose the turn measure in [Definition 5](#def-turn-measure) has exactly one negative atom $-v$ at a prevertex, with $0<v<1/2$, and let $a>0$ be one of the two adjacent positive atoms selected by the monotonicity sign. Then there is a corresponding effective edge arc $I$ such that
$$
c(a+v)\le D_I\le C\operatorname{osc}_I p,
$$
where
$$
D_I=\frac{\int_{s<t}(h(s)/h(t)-h(t)/h(s))\,dsdt}
{\int_{s<t}(h(s)/h(t)+h(t)/h(s))\,dsdt},
\qquad h=|F'|.
$$



### Proof of Lemma 32 {#proof-lem-reflex-edge-pressure-comparison}

Here $p_D=j/\sqrt\pi>0$ is fixed, so the factor $1/p_D$ below is universal. By [Lemma 29](#lem-reflex-monotone-edge), the selected adjacent edge has monotone $h$ and a central logarithmic drop at least $c(a+v)$. On the two central rectangles, the ratio $h(s)/h(t)$ is at least $e^{c(a+v)}$, while the denominator is positive; hence the elementary rectangle comparison gives
$$
D_I\ge c\min\{a+v,1\}.
$$
By [Lemma 30](#lem-physical-pressure-moment), the edge moments give the centered condition in the normalized physical coordinate, and [Lemma 31](#lem-monotone-weight-comparison) applies with $p_0=p_D/2$, $C_0=4$ once $S$ is sufficiently small. By [Lemma 28](#lem-edge-pressure-oscillation), $p_D/2\le p\le2p_D$ and therefore
$$
D_I\le C\operatorname{osc}_I p/p_D\le C'\operatorname{osc}_I p.
$$
The right-hand side is $O(S^{3/4}\sqrt{\log(e/S)})$, so after decreasing the universal small-$S$ threshold it is below the fixed constant in the lower bound whenever $a+v\ge1$. Thus $a+v<1$, and the lower bound becomes $D_I\ge c(a+v)$. Combining the inequalities proves the result.



## Lemma 33: Single-reflex small positive atom {#lem-single-reflex-small-atom}

There is a universal $C$ such that a stationary admissible $N$-gon with an effective-edge canonical presentation, satisfying [Lemma 1](#lem-edge-moments), [Lemma 5](#lem-disk-perturbation), and $J(P)\le J(R_{N-1})$ in the regime of [Lemma 6](#lem-near-circle-conformal), with exactly one reflex corner, has an adjacent convex corner $i$ whose turn weight $a=w_i>0$ in [Definition 5](#def-turn-measure) satisfies
$$
a\le C N^{-9/4}\sqrt{\log N}.
$$



### Proof of Lemma 33 {#proof-lem-single-reflex-small-atom}

By [Definition 5](#def-turn-measure) and the angle restriction in [Definition 1](#def-admissible-polygon), a reflex corner contributes exactly one negative atom $-v$ with $0<v<1/2$, while its adjacent convex corners contribute positive atoms. The hypotheses of [Lemma 6](#lem-near-circle-conformal) and [Lemma 5](#lem-disk-perturbation) are met, so $S\le CN^{-3}$ and the pressure estimate applies. By [Lemma 27](#lem-prevertex-gap) and [Lemma 28](#lem-edge-pressure-oscillation), every edge arc has length at most $CS^{1/4}$ and
$$
\operatorname{osc}_I p\le CS^{3/4}\sqrt{\log(e/S)}.
$$
The one-reflex comparison [Lemma 32](#lem-reflex-edge-pressure-comparison) gives, for one adjacent positive atom $a$ and the negative mass $v$,
$$
c(a+v)\le D_I\le C\operatorname{osc}_I p.
$$
Thus $a\le C S^{3/4}\sqrt{\log(e/S)}$. After decreasing the small-$S$ threshold, $s\mapsto s^{3/4}\sqrt{\log(e/s)}$ is increasing on $(0,S_0]$. Therefore
$$
a\le C N^{-9/4}\sqrt{\log N}.
$$



## Lemma 34: Deletion preserves the comparison energy {#lem-atom-deletion}

Let $(P_N)$ be a sequence of stationary admissible $N$-gons with effective-edge canonical presentations, satisfying [Lemma 1](#lem-edge-moments), [Lemma 5](#lem-disk-perturbation), [Lemma 7](#lem-gradient-perturbation), [Lemma 17](#lem-spectral-core), [Lemma 6](#lem-near-circle-conformal), and $J(P_N)\le J(R_{N-1})$, in the one-reflex regime of [Definition 5](#def-turn-measure). Let $p=N-1$, let $a$ be the small positive atom from [Lemma 33](#lem-single-reflex-small-atom), and define $E_b$ as in [Definition 6](#def-positive-kernel). Put
$$
\widetilde\mu=\frac{\mu-a\delta_{\theta_*}}{1-a}.
$$
Then $\widetilde\mu$ has total mass $1$ and $N-2$ positive atoms, and
$$
E_b(\widetilde\mu)-E_b(\mu)=o(N^{-4}).
$$



### Proof of Lemma 34 {#proof-lem-atom-deletion}

By [Definition 5](#def-turn-measure), the one-reflex measure has total mass $1$, exactly $N-1$ positive atoms at distinct prevertices, and one negative atom. For sufficiently large $N$, [Lemma 33](#lem-single-reflex-small-atom) gives $0<a<1/2$. By [Lemma 36](#lem-one-reflex-energy-gap), with $p=N-1$,
$$
0\le\delta:=E_b(\mu)-B_{N-1}\le CN^{-9/2}\sqrt{\log N},
\qquad E_b(\mu)=O(N^{-3}).
$$
By [Lemma 35](#lem-energy-deletion-identity), the exact difference is
$$
E_b(\widetilde\mu)-E_b(\mu)=
\frac{2a(E_b(\mu)-U_b(\theta_*))+a^2(K_b(0)-E_b(\mu))}{(1-a)^2}.
$$
By [Lemma 37](#lem-kernel-potential-bound), $\|U_b\|_\infty\le C\sqrt\delta+CN^{-5/2}$. By [Lemma 38](#lem-kernel-diagonal-bound), $K_b(0)=O(1)$. Since [Lemma 33](#lem-single-reflex-small-atom) gives $a=O(N^{-9/4}\sqrt{\log N})$, the displayed identity and the bounds on $U_b$ and $E_b(\mu)$ give
$$
E_b(\widetilde\mu)-E_b(\mu)=O(N^{-9/2}\log N)=o(N^{-4}).
$$



## Lemma 35: Exact normalized energy deletion identity {#lem-energy-deletion-identity}

Let $\mu$ be a finite real atomic measure of total mass $1$ and let $0<a<1$. For $\theta_*$ set
$$
\widetilde\mu=\frac{\mu-a\delta_{\theta_*}}{1-a},
\qquad
U_b(\theta)=\sum_{n\ge1}b_n\operatorname{Re}(\widehat\mu(n)e^{in\theta}),
\qquad K_b(0)=\sum_{n\ge1}b_n.
$$
Then
$$
E_b(\widetilde\mu)-E_b(\mu)=
\frac{2a(E_b(\mu)-U_b(\theta_*))+a^2(K_b(0)-E_b(\mu))}{(1-a)^2}.
$$



### Proof of Lemma 35 {#proof-lem-energy-deletion-identity}

By [Definition 6](#def-positive-kernel), $E_b(\nu)=\sum_{n\ge1}b_n|\widehat\nu(n)|^2$ and the series converges absolutely for every finite atomic measure.
For every $n\ge1$,
$$
\widehat{\widetilde\mu}(n)=\frac{\widehat\mu(n)-a e^{-in\theta_*}}{1-a}.
$$
Squaring the modulus, multiplying by $b_n$, summing, and using
$$
\sum_{n\ge1}b_n\operatorname{Re}(\widehat\mu(n)e^{in\theta_*})=U_b(\theta_*),
\qquad
\sum_{n\ge1}b_n=K_b(0),
$$
gives the identity by direct algebra.



## Lemma 36: One-reflex energy gap estimate {#lem-one-reflex-energy-gap}

For a sequence of admissible stationary $N$-gons with effective-edge canonical presentations, satisfying [Lemma 1](#lem-edge-moments), [Lemma 5](#lem-disk-perturbation), [Lemma 7](#lem-gradient-perturbation), [Lemma 17](#lem-spectral-core), and $J(P)\le J(R_{N-1})$, with exactly one reflex corner, let $p=N-1$ and define $E_b$ and $B_p$ as in [Definition 6](#def-positive-kernel). In the regime of [Lemma 6](#lem-near-circle-conformal), with $\delta=E_b(\mu)-B_p$, one has
$$
0\le\delta\le C N^{-9/2}\sqrt{\log N},
\qquad E_b(\mu)=O(N^{-3}).
$$



### Proof of Lemma 36 {#proof-lem-one-reflex-energy-gap}

By [Definition 6](#def-positive-kernel) and [Definition 5](#def-turn-measure), in the one-reflex regime $\mu$ is a total-mass-one signed atomic measure with exactly $p=N-1$ positive atoms. Thus [Lemma 19](#lem-kernel-comparison) gives $E_b(\mu)\ge B_p$, so $\delta\ge0$. All hypotheses of [Lemma 17](#lem-spectral-core) are included in the statement, and its coefficient comparison gives
$$
\frac{J(P)}{\pi j^2}\ge1+4E_b(\mu)-C S^{3/2}\sqrt{\log(e/S)}.
$$
By [Lemma 6](#lem-near-circle-conformal), $S\le CN^{-3}$, so the error is $O(N^{-9/2}\sqrt{\log N})$. By [Lemma 25](#lem-regular-polygon-asymptotic),
$$
\frac{J(R_{N-1})}{\pi j^2}=1+4B_{N-1}+O(N^{-9/2}).
$$
Comparing with $J(P)\le J(R_{N-1})$ gives the bound on $\delta$. Finally [Lemma 21](#lem-bp-asymptotic) gives $B_{N-1}=O(N^{-3})$, so $E_b(\mu)=B_{N-1}+\delta=O(N^{-3})$.



## Lemma 37: Laplace kernel potential bound {#lem-kernel-potential-bound}

Let $\mu$ be a total-mass-one finite real atomic measure with $p$ positive atoms and put $\delta=E_b(\mu)-B_p\ge0$. For
$$
U_b(\theta)=\sum_{n\ge1}b_n\operatorname{Re}(\widehat\mu(n)e^{in\theta}),
$$
one has
$$
\|U_b\|_\infty\le C\sqrt\delta+C p^{-5/2}.
$$



### Proof of Lemma 37 {#proof-lem-kernel-potential-bound}

Use the Laplace representation in [Definition 6](#def-positive-kernel) and set
$$
E(t)=\sum_{n\ge1}e^{-nt}|\widehat\mu(n)|^2,
\qquad E_0(t)=\frac1{e^{pt}-1}.
$$
The Toeplitz bound [Lemma 18](#lem-toeplitz-positive-atoms) gives $E(t)\ge E_0(t)$, and Tonelli gives
$$
\delta=\int_0^\infty\frac{1-\cos(\sqrt\kappa t)}\kappa\,[E(t)-E_0(t)]dt.
$$
By Cauchy--Schwarz,
$$
\left|\sum_{n\ge1}e^{-nt}\widehat\mu(n)e^{in\theta}\right|
\le\sqrt{\frac{E(t)}{e^t-1}}.
$$
Splitting $E=E-E_0+E_0$ and applying Cauchy--Schwarz to the first part gives $C\sqrt\delta$, since
$$
\int_0^\infty\frac{1-\cos(\sqrt\kappa t)}{\kappa(e^t-1)}dt<\infty.
$$
For the second part, use $1-\cos(\sqrt\kappa t)\le Ct^2$ near $0$, $e^t-1\ge t$, and split at $t=p^{-1}$; this gives
$$
\int_0^\infty\frac{1-\cos(\sqrt\kappa t)}\kappa
\sqrt{\frac{E_0(t)}{e^t-1}}dt\le Cp^{-5/2}.
$$
Taking the supremum over $\theta$ proves the claim.



## Lemma 38: Uniform kernel diagonal bound {#lem-kernel-diagonal-bound}

For $K_b(0)=\sum_{n\ge1}b_n$ in [Definition 6](#def-positive-kernel),
$$
0<K_b(0)\le\zeta(3).
$$



### Proof of Lemma 38 {#proof-lem-kernel-diagonal-bound}

By [Definition 6](#def-positive-kernel), $b_n=1/[n(n^2+\kappa)]$ with $\kappa>0$, so $0<b_n\le n^{-3}$. Summing gives $K_b(0)\le\zeta(3)$.



## Theorem 1: Large-N low-threshold stationary polygons are convex {#thm-main-large-n-convexity}

There is a universal $N_0$ such that, for every $N\ge N_0$, every admissible stationary simple $N$-gon $P$ satisfying
$$
J(P)\le J(R_{N-1})
$$
 is convex. Consequently, no such polygon satisfies $J(P)<m_{N-1}$ while being non-convex.



### Proof of Theorem 1 {#proof-thm-main-large-n-convexity}

Assume the conclusion fails and choose a sequence of counterexamples with $N\to\infty$. By [Definition 1](#def-admissible-polygon), each canonical presentation consists of effective edges. By [Definition 3](#def-stationary-polygon) and [Lemma 1](#lem-edge-moments), each polygon satisfies the edge moments. Therefore the sequence satisfies every hypothesis of [Lemma 6](#lem-near-circle-conformal), including $J(P_N)\le J(R_{N-1})$, and that lemma gives $S_N\le CN^{-3}$. For all sufficiently large indices this is below the fixed $S_0$ thresholds in [Lemma 5](#lem-disk-perturbation) and [Lemma 7](#lem-gradient-perturbation). The normalized data then satisfy the hypotheses of [Lemma 17](#lem-spectral-core); the same effective-edge, edge-moment, and near-circle facts verify the hypotheses of [Lemma 26](#lem-two-reflex-exclusion), [Lemma 33](#lem-single-reflex-small-atom), and [Lemma 34](#lem-atom-deletion).

If there are at least two reflex corners, [Lemma 26](#lem-two-reflex-exclusion) gives a contradiction. Thus, after discarding finitely many terms, there is exactly one reflex corner. The hypotheses of [Lemma 33](#lem-single-reflex-small-atom) and [Lemma 34](#lem-atom-deletion) hold, so the deleted measure has $N-2$ positive atoms and [Lemma 19](#lem-kernel-comparison) yields $E_b(\widetilde\mu)\ge B_{N-2}$. By [Lemma 34](#lem-atom-deletion),
$$
E_b(\mu)\ge B_{N-2}-o(N^{-4}).
$$
By [Definition 6](#def-positive-kernel), $E_b(\mu)=\sum_{n\ge1}b_n|\widehat\mu(n)|^2$; since [Definition 5](#def-turn-measure) gives $\widehat\mu(1)=0$ and [Lemma 19](#lem-kernel-comparison) gives $b_n\le a_n$, the spectral-core estimate [Lemma 17](#lem-spectral-core) together with [Definition 5](#def-turn-measure) gives
$$
\frac{J(P)}{\pi j^2}\ge1+4E_b(\mu)-C S^{3/2}\sqrt{\log(e/S)}.
$$
Using [Lemma 6](#lem-near-circle-conformal), the error is $o(N^{-4})$, so
$$
\frac{J(P)}{\pi j^2}\ge1+4B_{N-2}-o(N^{-4}).
$$
The regular-polygon asymptotic [Lemma 25](#lem-regular-polygon-asymptotic) gives
$$
\frac{J(R_{N-1})}{\pi j^2}=1+\frac{4\zeta(3)}{(N-1)^3}+O(N^{-9/2}),
$$
while [Lemma 21](#lem-bp-asymptotic) gives $B_{N-2}=\zeta(3)(N-2)^{-3}+O(N^{-5})$. Their difference is $12\zeta(3)N^{-4}+O(N^{-9/2})+o(N^{-4})>0$ for large $N$, contradicting $J(P)\le J(R_{N-1})$.

Finally, by [Definition 2](#def-j-functional), $m_{N-1}$ is the infimum over admissible polygons with at most $N-1$ effective edges, and $R_{N-1}$ is one such polygon; hence $m_{N-1}\le J(R_{N-1})$. Therefore any nonconvex stationary polygon with $J(P)<m_{N-1}$ also satisfies the threshold already ruled out.

