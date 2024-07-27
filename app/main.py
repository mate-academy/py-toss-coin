import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = ["heads", "tails"]
    results_dict = {i: 0 for i in range(11)}

    for i in range(10000):
        temp_result = 0
        for _ in range(1, 11):
            if random.choice(results) == "heads":
                temp_result += 1
        results_dict[temp_result] += 1

    for i in range(11):
        results_dict[i] /= 100
    return results_dict


def draw_gaussian_distribution_graph() -> None:
    xpoints = np.array(list(map(int, flip_coin().keys())))
    ypoints = np.array(list(flip_coin().values()))

    plt.plot(xpoints, ypoints, color="blue")

    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    plt.xlim(0, 10)
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 101, 10))

    plt.show()
