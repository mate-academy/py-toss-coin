import random
import matplotlib.pyplot as plt
import numpy as np


def draw_gaussian_distribution_graph() -> None:

    dicter = {}

    for i in range(10000):
        heads = 0
        for i in range(10):

            if random.randint(1, 2) % 2 == 0:
                heads += 1
        dicter[heads] = dicter.setdefault(heads, 0) + 1

    for i in dicter:
        dicter[i] = dicter[i] / 10000
    print(dicter)

    x_points = np.array(sorted(dicter.keys()))  # Sort the keys for proper plotting
    y_points = np.array([dicter[key] for key in x_points])

    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()

draw_gaussian_distribution_graph()