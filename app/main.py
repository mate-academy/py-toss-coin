# write your code here
from random import choice

import matplotlib.pyplot as plt

import numpy as np

NUM_ATTEMPTS = 10_000


def flip_coin() -> dict:
    results = {}

    for _ in range(NUM_ATTEMPTS):
        num_heads = sum(choice([0, 1]) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    sorted_results = dict(sorted(results.items(), key=lambda x: x[0]))

    for key in sorted_results:
        sorted_results[key] = round(
            (sorted_results[key] / NUM_ATTEMPTS) * 100, 2
        )

    return sorted_results


def draw_gaussian_distribution_graph() -> None:
    dict_of_data = flip_coin()
    xpoints = np.array(list(dict_of_data.keys()))
    ypoints = np.array(list(dict_of_data.values()))
    plt.xlabel("Heads counts")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)
    plt.show()
