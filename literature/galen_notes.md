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

There is also a boundary 1-skeleton reading. In the unit-subdivided boundary
cycle, the number of unit edges is `P`, and the number of boundary vertices is
also `P`; the vertices are partitioned into turn vertices `n` and flat
subdivision vertices `f`. Under this reading the hybrid expression weights the
same boundary 1-skeleton differently at turns and straight-through vertices.

## 3D Surface-Area Question

Working prompt: can we get a guard bound like `S/8`, where `S` is surface area?

This only makes sense after choosing a lattice normalization and a guard model.
Candidate version: for polycubes or grid-refined orthogonal polyhedra, let `S`
be the number of exposed unit square faces. Ask whether the object can be
guarded by at most `S/8` guards under a specified guard model.

This can also be written in terms of the unit-refined boundary 1-skeleton. If
`E_boundary` counts unit edges in the boundary surface mesh of a closed
polycube boundary, then each unit square contributes four incidences and each
boundary edge is incident to two unit squares, so `E_boundary = 2S`. In that
mesh-normalized model, `S/8` is the same numerical target as
`E_boundary/16`.

This is not the same as the unrefined edge count of a continuous orthogonal
polyhedron. Scaling a box changes Euclidean surface area while leaving the
unrefined skeleton combinatorics unchanged, so any skeleton version must say
whether it uses the original polyhedron graph or the unit-refined boundary
graph.

Caveat: continuous Euclidean surface area is scale-dependent. Viglietta's
face-guard results use face count and face guards, and Pinciu's polyhypercube
theorem uses volume/cell count and point guards. Those do not directly imply a
surface-area-over-eight result.
