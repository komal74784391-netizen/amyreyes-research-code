def split_corpus(docs, n):
    step = max(1, len(docs) // n)
    return [docs[i:i + step] for i in range(0, len(docs), step)]
