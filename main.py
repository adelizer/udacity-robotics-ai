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


    p = get_test_distribution(grid)
    print_dist(p)
    p = move(p, [0, 1], 0.8)
    print_dist(p)



if __name__ == '__main__':
    main()
