# Search Log

This log records searches that support completeness claims. It should include
both included sources and relevant-looking exclusions.

## How to Record Searches

Use one entry per meaningful search.

```md
### YYYY-MM-DD -- short search label

- Search target:
- Query:
- Hits inspected:
- Included:
- Excluded:
- Follow-up:
```

## Seed Searches Already Reflected in the Registry

### 2026-05-22 -- Massberg 2014 primary-source verification

- Search target: primary DOI/PDF for the hole-free perimeter-over-six theorem.
- Query: DOI `10.1007/s00454-014-9587-4`, exact title search for
  `"Perfect graphs and guarding rectilinear art galleries"`.
- Hits inspected: Springer PDF, Mendeley metadata page, DBLP metadata.
- Included: `Massberg2014`.
- Excluded: metadata-only pages were not used for theorem locators.
- Follow-up: verify `MassbergHabilitation` next, because Massberg 2014
  Conjecture 9 is related to but not identical with the habilitation's
  Conjecture 6.10 reference already tracked in the review.

### 2026-05-22 -- Massberg habilitation conditional hole route

- Search target: primary habilitation PDF for the rectangle-packing conjecture
  behind the conditional holes statement.
- Query: exact URL
  `https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.080/Massberg/habilitation_massberg.pdf`,
  plus text searches for `Conjecture 6.10`, `Lemma 6.9`, and `Theorem 6.3`.
- Hits inspected: Ulm-hosted habilitation PDF, Chapter 6, pp. 67--75.
- Included: `MassbergHabilitation`.
- Excluded: no secondary pages were used for locators.
- Follow-up: verify `BiedlEtAl2012` next, because it is the independent
  holes-allowed area theorem that should be kept separate from the conditional
  perimeter theorem.

### 2026-05-22 -- Biedl et al. 2012 cell-count theorem

- Search target: primary PDF and metadata for the polyomino area/cell-count
  theorem with holes.
- Query: exact title `"The Art Gallery Theorem for Polyominoes"`, DOI
  `10.1007/s00454-012-9429-1`, and author-hosted PDF search.
- Hits inspected: author-hosted journal PDF, SUNY Research Connect metadata,
  DOI/Springer metadata, DBLP volume page.
- Included: `BiedlEtAl2012`.
- Excluded: metadata-only pages were not used for theorem locators.
- Follow-up: verify `DiazBanezEtAl2025` next if continuing the 2D perimeter
  thread, or `BiedlEtAl2019` if moving to algorithmic restricted-visibility
  variants.

### 2026-05-22 -- perimeter-over-six and polyomino perimeter

- Search target: DOI pages, author/university PDFs, exact title searches.
- Query: `"Perfect graphs and guarding rectilinear art galleries"`,
  `"Massberg" "Conjecture 6.10" maximal rectangles guarding holes`,
  `"The art gallery theorem for polyominoes"`.
- Hits inspected: Ma{\ss}berg 2014, Ma{\ss}berg habilitation thesis, Biedl et
  al. 2012.
- Included: `Massberg2014`, `MassbergHabilitation`, `BiedlEtAl2012`.
- Excluded: none recorded yet.
- Follow-up: primary-check page and theorem locators for all three records.

### 2026-05-22 -- orthogonal polygons with holes

- Search target: open-problem pages, exact title searches, DOI pages.
- Query: `"orthogonal art galleries with holes" "Shermer" "Hoffmann"`,
  `"floor((n+h)/4)" "orthogonal polygon" holes "vertex guards"`,
  `"How to guard orthogonal polygons" "diagonal graphs"`.
- Hits inspected: Urrutia open-problem page, Zylinski 2006,
  Hoffmann--Kriegel 1996, Michael--Pinciu 2016.
- Included: `UrrutiaOpenProblems`, `Zylinski2006`, `HoffmannKriegel1996`,
  `MichaelPinciu2016`.
- Excluded: none recorded yet.
- Follow-up: record exact theorem/conjecture locators and any later papers
  citing these conjectures.

### 2026-05-22 -- 3D orthogonal polyhedra and edge guards

- Search target: author PDFs, arXiv, DOI pages, exact title searches.
- Query: `"orthogonal polyhedron" "edge guards" "m/12"`,
  `"reflex edge guards" "orthogonal polyhedra" "2-reflex"`,
  `"edge guards for polyhedra in three-space"`.
- Hits inspected: Benbernou et al. 2011, Viglietta thesis, Viglietta 2020,
  Cano--Toth--Urrutia--Viglietta 2022.
