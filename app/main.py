import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    return {key: (value / trials) * 100 for key, value in results.items()}


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    keys = list(results.keys())
    values = list(results.values())

    plt.bar(keys, values, tick_label=keys)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.show()
