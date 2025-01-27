import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    results = {i: 0 for i in range(11)}
    num_cases = 10_000
    for _ in range(num_cases):
        head_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                head_count += 1
        results[head_count] += 1

    for key, value in results.items():
        results[key] = round((value / num_cases) * 100, 2)
    return results


def draw_gaussian_distribution_graph(
        data: Dict[int, float],
        title: str = "Coin Flip Distribution",
        x_label: str = "Number of Heads",
        y_label: str = "Percentage of Cases"
) -> None:
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), color="skyblue")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(list(data.keys()))
    plt.grid(axis="y", alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
