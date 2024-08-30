import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    results = {i: 0 for i in range(11)}
    experiments = 10000

    for _ in range(experiments):
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / experiments) * 100

    return results


def draw_gaussian_distribution_graph(results: Dict[int, float]) -> None:
    heads = list(results.keys())
    percentages = list(results.values())

    plt.plot(heads, percentages, marker="o")

    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)

    plt.show()


flip_coin_results = flip_coin()
draw_gaussian_distribution_graph(flip_coin_results)
