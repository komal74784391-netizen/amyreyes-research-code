def low_rank_compress(tensor, rank):
    u, s, v = tensor.svd()
    return (u[:, :rank] * s[:rank]) @ v[:rank]
