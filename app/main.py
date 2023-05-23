import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {}
    for _ in range(10000):
        flips = [random.choice(["Heads", "Tails"]) for _ in range(10)]
        heads_count = flips.count("Heads")
        if heads_count not in results:
            results[heads_count] = 0
        results[heads_count] += 1
    total_cases = sum(results.values())
    percentages = {heads_count: (count / total_cases) * 100
                   for heads_count, count in results.items()}
    sorted_percentages = dict(sorted(percentages.items(), key=lambda x: x[0]))
    return sorted_percentages


def draw_gaussian_distribution_graph(sorted_percentages: dict) -> None:
    axis_x = list[sorted_percentages.keys()]
    axis_y = list[sorted_percentages.values()]

    fig, ax = plt.subplots()
    ax.plot(axis_x, axis_y)

    ax.set_title("Графік")
    ax.set_xlabel("Вісь x")
    ax.set_ylabel("Вісь y")
    ax.legend(["Дані"])

    plt.show()
