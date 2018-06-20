#!/usr/bin/env python


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
