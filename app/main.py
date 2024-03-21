import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    return {
        number:
            [sum(random.randint(0, 1)
                 for i in range(10))
             for j in range(10000)].count(number) / 100
        for number in range(11)
    }


def draw_gaussian_distribution_graph(distribution_data: dict):
    xpoints = np.array(list(distribution_data.keys()))
    ypoints = np.array(list(distribution_data.values()))
    plt.plot(xpoints, ypoints)
    plt.xlabel("Count of head")
    plt.ylabel("Probability")
    plt.show()