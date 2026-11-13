# KV-Cache Compression Toolkit

Official implementation of "Scalable KV-Cache Compression for Long-Context Serving"
(MLSys 2027) by Amy Reyes, Tomas Lindqvist and Priya Natarajan.

**Status: released.** This repository contains the complete implementation, the dataset
preparation scripts and the experiment configurations used to produce the results in the
paper. Issues and pull requests are welcome.

## Layout
- `src/` — core compression library and cache manager.
- `data/` — dataset preparation utilities.
- `experiments/` — training and evaluation entry points.
