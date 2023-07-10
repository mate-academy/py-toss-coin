import random
from matplotlib import pyplot
from numpy import array, arange


def flip_coin() -> dict:
    cases_list = []

    for _ in range(10000):
        value = 0

        for _ in range(10):
            value += random.randint(0, 1)

        cases_list.append(value)

    results = {count: cases_list.count(count) / 100 for count in range(11)}

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_array = array(list(data.keys()))
    y_array = array(list(data.values())).astype(float)

    pyplot.plot(x_array, y_array)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.xlim(0, 10)
    pyplot.ylim(0, 100)

    pyplot.yticks(arange(0, 101, 10))

    pyplot.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin())
