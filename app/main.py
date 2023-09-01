import random
from typing import Any
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {}
    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] = results.get(heads_count, 0) + 1
    percent = {
        heads: (count / num_cases) * 100
        for heads, count in results.items()
    }

    return percent


def draw_gaussian_distribution_graph(func: Any) -> None:
    sorted_percent = dict(sorted(func().items()))
    x_points = np.array([x for x in sorted_percent.keys()])
    y_points = np.array([y for y in sorted_percent.values()])
    plt.plot(x_points, y_points)
