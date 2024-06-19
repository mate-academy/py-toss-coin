import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin(num_flips=10, num_trials=10000):
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.randint(0, 1) for _ in range(num_flips))
        results[heads_count] += 1

    for count in results:
        results[count] = (results[count] / num_trials) * 100

    return results


def draw_gaussian_distribution_graph():
    keys = list(flip_coin().keys())
    values = list(flip_coin().values())

    x = np.array(keys)
    y = np.array(values)

    plt.plot(x, y)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 5))

    plt.show()
