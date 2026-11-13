import time

from src.kernel import sparse_attn_fwd


def bench(fn, warmup=5, iters=20):
    for _ in range(warmup):
        fn()
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    return (time.perf_counter() - start) / iters
