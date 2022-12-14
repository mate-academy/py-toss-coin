import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    count = 0
    result_dict = {0: 0,
                   1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0,
                   7: 0,
                   8: 0,
                   9: 0,
                   10: 0}
    while count < 10000:
        heads = 0
        for i in range(10):
            coin = random.randint(1, 2)
            if coin == 1:
                heads += 1
        result_dict[heads] += 1
        count += 1
    percentage_dict = {}
    for i in result_dict:
        percentage_dict[i] = result_dict[i] / 100
    return percentage_dict


def draw_gaussian_distribution_graph(flipping_coin_chart: dict) -> None:
    x_axis = []
    y_axis = []
    for key, value in flipping_coin_chart.items():
        x_axis.append(key)
        y_axis.append(value)

    plt.plot(np.array(x_axis), np.array(y_axis))
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.show()
