import matplotlib.pyplot as plt
import numpy as np
import random
from collections import defaultdict


def flip_coin(trials: int = 10000) -> dict[int, float]:
    dict_result: defaultdict[int, float] = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))

        dict_result[heads_count] += 1

    final_result = {key: 0.0 for key in range(11)}

    for key in dict_result:
        percentage = (dict_result[key] / trials) * 100
        final_result[key] = round(percentage, 2)

    return final_result


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_points = np.array(list(data.keys()))
    y_points = np.array(list(data.values()))

    plt.plot(x_points, y_points)
    plt.title("Gaussain distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(0, 11))

    plt.show()


result = flip_coin(10000)
draw_gaussian_distribution_graph(result)
