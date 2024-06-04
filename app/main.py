import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    head_counts = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        head_counts[heads] += 1

    total_cases = float(num_cases)
    percentages = {heads: round(count / total_cases * 100, 2)
                   for heads, count in head_counts.items()}

    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:

    x_points = np.array(list(percentages.keys()))
    y_points = np.array(list(percentages.values()))

    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points)
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
