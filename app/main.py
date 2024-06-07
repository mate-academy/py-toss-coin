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
    percentages = {k: (v / total_experiments) * 100 for k, v in counter.items()}
    return percentages


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    x = np.array(list(distribution.keys()))
    y = np.array(list(distribution.values()))

    plt.plot(x, y, marker='o')

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips (10 flips, 10000 experiments)")

    plt.grid(True)
    plt.show()
