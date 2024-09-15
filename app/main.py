import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_count = {}
    for _ in range(50000):
        heads = 0
        for i in range(10):
            side = random.randint(0, 1)
            if side == 0:
                heads += 1
        if heads not in heads_count:
            heads_count[heads] = 1
        else:
            heads_count[heads] += 1
    for key in heads_count:
        heads_count[key] /= 500
    return heads_count


def draw_gaussian_distribution_graph(heads_count: dict) -> None:
    keys_list = []
    values_list = []
    for key, value in heads_count.items():
        keys_list.append[key]
        values_list.append[value]
    x_array = np.array(values_list)
    y_array = np.array(keys_list)

    plt.plot(x_array, y_array)

    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")

    plt.show()
