import random
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin() -> dict:
    num_trials = 10000
    num_flips = 10

    counts = Counter(
        sum(random.choice([0, 1]) for _ in range(num_flips))
        for _ in range(num_trials)
    )

    return {
        heads: round((count / num_trials) * 100, 2)
        for heads, count in sorted(counts.items())
    }


def draw_gaussian_distribution_graph(dist: dict) -> None:
    head_counts = list(dist.keys())
    percentages = list(dist.values())
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(0, 11))
    plt.plot(head_counts, percentages, color="blue")
    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Drop percentage %", fontsize=12)
    plt.title("Gaussian distribution", fontsize=14)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    draw_gaussian_distribution_graph(distribution)
