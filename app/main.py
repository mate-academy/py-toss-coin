import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    head_times = {i: 0 for i in range(11)}
    for case in range(10_000):
        head_times[sum(
            1 if random.choice(("head", "tail")) == "head" else 0
            for head in range(10)
        )] += 1

    return {head_time: round(head_times[head_time] / 100, 2)
            for head_time in head_times}


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = np.array(data.keys())
    y_points = np.array(data.values())

    plt.xlim(0, 11)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_points, y_points)
    plt.show()
