import random
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[num_heads] += 1

    distribution = {
        key: (value / num_cases) * 100 for key,
        value in results.items()
    }
    return distribution


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.bar(x_values, y_values, color="blue", alpha=0.7)
    plt.title("Coin Flips Distribution")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.xticks(x_values)
    plt.show()
