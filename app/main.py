import random
import matplotlib.pyplot as plt
from collections import defaultdict


def flip_coin() -> dict:
    num_simulations = 10000
    num_flips = 10
    results = defaultdict(int)

    for _ in range(num_simulations):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[num_heads] += 1
    probable_distribution = {k: v / num_simulations * 100
                             for k, v in results.items()}
    return probable_distribution


def draw_gaussian_distribution_graph(probable_distribution: dict) -> None:
    x_value = list(probable_distribution.keys())
    y_value = list(probable_distribution.values())

    plt.bar(x_value, y_value, align="center", alpha=0.7)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.grid(True)

    plt.show()
