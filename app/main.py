import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flip: int = 10) -> dict:
    times = {i: 0 for i in range(11)}
    for _ in range(cases):
        amount = 0
        for _ in range(flip):
            if random.randint(0, 1):
                amount += 1
        times[amount] += 1

    result = {key: round(times[key] / cases * 100, 2) for key in times}

    return result


def draw_flip_graph(result: dict) -> None:
    x_axis = np.array(list(result.keys()))
    y_axis = np.array(list(result.values()))

    plt.plot(x_axis, y_axis, color="#000080")

    plt.xlim([0, 10])
    plt.ylim([0, 100])

    plt.xticks(np.arange(11))
    plt.yticks(np.arange(0, 101, 10))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()
