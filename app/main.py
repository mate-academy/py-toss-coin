import matplotlib.pyplot as plt
import random


def flip_coin(attempts: int = 10000) -> dict:
    result = {}
    for _ in range(attempts):
        head_count = sum(random.randint(0, 1) for _ in range(10))
        result[head_count] = result.get(head_count, 0) + 1
    result = dict(sorted(result.items()))
    for key in result:
        result[key] = round(result[key] / attempts * 100, 2)
    return result


def draw_gaussian_distribution_graph(data: dict) -> plt:
    plt.bar(data.keys(), data.values())
    plt.ylabel("Frequency, %")
    plt.xlabel("Heads counts")
    plt.xticks(list(range(0, 11)))
    return plt.show()
