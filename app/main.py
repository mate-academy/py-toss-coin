import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number = 10000
    spys = {i: 0 for i in range(11)}

    for _ in range(number):
        count = 0
        for i in range(10):
            result = random.choice([0, 1])
            if result == 1:
                count += 1
        spys[count] += 1

    res = {i: round(((value / number) * 100), 2)
           for i, value in spys.items()}
    return res


def draw_gaussian_distribution_graph() -> None:
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    result = flip_coin()
    x_coordinate = np.array(list(result.keys()))
    y_coordinate = np.array(list(result.values()))
    plt.plot(x_coordinate, y_coordinate, marker="o")
    plt.grid(True)
    plt.show()


draw_gaussian_distribution_graph()
