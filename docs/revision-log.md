# Revision log, Yamuna floodplain paper (final)

Build: 10 pages, 62 references (all cited), 0 undefined references, 0 overfull or very loose lines, 0 BibTeX warnings. The Overleaf zip (pdfLaTeX) was rebuilt from scratch in an empty folder and produces an identical PDF.

## 1. Framework diagram (Fig. 1)
- Five-stage IEEE-style figure built from real outputs: floodplain polygon from the shapefile, reflectance, DEM, HAND, LULC maps, transition matrix, built-up series, forecast, projected 2035 map, hindcast map.
- Vector PDF with embedded fonts; automated check: all 79 labels inside their panels, no overlaps.
- Prints on page 2 directly after its first citation.

## 2. Figures: overlap scan of all 13
- Fig. 8 (CNN): second axis of panel (a) overprinted panel (b). Rebuilt from the notebook's logged values (training log at epochs 0 to 29 in steps of 5, per-class IoU, four example tiles).
- Fig. 9 (areas): percentage labels clipped at the plot edges. Rebuilt from the exact area table.
- Fig. 11 (forecast): "18.2" label crossed by a fitted line. Rebuilt by re-running the notebook's fitting code; every RMSE, forecast and 90% band reproduced exactly (K = 22.02, r = 0.0950, inflection 2013.6).
- Fig. 5: title changed from "2000-2025" to "2000 to 2025".
- Rebuilt figures pass an automated check requiring at least a 2 pt gap between all labels and no label on any plotted line. Remaining figures inspected and clean.

## 3. Figure, table and algorithm citations
- All 13 figures, 3 tables and 2 algorithms cited in text, first citations in numerical order, each float on or after the page of its first citation.

## 4. Table I
- Shaded "Our work" row with metrics; "Reported performance" column with values checked against each published study.
- Note: our values are on the controlled benchmark and not directly comparable with accuracies on real imagery; classification accuracy and simulation agreement measure different quantities.

## 5. References: all 62 verified against sources
Removed: Yadav and Khandegar 2019 (no record found), Janizadeh 2024 (unverifiable), Pontius 2011 (replaced by Pontius et al. 2008, which supports the FoM statement).
Added: Singh et al. 2025 (Natural Hazards, July 2023 flood), Tripathy and Kumar 2019 (Cities), Pontius et al. 2008 (Ann. Reg. Sci.).
Corrected:
- Khan 2020: title, first author (Armugha Khan), fourth author (Rucha Dave); study area is the Yamuna-Chambal ravines, so no longer cited for Delhi.
- Rao 2007: title and co-author (five authors, Hydrogeol. J. 15(6):1157-1167).
- Jain 2024: author Madhavi Jain, issue 14; its 79.78% / 77.25% are simulation-validation scores and are compared with our hindcast, not our classifiers.
- Bhadu 2023: author Shobhika Bhadu, pages 191-228, editors added.
- Given names: Singh 2022 (Bhavna, Veluswamy, Benidhar), Tang 2024 (Xiaoyan, Funan, Xinling), Gui 2025 (Baoling, Anshuman, Lydia), Naikoo 2020 (Mohammad Ishtiaque), Yang 2014 (Xin-Qi Zheng).
- Complete author lists: Tariq 2023 (2), Liu 2024 (6), Lv 2021 (6), Bai 2023 (7).
- Rouse 1974: first author J. W. Rouse, Jr. Box 2015: publisher John Wiley & Sons. Rikimaru 2002: journal article.
Formatting: IEEE author rule (all names up to six, otherwise first author et al.; one setting in refs.bib lists all), "Art. no." for article-numbered journals, full journal names, sentence-case titles, conference locations, book editions and publisher locations.

## 6. Text: final scan for accuracy
- Flood level 208.66 m now cited to Singh et al. 2025; the 205.33 m danger mark removed (not confirmable in an accessible peer-reviewed source).
- Random Forest vs reference: in 2025 the RF maps give 16.41 km2 of floodplain built-up against a benchmark reference of 23.51 km2 (32.8%); the CNN maps give 23.70 km2, within 1%. Now stated in abstract, Results, Discussion and Conclusion; RF-based change and forecasts described as conservative.
- Evaluation scope disclosed: equal-allocation sample (up to 1,500 pixels per class and epoch) from grid rows 600 to 833, which include urban surroundings.
- Hindcast correctly described as scored against the RF 2025 map (abstract, methods, results, Algorithm 2, Fig. 13 caption).
- Fixed claims contradicted by the paper's own figures: water does not convert to built-up (transition matrix 0.0); agriculture's main confusion is with vegetation (confusion matrix).
- Removed or reworded unsupported statements ("national agencies", "less than two percent of the river's length", "agency assessments", "well-documented", "largest gains on geometric classes").
- Discussion: HAND importance and hindcast generalization described as partly by construction in the benchmark.
- Verified against data: coordinates (lat 28.5085 to 28.8598 N, lon 77.1849 to 77.3478 E), 67.7 km2 polygon, 71.8 km2 grid floodplain, 240% increase, percentages, forecast parameters.

## Notes
- The only em dashes in the PDF are the IEEEtran "Abstract" and "Index Terms" labels.
- The executed notebook still shows the earlier layouts of Figs. 1, 5, 8, 9 and 11; all numbers are identical.

---

# Targeted revision (this round)

Build: 11 pages (was 10; the two worked examples added about 0.4 column, which pushed references 54 to 62 onto a final page), 62 references all cited, 0 undefined references, 0 overfull boxes, 0 very loose lines, 0 BibTeX warnings, 0 `[?]`. All 13 figures, 3 tables and 2 algorithms keep their previous numbers and are still cited in numerical order, each float on or after the page of its first citation. Clean-room rebuild of the Overleaf zip gives identical text.

