import random

import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> dict:
    results = {}

    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[num_heads] = results.get(num_heads, 0) + 1

    percentage_results = {key: (value / num_trials) * 100
                          for key, value in results.items()}

    return percentage_results


def draw_distribution_graph(results):
    plt.bar(results.keys(), results.values(), color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.show()

    draw_distribution_graph(results)
