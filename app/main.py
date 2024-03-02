import random
from collections import defaultdict
import matplotlib.pyplot


def flip_coin() -> dict:
    results = defaultdict(int)
    for _ in range(10000):
        heads_count = sum([random.choice([0, 1]) for _ in range(10)])
        results[heads_count] += 1
    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)
    return dict(sorted(results.items()))


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())

    matplotlib.pyplot.figure(figsize=(10, 5))
    matplotlib.pyplot.bar(keys, values, color="skyblue")
    matplotlib.pyplot.xlabel("Number of Heads")
    matplotlib.pyplot.ylabel("Percentage")
    matplotlib.pyplot.title("Gaussian Distribution of Coin Flips")
    matplotlib.pyplot.xticks(keys)
    matplotlib.pyplot.show()
