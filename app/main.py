import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    res_dict = {}

    for i in range(10001):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))

        if heads_count not in res_dict:
            res_dict[heads_count] = 0

        res_dict[heads_count] += 1

    total_simulations = 10001
    for heads_count, count in res_dict.items():
        percentage = (count / total_simulations) * 100
        res_dict[heads_count] = round(percentage, 2)

    return dict(sorted(res_dict.items()))


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_points = np.array(list(distribution.keys()))
    y_points = np.array(list(distribution.values()))

    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points)
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
