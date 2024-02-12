import random
import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


def flip_coin() -> dict:
    possible_heads_dict = {num: 0 for num in range(0, 11)}

    nuber_of_cases = 10000
    for _ in range(nuber_of_cases):
        heads_came_up = 0
        for _ in range(10):
            heads_came_up += random.randint(0, 1)
        possible_heads_dict[heads_came_up] += 1
    for key, value in possible_heads_dict.items():
        possible_heads_dict[key] = value / (nuber_of_cases / 100)

    return possible_heads_dict


def draw_gaussian_distribution_graph(flip_coin: Callable) -> None:
    possible_heads_dict = flip_coin()

    xpoints = np.array([key for key in possible_heads_dict.keys()])
    ypoints = np.array([value for value in possible_heads_dict.values()])

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")

    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 110, 10))

    plt.show()
