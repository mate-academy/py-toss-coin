import random
import matplotlib.pyplot as plot


def flip_coin() -> dict[int]:
    coin_flips = {key: 0 for key in range(11)}
    cases = 10000

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads += 1
        coin_flips[heads] += 1

    for heads in coin_flips:
        coin_flips[heads] = (coin_flips[heads] / cases) * 100

    return coin_flips


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_ax = [heads for heads in data]
    y_ax = [percentage for percentage in data.values()]

    fig, ax = plot.subplots()
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 100])
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage, %")

    plot.plot(x_ax, y_ax)
    plot.show()
