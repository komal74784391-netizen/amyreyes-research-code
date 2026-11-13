import torch

class SegmentCache:
    """Segmented KV cache with per-layer compression budgets."""

    def __init__(self, budget):
        self.budget = budget
