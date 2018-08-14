#!/usr/bin/env python

import matplotlib.pyplot as plt
from src.probabilistic_robotics.utils import resampling_wheel, gaussian, normalize


def main():
    data = gaussian(-10, 10, 1000, 0, 2)
    samples = resampling_wheel(data)
    plt.subplot(211)
    plt.xlabel('particles')
    plt.ylabel('weights')
    plt.plot(data)
    plt.subplot(212)
    plt.hist(samples)
    plt.xlabel('samples')
    plt.ylabel('frequency')
    plt.show()


if __name__ == '__main__':
    main()
