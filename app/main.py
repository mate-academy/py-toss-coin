import random
import matplotlib.pyplot as plt
import numpy as np
import sys


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    result = {heads: 0 for heads in range(num_flips + 1)}

    for _ in range(num_cases):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1
        result[heads_count] += 1

    for key, value in result.items():
        result[key] = (value / num_cases) * 100

    return result


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_points = np.array(results.keys())
    y_points = np.array(results.values())

    plt.xlim(0, 11)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_points, y_points)
    plt.savefig("plot.png")
    plt.show()

    sys.stdout.flush()
