import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) \
        -> Dict[int, float]:
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = sum(random.choices([0, 1], k=flips_per_trial))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100

    return results


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    heads = list(distribution.keys())
    percentages = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.plot(heads, percentages, marker="o", linestyle="-", color="b")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop Percentage %")
    plt.xticks(heads)
    plt.xlim(0, 10)
    plt.ylim(0, max(percentages) + 5)
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    result = flip_coin()
    print(result)
    draw_gaussian_distribution_graph(result)
