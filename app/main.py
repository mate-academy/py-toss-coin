import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:

    results = {i: 0 for i in range(11)}
    num_cases = 10000

    for _ in range(num_cases):
        heads_count = 0
        for _ in range(10):
            outcome = random.randint(0, 1)
            if outcome == 0:
                heads_count += 1
        results[heads_count] += 1
    for key in results:
        results[key] = round((results[key] / num_cases) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    xside = list(results.keys())
    yside = list(results.values())

    xpoints = np.array(xside)
    ypoints = np.array(yside)

    plt.plot(xpoints, ypoints)
    plt.plot(xside, yside)

    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads Count")
    plt.title("Gaussian Distribution")
    plt.show()
