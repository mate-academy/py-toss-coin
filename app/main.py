import random
from matplotlib import pyplot
import numpy


def flip_coin(cases: int = 10000, trials: int = 10) -> dict:
    normal_distribution = {n: 0 for n in range(trials + 1)}

    for _ in range(cases):
        number_of_heads = sum(random.randint(0, 1) for _ in range(trials))
        normal_distribution[number_of_heads] += 1

    probability_distribution = {
        key: round(value * 100 / cases, 2)
        for key, value in normal_distribution.items()
    }

    return probability_distribution


def draw_gaussian_distribution_graph(
        cases: int = 10000,
        trials: int = 10
) -> None:
    distribution = flip_coin(cases, trials)
    y_points = numpy.array(list(distribution.values()))

    pyplot.plot(y_points)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Drop percentage %")
    pyplot.ylabel("Heads count")

    pyplot.show()
