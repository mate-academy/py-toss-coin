import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {}
    ls = [0] * 11
    for _ in range(10000):
        temp = sum(random.randint(0, 1) for _ in range(10))
        ls[temp] += 1

    for i in range(11):
        results[i] = ls[i] / 100
    return results


def draw_gaussian_distribution_graph() -> object:
    result = flip_coin()
    keys, values = result.keys(), result.values()
    plt.plot(list(keys), list(values))
    plt.show()
    return plt
