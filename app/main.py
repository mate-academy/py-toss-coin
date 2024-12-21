import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        num = sum([random.randint(0, 1) for _ in range(10)])
        if num in result:
            result[num] += 1
        else:
            result[num] = 0

    return {
        num: round(count / 10000 * 100, 2) for num, count in result.items()
    }


def draw_gaussian_distribution_graph(num_dict: dict) -> None:
    sorted_dict = dict(sorted(num_dict.items()))
    x_axis = np.array(list(sorted_dict.keys()))
    y_axis = np.array(list(sorted_dict.values()))

    plt.plot(x_axis, y_axis, marker="o", color="blue", linestyle="-")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
