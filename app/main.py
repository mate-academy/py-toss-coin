import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    result = {i: 0 for i in range(11)}
    for i in range(0, 10001):
        heads_drop = 0
        for _ in range(10):
            side = random.randint(0, 1)
            if side == 1:
                heads_drop += 1
        result[heads_drop] += 1
    for key, value in result.items():
        value = value / 10001 * 100
        result[key] = round(value, 2)

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
