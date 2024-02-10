from typing import Dict

import matplotlib.pyplot as plt
import random


def flip_coin() -> Dict[int, float]:
    results: Dict[int, int] = {i: 0 for i in range(11)}
    total_flips: int = 10000

    for _ in range(total_flips):
        heads_count: int = sum(
            1 for _ in range(10) if random.choice([True, False]))
        results[heads_count] += 1

    percentages: Dict[int, float] = {
        k: v / total_flips * 100 for k, v in results.items()}

    return percentages


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    data: Dict[int, float] = flip_coin()

    plt.plot(list(data.keys()), list(data.values()))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()


draw_gaussian_distribution_graph()
