import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    probabilities = dict.fromkeys(range(11), 0)
    for case in range(10_000):
        counter = 0
        for flip in range(10):
            choice = random.choice(["heads", "tails"])
            if choice == "heads":
                counter += 1
        probabilities[counter] += 1
    for key in probabilities:
        probabilities[key] = round(probabilities[key] / 10_000 * 100, 2)
    return probabilities


def create_a_graph_of_gaussian_distribution() -> None:
    x_points = np.array([x for x in flip_coin().keys()])
    y_points = np.array([y for y in flip_coin().values()])

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("heads dropped out number")
    plt.ylabel("Percentage of cases per 10k attempts")
    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.show()


create_a_graph_of_gaussian_distribution()
