import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    chances = {}
    for _ in range(10000):
        counter = sum(random.randint(0, 1) for _ in range(10))
        if counter not in chances:
            chances[counter] = 0
        chances[counter] += 1
    return {
        key: round(value / 10000 * 100, 2)
        for key, value in sorted(chances.items(), key=lambda a: a[0])
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    ypoints = np.array([chance for chance in data.values()])
    xpoints = np.array([key for key in data.keys()])

    plt.plot(xpoints, ypoints)
    plt.ylim(0, 100)
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()
