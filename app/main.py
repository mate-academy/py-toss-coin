import matplotlib.pyplot as plt
import numpy as np
import random
from collections import Counter
from typing import Dict


def flip_coin() -> Dict[int, float]:
    def single_flip() -> int:
        heads_count = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1
        return heads_count

    results = [single_flip() for _ in range(10000)]
    counter = Counter(results)
    total_experiments = 10000
    percentages = {key: (value / total_experiments) * 100
                   for key, value in counter.items()}
    return percentages


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    num_heads = np.array(list(distribution.keys()))
    percentages = np.array(list(distribution.values()))

    plt.plot(num_heads, percentages, marker="o", color="blue")

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.grid(True)
    plt.show()


distribution = flip_coin()
draw_gaussian_distribution_graph(distribution)
