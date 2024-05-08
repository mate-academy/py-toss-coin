import numpy as np
import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results[num_heads] += 1
    percentages = {k: round((v / num_cases) * 100, 2)
                   for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    x_points = np.array(list(flip_coin().keys()))
    y_points = np.array(list(flip_coin().values()))

    plt.xlim(0, 11)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_points, y_points)
    plt.show()


draw_gaussian_distribution_graph()