- Included: `BenbernouEtAl2011`, `VigliettaThesis`, `Viglietta2020`,
  `CanoTothUrrutiaViglietta2022`.
- Excluded: none recorded yet.
- Follow-up: separate arbitrary-polyhedron results from orthogonal-specific
  conjectures in claim records.

### 2026-05-22 -- algorithmic and restricted-visibility context

- Search target: DOI pages and exact title searches.
- Query: `"Computational complexity of art gallery problems"`,
  `"Two NP-hard art-gallery problems for orthogonal polygons"`,
  `"sliding cameras" "orthogonal art galleries"`,
  `"guarding polyominoes" "k-hop visibility"`.
- Hits inspected: Lee--Lin 1986, Schuchardt--Hecker 1995, Katz--Roisman 2008,
  Durocher et al. 2017, Biedl et al. 2019, Filtser et al. 2025, Ghosh 2010.
- Included: `LeeLin1986`, `SchuchardtHecker1995`, `KatzRoisman2008`,
  `DurocherEtAl2017`, `BiedlEtAl2019`, `FiltserEtAl2025`, `Ghosh2010`.
- Excluded: none recorded yet.
- Follow-up: decide which adjacent models need theorem-level extraction versus
  brief survey treatment.

### 2026-05-22 -- central locator pass

- Search target: primary/public PDFs and open-problem pages for the central
  perimeter, holes, and 3D edge-guard claims.
- Query: exact public URLs from `download_manifest.json`, plus the Urrutia
  open-problem page `https://www.matem.unam.mx/~urrutia/openprob/Polygons/`.
- Hits inspected: Diaz-Banez et al. 2025 arXiv PDF, Cano--Toth--Urrutia--
  Viglietta 2022 author PDF, Viglietta 2012 arXiv thesis, Zylinski 2006
  journal PDF, and Urrutia's open-problem webpage.
- Included: page/theorem/conjecture locators for `DiazBanezEtAl2025`,
  `CanoTothUrrutiaViglietta2022`, `VigliettaThesis`, `Zylinski2006`, and
  `UrrutiaOpenProblems`.
- Excluded: metadata-only DOI/arXiv pages were not used as locators when a
  public PDF or explicit open-problem page was available.
- Follow-up: continue the locator pass for Kahn--Klawe--Kleitman, Gyori,
  Paterson--Yao, Hoffmann--Kriegel, Michael--Pinciu, and the algorithmic
  restricted-visibility papers.

### 2026-05-22 -- foundational 2D locator pass

- Search target: primary metadata and public book cross-checks for the classical
  simple-polygon and simple-orthogonal-polygon theorems.
- Query: exact DOI searches for Chvatal 1975, Fisk 1978,
  Kahn--Klawe--Kleitman 1983, and Gyori 1986; author-hosted O'Rourke book PDF
  at `https://www.science.smith.edu/~jorourke/books/ArtGalleryTheorems/Art_Gallery_Full_Book.pdf`.
- Hits inspected: O'Rourke's public book PDF; SIAM DOI pages for
  Kahn--Klawe--Kleitman, DOI `10.1137/0604020`, and Gyori, DOI
  `10.1137/0607051`; original page spans for Chvatal and Fisk from DOI
  metadata.
- Included: claim locators for `Chvatal1975`, `Fisk1978`, `Gyori1986`,
  `KahnKlaweKleitman1983`, and `ORourke1987`; source-registry verification
  notes for the same records; O'Rourke PDF marked downloaded in the manifest.
- Excluded: metadata-only pages were used only for bibliographic page spans, not
  as substitutes for theorem text when O'Rourke's survey gave an accessible
  theorem cross-check.
- Follow-up: if institutional access is available, primary-check the full
  Kahn--Klawe--Kleitman and Gyori proof text; otherwise continue the locator
  pass for Hoffmann--Kriegel, Michael--Pinciu, Paterson--Yao, and the
  restricted-visibility papers.

### 2026-05-22 -- holes, 3D, and restricted-visibility locator pass

- Search target: public PDFs and primary metadata for the remaining cited
  sources in the holes, 3D, approximation, and restricted-visibility clusters.
