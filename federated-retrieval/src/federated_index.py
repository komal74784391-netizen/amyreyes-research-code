class FederatedIndex:
    def __init__(self, shards):
        self.shards = shards

    def search(self, q):
        return [s.search(q) for s in self.shards]
