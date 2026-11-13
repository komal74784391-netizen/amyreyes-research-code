def schedule(jobs, policy):
    return sorted(jobs, key=lambda j: policy(j))
