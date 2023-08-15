import numpy as np

import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                   6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    counter = 0
    for cases in range(10000):
        for flip in range(10):
            head = random.randint(0, 1)
            if head == 1:
                counter += 1
        result_dict[counter] += 1
        counter = 0

    result_dict_percent = {i: result_dict[i] / 100 for i in range(11)}
    return result_dict_percent


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    x_coords = np.array([x_coord for x_coord in result_dict.keys()])
    y_coords = np.array([y_coord for y_coord in result_dict.values()])

    plt.plot(x_coords, y_coords)

    plt.title("Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage")

    plt.show()