- Query: exact DOI/title searches for Bjorling--Sachs 1998, Hoffmann--Kriegel
  1996, Paterson--Yao 1992, Viglietta 2014/2020, Lee--Lin 1986,
  Schuchardt--Hecker 1995, Katz--Roisman 2008, Durocher et al. 2017, Biedl et
  al. 2019, Filtser et al. 2025, Ghosh 2010, Pinciu 2015, Worman--Keil 2007,
  Shermer 1992, and Urrutia 2000.
- Hits inspected/downloaded: arXiv PDFs for Viglietta 2014/2020 and Durocher
  et al.; Springer open PDF for Filtser et al.; WRAP technical report for
  Paterson--Yao; MPI-hosted PDF for Ghosh; Refubium technical report for
  Hoffmann--Kriegel; DOI metadata pages for the closed-access or survey
  sources.
- Included: claim locators for the remaining 18 records previously flagged by
  the checker, plus source-registry verification notes and manifest entries for
  the public downloads.
- Corrected: `Ghosh2010` is a *Discrete Applied Mathematics* paper,
  158(6):718--722, DOI `10.1016/j.dam.2009.12.004`; the previous
  Journal-of-Discrete-Algorithms DOI was an erroneous bibliographic entry.
- Excluded: closed publisher PDFs were not downloaded; metadata-only records
  are treated as context unless an open PDF or secondary cross-check supports a
  specific locator.
- Follow-up: run forward-citation searches for post-2016 status of the
  orthogonal-polygons-with-holes conjectures and for any newer work on 3D
  orthogonal edge/reflex-edge guards.

### 2026-05-23 -- forward and adjacent-model sweep for open clusters

- Search target: post-2016 status changes and nearby-model exclusions for the
  orthogonal-polygons-with-holes, perimeter-over-six-with-holes, and 3D
  orthogonal-polyhedron guard clusters.
- Query: `"How to guard orthogonal polygons" diagonal graphs vertex covers
  citations`; `"orthogonal polygons with holes" "vertex guards" "art
  gallery"`; `"orthogonal polygons with holes" "floor" "2n/7" "vertex
  guards"`; `"orthogonal art galleries with holes" "vertex guards" "2016"`;
  `"orthogonal polygons with holes" "vertex guards" "2025"`; `"orthogonal
  art galleries with holes" "vertex guards" "2024"`; `"Shermer's Conjecture"
  "orthogonal" "holes" "vertex guards"`; `"Hoffmann" "floor(2n/7)"
  "orthogonal polygons"`.
- Query: `"Massberg" "Perfect graphs and guarding rectilinear art galleries"
  citations`; `"polyominoes with holes" "perimeter" "guards" "ell/6"`;
  `"perimeter-over-six" polyomino guards holes`; `"maximal rectangle packing"
  rectilinear art gallery holes guards`; `"Ma{\ss}berg" "polyomino"
  "guards"`; `"Massberg" "polyomino" "guards" "holes"`; `"Perfect Graphs"
  "rectilinear art galleries" "polyomino" "holes"`; `"l/6" "polyomino"
  "guards"`.
- Query: `"orthogonal polyhedra" "edge guards" "art gallery"`; `"Edge
  Guards for Polyhedra in Three-space" citations`; `"reflex edge guards"
  "orthogonal polyhedra"`; `"Optimally Guarding 2-Reflex Orthogonal
  Polyhedra" citations`; `"orthogonal polyhedra" "guard" "2024" "art
  gallery"`; `"orthogonal polyhedra" "edge guards" "2025"`; `"orthogonal
  polyhedron" "reflex edge guards" "2024"`; `"polycube" "guarding" "art
  gallery"`.
- Query: `"Abello" "orthogonal polygon" "holes" "vertex guards"`; `"Abello"
  "art gallery" "orthogonal" "holes" "guard"`; `"first tight bound"
  "orthogonal polygon" "holes" "vertex guards" "Abello"`; `"orthogonal
  polygon" "holes" "linear-time algorithm" "vertex guards" "Abello"`;
  `"Guarding Polyominoes, Polycubes and Polyhypercubes"`; `"Rook and Queen
  Vision" polycubes polyhypercubes`; `site:arxiv.org art gallery orthogonal
  polygon holes guards 2025`; `site:arxiv.org orthogonal polyhedra edge guards
  2025`; `site:arxiv.org polyomino perimeter guards holes`;
  `site:drops.dagstuhl.de orthogonal art gallery polygon holes vertex guards
  2025`.
