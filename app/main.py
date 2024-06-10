import random
from matplotlib import pyplot as plt, pyplot


def flip_coin(flips: int = 10, cases: int = 10000) -> dict:
    result = {attempt: 0 for attempt in range(flips + 1)}
    for _ in range(cases):
        heads_count = 0
        for _ in range(flips):
            if random.random() < 0.5:
                heads_count += 1
        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] / cases) * 100

    return result


def draw_gaussian_distribution_graph(values: dict) -> pyplot.figure:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim([0, 10])
    plt.ylim([0, 100])

    x_values = list(values.keys())
    y_values = list(values.values())
    plt.plot(x_values, y_values)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
