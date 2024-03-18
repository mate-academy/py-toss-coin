import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> None:
    result = {i: 0 for i in range(11)}

    total_case = 10000
    for _ in range(total_case):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    percentages = {key: (value / total_case) * 100 for key,
                   value in result.items()}
    return percentages


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    x_data = list(data.keys())
    y_data = list(data.values())
    plt.plot(x_data, y_data, marker="o", linestyle="-")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Cases")
    plt.grid(True)
    plt.show()
