import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    percentages = {
        key: (value / 10000) * 100
        for key, value in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    x_values = list(percentages.keys())
    y_values = list(percentages.values())

    plt.xticks(x_values, x_values)
    plt.yticks(range(0, 100, 10))

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
