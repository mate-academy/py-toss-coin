import random
import matplotlib.pyplot as p_plt
import numpy as np


def flip_coin() -> dict:
    variants = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for _ in range(10000):
        key = [random.choice(["head", "bottom"])
               for _ in range(10)].count("head")
        variants[key] += 1

    for key in variants:
        variants[key] = variants[key] / 100

    return variants


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()

    x_points = np.array([key for key in points])
    y_points = np.array([value for value in points.values()])

    p_plt.plot(x_points, y_points)
    p_plt.ylim(0, 100)
    p_plt.title("Gaussian distribution")
    p_plt.xlabel("Heads count")
    p_plt.ylabel("Drop percentage %")

    p_plt.show()


draw_gaussian_distribution_graph()
