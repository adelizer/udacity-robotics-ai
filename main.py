#!/usr/bin/env python

from src.probability import get_uniform_vector, sense, move, get_entropy, get_test_distribution
from utils import print_world, print_dist
import logging
import yaml
import io


def main():
    logging.basicConfig(level=logging.DEBUG)
    with io.open('world.yaml', 'r') as file:
        world = yaml.load(file)
        grid = world['grid']
        # TODO: validate the size of grid
        z = world['z']
        u = world['u']
    print_world(grid)

    p = get_uniform_vector(grid)
    print_dist(p)
    for i in range(len(z)):
        p = sense(p, z[i], grid, world['hit'], world['miss'])
        p = move(p, u[i], world['move_exact'])
        print_dist(p)


if __name__ == '__main__':
    main()
