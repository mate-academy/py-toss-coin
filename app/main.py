import random
import matplotlib
import numpy as np


def flip_coin() -> dict:
    return_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for experiment_number in range(10000):
        number_of_times = 0
        for coin_flip_number in range(1, 11):
            if random.randint(0, 1):
                number_of_times += 1
        return_dict[number_of_times] += 1
    for number_of_times in range(0, 11):
        return_dict[number_of_times] = round(
            return_dict[number_of_times] / 100, 2
        )
    return return_dict


def draw_gaussian_distribution_graph(interest_dictionary: dict) -> None:
    xpoints = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ypoints = np.array(
        [key for key in interest_dictionary.values()]
    )

    matplotlib.pyplot.plot(xpoints, ypoints)
    matplotlib.pyplot.title("Gaussian distribution")
    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")
    matplotlib.pyplot.show()
