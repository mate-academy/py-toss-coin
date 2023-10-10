import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    variants = ["heads", "tails"]

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            choice = random.choice(variants)
            if choice == "heads":
                heads_count += 1
        result_dict[heads_count] += 1
    for key in result_dict:
        result_dict[key] = (result_dict[key] / 10000) * 100
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    axis_x = list(data.keys())
    axis_y = list(data.values())

    plt.plot(axis_x, axis_y, marker="o", linestyle="-")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.grid(True)
    mu = np.mean(axis_x)
    sigma = np.std(axis_x)
    part_of_equation = (axis_x - mu) ** 2 / (2 * sigma ** 2)
    curve = np.exp(-part_of_equation) / (sigma * np.sqrt(2 * np.pi))
    plt.plot(axis_x, curve, "r--")

    plt.show()
