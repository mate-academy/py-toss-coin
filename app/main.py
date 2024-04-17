import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, int | float]:
    counts = {i: 0 for i in range(10 + 1)}
    num_trials = 10000

    for _ in range(num_trials):
        heads_count = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        counts[heads_count] += 1

    percentages = {
        number: (count / num_trials) * 100
        for number, count in counts.items()
    }
    return percentages


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    xpoints = np.array(list(results.keys()))
    ypoints = np.array(list(results.values()))

    plt.plot(xpoints, ypoints, marker="o")
    plt.show()
