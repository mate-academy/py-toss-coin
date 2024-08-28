import random
import matplotlib.pyplot as plt


def flip_coin(num_trials=10000, num_flips=10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads] += 1

    # Convert counts to percentages
    for key in results:
        results[key] = (results[key] / num_trials) * 100

    return results


def draw_gaussian_distribution_graph(data) -> None:
    plt.bar(data.keys(), data.values())
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips (10000 trials)")
    plt.show()
