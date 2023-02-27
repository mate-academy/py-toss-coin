import random
import matplotlib.pyplot as plt
import numpy


def draw_gaussian_distribution_graph(coords: dict) -> None:

    x_coords = []
    y_coords = []

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")

    for index, value in coords.items():
        x_coords.append(index)
        y_coords.append(value)

    xpoints = numpy.array(x_coords)
    ypoints = numpy.array(y_coords)
    plt.plot(xpoints, ypoints)


def flip_coin() -> dict:
    result = []

    for _ in range(10000):
        toss_coin = ""
        for i in range(10):
            toss_coin += str(random.randint(0, 1))

        result.append(toss_coin.count("0"))

    flip_coin_result = {}

    for i in range(11):
        flip_coin_result[i] = round((result.count(i) / 10000) * 100, 2)

    draw_gaussian_distribution_graph(flip_coin_result)

    return flip_coin_result
