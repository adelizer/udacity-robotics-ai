#!/usr/bin/env python
import random
import numpy as np


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


def gaussian(start, end, N, mu, sig):
    x = np.linspace(start, end, N)
    return normalize(np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))


def normalize(data):
    s = sum(data)
    for i in range(len(data)):
        data[i] /= float(s)
    return data


def resampling_wheel(data):
    N = len(data)
    ret = []
    c = [data[0]]
    for i in range(1, N):
        # calculate cumulative sum
        c.append(c[i-1] + data[i])

    # start with the first spoke at random interval
    u = random.uniform(0, 1.0/N)
    j = 0
    for i in range(N):
        while u > c[j]:
            j += 1
        ret.append(j)
        u = u + 1.0 / N
    return ret
