from random import randint
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    output = {i: 0 for i in range(11)}

    for _ in range(10000):
        ten_flips = [randint(0, 1) for _ in range(10)]
        heads_count = ten_flips.count(0)
        output[heads_count] += 1

    total_samples = 10000
    for key in output:
        output[key] = round(output[key] / total_samples * 100, 2)

    return output


def draw_head_counts_distribution_graph(data: dict) -> None:
    x_points = np.array(list(data.keys()))
    y_points = np.array(list(data.values()))

    plt.figure()
    plt.plot(x_points, y_points)
    plt.title("Head Counts Distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Frequency (%)")
    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 101, 10))
    plt.grid(True)
    plt.show()
