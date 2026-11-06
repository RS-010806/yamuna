# LaTeX source

A self-contained IEEEtran project. Upload this whole directory to Overleaf, or
build locally:

```bash
pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper
```

Requirements: the `IEEEtran` document class and `IEEEtran.bst`. On TeX Live these
are in `texlive-publishers`; the project also uses `graphicx`, `amsmath`,
`amssymb`, `booktabs`, `array`, `textcomp`, `multirow`, `cite`, `algorithm`,
`algpseudocode`, `xcolor` and `siunitx`, all in `texlive-latex-extra` and
`texlive-science`.

Current build: 11 pages, 62 references all cited, 0 undefined references, 0
overfull boxes, 0 BibTeX warnings. `Yamuna_Encroachment_IEEE.pdf` is that build.

## Files

- `paper.tex`: the manuscript
- `refs.bib`: 62 references, each verified against the publisher or indexed
  record. The file opens with an `@IEEEtranBSTCTL` control entry that enforces
  the IEEE author rule (all names up to six, otherwise first author and
  et al.); setting `CTLuse_forced_etal` to `"no"` lists all authors instead.
- 13 figure files, duplicated from `../figures/` so the project compiles
  standalone. Four are vector PDFs. `fig_pipeline.pdf`, Fig. 1 of the paper, is
  the framework diagram and is drawn separately rather than by the notebook.

## Conventions the reviewers asked for

Year ranges are written "2000 to 2025" rather than with an arrow or a dash.
Every reported value carries a citation or is computed in the notebook. The
contribution is referred to as "our work" throughout, in the Fig. 1 caption,
the Table I caption and row, the Related Work prose and the provenance
statement. `docs/revision-log.md` records each review round and what changed.
