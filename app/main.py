import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = {}
    for test in range(11):
        results[test] = 0
    for trial in range(trials):
        heads = 0
        for experement in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1
    for test in range(11):
        results[test] = round(results[test] / trials * 100, 2)
    return results


def draw_gaussian_distribution_graph(flip_coin: flip_coin()) -> None:
    keys = flip_coin.keys()
    values = flip_coin.values()

    plt.bar(keys, values)
    plt.xlabel("Heads")
    plt.ylabel("Percentage")
    plt.title("Flip coin")
    plt.show()
