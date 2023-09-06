import random
import matplotlib.pyplot as plt
import math
from typing import Dict


def flip_coin(
        num_experiments: int = 10000, num_flips: int = 10
) -> Dict[int, float]:
    results = {}  # Create a dictionary to store results

    for _ in range(num_experiments):
        heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                # Simulate coin flip
                heads += 1
        if heads in results:
            results[heads] += 1
        else:
            results[heads] = 1

    total_experiments = float(num_experiments)
    for key in results:
        results[key] = (results[key] / total_experiments) * 100.0

    return results


def binomial_probability(
        total_trials: int, successes: int, probability_success: float
) -> float:
    return math.comb(total_trials, successes)\
        * (probability_success ** successes)\
        * ((1 - probability_success) ** (total_trials - successes))


def draw_gaussian_distribution_graph(result_dict: Dict[int, float]) -> None:
    x_values = list(result_dict.keys())
    y_values = list(result_dict.values())

    plt.bar(x_values, y_values, align="center", alpha=0.5)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Cases")
    plt.title("Coin Flip Distribution")

    plt.show()


if __name__ == "__main__":
    coin_results = flip_coin()
    print(coin_results)
    draw_gaussian_distribution_graph(coin_results)
