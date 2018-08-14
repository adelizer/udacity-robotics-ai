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
    return uniform_probability


def sense(p, z, world, hit, miss):
    """measurement update function"""
    print("performing measurement:{} ".format(z))
    l = len(p)
    w = len(p[0])
    q = []
    for i in range(l):
        row = []
        for j in range(len(p[0])):
            if world[i][j] == z:
                row.append(p[i][j] * hit)
            else:
                row.append(p[i][j] * miss)
        q.append(row)

    return normalize(q)


def move(p, u, motion_exact):
    """Circular in exact motion"""
    print("performing motion:{} ".format(u))
    l = len(p)
    w = len(p[0])
    q = []
    for i in range(l):
        row = []
        for j in range(w):
            row.append(p[(i-u[1])%l][(j-u[0])%w] * motion_exact + p[i][j] * (1-motion_exact))
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
        for j in range(len(p[0])):
            q += p[i][j] * log(p[i][j])
    return -1 * q
