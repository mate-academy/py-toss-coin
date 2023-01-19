import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {x: 0 for x in range(0, 11)}
    for flip in range(10000):
        count = 0
        for _ in range(10):
            count += 1 if random.choice(["Eagle", "Tails"]) == "Tails" else 0
        result_dict[count] += 1
    return {x: result_dict[x] / 100 for x in result_dict}


def draw_gaussian_distribution_graph() -> None:
    coordinate = flip_coin()
    x_coordinate = np.array([x for x in coordinate])
    y_coordinate = np.array([coordinate[x] for x in coordinate])

    plt.axis([0, 10, 0, 100])
    plt.plot(x_coordinate, y_coordinate, "o-g", label="first", lw=3)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
