import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    template = {i: 0 for i in range(10 + 1)}
    sides = ["heads", "tails"]

    for _ in range(10000):
        current_flipping = [
            random.choice(sides) for _ in range(10)
        ].count("heads")
        template[current_flipping] += 1

    percentage = {
        key: (value / 10000) * 100 for key, value in template.items()
    }
    return percentage


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()


flip_coin()
draw_gaussian_distribution_graph()
