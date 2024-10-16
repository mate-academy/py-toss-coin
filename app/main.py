import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    trials = 10000
    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: (v / trials) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    count = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(count, percentages, alpha=0.7, color="blue")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(count)
    plt.grid(axis="y")
    plt.show()


if __name__ == "__main__":
    result = flip_coin()
    print(result)
    draw_gaussian_distribution_graph(result)
