import random
from matplotlib import pyplot
import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(10 + 1)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = round((results[heads_count] / 10000) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_points = np.array(list(results.keys()))
    y_points = np.array(list(results.values()))

    pyplot.plot(x_points, y_points)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.show()


print(flip_coin())
draw_gaussian_distribution_graph(flip_coin())
