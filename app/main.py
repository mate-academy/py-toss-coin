import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    possible_heads_dropped = {}
    for index in range(11):
        possible_heads_dropped[index] = sum([random.randint(0, 1) for _ in range(10000)]) / 100

    return possible_heads_dropped


def draw_gaussian_distribution_graph() -> None:

    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    plt.plot(x, y)

    plt.title("Sports Watch Data")
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    plt.show()


print(flip_coin())
print(draw_gaussian_distribution_graph())
