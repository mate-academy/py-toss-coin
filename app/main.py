import random
import matplotlib.pyplot as plt


def flip_coin():
    total = [[random.choice(['c', 'h'])
              for _ in range(10)] for _ in range(10000)]
    list_count = [case.count('h') for case in total]
    dicts = {i: list_count.count(i) / 100 for i in range(11)}
    return dicts


def draw_gaussian_distribution_graph():
    x = []
    y = []
    for key, value in flip_coin().items():
        x.append(key)
        y.append(value)
    plt.figure(figsize=(12, 7))
    plt.plot(x, y, 'o-r', alpha=0.7, label="first",
             lw=5, mec='b', mew=2, ms=10)
    plt.legend()
    plt.grid(True)
    plt.show()
