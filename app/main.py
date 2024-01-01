import random
from numpy import array
from matplotlib import pyplot


def flip_coin() -> dict:
    dict_cases = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_case = sum(random.randint(0, 1) for _ in range(10))
        dict_cases[count_case] += 1
    return {
        key: round((value / 10000) * 100, 2)
        for key, value in dict_cases.items()
    }


def draw_gaussian_distribution_graph(dict_cases: dict):
    xpoints = array([*dict_cases.keys()])
    ypoints = array([*dict_cases.values()])
    pyplot.plot(xpoints, ypoints)
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.ylim(0, 100)
    return pyplot.show()
