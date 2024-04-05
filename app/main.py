import random
import matplotlib.pyplot as plt
import numpy as np


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = np.array([num for num in range(11)])
    y_points = np.array([data[num] for num in range(11)])
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11, 1))
    plt.show()


def flip_coin() -> dict:
    result_dict = {}
    for num in range(11):
        result_dict[num] = 0
    for _ in range(10000):
        num_head = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                num_head += 1
        result_dict[num_head] += 1
    for num in range(11):
        result_dict[num] = round(result_dict[num] / 100, 2)
    return result_dict


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
