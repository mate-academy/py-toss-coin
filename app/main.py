import matplotlib.pyplot as plt
from typing import Callable
from random import randint


def flip_coin() -> dict:
    output = {i: 0 for i in range(11)}
    repeats = 10**4

    for _ in range(repeats):
        result = [randint(0, 1) for _ in range(10)].count(1)
        output[result] = output.get(result, 0) + 1 / repeats

    return {key: round(value * 100, 2) for key, value in output.items()}


def draw_gaussian_distribution_graph(func: Callable) -> None:
    x_points = range(0, 11)
    y_points = func().values()

    plt.plot(x_points, y_points)
    plt.xticks(x_points)
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
