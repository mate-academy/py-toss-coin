import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(flips: int = 10000) -> dict:

    result = {key: 0 for key in range(11)}

    for _ in range(flips):
        flip_count = sum(random.randint(0, 1) for _ in range(10))
        result[flip_count] += 1

    for key, value in result.items():
        result[key] = round(value / flips * 100, 2)

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    heads = list(result.keys())
    percent = list(result.values())

    plt.figure(figsize=(10, 6))
    plt.plot(heads, percent, color="blue")

    plt.xlim(left=0, right=10)
    plt.ylim(bottom=0)

    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
