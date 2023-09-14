import random

import matplotlib.pyplot as plt

import numpy as np


def flip_coin() -> dict:
    result = []

    flipping = {}
    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            if random.choice([0, 1]) == 0:
                head_count += 1
        result.append(head_count)

    for item in result:
        flipping[item] = result.count(item) / 100

    return dict(sorted(flipping.items()))


def draw_gaussian_distribution_graph() -> None:
    flipping_data = flip_coin()
    x_point = np.array(list(flipping_data.keys()))
    y_point = np.array(list(flipping_data.values()))

    plt.plot(x_point, y_point)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    # Задаємо діапазони осей x і y
    plt.xlim(0, 10)  # Шкала x від 0 до 10
    plt.ylim(0, 100)  # Шкала y від 0 до 100

    plt.show()


draw_gaussian_distribution_graph()
