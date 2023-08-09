import random
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict


def flip_coin() -> Dict[int, float]:
    num_trials = 10000
    results = {i: 0 for i in range(11)}  # Від 0 до 10 голів
    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentage_results = {key: (value / num_trials) * 100
                          for key, value in results.items()}
    return percentage_results


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values)
    plt.xlabel("Кількість голів")
    plt.ylabel("Відсоток")
    plt.title("Розподіл випадання голів при підкиданні монети 10 разів")
    plt.xticks(np.arange(0, 11, 1))
    plt.show()


result = flip_coin()
draw_gaussian_distribution_graph(result)
