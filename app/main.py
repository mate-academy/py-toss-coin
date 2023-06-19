import random
from typing import Any
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    results = {}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1

        if num_heads in results:
            results[num_heads] += 1
        else:
            results[num_heads] = 1

    for num_heads in results:
        results[num_heads] = (results[num_heads] / num_cases) * 100

    return results


def draw_gaussian_distribution_graph(result: dict) -> None:
    lists = sorted(result.items())
    x, y = zip(*lists)
    plt.plot(x, y)

    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
