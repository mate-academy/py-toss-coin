import random

from matplotlib import pyplot


def flip_coin() -> dict:
    resoults = {}
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        resoults[heads_count] = resoults.get(heads_count, 0) + 1
    calculate_resoults = {key: round(((value / 10000) * 100), 2)
                          for key, value in resoults.items()}
    calculate_resoults = dict(sorted(calculate_resoults.items()))
    return calculate_resoults


def draw_gaussian_distribution_graph(flip_coin: dict) -> None:
    x_cor = list(flip_coin.keys())
    y_cor = list(flip_coin.values())

    pyplot.plot(x_cor, y_cor)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage, %")

    pyplot.show()
