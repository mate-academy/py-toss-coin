import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1
    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)
    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_axis = list(distribution.keys())
    y_axis = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x_axis, y_axis, color="skyblue", edgecolor="black", alpha=0.7)
    plt.title("Gaussian Distribution of Heads in 10 Coin Flips", fontsize=16)
    plt.xlabel("Number of Heads", fontsize=14)
    plt.ylabel("Percentage (%)", fontsize=14)
    plt.xticks(x_axis, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()
