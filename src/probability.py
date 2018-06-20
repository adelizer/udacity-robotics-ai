from math import log


def get_test_distribution(grid):
    l = len(grid)
    w = len(grid[0])
    uniform_probability = []
    for i in range(l):
        row = []
        for j in range(w):
            row.append(1. / (l * w))
        uniform_probability.append(row)
    uniform_probability[int(l/2)][int(w/2)] = 0.8
    return normalize(uniform_probability)


def get_uniform_vector(grid):
    """Initialize robot belief"""
    l = len(grid)
    w = len(grid[0])
    uniform_probability = []
    for i in range(l):
        row = []
        for j in range(w):
            row.append(1./(l*w))
        uniform_probability.append(row)
    # uniform_probability = {(i, j): 1./(l*w) for i in range(l) for j in range(w)}
    return uniform_probability


def sense(prior, z, world, pHit, pMiss):
    """measurement update function"""
    l = len(prior)
    w = len(prior[0])
    q = [[None] * w]*l
    for arr in q:
        print(arr)
    for i in range(l):
        for j in range(w):
            print(i, j, world[i][j], z)
            if z == world[i][j]:
                q[i][j] = 1
            else:
                q[i][j] = 0
            for arr in q:
                print(arr)
    return normalize(q)


def move(p, u, motion_prop):
    """Circular in exact motion"""
    print("performing motion:{} ".format(u))
    l = len(p)
    w = len(p[0])
    q = []
    for i in range(l):
        row = []
        for j in range(w):
            row.append(p[(i-u[0])%l][(j-u[1])%w] * motion_prop + p[i][j] * (1-motion_prop))
        q.append(row)

    return normalize(q)


def normalize(q):
    """Normalize a list"""
    s = sum([sum(i) for i in q])
    for i in range(len(q)):
        for j in range(len(q[0])):
            q[i][j] = q[i][j] / s
    return q


def get_entropy(p):
    q = 0
    for i in range(len(p)):
        q += p[i] * log(p[i])
    return -1 * q