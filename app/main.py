import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    res = {}
    for index in range(11):
        res[index] = 0

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(["head", "other"]) == "head":
                count += 1
        res[count] += 1

    for i in res:
        res[i] = res[i] / 100

    return res


def draw_gaussian_distribution_graph(points_dict: dict) -> None:
    plt.ylabel("Drop percentage%")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")

    xpoints = np.array(list(points_dict.keys()))
    ypoints = np.array(list(points_dict.values()))

    plt.plot(xpoints, ypoints)
    plt.show()
