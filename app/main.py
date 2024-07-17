import random

import matplotlib
from matplotlib import pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1
    total_trials = float(10000)
    percentages = {
        heads: (count / total_trials) * 100
        for heads, count in results.items()
    }
    draw_gaussian_distribution_graph(percentages)
    return percentages


def draw_gaussian_distribution_graph(points: dict) -> None:
    x_axis = np.array(list(points.keys()))
    y_axis = np.array(list(points.values()))
    plt.plot(x_axis, y_axis)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")
    matplotlib.is_interactive()
