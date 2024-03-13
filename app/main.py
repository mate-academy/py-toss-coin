import random
from matplotlib import pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = sum(random.randint(0, 1) for i in range(10))
        result[heads] += 1
    for num in result:
        result[num] = result[num] / 100
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    mean = sum(k * v for k, v in data.items()) / sum(data.values())
    variance = sum((k - mean) ** 2 * v for k, v in data.items())
    std_dev = np.sqrt(variance / sum(data.values()))

    x_axis = np.arange(11)
    y_axis = (
        1 / (std_dev * np.sqrt(2 * np.pi))
        * np.exp(-0.5 * ((x_axis - mean) / std_dev) ** 2)
    )

    plt.plot(x_axis, y_axis)
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


coin_flip_data = flip_coin()
draw_gaussian_distribution_graph(coin_flip_data)
