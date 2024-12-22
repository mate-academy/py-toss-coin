import matplotlib.pyplot as plt
import random
from collections import Counter


def flip_coin() -> dict:
    results = Counter()
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentage_results = {
        possible_heads: (heads_dropped / 10000) * 100
        for possible_heads, heads_dropped in results.items()
    }
    return percentage_results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    point_x = list(data.keys())
    point_y = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(point_x, point_y, color="blue")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian distribution")
    plt.grid(True)
    plt.show()
