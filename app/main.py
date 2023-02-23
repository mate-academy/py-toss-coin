import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    dict_of_amounts = {i: 0 for i in range(11)}
    coin = ["head", "tail"]

    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            side_of_coin = random.choice(coin)
            if side_of_coin == "head":
                head_count += 1
        dict_of_amounts[head_count] += 1

    for key, value in dict_of_amounts.items():
        dict_of_amounts[key] = round((value / 10000) * 100, 2)

    return dict_of_amounts


def draw_gaussian_distribution_graph() -> None:
    dict_of_amounts = flip_coin()

    x_coord = np.arange(0, 11, 1)
    y_coord = [dict_of_amounts[i] for i in range(11)]

    plt.plot(x_coord, y_coord)
    plt.title("Gaussian Distribution")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of times")
    plt.show()
