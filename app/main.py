import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    results = {i: 0 for i in range(11)}

    num_cases = 10000
    for _ in range(num_cases):
        heads_count = sum(
            1 for _ in range(10) if random.random() > 0.5)
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / num_cases * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    number_of_heads = list(distribution.keys())
    percentage_values = list(distribution.values())

    plt.bar(number_of_heads, percentage_values)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution (10 flips, 10000 trials)")
    plt.show()
