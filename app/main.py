import numpy as np
import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    results = []
    for i in range(10000):
        random_list = [random.choice([0, 1]) for _ in range(10)]
        results.append(sum(random_list))
    result_dict = {
        num: results.count(num) / len(results) * 100
        for num in set(results)
    }
    return result_dict


def draw_gaussian_distribution_graph(points: dict) -> None:
    x_line = np.array([key for key in points.keys()])
    y_line = np.array([value for value in points.values()])

    plt.plot(x_line, y_line)

    plt.xlabel("Counts")
    plt.ylabel("Values")

    plt.show()
