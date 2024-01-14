from random import randint
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    value_list = list()

    # let's consider: choice 1 equal "head"

    # create a list of results of values 10000 attempts
    for _ in range(10000):
        head = 0
        for attempt in range(10):
            attempt_value = randint(0, 1)
            if attempt_value == 1:
                head += 1
        value_list.append(head)

    # create result_dict dict
    result_dict = {x: 0.0 for x in range(11)}
    for value in range(11):
        result_dict[value] = (value_list.count(value)) / 100

    return result_dict


result = flip_coin()


def draw_gaussian_distribution_graph(values: dict) -> None:
    yarr = [value for value in values.values()]

    xpoints = np.array(range(0, 11))
    ypoints = np.array(yarr)
    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph(result)
