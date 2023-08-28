import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    sides = ["heads", "tails"]
    flips = {i: 0 for i in range(0, 11)}
    for _ in range(10_000):
        heads = 0
        for _ in range(10):
            if random.choice(sides) == "heads":
                heads += 1
        flips[heads] += 1
    result = {key: round(value * (100 / 10_000), 2)
              for key, value in flips.items()}
    return result


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_points = np.array(range(0, 11))
    y_points = np.array(list(distribution.values()))

    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
