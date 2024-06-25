import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    results = defaultdict(int)

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100.0

    return dict(results)


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    sorted_results = dict(sorted(results.items()))
    xpoints = list(sorted_results.keys())
    ypoints = list(sorted_results.values())

    plt.plot(xpoints, ypoints, marker="o", linestyle="-")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 Trials)")
    plt.grid(True)  # Add grid lines
    plt.show()
