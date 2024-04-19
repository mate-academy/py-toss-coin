import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(10 + 1)}

    total_flip = 10000

    for _ in range(total_flip):
        head_flip = sum(1 for _ in range(10) if random.random() < 0.5)
        result[head_flip] += 1

    for key in result:
        result[key] = round((result[key] / total_flip) * 100, 2)

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_line = np.array(list(result.keys()))
    y_line = np.array(list(result.values()))

    plt.plot(x_line, y_line)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
