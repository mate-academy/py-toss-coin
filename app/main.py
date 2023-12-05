import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {
        i: 0 for i in range(11)
    }

    for number in range(10000):
        case_result = 0
        for num in range(10):
            case_result += random.randint(0, 1)

        result[case_result] += 1

    return {
        key: (value / 10000 * 100)
        for key, value in result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    xpoints = np.array([
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ])
    ypoints = np.array([
        0.13, 1.01, 4.34, 11.67,
        20.33, 24.94, 20.68, 11.53,
        4.41, 0.89, 0.69
    ])

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 11, 1))

    plt.show()


draw_gaussian_distribution_graph()
