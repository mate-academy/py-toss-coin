from matplotlib import pyplot
from numpy import array
import random


def flip_coin() -> dict:
    result = {}
    total_flips = 10
    cases = 10000

    for _ in range(cases):
        eagles = 0
        for _ in range(total_flips):
            if random.random() < 0.5:
                eagles += 1
        if eagles not in result:
            result[eagles] = 1
        else:
            result[eagles] += 1

    percents = {}
    for key, value in result.items():
        percent = round(value / cases * 100, 2)
        percents[key] = percent
    return {k: percents[k] for k in sorted(percents)}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    vertical_y = array(list(data.values()))
    horizontal_x = array(list(data.keys()))

    pyplot.plot(horizontal_x, vertical_y, "b")
    pyplot.yticks([i for i in range(101) if i % 10 == 0])
    pyplot.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    pyplot.xlim(left=0, right=10)
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.show()
