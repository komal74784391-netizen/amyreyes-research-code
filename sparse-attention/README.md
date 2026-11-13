# Sparse Attention Kernels

Implementation of "Sparse Attention Kernels for Long-Context Transformers"
(NeurIPS 2026) by Amy Reyes, Kenji Watanabe and Laura Fischer.

> **Status: to be released.** The code in this directory will be published after the
> NeurIPS 2026 camera-ready deadline. Until then it should not be treated as the public
> release of the paper.

## Layout
- `src/` — Triton kernels and block-sparse masking utilities.
- `data/` — benchmark dataset preparation.
- `experiments/` — benchmarking entry points.
