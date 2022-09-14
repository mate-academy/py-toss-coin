import random

import matplotlib.pyplot as plt


def flip_coin():
    dict_ = {0: 0,
             1: 0,
             2: 0,
             3: 0,
             4: 0,
             5: 0,
             6: 0,
             7: 0,
             8: 0,
             9: 0,
             10: 0,
             }
    coin = ["head", "tail"]
    for i in range(10000):
        count = 0
        for j in range(10):
            count += 1 if random.choice(coin) == "head" else 0
        dict_[count] += 0.01
    return dict_


def draw_gaussian_distribution_graph(flips: dict) -> None:
    plt.plot(flips.keys(), flips.values())
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
