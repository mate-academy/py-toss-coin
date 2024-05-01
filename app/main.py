import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[float]:
    result = {i: 0 for i in range(11)}
    for i in range(10000):
        toss = [random.randint(0, 1) for _ in range(10)].count(0)
        for number_of_heads in range(11):
            if number_of_heads == toss:
                result[number_of_heads] = (
                    ((result[number_of_heads] * i) / 100) + 1) * 100 / (i + 1)
            else:
                result[number_of_heads] = (
                    result[number_of_heads] * i) / (i + 1)
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    xpoints = np.array(data.keys())
    ypoints = np.array(data.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)
    plt.show()
