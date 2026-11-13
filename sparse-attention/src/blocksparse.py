import torch


def block_mask(seq_len, block, keep=0.25):
    mask = torch.zeros(seq_len // block, seq_len // block, dtype=torch.bool)
    idx = torch.randperm(mask.numel())[: int(mask.numel() * keep)]
    mask.view(-1)[idx] = True
    return mask
