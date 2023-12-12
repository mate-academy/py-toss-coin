import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    percentages = {
        key: (value / 10000) * 100 for key, value in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    keys = list(percentages.keys())
    values = list(percentages.values())

    plt.bar(keys, values, align="center")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Coin Flipping Distribution")
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)

    draw_gaussian_distribution_graph(results)
