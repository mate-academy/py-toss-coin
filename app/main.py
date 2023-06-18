import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {
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
    coin = ["head", "tail"]
    total_heads = []
    for _ in range(10000):
        head_number = 0
        for _ in range(10):
            flip = random.choice(coin)
            if flip == "head":
                head_number += 1
        total_heads.append(head_number)

    for key in results:
        results[key] = round(
            (total_heads.count(key) / len(total_heads) * 100), 2
        )
    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = np.array([key for key in data])
    y_points = np.array([data[key] for key in data])

    plt.plot(x_points, y_points)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
