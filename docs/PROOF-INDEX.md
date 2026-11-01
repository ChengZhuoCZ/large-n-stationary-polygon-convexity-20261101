# Proof fact index

Recorded semantic facts and their dependencies. IDs match the archived QMD.

| ID | Kind | Title | Global status | Dependencies |
| --- | --- | --- | --- | --- |
| `def-admissible-polygon` | definition | Admissible simple polygon | verified |  |
| `def-conformal-data` | definition | Normalized conformal data | verified | `def-admissible-polygon`, `def-j-functional` |
| `def-j-functional` | definition | Area-eigenvalue functional | verified | `def-admissible-polygon` |
| `def-positive-kernel` | definition | Positive comparison kernel | verified | `def-turn-measure` |
| `def-stationary-polygon` | definition | Vertex stationary polygon | verified | `def-admissible-polygon`, `def-j-functional` |
| `def-turn-measure` | definition | Signed Schwarz-Christoffel turn measure | verified | `def-admissible-polygon`, `def-conformal-data` |
| `lem-airy-boundary-flux` | lemma | Airy boundary flux and area identity | verified |  |
| `lem-airy-boundary-quadratic` | lemma | Airy boundary quadratic calculation | verified | `lem-airy-boundary-flux`, `lem-gradient-perturbation` |
| `lem-airy-identity` | lemma | Airy fourth-power identity | verified | `def-admissible-polygon`, `lem-edge-moments` |
| `lem-airy-quadratic-response` | lemma | Airy quadratic response | verified | `def-conformal-data`, `lem-airy-boundary-quadratic`, `lem-airy-identity`, `lem-bilinear-mode-replacement`, `lem-c1-perturbation`, `lem-disk-perturbation`, `lem-frequency-replacement`, `lem-gradient-perturbation`, `lem-inverse-energy` |
| `lem-atom-deletion` | lemma | Deletion preserves the comparison energy | verified | `def-turn-measure`, `lem-energy-deletion-identity`, `lem-kernel-diagonal-bound`, `lem-kernel-potential-bound`, `lem-one-reflex-energy-gap`, `lem-single-reflex-small-atom` |
| `lem-bessel-ratio-decay` | lemma | Large-order Bessel ratio decay | verified |  |
| `lem-bilinear-mode-replacement` | lemma | Bilinear mode replacement | verified | `lem-frequency-replacement`, `lem-gradient-perturbation` |
| `lem-bp-asymptotic` | lemma | Discrete comparison energy asymptotic | verified | `def-positive-kernel` |
| `lem-c1-perturbation` | lemma | Uniform C1 conformal perturbation | verified | `def-conformal-data` |
| `lem-disk-perturbation` | lemma | Uniform disk perturbation expansion | verified | `def-conformal-data`, `def-j-functional`, `lem-c1-perturbation` |
| `lem-edge-moments` | lemma | Stationary edge moments | verified | `def-stationary-polygon` |
| `lem-edge-pressure-oscillation` | lemma | Uniform disk pressure oscillation | verified | `lem-gradient-perturbation`, `lem-prevertex-gap` |
| `lem-energy-deletion-identity` | lemma | Exact normalized energy deletion identity | verified | `def-positive-kernel` |
| `lem-frequency-replacement` | lemma | Frequency-decaying quadratic replacement | verified | `def-conformal-data` |
| `lem-gradient-perturbation` | lemma | Gradient perturbation interface | verified | `lem-c1-perturbation`, `lem-disk-perturbation` |
| `lem-inverse-energy` | lemma | Inverse derivative energy | verified | `def-conformal-data`, `lem-airy-identity`, `lem-edge-moments`, `lem-inverse-left-bound`, `lem-weighted-eigen-balance` |
| `lem-inverse-left-bound` | lemma | Inverse-weighted gradient lower bound | verified | `def-conformal-data`, `lem-gradient-perturbation` |
| `lem-kernel-comparison` | lemma | Positive kernel comparison | verified | `def-positive-kernel`, `lem-spectral-core`, `lem-toeplitz-positive-atoms` |
| `lem-kernel-diagonal-bound` | lemma | Uniform kernel diagonal bound | verified | `def-positive-kernel` |
| `lem-kernel-potential-bound` | lemma | Laplace kernel potential bound | verified | `def-positive-kernel`, `lem-toeplitz-positive-atoms` |
| `lem-log-energy-bound` | lemma | Logarithmic Bergman energy bound | verified | `def-conformal-data` |
| `lem-monotone-weight-comparison` | lemma | Monotone weight double-integral comparison | verified |  |
| `lem-near-circle-conformal` | lemma | Near-circle conformal deficit | verified | `def-conformal-data`, `def-j-functional`, `lem-disk-perturbation`, `lem-uniform-w14` |
| `lem-one-reflex-energy-gap` | lemma | One-reflex energy gap estimate | verified | `def-positive-kernel`, `def-turn-measure`, `lem-bp-asymptotic`, `lem-kernel-comparison`, `lem-near-circle-conformal`, `lem-regular-polygon-asymptotic`, `lem-spectral-core` |
| `lem-physical-pressure-moment` | lemma | Conformal pressure moment identity | verified | `def-admissible-polygon`, `def-conformal-data`, `def-stationary-polygon`, `lem-edge-moments` |
| `lem-prevertex-gap` | lemma | Straight-edge prevertex gap bound | verified | `def-conformal-data` |
| `lem-reflex-edge-pressure-comparison` | lemma | One-reflex edge pressure comparison | verified | `lem-edge-pressure-oscillation`, `lem-monotone-weight-comparison`, `lem-physical-pressure-moment`, `lem-reflex-monotone-edge` |
| `lem-reflex-monotone-edge` | lemma | Monotone edge next to the unique reflex corner | verified | `def-turn-measure` |
| `lem-regular-center-maximizer` | lemma | Regular polygon center maximizes conformal radius | verified | `def-conformal-data` |
| `lem-regular-polygon-asymptotic` | lemma | Regular polygon spectral asymptotic | verified | `def-conformal-data`, `lem-bessel-ratio-decay`, `lem-disk-perturbation`, `lem-regular-center-maximizer`, `lem-regular-sc-coefficient-sum` |
| `lem-regular-sc-coefficient-sum` | lemma | Regular polygon coefficient sum | verified |  |
| `lem-signed-turn-lower-bound` | lemma | Signed-turn spectral lower bound | verified | `def-turn-measure`, `lem-kernel-comparison`, `lem-spectral-core` |
| `lem-single-reflex-small-atom` | lemma | Single-reflex small positive atom | verified | `def-admissible-polygon`, `def-turn-measure`, `lem-disk-perturbation`, `lem-edge-pressure-oscillation`, `lem-near-circle-conformal`, `lem-prevertex-gap`, `lem-reflex-edge-pressure-comparison` |
| `lem-spectral-core` | lemma | Uniform nonlinear spectral lower bound | verified | `def-turn-measure`, `lem-airy-quadratic-response`, `lem-disk-perturbation`, `lem-frequency-replacement`, `lem-gradient-perturbation`, `lem-inverse-energy`, `lem-log-energy-bound` |
| `lem-toeplitz-positive-atoms` | lemma | Positive-atom Toeplitz bound | verified |  |
| `lem-two-reflex-exclusion` | lemma | At least two reflex corners are excluded | verified | `lem-bp-asymptotic`, `lem-near-circle-conformal`, `lem-regular-polygon-asymptotic`, `lem-signed-turn-lower-bound` |
| `lem-uniform-w14` | lemma | Uniform W1,4 bound | verified | `lem-airy-identity` |
| `lem-weighted-eigen-balance` | lemma | Weighted eigenenergy balance | verified | `def-conformal-data`, `lem-c1-perturbation`, `lem-disk-perturbation` |
| `thm-main-large-n-convexity` | theorem | Large-N low-threshold stationary polygons are convex | verified | `def-admissible-polygon`, `def-j-functional`, `def-positive-kernel`, `def-stationary-polygon`, `def-turn-measure`, `lem-atom-deletion`, `lem-bp-asymptotic`, `lem-disk-perturbation`, `lem-edge-moments`, `lem-gradient-perturbation`, `lem-kernel-comparison`, `lem-near-circle-conformal`, `lem-regular-polygon-asymptotic`, `lem-single-reflex-small-atom`, `lem-spectral-core`, `lem-two-reflex-exclusion` |
