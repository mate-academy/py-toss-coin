import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    total_trials = sum(results.values())
    percentages = {k: (v / total_trials) * 100 for k, v in results.items()}

    return percentages


def draw_gaussian_distribution_graph(values: dict) -> None:
    x_axis = values.keys()
    y_axis = values.values()

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 11, 1))

    plt.plot(x_axis, y_axis)
    plt.show()
