import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100
    return results


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    heads = list(distribution.keys())
    percentages = list(distribution.values())

    plt.figure(figsize=(8, 6))
    plt.bar(heads, percentages, color="blue", alpha=0.7)
    plt.title("Coin Flip Distribution (10 flips)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(heads)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()
