import random
import numpy
import matplotlib.pyplot


def flip_coin(cases: int = 10000, times: int = 10) -> dict:
    count = {i: 0 for i in range(times + 1)}

    for _ in range(cases):
        ran = sum([random.choice([0, 1]) for _ in range(times)])
        count[ran] += 1

    count_percent = {
        key: round((value / cases) * 100, 2) for key, value in count.items()
    }
    return count_percent


def draw_gaussian_distribution_graph(count_percent: dict) -> None:

    x_axis = numpy.array([num for num in range(11)])
    y_axis = numpy.array([percent for percent in count_percent.values()])

    matplotlib.pyplot.plot(x_axis, y_axis)

    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")

    matplotlib.pyplot.show()

draw_gaussian_distribution_graph(flip_coin())