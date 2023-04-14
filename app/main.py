import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                count_heads += 1
        results[count_heads] += 1
    for key in results:
        results[key] = round(results[key] / 100, 2)
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_coord = np.arange(0, 11, 1)
    y_coord = [results[i] for i in x_coord]
    mean = sum(x_coord * y_coord) / 100
    variance = \
        sum([(xi - mean) ** 2 * yi for xi, yi in zip(x_coord, y_coord)])\
        / 100
    std_dev = variance ** 0.5
    plt.bar(x_coord, y_coord)
    plt.plot(x_coord, norm.pdf(x_coord, mean, std_dev) * 100, "r")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases")
    plt.title("Gaussian distribution of coin flips")
    plt.show()
