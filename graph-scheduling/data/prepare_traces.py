def normalize_traces(rows):
    return [r for r in rows if r['duration'] > 0]
