import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0.0 for i in range(11)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    return {heads_count: result / 10000 * 100 for heads_count, result in
            results.items()}


def draw_gaussian_distribution_graph() -> None:
    values = flip_coin()
    x_values = list(values.keys())
    y_values = list(values.values())

    plt.plot(x_values, y_values)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
