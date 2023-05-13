import random
import matplotlib.pyplot
import numpy


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}
    coin = ["eagle", "head"]
    for _ in range(10000):
        head_side_times_quantity = 0
        for i in range(10):
            head_site = random.choice(coin)
            if head_site == "head":
                head_side_times_quantity += 1
        result[head_side_times_quantity] += 1
    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)
    return result


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_points = numpy.array([i for i in results])
    y_points = numpy.array([value for value in results.values()])
    matplotlib.pyplot.plot(x_points, y_points, 100)
    matplotlib.pyplot.title("Gaussian distribution")
    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")
    matplotlib.pyplot.show()
