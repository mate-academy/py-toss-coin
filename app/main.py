import matplotlib.pyplot as plt
import random
from typing import Callable


def flip_coin() -> dict[int]:
    coin = ["head", "tail"]
    heads_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
        5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
        10: 0
    }

    for case in range(10_000):
        head_count = 0

        for flip in range(10):
            if random.choice(coin) == "head":
                head_count += 1

        heads_dict[head_count] += 1 / 100

    return heads_dict


def draw_gaussian_distribution_graph(
        flip_coin_func: Callable = flip_coin
) -> None:
    data_dict = flip_coin_func()

    plt.bar(
        list(data_dict.keys()),
        list(data_dict.values()),
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
