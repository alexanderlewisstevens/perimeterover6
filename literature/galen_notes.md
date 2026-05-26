# Note for Galen: Working Questions From Paul

Last updated: 2026-05-26

These are working prompts, not literature-confirmed open problems yet. They
should stay separate from source-stated conjectures until Paul/Galen confirm
the exact model or a citable source is found.

## Flat-Vertex Hybrid Question

Paul's prompt: can we find or use a regime where `n/8 + f/4 < P/6`?

Working convention: after subdividing an integral orthogonal polygon into unit
boundary steps, let `P` be total lattice perimeter, `n` be the number of turn
vertices, and `f` be the number of flat subdivision vertices. Under `P = n + f`,
the inequality is equivalent to `f < n/2`.

So the nontrivial problem is not the inequality by itself. The nontrivial
problem is whether a true guard theorem, lower-bound construction, or useful
class is controlled by `n/8 + f/4`, and whether `f` really means flat boundary
vertices rather than faces, cells, holes, or another parameter.

## 3D Surface-Area Question

Working prompt: can we get a guard bound like `S/8`, where `S` is surface area?

This only makes sense after choosing a lattice normalization and a guard model.
Candidate version: for polycubes or grid-refined orthogonal polyhedra, let `S`
be the number of exposed unit square faces. Ask whether the object can be
guarded by at most `S/8` guards under a specified guard model.

Caveat: continuous Euclidean surface area is scale-dependent. Viglietta's
face-guard results use face count and face guards, and Pinciu's polyhypercube
theorem uses volume/cell count and point guards. Those do not directly imply a
surface-area-over-eight result.
