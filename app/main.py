import random
from matplotlib import pyplot as plt
import numpy as np


def flip_coin() -> dict:

    result = {key: 0 for key in range(11)}

    for _ in range(10000):
        count_heads = sum(random.randint(0, 1) for _ in range(10))
        result[count_heads] += 1

    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    number_of_heads = list(result.keys())
    percentages = list(result.values())

    plt.figure(figsize=(10, 6))

    plt.plot(number_of_heads, percentages, color="blue")

    plt.xlim(left=0, right=10)
    plt.ylim(bottom=0)

    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 11, 1))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
