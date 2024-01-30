import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(try_number: int = 10000, flip_coin: int = 10) -> None:
    dict_percent = {}
    for _ in range(try_number):
        prob_head = sum(random.choice([0, 1]) for _ in range(flip_coin))
        dict_percent[prob_head] = dict_percent.get(prob_head, 0) + 1
    result = {key: value / try_number * 100
              for key, value in dict_percent.items()}
    return result


def draw_gaussian_distribution_graph(dict_percent: dict) -> None:
    xpoint = np.array([key for key in dict_percent.keys()])
    ypoint = np.array([val for val in dict_percent.values()])

    plt.plot(xpoint, ypoint)
    plt.title("Gaussian distribution")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")

    plt.show()
