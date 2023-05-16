import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}
    temp = []
    for _ in range(10000):
        temp_result = []
        for side in range(10):
            temp_result.append(random.choice(["heads", "tails"]))
        temp.append(temp_result)
    for sides in temp:
        result[sides.count("heads")] += 1
    for value in result:
        result[value] /= 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_axis = np.array([i for i in result])
    y_axis = np.array([result[i] for i in result])
    plt.plot(x_axis, y_axis, 100)
    plt.xticks(np.arange(0, 11, 1))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop %")
    plt.show()
