import random
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(num_cases):
        heads = sum(1 for _ in range(10) if random.random() < 0.5)
        results[heads] += 1
    for key in results:
        results[key] = (results[key] / num_cases) * 100
    return results


def draw_gaussian_distribution_graph(coin_flip_results: dict) -> None:
    number_of_heads = list(coin_flip_results.keys())
    percentage_of_cases = list(coin_flip_results.values())
    plt.bar(number_of_heads, percentage_of_cases)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()


coin_flip_results = flip_coin()
draw_gaussian_distribution_graph(coin_flip_results)
