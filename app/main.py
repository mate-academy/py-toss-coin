import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    result_dict = {i: 0 for i in range(11)}

    for number in range(0, 11000):
        heads = 0
        for tries in range(10):
            sides_of_coin = random.randint(0, 1)
            if sides_of_coin == 1:
                heads += 1
        result_dict[heads] += 1

    for key, value in result_dict.items():
        result_dict[key] = round(value / 11000 * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:

    percent = []
    heads = []

    for key, values in flip_coin().items():
        percent.append(key)
        heads.append(values)

    x_cord = np.array(heads)
    y_cord = np.array(percent)

    plt.plot(x_cord, y_cord)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
