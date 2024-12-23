import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    cases = 10000

    for case in range(cases):
        streak_result = []

        for num in range(10):
            streak_result.append(random.randint(0, 1))

        key = streak_result.count(0)
        result[key] += 1

    final_result = {key: round(value / cases * 100, 2)
                    for key, value in result.items()}
    return final_result


def draw_gaussian_distribution_graph(values: dict) -> None:
    keys = [num for num in values.keys()]
    values = [num for num in values.values()]
    xpoints = np.array(keys)
    ypoints = np.array(values)

    plt.plot(xpoints, ypoints)
    plt.show()
