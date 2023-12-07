import random
import numpy
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    temporary_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        flip = sum(random.randint(0, 1) for _ in range(10))
        temporary_dict[flip] += 1
    percentage_dict = {
        value: (count / 10000) * 100
        for value, count in temporary_dict.items()
    }
    return percentage_dict


def draw_gaussian_distribution_graph(percentage_dict: dict) -> None:
    x_axis = numpy.array([value for value in percentage_dict.keys()])
    y_axis = numpy.array([percent for percent in percentage_dict.values()])

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
