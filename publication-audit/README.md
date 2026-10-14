# Publication checks for Dujella's Problem 1.7

The mathematical article and its exact-arithmetic verifier are in [dujella-problem-1.7](../dujella-problem-1.7/). This directory contains publication checks, not additional mathematical claims or an independent peer review.

## Scope

The workflow checks the root index and the full article on actual, commit-specific GitHub pages, both in file preview and directory landing views, at widths of 430 and 1440 pixels. It compares the server's TeX with the Markdown source, waits for every mathematical output, detects parser errors and clipped equations, verifies local anchors, and captures overlapping screenshots of the complete pages. It also checks table structure and the exact publication-date and review-status fields. Native horizontal scrolling in wide tables and command blocks is tested separately from page overflow.

The article contains 95 display expressions, 463 inline TeX expressions and 91 semantic single-letter variables. All 649 mathematical items are checked in source order against the manuscript inventory. The PDF and LaTeX source are the unchanged revised manuscript. Reflowed alignments, named set delimiters, equivalent alphabet glyphs and semantic variables are typographical adaptations only. Finite symbolic, enumeration and local-density checks are rerun and compared with the recorded mathematical verification results.

The two `*_v2` reference tools are preserved from the repository owner's supplied mathematical-formatting reference package. `render.mjs` extends its browser checks with inner equation bounds, semantic-variable checks, downloaded-file equality and evidence preservation. `editorial.mjs` checks the tables, native scrollers and hashes of all publication files. The additional macros explicitly allowed by the strict linter are tested by the live browser rather than accepted solely on the basis of a local TeX renderer.

## Reproduction and evidence

Use the **Dujella 1.7 publication audit** workflow in the repository's Actions tab. It runs automatically after relevant changes on `main` and can also be dispatched manually. It has read-only repository permissions and does not modify the manuscript or the branch.

Each run uploads a commit-specific artifact containing `manifest.json`, full-page and overlapping viewport screenshots, server HTML, browser diagnostics, mathematical inventories, exact verification output, downloaded source snapshots and SHA-256 hashes. Artifact retention is 90 days. `release-manifest.json` permanently records the original validated manuscript and page hashes; later workflow manifests identify their own exact tested commits.

The screenshots were also inspected during the AI-assisted publication review. These checks establish fidelity and rendering for the tested version and viewports, not a guarantee about every browser or future change to GitHub. They do not certify mathematical novelty, formal verification or third-party approval. Part (d) remains unresolved, and the public third-party review field remains **Not Yet**.
