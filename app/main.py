from collections import Counter
from random import randint

import matplotlib.pyplot as plt


def flip_coin(times: int = 10_000) -> dict[int, float]:
    # heads == 1
    heads_counts = Counter(
        sum(
            randint(0, 1)
            for _ in range(10)
        )
        for _ in range(times)
    )
    return {
        key: round((count * 100) / times, 2)
        for key, count in heads_counts.items()
    }


def draw_gaussian_distribution_graph(
        heads_percentages: dict[int, float]
) -> None:

    percentages = [
        heads_percentages[key]
        for key in sorted(heads_percentages.keys())
    ]

    plt.title("Gaussian distribution")
    plt.ylabel("Drop Percentage, %")
    plt.xlabel("Head Count")

    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.yticks(range(5, 96, 10), minor=True)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(1, 11))

    plt.plot(percentages)
    plt.show()


if __name__ == "__main__":
    heads_percentage = flip_coin()
    draw_gaussian_distribution_graph(heads_percentage)
