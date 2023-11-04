import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1
    for key in results:
        results[key] /= 100
    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    plt.bar(results.keys(), results.values())
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
