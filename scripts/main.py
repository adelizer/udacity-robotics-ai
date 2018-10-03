#!/usr/bin/env python

from src.probabilistic_robotics.histogram_filter import get_uniform_vector, sense, move
from src.probabilistic_robotics.kalman_filter import KalmanFilter
from src.probabilistic_robotics.robot import Robot, eval
from src.probabilistic_robotics.utils import print_world, print_dist, resampling_wheel, normalize
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

    # TODO: parametrize matrices
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

    myrobot = Robot()
    myrobot = myrobot.move(0.1, .1)
    print(myrobot)
    N = 100
    p = []
    for i in range(N):
        x = Robot()
        x.set_noise(0.05, 0.05, 5)
        p.append(x)

    print(eval(myrobot, p))

    for t in range(10):
        myrobot = myrobot.move(0.1, .1)
        Z = myrobot.sense()

        p2 = []
        for i in range(N):
            p2.append(p[i].move(0.1, .1))

        p = p2
        w = []
        for i in range(N):
            w.append(p[i].measurement_prob(Z))

        new_indices = resampling_wheel(normalize(w))
        p3 = []
        for i in range(N):
            p3.append(p[new_indices[i]])
        p = p3
        print(eval(myrobot, p))

    # for i in range(N):
    #     print(p[i])
    # print(myrobot)
if __name__ == '__main__':
    main()
