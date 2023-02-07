import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    outcome = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }

    for _ in range(0, 10000):
        heads = 0

        for _ in range(0, 10):
            if random.choice([True, False]):
                heads += 1

        outcome[heads] += 1

    for item, value in outcome.items():
        outcome[item] = round(value / 100, 2)

    return outcome


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = data.keys()
    y_points = data.values()

    plt.plot(x_points, y_points)

    plt.yticks([0, 20, 40, 60, 80, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.show()
