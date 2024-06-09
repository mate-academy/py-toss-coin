import random
import numpy as np
from matplotlib import pyplot


def flip_coin(flips: int = 10, repeats: int = 10000) -> dict:
    results = {attempt: 0 for attempt in range(flips + 1)}

    for _ in range(repeats):
        heads_count = sum(random.choice([True, False]) for _ in range(flips))
        results[heads_count] += 1

    return {heads: (count / repeats) * 100 for heads, count in results.items()}


def draw_gaussian_distribution_graph(values: dict) -> None:
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.ylim(0, 100)
    pyplot.xlim(0, 10)

    x_points = np.array(list(values.keys()))
    y_points = np.array(list(values.values()))
    pyplot.plot(x_points, y_points)
    pyplot.show()


draw_gaussian_distribution_graph(flip_coin())
