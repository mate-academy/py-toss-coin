import random
import matplotlib.pyplot as plt
from collections import defaultdict


def flip_coin():
    num_simulations = 10000
    num_flips = 10
    results = defaultdict(int)

    for _ in range(num_simulations):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[num_heads] += 1
    probable_distribution = {k: v / num_simulations * 100 for k, v in results.items()}
    return probable_distribution


def draw_gaussian_distribution_graph(probable_distribution):
    x = list(probability_distribution.keys())
    y = list(probability_distribution.values())

    plt.bar(x, y, align='center', alpha=0.7)
    plt.xlabel('Number of Heads')
    plt.ylabel('Percentage')
    plt.title('Gaussian Distribution of Coin Flips')
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    probability_distribution = flip_coin()
    print(probability_distribution)
    draw_gaussian_distribution_graph(probability_distribution)
