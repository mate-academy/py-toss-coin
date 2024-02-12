import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] = results.get(num_heads, 0) + 1

    for num_heads in results:
        number = results[num_heads]
        results[num_heads] = round((number / float(10000)) * 100, 3)
    return results


def draw_gaussian_distribution_graph(funck: dict) -> None:
    xpoints = np.array([key for key in funck.keys()])
    ypoints = np.array([vel for vel in funck.values()])
    plt.bar(xpoints, ypoints)
    plt.show()
