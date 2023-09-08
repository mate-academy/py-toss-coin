import random
from typing import Dict
import matplotlib as plt
import numpy as np


def flip_coin(numbers: int = 10000) -> Dict[int, float]:
    results = {}

    for i in range(numbers):
        coin_count = 0
        for num in range(10):
            if random.choice(["O", "P"]) == "O":
                coin_count += 1
        # перевіряємо, чи є ключ coin_count у словнику results
        if coin_count not in results:
            # якщо немає, то створюємо його з початковим значенням 0
            results[coin_count] = 0
        # додаємо одиницю до значення за ключем coin_count
        results[coin_count] += 1
    # обчислюємо відсотки для кожного ключа
    for key in results:
        results[key] = round(results[key] / numbers * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    coin_flips = flip_coin()

    x_points = np.plot(list(coin_flips.keys()))
    y_points = np.plot(list(coin_flips.values()))

    plt.plot(x_points, y_points)

    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 101, 10))

    # Показуємо графік
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage")

    plt.show()
