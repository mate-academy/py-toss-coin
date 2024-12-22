import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        count = sum(random.choice([0, 1]) for _ in range(10))
        results[count] += 1

    for key, value in results.items():
        results[key]: (value // num_trials) * 100
    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    keys = list(distribution.keys())
    values = list(distribution.values())

    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.xticks(range(11))  # Set x-axis ticks from 0 to 10
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

    coin_flip_distribution = flip_coin()
    print(coin_flip_distribution)

    draw_gaussian_distribution_graph(coin_flip_distribution)
