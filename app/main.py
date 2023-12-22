import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    head_statistic = {
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

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            choice = random.choice(["Heads", "Tails"])
            if choice == "Heads":
                heads += 1

        head_statistic[heads] += 1

    for head_value in head_statistic:
        head_statistic[head_value] *= 100 / 10000

    return head_statistic


def draw_gaussian_distribution_graph(statistic: dict) -> None:
    x_values = np.arange(len(statistic))
    y_values = np.array(list(statistic.values()))
    plt.plot(x_values, y_values)

    plt.xticks(x_values, list(statistic.keys()))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.tick_params(axis='y', which='minor', length=4)
    plt.yticks(np.arange(0, 101, 5), minor=True)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
