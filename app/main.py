import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(one_flip: int = 10) -> dict:
    results = {
        i: 0
        for i in range(one_flip + 1)
    }
    flips = 10000
    for _ in range(flips):
        flips = [
            random.randint(0, 1)
            for _ in range(10)
        ]
        heads = sum(flips)
        results[heads] += 1
    for key, value in results.items():
        results[key] = value / 100
    draw_gaussian_distribution_graph(results)
    return results


def draw_gaussian_distribution_graph(results: dict):
    ypoints = np.array(list(results.values()))
    xpoints = np.array(list(results.keys()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)
    plt.show()
