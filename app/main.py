import matplotlib.pyplot as plt
import random

from matplotlib.ticker import PercentFormatter


def flip_coin() -> dict:
    result = dict.fromkeys([x for x in range(0, 11)], 0)

    for _ in range(10000):
        count = 0
        for _ in range(1, 11):
            count += random.randint(0, 1)
        result[count] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result


def draw_gaussian_distribution_graph() -> None:
    plt.plot(range(0, 11), flip_coin().values())
    plt.gca().yaxis.set_major_formatter(PercentFormatter(100))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
