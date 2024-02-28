import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = defaultdict(int)
    for _ in range(trials):
        heads = sum([random.randint(0, 1) for _ in range(10)])
        results[heads] += 1
    for key in results.keys():
        results[key] = (results[key] / trials) * 100
    return dict(sorted(results.items()))


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    plt.bar(results.keys(), results.values())
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
