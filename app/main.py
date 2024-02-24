import matplotlib.pyplot
import numpy
import random


def flip_coin() -> dict:
    rounds_num = 10000
    rounds_dict = {i: 0 for i in range(11)}
    for _ in range(rounds_num):
        heads = sum(random.choice((1, 0)) for _ in range(10))
        rounds_dict[heads] += 1
    return {k: round(v / rounds_num * 100, 2) for k, v in rounds_dict.items()}


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_points = numpy.array([distribution.keys()])
    y_points = numpy.array([distribution.values()])
    matplotlib.pyplot.plot(x_points, y_points)
    matplotlib.pyplot.show()
