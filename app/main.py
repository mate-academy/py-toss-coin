import random
import numpy
import matplotlib.pyplot


def flip_coin() -> dict:
    heads_list = []

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads += 1
        heads_list.append(heads)

    return {i: heads_list.count(i) / 100 for i in range(11)}


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_points = numpy.array([key for key in result.keys()])
    y_points = numpy.array([value for value in result.values()])
    matplotlib.pyplot.plot(x_points, y_points)
    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")
    matplotlib.pyplot.show()
