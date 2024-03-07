import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    trials = 10000

    for i in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    heads_count = list(results.keys())
    percentages = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.bar(heads_count, percentages, color="skyblue")

    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage (%)")

    plt.grid(axis="y", linestyle="--")
    plt.show()
