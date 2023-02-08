import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    possible_heads_dropped = {}
    heads_drop = {}

    for _ in range(10000):
        drop_heads = sum([random.randint(0, 1) for _ in range(10)])

        if heads_drop.get(drop_heads):
            heads_drop[drop_heads] += 1
        else:
            heads_drop[drop_heads] = 1

    for number, possible_drop in heads_drop.items():
        possible_heads_dropped[number] = possible_drop / 100

    return possible_heads_dropped


def draw_gaussian_distribution_graph() -> None:
    flip_coin_dict = flip_coin()

    xpoint = np.array(
        [heads_count for heads_count in flip_coin_dict]
    )
    ypoint = np.array(
        [drop_percentage for drop_percentage in flip_coin_dict.values()]
    )

    plt.plot(xpoint, ypoint)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
