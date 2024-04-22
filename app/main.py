import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    percentages = {
        key: (value / trials * 100)
        for key, value in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    plt.bar(percentages.keys(), percentages.values(), color="skyblue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.show()
