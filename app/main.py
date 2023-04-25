import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def flip_coin() -> dict:
    dic = {key: 0 for key in range(11)}
    for _ in range(10000):
        i = [random.randint(0, 1) for _ in range(10)]
        dic[i.count(0)] = dic.get(i.count(0)) + 1
    for key, value in dic.items():
        dic[key] = value / 10000 * 100
    return dic


def draw_gaussian_distribution_graph(dic: dict) -> None:
    ylst = [v for v in dic.values()]

    fig, ax = plt.subplots()

    ax.set_ylim((0, 100))
    ax.set_xlim([0, 10])

    plt.title("Guassian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter("{x:.0f}")
    ax.yaxis.set_minor_locator(MultipleLocator(5))

    ypoints = np.array(ylst)
    ax.plot(ypoints)
    plt.show()
