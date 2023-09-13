import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    list_drop = []
    list_data = []
    result = {}
    for i in range(1, 1001):
        for _ in range(1, 11):
            list_drop.append(random.randint(0, 1))
            if len(list_drop) >= 10:
                list_data.append(list_drop.count(1))
                list_drop = []
    for i in list_data:
        key = list_data.count(i)
        value = 100 / len(list_data) * key
        result[i] = round(value, 2)

    return result


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    flip_cn = sorted(flip_coin().copy().items())
    ar_x = []
    ar_y = []

    for key, value in flip_cn:
        ar_x.append(key)
        ar_y.append(value)

    ox = np.array(ar_x)
    oy = np.array(ar_y)

    plt.plot(ox, oy)

    plt.ylim(0, 100)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads counts")
    plt.ylabel("Drop percentage")

    plt.show()


draw_gaussian_distribution_graph()
