import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    flips = {index: 0 for index in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice([0, 1]):
                count += 1
        flips[count] += 1

    return {k: v / 100 for k, v in flips.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values())
    plt.title("Normal (Gaussian) distribution")
    plt.show()
