import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(num_cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(num_cases):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1
    for key in results:
        results[key] = round(results[key] / num_cases * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    fig, ax = plt.subplots()
    plt.title("Guassian distribution", fontdict={"size": 20})
    plt.xlabel("Heads count", fontdict={"size": 15})
    plt.ylabel("Drop percentage %", fontdict={"size": 15})

    x_list = []
    y_list = []

    plt.xticks(range(11))
    plt.yticks(range(0, 101, 5), minor=True)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)

    for key, value in flip_coin().items():
        x_list.append(key)
        y_list.append(value)

    plt.plot(x_list, y_list, color="b")
    ax.set_yticks(np.arange(0, 110, 10))
    plt.show()
