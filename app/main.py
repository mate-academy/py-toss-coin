# write your code here
import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {
        i: 0
        for i in range(0, 11)
    }
    for _ in range(10000):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        result[heads_count] += 1

    for key in result.keys():
        result[key] = result[key] / 100

    return result


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    x_points = np.array([key for key in flip_coin().keys()])
    y_points = np.array([value for value in flip_coin().values()])

    plt.plot(x_points, y_points)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph()
