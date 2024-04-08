import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {
        key: (value / total_cases) * 100
        for key, value in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(percentages: Dict[int, float]) -> None:
    plt.bar(percentages.keys(), percentages.values(), color="blue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
