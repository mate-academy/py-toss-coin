import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {}
    for _ in range(10_000):
        head_counts = sum(
            random.randint(0, 1)
            for _ in range(10)
        )
        result[head_counts] = result.get(head_counts, 0) + 1
    result = {
        key: value / 100
        for key, value in result.items()
    }
    return dict(sorted(result.items()))


def draw_gaussian_distribution_graph(data: dict) -> None:
    heads_count = np.array([*data.keys()])
    drop_percentage = np.array([*data.values()])

    plt.plot(heads_count, drop_percentage)
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 110, 10))
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
