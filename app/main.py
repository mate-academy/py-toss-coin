import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}
    for i in range(10000):
        head = 0
        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                head += 1
        result[head] += 1
    for value in result:
        result[value] /= 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    xpoints = np.array([key for key in result])
    ypoints = np.array([result[value] for value in result])
    plt.plot(xpoints, ypoints, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
