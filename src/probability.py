def get_uniform_vector(n):
    """Initialize robot belief"""
    uniform_probability = []
    for i in range(n):
        uniform_probability.append(1. / n)
    return uniform_probability


def sense(prior, z, world, pHit, pMiss):
    """measurement update function"""
    q = []
    for i in range(len(prior)):
        if z == world[i]:
            q.append(prior[i] * pHit)
        else:
            q.append(prior[i] * pMiss)
    return normalize(q)


def move(p, u, exact, over, under):
    """Circular in exact motion"""
    q = []
    l = len(p)
    for i in range(l):
        q.append(p[(i-u)%l]*exact + p[(i-u-1)%l]*over + p[(i-u+1)%l]*under)
    return normalize(q)


def normalize(q):
    """Normalize a list"""
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q