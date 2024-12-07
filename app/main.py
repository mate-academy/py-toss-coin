import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                   5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        half_list = []
        for i in range(10):
            half_list.append(random.randint(0, 1))
        result_dict[half_list.count(1)] += 1
    for dict_key, dict_value in result_dict.items():
        dict_value /= 100
        result_dict[dict_key] = dict_value
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    start_data_dict = flip_coin()
    x_list = []
    y_list = []

    for dict_key, dict_value in start_data_dict.items():
        x_list.append(dict_key)
        y_list.append(dict_value)

    x_axis = np.array(x_list)
    y_axis = np.array(y_list)

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)

    plt.show()
