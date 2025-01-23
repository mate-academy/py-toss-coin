import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:

    dicter = {}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(1, 2) % 2 == 0:
                heads += 1
        dicter[heads] = dicter.setdefault(heads, 0) + 1

    for key in dicter:
        dicter[key] = dicter[key] / 10000 * 100

    return dicter


def draw_gaussian_distribution_graph() -> None:

    dicter = flip_coin()

    x_points = np.array(sorted(dicter.keys()))
    y_points = np.array([dicter[key] for key in x_points])

    plt.plot(x_points, y_points, marker="o")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage (%)")
    plt.title("Gaussian Distribution of Heads in 10 Coin Flips")
    plt.grid(True)
    plt.show()


draw_gaussian_distribution_graph()
