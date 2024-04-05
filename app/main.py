import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> list:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

    total_cases = sum(results.values())
    for key in results:
        results[key] = (results[key] / total_cases) * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:

    number_of_heads = np.array(list(results.keys()))
    percentage = np.array(list(results.values()))

    plt.title("Gaussian distribution", loc="left")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(number_of_heads, percentage)
    plt.show()
