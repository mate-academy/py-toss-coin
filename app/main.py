import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    result = []

    for _ in range(num_trials):
        head_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        result.append(head_count)

    counts = Counter(result)
    result_in_percent = {
        key: (value / num_trials) * 100 for key, value in counts.items()
    }

    return result_in_percent


def draw_gaussian_distribution_graph(results: dict) -> None:
    number_of_heads = list(results.keys())
    percentages = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.bar(
        number_of_heads,
        percentages,
        color="skyblue",
        edgecolor="black",
        width=0.8,
    )

    plt.title("Gaussian Distribution of Coin Flips", fontsize=16)
    plt.xlabel("Number of Heads", fontsize=14)
    plt.ylabel("Percentage", fontsize=14)
    plt.xticks(range(0, 11), fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    draw_gaussian_distribution_graph(results)
