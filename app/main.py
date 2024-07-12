import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def flip_coin() -> dict:
    head_list = {key: 0 for key in range(0, 11)}
    for _ in range(10000):
        count_head = sum([
            random.randint(0, 1) for _ in range(0, 10)
        ])
        head_list[count_head] += 1
    result = {
        key: (value / 10000) * 100 for key, value in head_list.items()
    }
    return result


def gaussian_plot(data: dict) -> None:
    x_points, y_points = list(data.keys()), list(data.values())
    plt.plot(x_points, y_points)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop Percentage, %")
    plt.ylim(0, 100)
    plt.gca().yaxis.set_major_locator(MultipleLocator(10))
    plt.show()
