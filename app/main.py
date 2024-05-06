import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    head_times = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for case in range(10_000):
        heads = 0
        for coin in range(10):
            if random.choice(("head", "tail")) == "head":
                heads += 1

        head_times[heads] += 1

    return {head_time: round(head_times[head_time] / 100, 2) for head_time in head_times}


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = []
    y_points = []
    for head in data:
        x_points.append(head)
        y_points.append(data[head])
    x_points, y_points = np.array(x_points), np.array(y_points)

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_points, y_points)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph({0: 0.13, 1: 1.24, 2: 4.41, 3: 11.95, 4: 20.02, 5: 24.32, 6: 20.16, 7: 11.92, 8: 4.65, 9: 1.05, 10: 0.15})
