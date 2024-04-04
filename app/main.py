import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    numbers_of_heads = {i: 0 for i in range(11)}

    for _ in range(10000):
        flipping_coin_10_times = [random.choice(coin) for _ in range(10)]
        numbers_of_heads[flipping_coin_10_times.count("heads")] += 1

    percentage_dict = {
        key: 100 * value / 10000 for key, value in numbers_of_heads.items()
    }
    return percentage_dict


def draw_gaussian_distribution_graph(percentage_dict: dict) -> None:
    ypoints = np.array([value for value in percentage_dict.values()])
    plt.plot(ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
