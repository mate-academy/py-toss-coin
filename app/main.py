import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {}
    for key in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        if heads_count not in result_dict:
            result_dict[heads_count] = 0
        result_dict[heads_count] += 1 / 100
    return result_dict


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_points = np.array(list(distribution.keys()))
    y_points = np.array(list(distribution.values()))
    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.figure(figsize=(8, 6))
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
