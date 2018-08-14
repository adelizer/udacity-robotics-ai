#!/usr/bin/env python
import random

def print_dist(dist):
    print("Probability distribution: \n")
    blue = '\033[94m'
    endc = '\033[0m'
    for i in range(len(dist)):
        p = ''
        for j in range(len(dist[0])):
            color = [int(255 * dist[i][j])] * 3
            bg = '\033[{};2;{};{};{}m'.format(48, *color)
            p += bg + blue + str(round(dist[i][j], 2)) + endc + ', '
        print(p)


def print_world(grid):
    print("World: \n")
    for i in range(len(grid)):
        s = ''
        for j in range(len(grid[0])):
            s += '(%s), \t' % grid[i][j]
        print(s)
    print('')


def resambling_wheel(data):
    N = len(data)
    s = sum(data)
    for i in range(N):
        data[i] = data[i] / s
    print(sum(data))
    ret = []
    c = [data[0]]
    for i in range(1, N):
        c.append(c[i-1] + data[i])
    u = random.uniform(0, 1.0/N)
    j = 0
    for i in range(N):
        while u > c[j]:
            j += 1
        ret.append(j) # output
        u = u + 1.0 / N # next spoke
    print(ret)
