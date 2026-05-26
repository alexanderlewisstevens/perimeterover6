# Evidence Report

Generated from the structured literature ledgers. This report is an audit companion for the review paper, not a substitute for the prose.

## Summary

- Sources: 34
- Claims: 37
- Coverage cells: 18
- Scope-exclusion cells: 2
- Open-problem clusters: 8
- Claims missing page/theorem locators: 0
- Coverage cells still unsearched/searching: 0

## Status Counts

### Source Statuses

- `approximation`: 1
- `conditional`: 1
- `hardness`: 5
- `open_problem`: 1
- `survey`: 4
- `theorem`: 15
- `tight_theorem`: 7

### Claim Types

- `approximation`: 1
- `conditional`: 1
- `conjecture`: 1
- `hardness`: 5
- `lower_bound`: 1
- `open_problem`: 1
- `survey`: 4
- `theorem`: 16
- `tight_theorem`: 7

### Coverage Statuses

- `open_gap`: 1
- `scope_excluded_adjacent`: 2
- `synthesized`: 15

### Open-Problem Statuses

- `active_research_direction`: 1
- `open`: 1
- `open_or_conditional`: 2
- `open_with_partial_results`: 4

## Declared Status Vocabularies

### Source Status Values

- `theorem`
- `tight_theorem`
- `conditional`
- `conjecture`
- `lower_bound`
- `open_problem`
- `hardness`
- `approximation`
- `survey`

### Claim Type Values

- `theorem`
- `tight_theorem`
- `conditional`
- `conjecture`
- `lower_bound`
- `open_problem`
- `hardness`
- `approximation`
- `survey`

### Coverage Status Values

- `unsearched`
- `searching`
- `synthesized`
- `open_gap`
- `scope_excluded_adjacent`

### Result Status Values

- `theorem`
- `tight_theorem`
- `tight_theorem_context`
- `tight_theorem_for_restricted_class`
- `adjacent_limited_field_theorem`
- `conditional`
- `open_with_partial_results`
- `open_or_conditional_beyond_hole_free`
- `restricted_visibility_context`
- `restricted_visibility_out_of_scope`
- `optimization_or_motion_variant_out_of_scope`
- `discrete_visibility_context`
- `face_guard_context`
- `hardness_and_approximation_context`

### Open-Problem Status Values

- `open`
- `open_with_partial_results`
- `open_or_conditional`
- `active_research_direction`

## Major Proven Results

### `claim_BenbernouEtAl2011`

- Source: `BenbernouEtAl2011` (Canadian Conference on Computational Geometry)
- Status: `theorem`
- Result: Every orthogonal polyhedron with e total edges and r reflex edges is guardable by floor((e+r)/12) open edge guards; using the e/r/genus relation gives open-edge-guard bounds of (11/72)e - g/6 - 1 and (7/12)r - g + 1.
- Translation note: This is a 3D edge-guard result, not a point-guard or perimeter result. The (7/12)r expression is parameterized by the number of reflex edges; it is not a theorem using only reflex-edge guards.
- Locator: Theorem 5, PDF pp. 5-6; Corollaries 6-7, PDF p. 6; Theorem 2, PDF pp. 3-4, for the e/r/genus relation; Theorem 4, PDF pp. 4-5, for the open/closed edge-guard comparison.

