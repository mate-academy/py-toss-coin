import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for _ in range(0, 10000):
        count = 0
        for i in range(0, 10):
            if random.randint(0, 1) == 1:
                count += 1

        result[count] += 1

    for i in range(0, 11):
        result[i] /= 100

    return result


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    yarray = []

    for i in range(0, len(points)):
        yarray.append(points[i])

    ypoints = np.array(yarray)

    plt.title("Gaussian distribuition")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(ypoints)
    plt.show()
