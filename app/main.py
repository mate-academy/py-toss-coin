import matplotlib.pyplot as plt
import numpy as np
from random import randint


def flip_coin() -> dict:
    cases = dict.fromkeys(range(0, 11), 0)
    for _ in range(10001):

        heads = sum([randint(0, 1) for _ in range(10)])
        cases[heads] += 1

    for heads_number, cases_number in cases.items():
        cases[heads_number] = cases_number / 100

    return cases


def draw_gaussian_distribution_graph() -> None:
    cases = flip_coin()
    x_points = np.array(range(11))
    y_points = np.array([cases[case] for case in cases])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_points, y_points)
    plt.show()
