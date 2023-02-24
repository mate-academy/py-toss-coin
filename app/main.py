import random
from numpy import arange as np
import matplotlib.pyplot as plt


from matplotlib.ticker import AutoMinorLocator


def flip_coin() -> dict:
    result_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    coin = ["Heads", "Tails"]
    for case in range(10000):
        count = 0
        for flip in range(10):
            if random.choice(coin) == "Heads":
                count += 1
        result_dict[count] += 1
    for num_of_heads_drop, times_of_drop in result_dict.items():
        percent_of_drop = times_of_drop / 100
        result_dict[num_of_heads_drop] = percent_of_drop
    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict[flip_coin()]) -> None:
    x_ax = [item for item in result_dict.keys()]
    y_ax = [item for item in result_dict.values()]
    fig, ax = plt.subplots()
    ax.plot(x_ax, y_ax)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])
    plt.xticks(np(min(x_ax), max(x_ax) + 1, 1))
    plt.yticks(np(min(y_ax), max(y_ax) + 80, 10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.show()
