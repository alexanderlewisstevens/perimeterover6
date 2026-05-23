# Evidence Report

Generated from the structured literature ledgers. This report is an audit companion for the review paper, not a substitute for the prose.

## Summary

- Sources: 33
- Claims: 33
- Coverage cells: 10
- Open-problem clusters: 8
- Claims missing page/theorem locators: 32
- Coverage cells still unsearched/searching: 0

## Status Counts

### Source Statuses

- `approximation`: 1
- `conditional`: 1
- `hardness`: 5
- `open_problem`: 1
- `survey`: 4
- `theorem`: 14
- `tight_theorem`: 7

### Claim Types

- `approximation`: 1
- `conditional`: 1
- `hardness`: 5
- `open_problem`: 1
- `survey`: 4
- `theorem`: 14
- `tight_theorem`: 7

### Coverage Statuses

- `open_gap`: 1
- `synthesized`: 9

### Open-Problem Statuses

- `active_research_direction`: 1
- `open`: 1
- `open_or_conditional`: 2
- `open_with_partial_results`: 4

## Major Proven Results

### `claim_BenbernouEtAl2011`

- Source: `BenbernouEtAl2011` (Canadian Conference on Computational Geometry)
- Status: `theorem`
- Result: Improves asymptotic orthogonal-polyhedron edge-guard upper bounds to (11/72)m edge guards and (7/12)r reflex-edge-style bounds.
- Translation note: This is a 3D edge-guard result, not a point-guard or perimeter result. It is central evidence for the remaining gap to Urrutia-type m/12 + O(1) targets.
- Locator: not_recorded

