import random
from matplotlib import pyplot
import numpy


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    variants = ["heads", "tails"]

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            choice = random.choice(variants)
            if choice == "heads":
                heads_count += 1
        result_dict[heads_count] += 1
    for key in result_dict:
        result_dict[key] = (result_dict[key] / 10000) * 100
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    axis_x = list(data.keys())
    axis_y = list(data.values())

    pyplot.plot(axis_x, axis_y, marker="o", linestyle="-")
    pyplot.title("Gaussian Distribution of Coin Flips")
    pyplot.xlabel("Number of Heads")
    pyplot.ylabel("Percentage")
    pyplot.grid(True)
    mu = numpy.mean(axis_x)
    sigma = numpy.std(axis_x)
    part_of_equation = (axis_x - mu) ** 2 / (2 * sigma ** 2)
    curve = numpy.exp(-part_of_equation) / (sigma * numpy.sqrt(2 * numpy.pi))
    pyplot.plot(axis_x, curve, "r--")

    pyplot.show()
