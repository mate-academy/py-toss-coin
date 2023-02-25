from random import randint
from matplotlib import pyplot


def flip_coin() -> dict:
    flips = {i: 0 for i in range(11)}
    for i in range(10000):
        heads = 0
        for _ in range(10):
            if randint(0, 1) == 1:
                heads += 1
        flips[heads] += 1
    return {key: value / 100 for key, value in flips.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    pyplot.plot(data.keys(), data.values())
    pyplot.show()
