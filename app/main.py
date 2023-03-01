import random
from matplotlib import pyplot


def ten_trows() -> list:
    return [random.randint(0, 1) for _ in range(10)]


def flip_coin() -> dict:
    result_dict = {k: 0 for k in range(11)}

    for _ in range(10000):
        result_dict[ten_trows().count(1)] += 1 / 100

    return result_dict


def draw_gaussian_distribution_graph(data: dict) -> None:
    pyplot.plot(data.keys(), data.values())
    pyplot.show()
