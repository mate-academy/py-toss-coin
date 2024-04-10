import random

import matplotlib.pyplot as plt


def flip_coin(amount: int = 10000) -> dict:
    coins_dict = dict.fromkeys(range(11), 0)
    for _ in range(amount):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        coins_dict[heads_count] += 1

    for heads in coins_dict:
        coins_dict[heads] = (coins_dict[heads] / amount) * 100

    return coins_dict


def draw_gaussian_distribution_graph(coins_dict: dict) -> None:
    plt.bar(coins_dict.keys(), coins_dict.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian Distribution")
    plt.show()
