import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin = ["head", "tail"]
    num_of_cases = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(num_of_cases):
        num_heads = sum(random.choice(coin) == "head" for _ in range(10))
        result[num_heads] += 1

    for i in range(11):
        result[i] = (result[i] / num_of_cases) * 100

    return result


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()

    x_array = np.array([i for i in range(0, 10)])
    y_array = np.array([value for value in result.values()])

    plt.plot(x_array, y_array)

    plt.xlabel("Drop percentage%")
    plt.ylabel("Heads count")

    plt.show()
