import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    num_trials = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        flips = [random.randint(0, 1) for _ in range(10)]
        heads = sum(flips)
        counts[heads] += 1

    percentages = {
        k: round((v / num_trials) * 100, 2) for k, v in counts.items()
    }
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    head_counts = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(
        head_counts,
        percentages,
        width=0.8,
        align="center",
        alpha=0.7,
        color="skyblue"
    )

    # Додати значення на стовпці
    for bar_plot in bars:
        height = bar_plot.get_height()
        plt.text(
            bar_plot.get_x() + bar_plot.get_width() / 2.0,
            height,
            f"{height: .2f}%",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.xticks(head_counts)
    plt.ylim(0, max(percentages) + 5)
    plt.xlabel("Number of Heads", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.title("Gaussian Distribution of Heads in 10 Coin Flips", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
