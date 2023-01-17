import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    coin_flips = 10
    cases = 10000
    heads_count = {i: 0 for i in range(coin_flips + 1)}

    for _ in range(cases):
        heads = 0

        for _ in range(coin_flips):
            if random.random() < 0.5:
                heads += 1

        heads_count[heads] += 1

    for i in range(coin_flips + 1):
        heads_count[i] = round(heads_count[i] / cases * 100, 2)

    return heads_count


def draw_gaussian_distribution_graph(data: callable) -> None:

    x_points = list(data.keys())
    y_points = list(data.values())

    plt.plot(x_points, y_points)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()


data = flip_coin()
draw_gaussian_distribution_graph(data)
