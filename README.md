# Large-N Convexity of Low-Threshold Stationary Polygons

Private research archive by **Zhuo Cheng**, prepared from the completed research
thread identified below. The repository preserves the original manuscript, the
reconstructed QMD proof, historical checking evidence, the exact installed
qmd-prover source, and a self-contained PDF/LaTeX reading copy.

## Author

Zhuo Cheng

School of Mathematics and Statistics, HNP-LAMA, Central South University, Changsha, Hunan 410083, P. R. China

[zhuo@outlook.cz](mailto:zhuo@outlook.cz)

## Project introduction

The project studies the exclusion of non-convex stationary planar polygons at
large effective edge count, using the scale-invariant first-Dirichlet-eigenvalue
functional

$$J(P)=A(P)\lambda_1(P).$$

An admissible domain is a bounded simple planar polygon with no self-contact;
redundant collinear vertices are removed when counting its effective edges.
Stationarity is taken with respect to variations of the effective vertex
coordinates. Write $R_k$ for a unit-area regular $k$-gon, and let $m_k$ be the
infimum of $J$ over admissible polygons having at most $k$ effective edges.

The main assertion recorded in this project is:

> There is a universal $N_0$ such that, for every $N\ge N_0$, every admissible
> stationary simple $N$-gon $P$ with $J(P)\le J(R_{N-1})$ is convex.
> Consequently, a non-convex stationary polygon in this class cannot satisfy
> $J(P)<m_{N-1}$.

The proof chain develops vertex-stationarity edge moments, near-circle conformal
normalization, Airy and spectral perturbation identities, positive-atom Toeplitz
and kernel comparisons, regular-polygon asymptotics, and the one-reflex-corner
pressure/deletion argument. Its final contradiction compares the deleted-atom
energy gap with the regular-polygon threshold at order $N^{-4}$.

## Recorded verification state

- 45 semantic facts, all globally marked `verified`, including
  `thm-main-large-n-convexity`.
- 0 recorded structural errors, dependency cycles, unresolved references,
  or render warnings at the final recorded check.
- Independent checker configuration: `codex`, model `gpt-6.1-sol`, effort `high`,
  `citations: standard`, `rigor: standard`, isolated checking contexts.
- Verification consists of AI-assisted mathematical review. The original
  verdicts, including earlier failed checks and historical snapshots, are
  preserved for inspection.

The archive operation copied and checked the saved evidence; it did not request
another model-verification run or change the mathematical source. The archived
Goal is marked `complete`, with no total Token budget.

See [the recorded status](archive/recorded-verification.json),
[the verification summary](docs/VERIFICATION-SUMMARY.md), and the preserved
[audit report](project/AUDIT-REPORT.md).

## Timestamps

All local times below use **Asia/Shanghai, UTC+08:00**. UTC instants are also
provided to make the archive portable across time zones.

| Event | Asia/Shanghai | UTC |
| --- | --- | --- |
| Source thread created | `2026-10-31T22:27:38+08:00` | `2026-10-31T14:27:38+00:00` |
| Goal completion recorded | `2026-11-01T08:01:52+08:00` | `2026-11-01T00:01:52+00:00` |
| Source snapshot completed | `2026-11-01T14:23:30.157824+08:00` | `2026-11-01T06:23:30.157824+00:00` |
| Repository assembled | `2026-11-01T14:30:04.018044+08:00` | `2026-11-01T06:30:04.018044+00:00` |

Source thread: [01a1925b-e627-7933-b8e7-cb35b9d43a1a](http://100.95.50.98:8215/thread/01a1925b-e627-7933-b8e7-cb35b9d43a1a).
Original file modification times and SHA-256 hashes are preserved in
[`archive/source-manifest.json`](archive/source-manifest.json).
Git commits and the annotated archive tag provide the upload history.

## Reading guide

1. Read [`manuscript/large-n-proof.pdf`](manuscript/large-n-proof.pdf) for the
   typeset proof and author information.
2. Use [`project/workspace/large-n-proof.qmd`](project/workspace/large-n-proof.qmd)
   as the original semantic mathematical source.
3. Consult [the fact index](docs/PROOF-INDEX.md) and
   [the dependency diagram](project/.qmd-prover/generated/dependencies.svg)
   to navigate the proof chain.
4. Inspect [`project/.qmd-prover/`](project/.qmd-prover/) for the current manifest,
   statement locks, historical graphs, and verifier evidence.
5. Read the timestamped [conversation](archive/conversation.md) and
   [tool records](archive/tool-records.jsonl) for development provenance.

## Repository contents

| Path | Contents |
| --- | --- |
| `project/` | Complete captured proof project, including all original QMD, Markdown, configuration, audit and verification files |
| `inputs/` | Original uploaded source attachments |
| `manuscript/` | Derived reading Markdown, self-contained LaTeX and PDF |
| `tooling/qmd-prover/` | Exact installed qmd-prover package source and its original MIT license |
| `archive/` | Thread/Goal metadata, timestamps, visible conversation, tool records, source manifest and build records |
| `docs/` | Project guide, fact index and a summary of the saved checking evidence |
| `scripts/` | Offline integrity check and reproducible reading-copy builder |
| `AUTHORS.md`, `CITATION.cff` | Author, affiliation, contact and citation metadata |
| `CHECKSUMS.sha256` | File-integrity manifest |

The original project contains 338 files
(30,851,485 bytes), including 128 historical
dependency-graph files and 193 verification-evidence files. All original project
files were captured byte-for-byte. The vendored runtime contains
52 files; its package metadata reports
version `0.1.0` and Node.js `>=20`.

## Reproduction and integrity

The supplied PDF can be read directly. To validate the archive without making a
model request:

```sh
python3 scripts/verify_archive.py
```

To rebuild the reading copy, install Pandoc and XeLaTeX with the standard
`fontspec`, AMS, `mathtools`, `unicode-math`, `geometry`, `hyperref`, `longtable`, and `booktabs`
packages, then run:

```sh
python3 scripts/build_reading_copy.py
```

The builder changes only derived reading-copy/build-report files. Those files
carry their captured hashes in this dated snapshot, so a new local PDF build can
legitimately change their checksums. The authoritative QMD source is retained.

To inspect the bundled checker command set:

```sh
node tooling/qmd-prover/skills/qmd-prover/scripts/qmd-prover.js --help
```

The original configuration and runtime documentation are preserved in
[`project/.qmd-prover/config.yml`](project/.qmd-prover/config.yml) and
[`tooling/qmd-prover/readme.md`](tooling/qmd-prover/readme.md).
Running new independent checks requires a separately authenticated Codex CLI
and may use model quota. The repository contains no account credentials.

## Provenance and rights

The original Chinese manuscript and expanded reference draft are retained as
`project/source-original.md` and `project/source-reference-expanded.md`.
The reading copy changes presentation and cross-reference labels while
preserving the archived mathematical content. Earlier rejected/stale reports
remain part of the research history; the final state is summarized separately.

The conversation archive contains visible user/assistant messages and recorded
tool activity. Native runtime-internal records and authentication material are
outside the exported conversation. See [`archive/snapshot.json`](archive/snapshot.json)
for the export scope, counts and original rollout digest.

This is a private research archive. Research authorship and contact information
are given above; bundled third-party software retains its own license.
