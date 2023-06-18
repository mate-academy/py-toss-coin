import random
import typing
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> typing.Dict:
    quantity_of_heads = 0
    list_of_possibilities = [0] * 11
    final_dict = {}

    for _ in range(10000):
        for _ in range(10):
            if random.randint(0, 1) == 1:
                quantity_of_heads += 1
        list_of_possibilities[quantity_of_heads] += 1
        quantity_of_heads = 0

    for i in range(11):
        final_dict[i] = list_of_possibilities[i] / 100

    return final_dict


def draw_gaussian_distribution_graph() -> None:
    numbers_dict = list(flip_coin().values())
    xpoints = np.array(numbers_dict)
    plt.axis([0, 10, 0, 100])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(xpoints)
    plt.show()
