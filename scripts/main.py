#!/usr/bin/env python

from src.probabilistic_robotics.histogram_filter import get_uniform_vector, sense, move
from src.probabilistic_robotics.kalman_filter import KalmanFilter
from src.probabilistic_robotics.robot import Robot
from src.probabilistic_robotics.utils import print_world, print_dist, resampling_wheel
import random
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

    print('#'*80 + "\n\t\t\t\t Week 2 \n" + '#'*80)

    # TODO: parametriz matrices
    dt = 0.1
    F = [[1,0,dt,0], [0,1,0,dt], [0,0,1,0], [0,0,0,1]]
    H = [[1,0,0,0], [0,1,0,0]]
    init = [[4.], [12.], [0.], [0.]]
    cov = [[0,0,0,0], [0,0,0,0], [0,0,1000,0], [0,0,0,1000]]

    k = KalmanFilter(4, init, cov)
    k.set_sys_matrices(F, H)
    z = [[5., 10.],[6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
    u = [0., 0.]
    for i in range(len(z)):
        k.filter(u, [[z[i][0]], [z[i][1]]])

    print('#'*80 + "\n\t\t\t\t Particle filters\n" + '#'*80)

    N = 1000
    p = []
    for i in range(N):
        x = Robot()
        x.set_noise(0.05, 0.05, 5.0)
        p.append(x)


if __name__ == '__main__':
    main()