- Tracking issue: [#2](https://github.com/alexanderlewisstevens/perimeterover6/issues/2)

### `claim_BiedlEtAl2012`

- Source: `BiedlEtAl2012` (Discrete & Computational Geometry)
- Status: `tight_theorem`
- Result: Every m-cell polyomino, possibly with holes, can be guarded by floor((m+1)/3) point guards; the bound is sometimes necessary.
- Translation note: This is an area/cell-count theorem. It does not imply a perimeter-over-six theorem because area and perimeter are incomparable for the needed extremal question.
- Locator: not_recorded

- Tracking issue: [#3](https://github.com/alexanderlewisstevens/perimeterover6/issues/3)

### `claim_CanoTothUrrutiaViglietta2022`

- Source: `CanoTothUrrutiaViglietta2022` (Computational Geometry: Theory and Applications)
- Status: `theorem`
- Result: Every polyhedron with m edges can be guarded by at most (5/6)m edge guards; the paper emphasizes the remaining gap to lower bounds.
- Translation note: General 3D edge-guard result. For this review it frames the broader 3D gap around the sharper orthogonal-polyhedron conjectures.
- Locator: not_recorded

- Tracking issue: [#6](https://github.com/alexanderlewisstevens/perimeterover6/issues/6)

### `claim_DiazBanezEtAl2025`

- Source: `DiazBanezEtAl2025` (Graphs and Combinatorics)
- Status: `tight_theorem`
- Result: Every ortho-unit polygon with n >= 12 vertices can be guarded by floor((n-4)/8) guards, tightly. The paper also frames an integral-perimeter N/6 direction.
- Translation note: The ortho-unit theorem is stronger than perimeter/6 in that narrow unit-edge model. The hole-free integral N/6 reading is covered by Massberg after subdivision; only holes or broader lattice-domain readings remain open.
- Locator: not_recorded

- Tracking issue: [#8](https://github.com/alexanderlewisstevens/perimeterover6/issues/8)

### `claim_Gyori1986`

- Source: `Gyori1986` (SIAM Journal on Algebraic and Discrete Methods)
- Status: `theorem`
- Result: Provides a short proof of the floor(n/4) rectilinear art-gallery theorem.
- Translation note: Vertex-count theorem for simple orthogonal polygons. It does not address holes or lattice perimeter.
- Locator: not_recorded

- Tracking issue: [#13](https://github.com/alexanderlewisstevens/perimeterover6/issues/13)

### `claim_KahnKlaweKleitman1983`

- Source: `KahnKlaweKleitman1983` (SIAM Journal on Algebraic and Discrete Methods)
- Status: `tight_theorem`
- Result: Every simple orthogonal n-vertex polygon is guardable by floor(n/4) point guards, and the bound is tight.
- Translation note: Core 2D orthogonal theorem. It is a vertex-count result for simple polygons; holes and perimeter are separate.
- Locator: not_recorded

- Tracking issue: [#15](https://github.com/alexanderlewisstevens/perimeterover6/issues/15)

### `claim_Massberg2014`

- Source: `Massberg2014` (Discrete & Computational Geometry)
- Status: `tight_theorem`
- Result: A hole-free polyomino with perimeter ell >= 6 can be guarded by at most floor(ell/6) point guards; the bound is tight.
- Translation note: This is the central perimeter-over-six theorem. It covers hole-free integral orthogonal polygons after unit-grid subdivision. It does not prove the hole case.
- Locator: not_recorded

- Tracking issue: [#18](https://github.com/alexanderlewisstevens/perimeterover6/issues/18)

### `claim_MichaelPinciu2016`

- Source: `MichaelPinciu2016` (Discrete & Computational Geometry)
- Status: `theorem`
- Result: Introduces same-sign diagonal graphs and vertex-cover methods, including h-independent upper bounds such as floor((17n-8)/52) for orthogonal polygons with holes.
- Translation note: Important improvement for holes in vertex-count frameworks. It does not settle perimeter-over-six point guards.
- Locator: not_recorded

- Tracking issue: [#20](https://github.com/alexanderlewisstevens/perimeterover6/issues/20)

### `claim_PatersonYao1992`

- Source: `PatersonYao1992` (Journal of Algorithms)
- Status: `theorem`
- Result: Binary-space partition result used in the 3D guarding literature to obtain tight Theta(n^(3/2)) point-guard behavior for orthogonal polyhedra.
- Translation note: This blocks a direct linear point-guard analogue in 3D and motivates edge/reflex-edge models.
- Locator: not_recorded

- Tracking issue: [#23](https://github.com/alexanderlewisstevens/perimeterover6/issues/23)

### `claim_Zylinski2006`

- Source: `Zylinski2006` (Electronic Journal of Combinatorics)
- Status: `theorem`
- Result: Gives a coloring proof of Aggarwal's theorem: floor((n+h)/4) vertex guards suffice for orthogonal polygons with h <= 2 holes and for cactus-dual quadrilateralizations.
- Translation note: Partial positive result for Shermer-type vertex-guard conjectures. It does not settle arbitrary holes or point-guard perimeter bounds.
- Locator: not_recorded

- Tracking issue: [#33](https://github.com/alexanderlewisstevens/perimeterover6/issues/33)

## Open and Conditional Problems

### `polyomino_perimeter_holes`

- Title: Perimeter-over-six for polyominoes with holes
- Status: `open_or_conditional`
- Question: If a polyomino has total lattice perimeter ell, including hole boundaries, do max(1, floor(ell/6)) point guards always suffice?
- Known: Massberg proves the hole-free theorem. The hole extension is identified as conditional on a maximal-rectangle packing conjecture.
- Confirming sources: Massberg2014, MassbergHabilitation, BiedlEtAl2012
- Progress paths: Prove the packing conjecture.; Prove the ell/6 bound by another structural method.; Construct a counterexample with holes.

### `massberg_rectangle_packing`

- Title: Massberg maximal-rectangle packing conjecture
- Status: `open`
- Question: Does the maximal-rectangle packing structure needed for Massberg's method hold in rectilinear galleries with holes?
- Known: Massberg's habilitation identifies this as the missing ingredient for extending the perimeter theorem to holes.
- Confirming sources: MassbergHabilitation
- Progress paths: Prove the packing statement.; Find the precise obstruction and replace it with a different guard-count invariant.

### `integral_perimeter_beyond_hole_free`

- Title: Integral orthogonal polygon perimeter bounds beyond the hole-free case
- Status: `open_or_conditional`
- Question: Under the broader integral-domain reading, does floor(N/6) point guarding hold when holes or other lattice-domain conventions are allowed?
- Known: The hole-free reading reduces to Massberg's hole-free polyomino theorem by unit-grid subdivision.
- Confirming sources: DiazBanezEtAl2025, Massberg2014, MassbergHabilitation
- Progress paths: State the exact integral-domain convention.; Resolve the holes version or reduce it to the polyomino-with-holes problem.

### `orthogonal_holes_vertex_guards`

- Title: Vertex guards for orthogonal polygons with holes
- Status: `open_with_partial_results`
- Question: Do the Shermer floor((n+h)/4) and Hoffmann floor(2n/7) style vertex-guard bounds hold for orthogonal polygons with holes?
- Known: Zylinski proves the floor((n+h)/4) bound for h <= 2 and cactus-dual cases; Michael-Pinciu give improved h-independent bounds.
- Confirming sources: UrrutiaOpenProblems, Zylinski2006, HoffmannKriegel1996, MichaelPinciu2016
- Progress paths: Close the gap between conjectured bounds and h-independent upper bounds.; Classify quadrilateralization or diagonal-graph structures that force the conjectured color class.

### `orthogonal_polyhedra_edge_guards`

- Title: Urrutia-type edge-guard bounds for orthogonal polyhedra
- Status: `open_with_partial_results`
- Question: Can genus-zero orthogonal polyhedra with m edges be guarded with m/12 + O(1) closed edge guards?
- Known: Benbernou et al. improve upper bounds but do not reach the conjectured target; Viglietta's thesis records the point-guard obstruction and edge-guard direction.
- Confirming sources: VigliettaThesis, BenbernouEtAl2011, CanoTothUrrutiaViglietta2022
- Progress paths: Improve edge-guard upper bounds for orthogonal polyhedra.; Find lower-bound constructions requiring a larger correction term.

### `orthogonal_polyhedra_reflex_edge_guards`

- Title: Reflex-edge guards in general orthogonal polyhedra
- Status: `open_with_partial_results`
- Question: Can the tight 2-reflex reflex-edge-guard behavior be extended to general 3-reflex orthogonal polyhedra?
- Known: Viglietta proves strong results for 2-reflex orthogonal polyhedra; the general case remains open.
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
- Known: General and many orthogonal variants are hard; several restricted visibility models have approximation or hardness results.
- Confirming sources: LeeLin1986, SchuchardtHecker1995, KatzRoisman2008, DurocherEtAl2017, BiedlEtAl2019, FiltserEtAl2025, Ghosh2010
- Progress paths: Find exact algorithms for natural subclasses.; Connect approximation algorithms to the structural decompositions used in extremal proofs.

## Conditional or Open Claim Records

- `claim_MassbergHabilitation` (`conditional`): States a maximal-rectangle packing conjecture whose truth would extend the perimeter-over-six method to hole cases.
- `claim_UrrutiaOpenProblems` (`open_problem`): Records Shermer's floor((n+h)/4) vertex-guard conjecture and Hoffmann's floor(2n/7) vertex-guard conjecture for orthogonal polygons with holes.

## Coverage Matrix

### `simple_orthogonal_polygons_point_guards_vertex_count`

- Title: Simple orthogonal polygons, point guards, vertex count
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: The floor(n/4) bound is proven tight for simple orthogonal polygons.
- Supporting claims: claim_KahnKlaweKleitman1983, claim_Gyori1986
- Next action: Record page/theorem locators from primary sources.

### `orthogonal_polygons_with_holes_vertex_guards`

- Title: Orthogonal polygons with holes, vertex guards
- Coverage status: `synthesized`
- Result status: `open_with_partial_results`
- Summary: Shermer/Hoffmann-style bounds remain open in general; cactus-dual, h <= 2, and h-independent upper-bound results are known.
- Supporting claims: claim_UrrutiaOpenProblems, claim_Zylinski2006, claim_HoffmannKriegel1996, claim_MichaelPinciu2016
- Next action: Primary-check exact theorem statements and page locators for the partial bounds.

### `hole_free_polyominoes_point_guards_lattice_perimeter`

- Title: Hole-free polyominoes, point guards, lattice perimeter
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: Massberg proves the tight floor(ell/6) perimeter theorem for hole-free polyominoes.
- Supporting claims: claim_Massberg2014
- Next action: Record theorem/page locator and lower-bound construction details.

### `polyominoes_with_holes_point_guards_lattice_perimeter`

- Title: Polyominoes with holes, point guards, lattice perimeter
- Coverage status: `open_gap`
- Result status: `conditional`
- Summary: The perimeter-over-six extension to holes is conditional on Massberg's maximal-rectangle packing conjecture.
- Supporting claims: claim_MassbergHabilitation, claim_Massberg2014
- Next action: Extract the exact Conjecture 6.10 statement and surrounding examples from Massberg's habilitation.

### `polyominoes_with_holes_point_guards_area`

- Title: Polyominoes with holes, point guards, cell count
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: Biedl et al. prove the tight floor((m+1)/3) theorem for m-cell polyominoes, holes allowed.
- Supporting claims: claim_BiedlEtAl2012
- Next action: Record theorem/page locator and examples showing tightness.

### `ortho_unit_polygons_point_guards_perimeter`

- Title: Ortho-unit polygons, point guards, perimeter
- Coverage status: `synthesized`
- Result status: `tight_theorem`
- Summary: Diaz-Banez et al. prove the tight floor((n-4)/8) theorem for ortho-unit polygons.
- Supporting claims: claim_DiazBanezEtAl2025
- Next action: Record exact theorem locator and clarify hole assumptions from the primary paper.

### `integral_orthogonal_polygons_point_guards_perimeter`

- Title: Integral orthogonal polygons, point guards, perimeter
- Coverage status: `synthesized`
- Result status: `open_or_conditional_beyond_hole_free`
- Summary: Hole-free integral polygons reduce to hole-free polyominoes; broader versions with holes remain open or conditional.
- Supporting claims: claim_Massberg2014, claim_DiazBanezEtAl2025, claim_MassbergHabilitation
- Next action: Make the exact broader domain convention explicit before stating a standalone open problem.

### `orthogonal_polyhedra_point_guards`

- Title: Orthogonal polyhedra, point guards
- Coverage status: `synthesized`
- Result status: `theorem`
- Summary: Paterson-Yao/Viglietta give Theta(n^(3/2)) point-guard behavior, blocking a direct planar linear analogue.
- Supporting claims: claim_PatersonYao1992, claim_VigliettaThesis
- Next action: Primary-check the precise transfer from binary-space partitions to the guarding statement.

### `orthogonal_polyhedra_edge_and_reflex_edge_guards`

- Title: Orthogonal polyhedra, edge and reflex-edge guards
- Coverage status: `synthesized`
- Result status: `open_with_partial_results`
- Summary: Known edge/reflex-edge upper bounds do not yet reach Urrutia-type lower-bound targets; 2-reflex cases are much better understood.
- Supporting claims: claim_BenbernouEtAl2011, claim_VigliettaThesis, claim_Viglietta2020, claim_CanoTothUrrutiaViglietta2022
- Next action: Separate arbitrary-polyhedron bounds from orthogonal-specific conjectures in claim locators.

### `algorithmic_and_restricted_visibility_context`

- Title: Algorithmic and restricted-visibility context
- Coverage status: `synthesized`
- Result status: `hardness_and_approximation_context`
- Summary: Optimization hardness and restricted visibility variants provide context but do not settle extremal perimeter bounds.
- Supporting claims: claim_LeeLin1986, claim_SchuchardtHecker1995, claim_KatzRoisman2008, claim_AbrahamsenAdamaszekMiltzow2022, claim_Ghosh2010, claim_DurocherEtAl2017, claim_BiedlEtAl2019, claim_FiltserEtAl2025, claim_Pinciu2015
- Next action: Decide which adjacent models deserve deeper theorem-level extraction versus brief survey treatment.

## Verification Gaps

- `claim_BenbernouEtAl2011` needs page/theorem locator ([#2](https://github.com/alexanderlewisstevens/perimeterover6/issues/2)).
- `claim_BiedlEtAl2012` needs page/theorem locator ([#3](https://github.com/alexanderlewisstevens/perimeterover6/issues/3)).
- `claim_BiedlEtAl2019` needs page/theorem locator ([#4](https://github.com/alexanderlewisstevens/perimeterover6/issues/4)).
- `claim_BjorlingSachs1998` needs page/theorem locator ([#5](https://github.com/alexanderlewisstevens/perimeterover6/issues/5)).
- `claim_CanoTothUrrutiaViglietta2022` needs page/theorem locator ([#6](https://github.com/alexanderlewisstevens/perimeterover6/issues/6)).
- `claim_Chvatal1975` needs page/theorem locator ([#7](https://github.com/alexanderlewisstevens/perimeterover6/issues/7)).
- `claim_DiazBanezEtAl2025` needs page/theorem locator ([#8](https://github.com/alexanderlewisstevens/perimeterover6/issues/8)).
- `claim_DurocherEtAl2017` needs page/theorem locator ([#9](https://github.com/alexanderlewisstevens/perimeterover6/issues/9)).
- `claim_FiltserEtAl2025` needs page/theorem locator ([#10](https://github.com/alexanderlewisstevens/perimeterover6/issues/10)).
- `claim_Fisk1978` needs page/theorem locator ([#11](https://github.com/alexanderlewisstevens/perimeterover6/issues/11)).
- `claim_Ghosh2010` needs page/theorem locator ([#12](https://github.com/alexanderlewisstevens/perimeterover6/issues/12)).
- `claim_Gyori1986` needs page/theorem locator ([#13](https://github.com/alexanderlewisstevens/perimeterover6/issues/13)).
- `claim_HoffmannKriegel1996` needs page/theorem locator ([#14](https://github.com/alexanderlewisstevens/perimeterover6/issues/14)).
- `claim_KahnKlaweKleitman1983` needs page/theorem locator ([#15](https://github.com/alexanderlewisstevens/perimeterover6/issues/15)).
- `claim_KatzRoisman2008` needs page/theorem locator ([#16](https://github.com/alexanderlewisstevens/perimeterover6/issues/16)).
- `claim_LeeLin1986` needs page/theorem locator ([#17](https://github.com/alexanderlewisstevens/perimeterover6/issues/17)).
- `claim_Massberg2014` needs page/theorem locator ([#18](https://github.com/alexanderlewisstevens/perimeterover6/issues/18)).
- `claim_MassbergHabilitation` needs page/theorem locator ([#19](https://github.com/alexanderlewisstevens/perimeterover6/issues/19)).
- `claim_MichaelPinciu2016` needs page/theorem locator ([#20](https://github.com/alexanderlewisstevens/perimeterover6/issues/20)).
- `claim_MotwaniRaghunathanSaran1990` needs page/theorem locator ([#21](https://github.com/alexanderlewisstevens/perimeterover6/issues/21)).
- `claim_ORourke1987` needs page/theorem locator ([#22](https://github.com/alexanderlewisstevens/perimeterover6/issues/22)).
- `claim_PatersonYao1992` needs page/theorem locator ([#23](https://github.com/alexanderlewisstevens/perimeterover6/issues/23)).
- `claim_Pinciu2015` needs page/theorem locator ([#24](https://github.com/alexanderlewisstevens/perimeterover6/issues/24)).
- `claim_SchuchardtHecker1995` needs page/theorem locator ([#25](https://github.com/alexanderlewisstevens/perimeterover6/issues/25)).
- `claim_Shermer1992` needs page/theorem locator ([#26](https://github.com/alexanderlewisstevens/perimeterover6/issues/26)).
- `claim_Urrutia2000` needs page/theorem locator ([#27](https://github.com/alexanderlewisstevens/perimeterover6/issues/27)).
- `claim_UrrutiaOpenProblems` needs page/theorem locator ([#28](https://github.com/alexanderlewisstevens/perimeterover6/issues/28)).
- `claim_VigliettaThesis` needs page/theorem locator ([#29](https://github.com/alexanderlewisstevens/perimeterover6/issues/29)).
- `claim_VigliettaFace2014` needs page/theorem locator ([#30](https://github.com/alexanderlewisstevens/perimeterover6/issues/30)).
- `claim_Viglietta2020` needs page/theorem locator ([#31](https://github.com/alexanderlewisstevens/perimeterover6/issues/31)).
- `claim_WormanKeil2007` needs page/theorem locator ([#32](https://github.com/alexanderlewisstevens/perimeterover6/issues/32)).
- `claim_Zylinski2006` needs page/theorem locator ([#33](https://github.com/alexanderlewisstevens/perimeterover6/issues/33)).

## Search and Completeness Gaps

- No coverage cells are currently marked `unsearched` or `searching`.
- Search log present: `literature/search_log.md`.

## Next Actions

- Simple orthogonal polygons, point guards, vertex count: Record page/theorem locators from primary sources.
- Orthogonal polygons with holes, vertex guards: Primary-check exact theorem statements and page locators for the partial bounds.
- Hole-free polyominoes, point guards, lattice perimeter: Record theorem/page locator and lower-bound construction details.
- Polyominoes with holes, point guards, lattice perimeter: Extract the exact Conjecture 6.10 statement and surrounding examples from Massberg's habilitation.
- Polyominoes with holes, point guards, cell count: Record theorem/page locator and examples showing tightness.
- Ortho-unit polygons, point guards, perimeter: Record exact theorem locator and clarify hole assumptions from the primary paper.
- Integral orthogonal polygons, point guards, perimeter: Make the exact broader domain convention explicit before stating a standalone open problem.
- Orthogonal polyhedra, point guards: Primary-check the precise transfer from binary-space partitions to the guarding statement.
- Orthogonal polyhedra, edge and reflex-edge guards: Separate arbitrary-polyhedron bounds from orthogonal-specific conjectures in claim locators.
- Algorithmic and restricted-visibility context: Decide which adjacent models deserve deeper theorem-level extraction versus brief survey treatment.
