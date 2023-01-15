import random
import numpy as np
import matplotlib.pyplot as plt


def flip_10_times() -> int:
    result = 0
    for _ in range(10):
        coin = random.choice(["heads", "tails"])
        if coin == "heads":
            result += 1
    return result


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        result_of_10_flips = flip_10_times()
        result_dict[result_of_10_flips] += 1

    for key, value in result_dict.items():
        result_dict[key] = (value / 10000) * 100

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    flip_dict = flip_coin()
    dict_keys = []
    dict_values = []
    for key, value in flip_dict.items():
        dict_keys.append(key)
        dict_values.append(value)

    x_point = np.array(dict_keys)
    y_point = np.array(dict_values)

    plt.plot(x_point, y_point)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