- Tracking issue: [#2](https://github.com/alexanderlewisstevens/perimeterover6/issues/2)

### `claim_BiedlEtAl2012`

- Source: `BiedlEtAl2012` (Discrete & Computational Geometry)
- Status: `tight_theorem`
- Result: For m >= 2, floor((m+1)/3) guards are sometimes necessary and always sufficient to cover a connected m-polyomino, possibly with holes; the sufficiency proof works even in the more restrictive r-visibility model.
- Translation note: This is an area/cell-count theorem for connected m-polyominoes, with the one-cell case handled separately. It does not imply a perimeter-over-six theorem because area and perimeter are incomparable for the needed extremal question.
- Locator: Definitions on journal p. 712; model/result overview in Section 2, journal p. 713; lower-bound construction in Fig. 3, journal p. 714; decomposition theorem in Theorem 1, journal pp. 716-717; tight guard bound in Corollary 1, journal p. 717; holes-with-or-without emphasis and open approximation note in Conclusion, journal p. 719.

- Tracking issue: [#3](https://github.com/alexanderlewisstevens/perimeterover6/issues/3)

### `claim_CanoTothUrrutiaViglietta2022`

- Source: `CanoTothUrrutiaViglietta2022` (Computational Geometry: Theory and Applications)
- Status: `theorem`
- Result: Every polyhedron with m edges can be guarded by at most (5/6)m edge guards; the paper emphasizes the remaining gap to lower bounds.
- Translation note: General 3D edge-guard result. For this review it frames the broader 3D gap around the sharper orthogonal-polyhedron conjectures.
- Locator: Abstract and open-gap discussion, author PDF pp. 1-2; Lemma 10 and Theorem 11, author PDF p. 10; Theorem 12, author PDF p. 11.

- Tracking issue: [#6](https://github.com/alexanderlewisstevens/perimeterover6/issues/6)

### `claim_DiazBanezEtAl2025`

- Source: `DiazBanezEtAl2025` (Graphs and Combinatorics)
- Status: `tight_theorem`
- Result: Every ortho-unit polygon with n >= 12 vertices can be guarded by floor((n-4)/8) guards, tightly.
- Translation note: The ortho-unit theorem is stronger than perimeter/6 in that narrow unit-edge model. It does not by itself prove a theorem for integral orthogonal polygons with arbitrary edge lengths or holes.
- Locator: Theorem 1, arXiv PDF p. 5; proof conclusion, arXiv PDF pp. 10-13.

- Tracking issue: [#8](https://github.com/alexanderlewisstevens/perimeterover6/issues/8)

### `claim_Gyori1986`

- Source: `Gyori1986` (SIAM Journal on Algebraic and Discrete Methods)
- Status: `theorem`
- Result: Provides a short proof of the floor(n/4) rectilinear art-gallery theorem.
- Translation note: Vertex-count theorem for simple orthogonal polygons. It does not address holes or lattice perimeter.
- Locator: SIAM DOI page abstract and article metadata, journal pp. 452-454.

- Tracking issue: [#13](https://github.com/alexanderlewisstevens/perimeterover6/issues/13)

### `claim_KahnKlaweKleitman1983`

- Source: `KahnKlaweKleitman1983` (SIAM Journal on Algebraic and Discrete Methods)
- Status: `tight_theorem`
- Result: Every simple orthogonal n-vertex polygon is guardable by floor(n/4) point guards, and the bound is tight.
- Translation note: Core 2D orthogonal theorem. It is a vertex-count result for simple polygons; holes and perimeter are separate.
- Locator: SIAM DOI page abstract and article metadata, journal pp. 194-206; O'Rourke Chapter 2, Theorems 2.1-2.2, book pp. 45-46.

- Tracking issue: [#15](https://github.com/alexanderlewisstevens/perimeterover6/issues/15)

### `claim_Massberg2014`

- Source: `Massberg2014` (Discrete & Computational Geometry)
- Status: `tight_theorem`
- Result: A hole-free polyomino with lattice perimeter ell can be guarded by at most max(1, floor(ell/6)) point guards; equivalently, floor(ell/6) guards suffice for ell >= 6, and the comb construction shows the bound is tight.
- Translation note: This is the central perimeter-over-six theorem. The source's default convention excludes holes unless otherwise stated, so Theorem 1 covers hole-free integral orthogonal polygons after unit-grid subdivision. It does not prove the hole case.
- Locator: Theorem 1, journal p. 570; proof in Section 4, journal pp. 572-575; tight comb example in Fig. 3 and following paragraph, journal p. 575.

- Tracking issue: [#18](https://github.com/alexanderlewisstevens/perimeterover6/issues/18)

### `claim_MichaelPinciu2016`

- Source: `MichaelPinciu2016` (Discrete & Computational Geometry)
- Status: `theorem`
- Result: Introduces same-sign diagonal graphs and vertex-cover methods, including h-independent upper bounds such as floor((17n-8)/52) for orthogonal polygons with holes.
- Translation note: Important improvement for holes in vertex-count frameworks. It does not settle perimeter-over-six point guards.
- Locator: Springer DOI page abstract and article metadata, Discrete & Computational Geometry 55(2), pp. 410--422; exact-title searches record the diagonal-graph/vertex-cover framework and the floor((17n-8)/52) h-independent bound.

- Tracking issue: [#20](https://github.com/alexanderlewisstevens/perimeterover6/issues/20)

### `claim_PatersonYao1992`

- Source: `PatersonYao1992` (Journal of Algorithms)
- Status: `theorem`
- Result: Binary-space partition result used in the 3D guarding literature to obtain tight Theta(n^(3/2)) point-guard behavior for orthogonal polyhedra.
- Translation note: This blocks a direct linear point-guard analogue in 3D and motivates edge/reflex-edge models.
- Locator: WRAP technical-report PDF application paragraph, p. 4, and Theorems 2--3, pp. 11 and 13; guard-theorem translation cross-checked in Viglietta thesis Theorem 3.7, p. 48.

- Tracking issue: [#23](https://github.com/alexanderlewisstevens/perimeterover6/issues/23)

### `claim_Zylinski2006`

- Source: `Zylinski2006` (Electronic Journal of Combinatorics)
- Status: `theorem`
- Result: Gives a coloring proof of Aggarwal's theorem: floor((n+h)/4) vertex guards suffice for orthogonal polygons with h <= 2 holes and for cactus-dual quadrilateralizations.
- Translation note: Partial positive result for Shermer-type vertex-guard conjectures. It does not settle arbitrary holes or point-guard perimeter bounds.
- Locator: Conjecture 1.1 and Theorems 1.2-1.4, journal PDF p. 2; Theorem 1.5, journal PDF p. 3; final open-status remark, journal PDF p. 10.

- Tracking issue: [#33](https://github.com/alexanderlewisstevens/perimeterover6/issues/33)

## Open and Conditional Problems

### `polyomino_perimeter_holes`

- Title: Perimeter-over-six for polyominoes with holes
- Status: `open_or_conditional`
- Question: If a polyomino has total lattice perimeter ell, including hole boundaries, do max(1, floor(ell/6)) point guards always suffice?
- Known: Massberg proves the hole-free theorem. The hole extension would follow from Conjecture 6.10 in Massberg's habilitation, together with Lemma 6.9. A 2026-05-23 forward-citation pass found only already tracked MassbergHabilitation and Pinciu2015 citing Massberg2014; no tracked source closes this gap.
- Confirming sources: Massberg2014, MassbergHabilitation, BiedlEtAl2012
- Progress paths: Prove the packing conjecture.; Prove the ell/6 bound by another structural method.; Construct a counterexample with holes.

### `massberg_rectangle_packing`

- Title: Massberg maximal-rectangle packing conjecture
- Status: `open`
- Question: Does the maximal-rectangle packing structure needed for Massberg's method hold in rectilinear galleries with holes?
- Known: Massberg's habilitation states Conjecture 6.10: in a rectilinear gallery with holes, the maximum packing size of maximal rectangles should upper-bound the required number of guards.
- Confirming sources: MassbergHabilitation
- Progress paths: Prove the packing statement.; Find the precise obstruction and replace it with a different guard-count invariant.

### `integral_perimeter_beyond_hole_free`

- Title: Integral orthogonal polygon perimeter bounds beyond the hole-free case
- Status: `open_or_conditional`
- Question: Under the broader integral-domain reading, does floor(N/6) point guarding hold when holes or other lattice-domain conventions are allowed?
- Known: The hole-free reading reduces to Massberg's hole-free polyomino theorem by unit-grid subdivision. Diaz-Banez et al.'s integral section gives an N/6 lower-bound family, states an N/5 upper bound with proof not included, and records an N/6 conjecture. The 2026-05-23 forward-citation and exact-title pass found no tracked source that changes the holes/broader-domain status; the 2026-05-26 flat-vertex/formula pass found no primary source for an n/8+f/4 variant.
- Confirming sources: DiazBanezEtAl2025, Massberg2014, MassbergHabilitation
- Progress paths: State the exact integral-domain convention.; Resolve the holes version or reduce it to the polyomino-with-holes problem.

### `orthogonal_holes_vertex_guards`

- Title: Vertex guards for orthogonal polygons with holes
- Status: `open_with_partial_results`
- Question: Do the Shermer floor((n+h)/4) and Hoffmann floor(2n/7) style vertex-guard bounds hold for orthogonal polygons with holes?
- Known: Zylinski proves the floor((n+h)/4) bound for h <= 2 and cactus-dual cases; Michael-Pinciu give improved h-independent bounds. A 2026-05-23 forward/adjacent-model sweep and final OpenAlex/web pass found relevant-looking floodlight and half-plane guarding work, now recorded as explicit adjacent scope exclusions, but no tracked standard vertex-guard resolution.
- Confirming sources: UrrutiaOpenProblems, Zylinski2006, HoffmannKriegel1996, MichaelPinciu2016
- Progress paths: Close the gap between conjectured bounds and h-independent upper bounds.; Classify quadrilateralization or diagonal-graph structures that force the conjectured color class.

### `orthogonal_polyhedra_edge_guards`

- Title: Urrutia-type edge-guard bounds for orthogonal polyhedra
- Status: `open_with_partial_results`
- Question: Can genus-zero orthogonal polyhedra with m edges be guarded with m/12 + O(1) closed edge guards?
- Known: Benbernou et al. prove floor((e+r)/12) open edge guards and the derived (11/72)e and (7/12)r parameterized upper bounds, but these do not reach the conjectured m/12 + O(1) closed-edge target; Viglietta's thesis records the point-guard obstruction and edge-guard direction. A 2026-05-23 OpenAlex/web forward and venue pass found no tracked source closing the general gap. Aldana-Galvan et al. give an adjacent pi/2-edge-guard theorem, but that is a limited-field model rather than a standard edge-guard closure.
- Confirming sources: VigliettaThesis, BenbernouEtAl2011, CanoTothUrrutiaViglietta2022
- Progress paths: Improve edge-guard upper bounds for orthogonal polyhedra.; Find lower-bound constructions requiring a larger correction term.

### `orthogonal_polyhedra_reflex_edge_guards`

- Title: Reflex-edge guards in general orthogonal polyhedra
- Status: `open_with_partial_results`
- Question: Can the tight 2-reflex reflex-edge-guard behavior be extended to general 3-reflex orthogonal polyhedra?
- Known: Viglietta proves strong results for 2-reflex orthogonal polyhedra; Benbernou et al. give edge-guard bounds parameterized by r and conjectural evidence around open reflex edges, but the general reflex-edge-only case remains open. A 2026-05-23 OpenAlex/web forward and venue pass found no tracked source closing this general reflex-edge-only case.
- Confirming sources: Viglietta2020, VigliettaThesis, BenbernouEtAl2011
- Progress paths: Extend induction or charging methods beyond two reflex-edge directions.; Identify a counterexample to the direct generalization.

### `general_edge_guard_gap`

- Title: General 3D polyhedron edge-guard gap
- Status: `open_with_partial_results`
- Question: How close can the best edge-guard upper bound for arbitrary polyhedra be brought to known lower-bound constructions?
- Known: Cano, Toth, Urrutia, and Viglietta prove a (5/6)m edge-guard upper bound for arbitrary m-edge polyhedra and leave a substantial gap to known lower bounds.
- Confirming sources: CanoTothUrrutiaViglietta2022
- Progress paths: Improve the general upper bound.; Separate the arbitrary-polyhedron and orthogonal-polyhedron gaps with sharper examples.

### `algorithmic_restricted_cases`

- Title: Algorithmic restricted cases aligned with extremal bounds
- Status: `active_research_direction`
- Question: Which restricted orthogonal, polyomino, or polyhedral models admit exact polynomial algorithms or useful approximation guarantees for minimum guarding?
- Known: General and many orthogonal variants are hard; several restricted visibility models have approximation or hardness results. The currently cited sliding-camera, sliding-transmitter, k-hop, polyform, face-guard, and 2-reflex variants have separate coverage cells; floodlight, half-plane, dispersive, contiguous, mobile, point-boundary, and related variants have explicit scope-exclusion cells unless promoted with source and claim records.
- Confirming sources: LeeLin1986, SchuchardtHecker1995, KatzRoisman2008, DurocherEtAl2017, BiedlEtAl2019, FiltserEtAl2025, Ghosh2010
- Progress paths: Find exact algorithms for natural subclasses.; Connect approximation algorithms to the structural decompositions used in extremal proofs.

## Conditional or Open Claim Records

- `claim_DiazBanezEtAl2025_integral_N6_conjecture` (`conjecture`): The paper conjectures that every integral orthogonal polygon of perimeter N can be guarded with at most floor(N/6) guards.
- `claim_MassbergHabilitation` (`conditional`): Conjecture 6.10 states that, in any rectilinear gallery that may contain holes, the maximum size of a packing of maximal rectangles is an upper bound on the number of guards required; if true, Lemma 6.9 would extend the perimeter-over-six theorem to polyominoes with holes.
- `claim_UrrutiaOpenProblems` (`open_problem`): Records Shermer's floor((n+h)/4) vertex-guard conjecture and Hoffmann's floor(2n/7) vertex-guard conjecture for orthogonal polygons with holes.

## Coverage Matrix

### `simple_orthogonal_polygons_point_guards_vertex_count`

- Title: Simple orthogonal polygons, point guards, vertex count
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: The floor(n/4) bound is proven tight for simple orthogonal polygons.
- Supporting claims: claim_KahnKlaweKleitman1983, claim_Gyori1986
- Next action: KKK and Gyori locators are now recorded from SIAM metadata, with O'Rourke book cross-checks for Theorems 2.1--2.2; full primary proof text can still be checked if access is available.

### `orthogonal_polygons_with_holes_vertex_guards`

- Title: Orthogonal polygons with holes, vertex guards
- Coverage status: `synthesized`
- Result status: `open_with_partial_results`
- Summary: Shermer/Hoffmann-style bounds remain open in general; cactus-dual, h <= 2, and h-independent upper-bound results are known.
- Supporting claims: claim_UrrutiaOpenProblems, claim_Zylinski2006, claim_HoffmannKriegel1996, claim_MichaelPinciu2016
- Next action: Urrutia, Zylinski, Hoffmann--Kriegel, and Michael--Pinciu locators are recorded. A 2026-05-23 forward/adjacent-model sweep and final OpenAlex/web pass found no tracked source changing this open-with-partial-results status; continue periodic exact-title and venue scans. Floodlight, half-plane, and other restricted-visibility variants require source and claim records before theorem-level treatment.

### `hole_free_polyominoes_point_guards_lattice_perimeter`

- Title: Hole-free polyominoes, point guards, lattice perimeter
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: Massberg proves the tight floor(ell/6) perimeter theorem for hole-free polyominoes.
- Supporting claims: claim_Massberg2014
- Next action: Complete unless a later pass adds algorithmic construction details.

### `polyominoes_with_holes_point_guards_lattice_perimeter`

- Title: Polyominoes with holes, point guards, lattice perimeter
- Coverage status: `open_gap`
- Result status: `conditional`
- Summary: The perimeter-over-six extension to holes is conditional on Massberg's maximal-rectangle packing conjecture.
- Supporting claims: claim_MassbergHabilitation, claim_Massberg2014
- Next action: Complete for the Massberg conditional route. A 2026-05-23 OpenAlex forward-citation pass for Massberg2014 found only Pinciu2015 and MassbergHabilitation as citing works; both are already tracked and neither is an independent proof of the ell/6 holes extension. Keep area/cell-count and discrete-visibility variants separate from the perimeter claim.

### `polyominoes_with_holes_point_guards_area`

- Title: Polyominoes with holes, point guards, cell count
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: Biedl et al. prove the tight floor((m+1)/3) theorem for connected m-cell polyominoes with m >= 2, holes allowed; m=1 is the trivial one-guard case.
- Supporting claims: claim_BiedlEtAl2012
- Next action: Complete for the main cell-count theorem; a later algorithmic pass can separate the related SoCG 2011 complexity results.

### `ortho_unit_polygons_point_guards_perimeter`

- Title: Ortho-unit polygons, point guards, perimeter
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: Diaz-Banez et al. prove the tight floor((n-4)/8) theorem for ortho-unit polygons.
- Supporting claims: claim_DiazBanezEtAl2025
- Next action: Clarify any remaining source-specific hole conventions from the primary text; keep the integral-perimeter conjecture separate from the ortho-unit theorem and from the Massberg overlap. A 2026-05-23 OpenAlex pass found no citing works for DiazBanezEtAl2025 and no status-changing exact-title or topic hit; a 2026-05-26 flat-vertex/formula search found no n/8+f/4 variant in the primary arXiv source or exact web searches.

### `integral_orthogonal_polygons_point_guards_perimeter`

- Title: Integral orthogonal polygons, point guards, perimeter
- Coverage status: `synthesized`
- Result status: `open_or_conditional_beyond_hole_free`
- Summary: Hole-free integral polygons reduce to hole-free polyominoes; broader versions with holes remain open or conditional.
- Supporting claims: claim_Massberg2014, claim_DiazBanezEtAl2025_integral_lower_bound, claim_DiazBanezEtAl2025_integral_n5_upper_statement, claim_DiazBanezEtAl2025_integral_N6_conjecture, claim_MassbergHabilitation
- Next action: The hole-free overlap is recorded. The 2026-05-26 targeted search found no primary source for an n/8+f/4 bound using flat vertices or faces; before stating any standalone broader-domain or flat-vertex parameter problem, specify whether holes, disconnected domains, inserted collinear grid points, or a different lattice-domain convention are intended.

### `orthogonal_polyhedra_point_guards`

- Title: Orthogonal polyhedra, point guards
- Coverage status: `synthesized`
- Result status: `theorem`
- Summary: Paterson-Yao/Viglietta give Theta(n^(3/2)) point-guard behavior, blocking a direct planar linear analogue.
- Supporting claims: claim_PatersonYao1992, claim_VigliettaThesis
- Next action: Paterson--Yao BSP locators and Viglietta thesis guard-translation locator are recorded; next action is optional full journal-version access if needed.

### `orthogonal_polyhedra_edge_and_reflex_edge_guards`

- Title: Orthogonal polyhedra, edge and reflex-edge guards
- Coverage status: `synthesized`
- Result status: `open_with_partial_results`
- Summary: Known edge/reflex-edge upper bounds do not yet reach Urrutia-type lower-bound targets; 2-reflex cases are much better understood.
- Supporting claims: claim_BenbernouEtAl2011, claim_VigliettaThesis, claim_Viglietta2020, claim_CanoTothUrrutiaViglietta2022
- Next action: Cano--Toth--Urrutia--Viglietta, Viglietta thesis, Benbernou, and Viglietta 2020 locators are recorded. A 2026-05-23 OpenAlex/web forward and venue pass found no tracked result closing the general edge/reflex-edge gaps; face guards, pi/2-edge guards, 2-reflex restrictions, and discrete polyform variants are represented in separate adjacent-model cells.

### `orthogonal_polyhedra_pi_over_2_edge_guards`

- Title: Orthogonal polyhedra, pi/2-edge guards
- Coverage status: `synthesized`
- Result status: `adjacent_limited_field_theorem`
- Summary: Aldana-Galvan et al. prove a pi/2-edge-guard bound for orthogonal polyhedra; the guard model is adjacent to, but distinct from, standard edge guards.
- Supporting claims: claim_AldanaGalvanEtAl2016
- Next action: Use only as adjacent 3D model context unless the review expands to limited-field edge-guard variants.

### `rectilinear_polygons_edge_guards_2d`

- Title: Rectilinear polygons, edge guards
- Coverage status: `synthesized`
- Result status: `tight_theorem_context`
- Summary: Bjorling-Sachs gives the 2D rectilinear edge-guard reference point used when comparing edge-guard models.
- Supporting claims: claim_BjorlingSachs1998
- Next action: Keep this cell as 2D edge-guard context; do not translate it into point-guard perimeter or 3D edge-guard statements.

### `orthogonal_polygons_sliding_camera_transmitter_visibility`

- Title: Orthogonal polygons, sliding cameras and sliding k-transmitters
- Coverage status: `synthesized`
- Result status: `restricted_visibility_context`
- Summary: Sliding-camera and sliding k-transmitter results form a restricted-visibility algorithmic line, not a standard point-guard perimeter theorem.
- Supporting claims: claim_DurocherEtAl2017, claim_BiedlEtAl2019
- Next action: Extract theorem-level algorithmic statements only if the review expands beyond extremal counting bounds.

### `orthogonal_polygons_floodlight_half_plane_visibility`

- Title: Orthogonal polygons, floodlights and half-plane guards
- Coverage status: `scope_excluded_adjacent`
- Result status: `restricted_visibility_out_of_scope`
- Summary: Floodlight and half-plane guarding results use directional or restricted visibility and are not standard point-guard, vertex-guard, or perimeter-over-six theorems.
- Evidence role: Scope-exclusion cell; this records a model decision, not a theorem-level claim.
- Supporting theorem claims: None recorded; this is expected for a scope-exclusion cell.
- Next action: Keep as an explicit exclusion unless a specific theorem is promoted into the review; promotion requires source, claim, locator, and translation records first.

### `guarding_variants_optimization_and_motion_models`

- Title: Dispersive, contiguous, mobile, point-boundary, and related guarding variants
- Coverage status: `scope_excluded_adjacent`
- Result status: `optimization_or_motion_variant_out_of_scope`
- Summary: These variants are useful for search completeness and terminology, but their objectives or guard behavior differ from the extremal point/vertex/edge-guard bounds surveyed here.
- Evidence role: Scope-exclusion cell; this records a model decision, not a theorem-level claim.
- Supporting theorem claims: None recorded; this is expected for a scope-exclusion cell.
- Next action: Record exact source and claim data only if the paper later discusses one of these variants beyond an exclusion note.

### `polyomino_discrete_k_hop_and_polyform_visibility`

- Title: Polyominoes and polyforms, discrete visibility variants
- Coverage status: `synthesized`
- Result status: `discrete_visibility_context`
- Summary: k-hop and polyform visibility results are discrete analogues and algorithmic context, not straight-line point-guard perimeter results.
- Supporting claims: claim_FiltserEtAl2025, claim_Pinciu2015
- Next action: Keep discrete visibility and continuous orthogonal-polyhedron visibility separate unless a future source explicitly bridges them.

### `orthogonal_polyhedra_face_guards`

- Title: Orthogonal polyhedra and related classes, face guards
- Coverage status: `synthesized`
- Result status: `face_guard_context`
- Summary: Face-guard results map part of the 3D model space but are not edge-guard, reflex-edge-guard, or point-guard perimeter analogues.
- Supporting claims: claim_VigliettaFace2014
- Next action: If face guards become more than context, add theorem-level subclaims by polyhedron class.

### `orthogonal_polyhedra_2_reflex_reflex_edge_guards`

- Title: 2-reflex orthogonal polyhedra, reflex-edge guards
- Coverage status: `synthesized`
- Result status: `tight_theorem_for_restricted_class`
- Summary: Viglietta proves tight-style reflex-edge guard bounds for 2-reflex orthogonal polyhedra, a restricted class that does not settle general 3-reflex cases.
- Supporting claims: claim_Viglietta2020
- Next action: Use as the restricted-class positive result when explaining why the general reflex-edge problem remains open.

### `algorithmic_and_restricted_visibility_context`

- Title: Algorithmic and restricted-visibility context
- Coverage status: `synthesized`
- Result status: `hardness_and_approximation_context`
- Summary: Optimization hardness and restricted visibility variants provide context but do not settle extremal perimeter bounds.
- Supporting claims: claim_LeeLin1986, claim_SchuchardtHecker1995, claim_KatzRoisman2008, claim_AbrahamsenAdamaszekMiltzow2022, claim_Ghosh2010, claim_DurocherEtAl2017, claim_BiedlEtAl2019, claim_FiltserEtAl2025, claim_Pinciu2015
- Next action: Core restricted-visibility, hardness, and approximation locators are recorded. The currently cited adjacent variants now have separate cells, and the currently excluded adjacent variants now have explicit scope-exclusion cells; newly discovered variants should receive a scope decision before theorem-level use.

## Verification Gaps

- No missing locators recorded.

## Search and Completeness Gaps

- No coverage cells are currently marked `unsearched` or `searching`.
- Scope-exclusion cells tracked: `orthogonal_polygons_floodlight_half_plane_visibility`, `guarding_variants_optimization_and_motion_models`.
- Search log present: `literature/search_log.md`.
- Progress tracker present: `literature/framework_progress.md`.
- Document assembly map present: `literature/document_assembly.md`.

## Next Actions

- Simple orthogonal polygons, point guards, vertex count: KKK and Gyori locators are now recorded from SIAM metadata, with O'Rourke book cross-checks for Theorems 2.1--2.2; full primary proof text can still be checked if access is available.
- Orthogonal polygons with holes, vertex guards: Urrutia, Zylinski, Hoffmann--Kriegel, and Michael--Pinciu locators are recorded. A 2026-05-23 forward/adjacent-model sweep and final OpenAlex/web pass found no tracked source changing this open-with-partial-results status; continue periodic exact-title and venue scans. Floodlight, half-plane, and other restricted-visibility variants require source and claim records before theorem-level treatment.
- Hole-free polyominoes, point guards, lattice perimeter: Complete unless a later pass adds algorithmic construction details.
- Polyominoes with holes, point guards, lattice perimeter: Complete for the Massberg conditional route. A 2026-05-23 OpenAlex forward-citation pass for Massberg2014 found only Pinciu2015 and MassbergHabilitation as citing works; both are already tracked and neither is an independent proof of the ell/6 holes extension. Keep area/cell-count and discrete-visibility variants separate from the perimeter claim.
- Polyominoes with holes, point guards, cell count: Complete for the main cell-count theorem; a later algorithmic pass can separate the related SoCG 2011 complexity results.
- Ortho-unit polygons, point guards, perimeter: Clarify any remaining source-specific hole conventions from the primary text; keep the integral-perimeter conjecture separate from the ortho-unit theorem and from the Massberg overlap. A 2026-05-23 OpenAlex pass found no citing works for DiazBanezEtAl2025 and no status-changing exact-title or topic hit; a 2026-05-26 flat-vertex/formula search found no n/8+f/4 variant in the primary arXiv source or exact web searches.
- Integral orthogonal polygons, point guards, perimeter: The hole-free overlap is recorded. The 2026-05-26 targeted search found no primary source for an n/8+f/4 bound using flat vertices or faces; before stating any standalone broader-domain or flat-vertex parameter problem, specify whether holes, disconnected domains, inserted collinear grid points, or a different lattice-domain convention are intended.
- Orthogonal polyhedra, point guards: Paterson--Yao BSP locators and Viglietta thesis guard-translation locator are recorded; next action is optional full journal-version access if needed.
- Orthogonal polyhedra, edge and reflex-edge guards: Cano--Toth--Urrutia--Viglietta, Viglietta thesis, Benbernou, and Viglietta 2020 locators are recorded. A 2026-05-23 OpenAlex/web forward and venue pass found no tracked result closing the general edge/reflex-edge gaps; face guards, pi/2-edge guards, 2-reflex restrictions, and discrete polyform variants are represented in separate adjacent-model cells.
- Orthogonal polyhedra, pi/2-edge guards: Use only as adjacent 3D model context unless the review expands to limited-field edge-guard variants.
- Rectilinear polygons, edge guards: Keep this cell as 2D edge-guard context; do not translate it into point-guard perimeter or 3D edge-guard statements.
- Orthogonal polygons, sliding cameras and sliding k-transmitters: Extract theorem-level algorithmic statements only if the review expands beyond extremal counting bounds.
- Orthogonal polygons, floodlights and half-plane guards: Keep as an explicit exclusion unless a specific theorem is promoted into the review; promotion requires source, claim, locator, and translation records first.
- Dispersive, contiguous, mobile, point-boundary, and related guarding variants: Record exact source and claim data only if the paper later discusses one of these variants beyond an exclusion note.
- Polyominoes and polyforms, discrete visibility variants: Keep discrete visibility and continuous orthogonal-polyhedron visibility separate unless a future source explicitly bridges them.
- Orthogonal polyhedra and related classes, face guards: If face guards become more than context, add theorem-level subclaims by polyhedron class.
- 2-reflex orthogonal polyhedra, reflex-edge guards: Use as the restricted-class positive result when explaining why the general reflex-edge problem remains open.
- Algorithmic and restricted-visibility context: Core restricted-visibility, hardness, and approximation locators are recorded. The currently cited adjacent variants now have separate cells, and the currently excluded adjacent variants now have explicit scope-exclusion cells; newly discovered variants should receive a scope decision before theorem-level use.

See `literature/framework_progress.md` for the framework-stage work queue.
See `literature/document_assembly.md` for the reader-facing document flow.
