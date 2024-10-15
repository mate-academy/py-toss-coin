import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    flip_results = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        head_counter = 0
        for i in range(10):
            if random.randint(0, 1) == 1:
                head_counter += 1
        flip_results[head_counter] += 1 / 10000 * 100
    return flip_results


def draw_gaussian_distribution_graph(flips_dict: dict) -> None:
    xpoints = np.array(list(flips_dict.keys()))
    ypoints = np.array(list(flips_dict.values()))
    plt.plot(xpoints, ypoints)
    plt.axis([0, 10, 0, 100])
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 101, 10))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
