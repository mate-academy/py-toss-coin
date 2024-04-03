from random import choices
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    options = ["heads", "tails"]
    heads = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10001):
        case = choices(options, k=10)
        heads[case.count("heads")] += 1

    return {key: round((value / 10000) * 100, 2)
            for key, value in heads.items()}


def draw_gaussian_distribution_graph() -> None:
    data_dict = flip_coin()
    x_points = np.array([key for key in data_dict])
    y_points = np.array([value for value in data_dict.values()])

    plt.plot(x_points, y_points)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)

    plt.show()
