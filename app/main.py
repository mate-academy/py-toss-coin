import numpy
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin(n_trials: int = 10000, n_flips: int = 10) -> dict:
    results = []
    for _ in range(n_trials):
        heads = numpy.sum(numpy.random.randint(0, 2, n_flips))
        results.append(heads)
    counter = Counter(results)
    percentages = {
        n: (counter[n] / n_trials) * 100 for n in range(n_flips + 1)
    }
    return percentages


def draw_graph(percentages: dict) -> None:
    keys = list(percentages.keys())
    values = list(percentages.values())
    plt.figure(figsize=(10, 6))
    plt.plot(keys, values, color="blue")
    plt.xlabel("heads")
    plt.ylabel("percentages")
    plt.title("flip_coin")
    plt.grid()
    plt.show()
