import random
import matplotlib.pyplot as plt


def flip_coin():
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: round((v / trials) * 100, 3) for k, v in results.items()}

    return percentages


def draw_gaussian_distribution_graph():
    percentages = flip_coin()

    x = list(percentages.keys())
    y = list(percentages.values())

    plt.plot(x, y)
    plt.show()

draw_gaussian_distribution_graph()