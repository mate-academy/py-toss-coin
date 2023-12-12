import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
              5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in range(10000):
        count_1 = 0
        for i in range(10):
            if random.randint(0, 1) == 1:
                count_1 += 1
        result[count_1] += 1

    for key in result.keys():
        result[key] = (result[key] * 100) / 10000

    return result


def draw_gaussian_distribution_grap(dates: dict) -> None:

    xpoints = np.array(list(dates.keys()))
    ypoints = np.array(list(dates.values()))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)
    plt.show()
