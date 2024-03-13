import random
import matplotlib.pyplot as plot
import numpy as np


def flip_coin() -> dict:
    cases = {
        0: 0, 1: 0, 2: 0,
        3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0,
        9: 0, 10: 0
    }

    seq = ["coin_head", "coin_tail"]
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            if random.choice(seq) == "coin_head":
                counter += 1

        cases[counter] += 1

    for i in range(11):
        cases[i] = round(cases[i] / 10000, 2)

    return cases


def draw_gaussian_distribution_graph() -> None:
    heads = flip_coin()
    x_axis = np.array([int(key) for key, value in heads.items()])
    y_axis = np.array([value * 100 for key, value in heads.items()])

    plot.title("Gaussian distribution")
    plot.xlabel("Heads count")
    plot.ylabel("Drop percentage, %")

    plot.plot(x_axis, y_axis)
    plot.show()


draw_gaussian_distribution_graph()
