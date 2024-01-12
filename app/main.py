from random import choice
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    percentage = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                  5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    is_head = [1, 0]
    for _ in range(10000):
        heads = 0
        for __ in range(10):
            heads += choice(is_head)
        percentage[heads] += 1
    for case in percentage:
        percentage[case] /= 100
    return percentage


def draw_gaussian_distribution_graph(percentage: dict) -> None:
    heads = []
    quantity_of_heads = []
    for key, value in percentage.items():
        heads.append(key)
        quantity_of_heads.append(value)
    xpoints = np.array(heads)
    ypoints = np.array(quantity_of_heads)
    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
