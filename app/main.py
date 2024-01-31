import random
import matplotlib.pyplot
from typing import Dict


def flip_coin(num_flips: int = 10000, num_coins: int = 10) -> Dict[int, float]:
    results = {i: 0 for i in range(num_coins + 1)}

    for _ in range(num_flips):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coins))
        results[num_heads] += 1

    percentages = {key: (value / num_flips) * 100
                   for key, value in results.items()}
    return percentages


def draw_gaussian_distribution_graph(
        percentages: Dict[int, float]
) -> None:
    matplotlib.pyplot.plot(
        list(percentages.keys()),
        list(percentages.values()),
        marker="o",
        linestyle="-")
    matplotlib.pyplot.title("Coin Flip Distribution")
    matplotlib.pyplot.xlabel("Number of Heads")
    matplotlib.pyplot.ylabel("Percentage")
    matplotlib.pyplot.show()
