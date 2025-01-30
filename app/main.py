import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin_ten_times() -> int:
    coin = ["head", "tail"]
    head_counter = 0
    for i in range(10):
        if random.choice(coin) == "head":
            head_counter += 1
    return head_counter


def flip_coin() -> dict:
    flip_dict = {}
    total_cases = 10_000
    for i in range(total_cases):
        head_number = flip_coin_ten_times()
        if head_number not in flip_dict:
            flip_dict[head_number] = 1
        else:
            flip_dict[head_number] += 1

    for key in flip_dict:
        flip_dict[key] = round((flip_dict[key] / total_cases) * 100, 2)
    sorted_flip_dict = sorted(flip_dict.items())

    return dict(sorted_flip_dict)


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    points = flip_coin()
    x_point = np.array(list(points.keys()))
    y_point = np.array(list(points.values()))
    plt.plot(x_point, y_point)
    plt.show()