## 1. Title
Was: "Random Forest, CNN, and Cellular-Automata Modelling of Built-Up Encroachment in the Delhi Yamuna Floodplain"
Now: "Terrain-Informed Random Forest, CNN, and Cellular Automata for Mapping and Forecasting Delhi Yamuna Floodplain Encroachment"
It now names the distinctive input (terrain, i.e. HAND), the three methods, both tasks the paper actually performs (mapping and forecasting), and the exact site. It sets as three balanced lines, keeps Rahul's rules (short, no "AI-based", algorithms named), and claims nothing about real imagery.

## 2. Section VII
Retitled "Conclusion and Future Work". One closing sentence added, framed as building on the accuracy already established rather than as a gap: re-running the identical pipeline on multi-date Landsat and Sentinel-2 composites of this reach, driving change detection and allocation from the CNN maps, and extending the driver set with regulatory and socio-economic layers. No existing claim weakened or removed.

## 3. Worked examples for the two formulae after Fig. 4
Both illustrations open with "Concretely" and both trace the paper's own numbers, so the two read as one pattern.
- Subsection E (CNN architecture): a tile enters as 9 channels; the three 3x3 layers lift it to 24 then 32 channels and widen support to 7x7 cells, which on the 50 m grid is a 350 x 350 m (12.25 ha) window; the 1x1 layer maps 32 channels to 5 class scores. Weights 1,968 + 6,944 + 9,248 + 165 = 18,325. Tied to the result: built-up IoU 0.939 and 2025 area within 1% of reference, against the Random Forest's roughly 30% under-detection.
- Subsection G (logistic growth, now labelled and cross-referenced as (1)): K = 22.02 km2, r = 0.0950 per year, t0 = 2013.6 give A(2030) = 22.02/(1 + e^(-0.0950 x 16.4)) = 18.2 km2 and A(2035) = 19.5 km2; with A_2025 = 16.41 km2 and rho = 50 m the cell demand is (18.2 - 16.41)/0.0025 = 716 cells of 0.25 ha for 2030 and a further 520 for 2035. Every value is one already reported in the paper, so no new result is introduced.
- The Figure of Merit already carries its own worked instance in Results (3,189 hits, 1,846 misses, 1,445 false alarms, FoM 0.492), so it was left as it stands.

## 4. One wording for our contribution
All variants removed. The paper now uses "our work" only: Fig. 1 caption "Overview of our work", Table I caption "Comparison of representative studies with our work", Table I shaded row "Our work", Related Work prose "compares representative studies with our work" and "Our work complements both by", and the provenance statement "the offline compute environment used for our work". Zero occurrences of "proposed work", "proposed framework", "the present work" or "this work" remain.

## Incidental
Fig. 8 (CNN) set at 0.97 columnwidth instead of full width, which clears a 2.4 pt overfull vbox created by the reflow. No other figure changed.

---

# IEEE compliance fix, 6 November 2026

TGRS unsubmitted manuscript TGRS-2026-10828 with the reason: "per the IEEE
article template, the first page of the manuscript must include a footnote with
author institution information."

## Cause

The author block typeset the affiliations inline, underneath the author names,
which is the IEEEtran *conference* layout:

```latex
\author{Prachi\textsuperscript{1}, Rahul Katarya\textsuperscript{2}, ...\\[3pt]
\small\textsuperscript{1}Department of Geospatial Science and Technology, ...\\
\small\textsuperscript{2}Department of Computer Science and Engineering, ...%
\thanks{Corresponding author: Rahul Katarya (e-mail: rahulkatarya@dtu.ac.in).}}
```

In the journal layout IEEE requires the affiliations to sit in `\thanks{}`
blocks, which IEEEtran renders as the unnumbered footnote at the foot of the
first column of page 1. The old block produced no such footnote, so the
automated template check failed.

## Fix

Author names only in `\author`; one `\thanks` per affiliation plus the
corresponding-author line:

```latex
\author{Prachi,~Rahul~Katarya,~and~Kailash~Chand~Tiwari%
\thanks{Prachi and K. C. Tiwari are with the Department of Geospatial Science and Technology, Delhi Technological University, Delhi 110042, India.}%
\thanks{R. Katarya is with the Department of Computer Science and Engineering, Delhi Technological University, Delhi 110042, India (e-mail: rahulkatarya@dtu.ac.in).}%
\thanks{(Corresponding author: Rahul Katarya.)}}
```

The running head was also empty (`\markboth{}{}`) and is now set to the journal
name and a short author-and-title line, as the template expects.

## Verified on the rebuilt PDF

- Affiliation footnote present at the foot of column 1, page 1
- Running head "IEEE Transactions on Geoscience and Remote Sensing" on page 1,
  short title on later pages
- 11 pages, 62 references all cited, 0 undefined references, 0 overfull boxes,
  0 BibTeX warnings
- All 26 fonts embedded and subsetted, no encryption, US Letter, PDF 1.5
- Pages numbered 1 to 11 in one continuous series
- Clean-room rebuild from the Overleaf zip gives identical text

## Open items for the authors

- Two e-mail addresses are missing from the first `\thanks`; a comment in
  `paper.tex` marks where they go.
- The submitted title ("... Using Multitemporal Satellite Imagery") does not
  match this source and contradicts the data-provenance statement in
  Section III-B. See the repository README.
- At 11 pages the paper crosses the TGRS overlength threshold, which starts at
  page 11 for submissions after 1 January 2026.
