import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = defaultdict(int)

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = (results[heads_count] / 10000) * 100

    for i in range(11):
        if i not in results:
            results[i] = 0.0
    return dict(results)


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    sorted_keys = sorted(distribution.keys())
    sorted_values = [distribution[key] for key in sorted_keys]

    plt.bar(sorted_keys, sorted_values, color="blue", alpha=0.7)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Tosses")
    plt.show()
