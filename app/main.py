import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    cases = 10000
    coin = [0, 1]
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
    }
    for case in range(cases):
        flip_heads = 0
        for _ in range(10):
            flip = random.choice(coin)
            flip_heads += flip

        result[flip_heads] += 1

    for _ in range(11):
        result[_] /= (cases / 100)

    return result


def draw_gaussian_distribution_graph() -> None:
    result_flip = flip_coin()
    xpoints = np.array([key for key in result_flip.keys()])
    ypoints = np.array([value for value in result_flip.values()])

    plt.plot(xpoints, ypoints)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian distribution")
    plt.show()
