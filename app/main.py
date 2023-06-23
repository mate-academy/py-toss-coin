import random
import matplotlib.pyplot as plt
from typing import Dict, Callable


def flip_coin() -> Dict[str, float]:
    raw_heads_dict = {_: 0 for _ in range(11)}
    for _ in range(10000):
        number_of_heads_in_ten_flips = 0
        for _ in range(10):
            number_of_heads_in_ten_flips += random.choice([0, 1])
        raw_heads_dict[number_of_heads_in_ten_flips] += 1

    percent_heads_dict = {_: round(raw_heads_dict[_] / 100, 2)
                          for _ in raw_heads_dict}

    return percent_heads_dict


def draw_gaussian_distribution_graph(func: Callable):
    heads = func()
    x = heads.keys()
    y = heads.values()
    plt.plot(x, y)
    plt.title("Coin flip distribution")
    plt.xlabel("Heads Count (times per 10 flips)")
    plt.ylabel("Drop percentage, %")
    plt.show()
