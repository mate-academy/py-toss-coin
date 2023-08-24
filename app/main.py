import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> dict:
    result = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                num_heads += 1
        result[num_heads] += 1

    percentages = {key: (value / num_cases) * 100
                   for key, value in result.items()}
    return percentages


def draw_gaussian_distribution_graph(data_dict: dict) -> None:
    xpoint = np.array(list(data_dict.keys()))
    ypoint = np.array(list(data_dict.values()))

    plt.plot(xpoint, ypoint)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()
