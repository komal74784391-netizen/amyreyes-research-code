import triton
import triton.language as tl


@triton.jit
def sparse_attn_fwd(Q, K, V, Out, stride_q, stride_k, stride_v, stride_o,
                    BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr):
    offs_m = tl.arange(0, BLOCK_M)
    offs_n = tl.arange(0, BLOCK_N)
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    tl.store(Out + offs_m[:, None] * stride_o + offs_n[None, :], acc)
