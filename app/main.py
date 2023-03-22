import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_dict = {i: 0 for i in range(11)}
    for i in range(10000):
        head_count = 0
        for number in range(10):
            if random.choice([0, 1]) == 1:
                head_count += 1
        flip_dict[head_count] += 1
    for key, value in flip_dict.items():
        flip_dict[key] = (value / 10000) * 100
    return flip_dict


def draw_gaussian_distribution_graph(flip_dict: dict) -> None:
    flip_x = np.array(list(flip_dict.keys()))
    flip_y = np.array(list(flip_dict.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(flip_x, flip_y)
    plt.show()
