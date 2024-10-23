import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    results = []
    for _ in range(cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results.append(heads_count)

    counts = Counter(results)
    percentages = {
        key: (round((value / cases * 100), 2))
        for key, value in counts.items()
    }
    return percentages


def draw_gaussian_distribution_graph(results: dict) -> None:
    sorted_results = dict(sorted(results.items()))
    categories = list(sorted_results.keys())
    frequencies = list(sorted_results.values())

    plt.plot(categories, frequencies)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian Distribution")

    plt.show()
