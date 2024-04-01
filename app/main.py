import matplotlib.pyplot as plotter
import numpy as np
from random import choice


def flip_coin(times: int = 10_000) -> dict:
    cases = {i: 0 for i in range(11)}
    coin_seq = ["head", "tail"]

    for _ in range(times):
        count_of_head = 0
        for _ in range(10):
            if choice(coin_seq) == "head":
                count_of_head += 1
        cases[count_of_head] += 1

    sum_values = sum(cases[value] for value in cases)

    for value in cases:
        cases[value] = round((cases[value] / sum_values) * 100, 2)

    return cases


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()

    x_axis = np.array([value for value in result])
    y_axis = np.array([result[value] for value in result])

    plotter.plot(x_axis, y_axis)

    plotter.title("Gaussian distribution")
    plotter.xlabel("Heads count")
    plotter.ylabel("Drop percentage %")

    plotter.show()
