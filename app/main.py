import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    unsorted_dict = {}
    iterations = 10000

    for _ in range(iterations):
        heads_counter = 0

        for _ in range(10):

            drop = random.choice(["heads", "tails"])
            if drop == "heads":
                heads_counter += 1

        unsorted_dict[heads_counter] = unsorted_dict.get(heads_counter, 0) + 1

    sorted_dict = {key: unsorted_dict[key] for key in sorted(unsorted_dict)}
    for key, value in sorted_dict.items():
        sorted_dict[key] = round((value / iterations * 100), 2)
    return sorted_dict


def draw_gaussian_distribution_graph() -> None:
    x_points = np.array([i for i in range(11)])
    y_points = np.array([flip_coin().get(i, 0) for i in range(11)])

    plt.plot(x_points, y_points, label="Coin flip results")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Results - Gaussian Distribution")
    plt.grid(True)
    plt.show()


draw_gaussian_distribution_graph()
