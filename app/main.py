import random
import matplotlib
from typing import Dict


def flip_coin(num_cases: int = 10000,
              num_flips: int = 10) -> Dict[int, float]:
    results = {heads: 0 for heads in range(num_flips + 1)}

    for _ in range(num_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    for heads, count in results.items():
        results[heads] = (count / num_cases) * 100

    return results


def draw_gaussian_distribution_graph(results: Dict[int, float]) -> None:
    x_values = list(results.keys())
    y_values = list(results.values())

    matplotlib.plot(x_values, y_values, marker="o", linestyle="-")
    matplotlib.title("Gaussian Distribution of Coin Flips")
    matplotlib.xlabel("Number of Heads")
    matplotlib.ylabel("Percentage")
    matplotlib.grid(True)
    matplotlib.show()