- Hits inspected: existing tracked sources around Urrutia's open-problem
  page, Zylinski 2006, Hoffmann--Kriegel 1996, Michael--Pinciu 2016,
  Ma{\ss}berg 2014 and habilitation, Biedl et al. 2012, Benbernou et al.
  2011, Viglietta thesis/2020, Cano--Toth--Urrutia--Viglietta 2022, Pinciu
  2015, plus recent arXiv/DROPS/topic hits on restricted or adjacent
  visibility variants.
- Included: no new theorem source was added to the registry from this sweep;
  the tracked status of the main open cells remains unchanged.  The sweep
  updates `coverage_matrix.json`, `open_problems.json`, and the paper's
  evidence-audit discussion.
- Excluded: Abello--Estivill-Castro--Shermer--Urrutia-style orthogonal
  floodlight results use restricted-angle/floodlight visibility and are not
  standard point- or vertex-guard theorems; half-plane or one-sided guarding
  results for orthogonal polygons with holes use a different visibility model;
  rook/queen, k-hop, and polycube/polyhypercube visibility results are
  discrete or polyform variants; recent dispersive, contiguous, mobile,
  point-boundary, sliding-camera, and transmitter results are optimization or
  restricted-visibility variants rather than proofs of the perimeter-over-six
  holes theorem or the general 3D edge/reflex-edge conjectures.
- Follow-up: repeat exact-title, venue, author-page, and forward-citation
  scans before publication; create separate coverage cells before citing any
  excluded adjacent model as a theorem-level result.

### 2026-05-23 -- adjacent-model scope-exclusion pass

- Search target: turn the adjacent-model exclusions from the forward sweep
  into auditable scope decisions.
- Included: no theorem-level source was promoted.  The coverage matrix now has
  explicit scope-exclusion cells for floodlight and half-plane visibility, and
  for dispersive, contiguous, mobile, point-boundary, and related optimization
  or motion variants.
- Excluded from source intake: these adjacent variants remain outside the
  current extremal point/vertex/edge-guard focus unless the paper later cites a
  specific theorem.  At that point, the source must receive a registry record,
  claim record, locator, translation note, and coverage-cell link before the
  prose is updated.
- Follow-up: repeat source-level searches only when one of these variants is
  promoted beyond exclusion context.

### 2026-05-23 -- final OpenAlex and venue-status pass

- Search target: final status check for the central open or conditional cells
  before rebuilding the review PDF.
- Query: OpenAlex DOI lookup for Ma{\ss}berg 2014,
  `10.1007/s00454-014-9587-4`, followed by `cites:W2069841121`; OpenAlex DOI
  lookup for Diaz-Banez et al. 2025, `10.1007/s00373-024-02880-8`, followed
  by `cites:W4405867242`; OpenAlex exact/topic searches for `"Edge-guarding
  Orthogonal Polyhedra"`, `"Optimally guarding 2-reflex orthogonal polyhedra
  by reflex edge guards"`, and `"Edge Guards for Polyhedra in Three-space"`;
  web/topic searches for `"orthogonal polyhedra" "edge guards" "2024"`,
  `"orthogonal polyhedron" "reflex edge guards" "2025"`, `"perimeter over
  six" polyomino holes`, and `"integral orthogonal polygon" "N/6" guards`.
- Hits inspected: OpenAlex work `W2069841121` for Ma{\ss}berg 2014 and its
  two citing works, `Pinciu2015` and `MassbergHabilitation`; OpenAlex work
  `W4405867242` for Diaz-Banez et al. 2025 and its empty citing-work set;
  OpenAlex records and citing works around `BenbernouEtAl2011`,
  `Viglietta2020`, `VigliettaThesis`, and
  `CanoTothUrrutiaViglietta2022`; recent web/topic hits around 2024--2025
  orthogonal-polyhedron edge/reflex-edge guarding.
- Included: `AldanaGalvanEtAl2016` was added as an adjacent limited-field
  3D source: it proves a theorem for `pi/2`-edge guards in orthogonal
  polyhedra, not for standard edge guards or reflex-edge-only guards.
- Excluded: no citing or topic hit found in this pass changes the status of
  the perimeter-over-six polyominoes-with-holes question, the broader
  integral-perimeter question, the standard orthogonal-polygons-with-holes
  vertex-guard questions, or the general 3D standard edge/reflex-edge guard
  gaps.  City-guarding, limited-field, face-guarding, 2-reflex, discrete
  polyform, and other restricted-visibility variants remain separate cells.
- Follow-up: repeat this exact forward/venue pass after new central papers,
  proceedings volumes, or author-page updates appear.
