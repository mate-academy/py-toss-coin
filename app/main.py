from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_flips = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if randint(0, 1) == 1:
                heads_count += 1
        coin_flips[heads_count] += 1

    percents = {
        key: (value / 10000) * 100
        for key, value in coin_flips.items()
    }

    return percents


def draw_gaussian_distribution_graph() -> None:
    percents = flip_coin()

    x_values = list(percents.keys())
    y_values = list(percents.values())

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
