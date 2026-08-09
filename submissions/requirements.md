# Editorial requirements matrix (checked 2026-07-15)

| Destination | Required source | Length/layout | Current eligibility | Blocking work |
|---|---|---|---|---|
| JOSS | `paper.md`, bibliography, figures in the software repository | 750–1750 words; required sections include Summary, Statement of need, State of the field, Software design, Research impact, AI disclosure, acknowledgements, references | Not eligible now | make repo public; build >6 months public history; demonstrate research use; release/archive DOI |
| Formal Aspects of Computing | LaTeX using the publisher's current class/instructions | Full formal-methods article; publisher class governs final layout | Draft only | compile all provers; deepen semantics; compare related formal tools; verify current submission portal metadata |
| Preprint repository/arXiv | TeX source, bibliography and all figures needed to compile | Self-contained scholarly manuscript; category and source checks apply | Closest to ready | author metadata; references; TeX compilation; endorsement/category decision; upload-source validation |

Requirements change. Re-check official author pages on the day of submission.

## Package-wide checklist

- [ ] Title and abstract describe a specification calculator, not a Millennium proof.
- [ ] Every numeric claim has a script, parameters, hardware and uncertainty.
- [ ] `Div` feature sets and weights are versioned and independently motivated.
- [ ] Lean, Coq, Isabelle and Agda versions and successful logs are archived.
- [ ] Security claims have a threat model and adversarial/load tests.
- [ ] No claim of AES-512, zero latency, DoS immunity or equivalence to Perelman.
- [ ] Figures have captions stating whether they are definitions, measurements or illustrations.
- [ ] Code release is tagged and archived; DOI appears in data/software availability.
- [ ] AI usage is disclosed and every generated passage/code path reviewed by authors.
- [ ] Author, affiliation, ORCID, funding, conflicts and correspondence are confirmed.
