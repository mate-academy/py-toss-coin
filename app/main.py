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
    mu = 5
    sigma = 2
    axis_x = np.linspace(0, 10, 100)
    axis_y = ((1 / (sigma * np.sqrt(2 * np.pi)))
              * np.exp(-((axis_x - mu) ** 2) / (2 * sigma ** 2)))
    axis_y *= 100 / np.max(axis_y)
    plt.plot(flip_coin().values())
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.yticks(np.linspace(0, 100, 11))
    plt.legend()
    plt.grid(True)
    plt.show()


draw_gaussian_distribution_graph()
