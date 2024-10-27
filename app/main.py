import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    total_flips = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(total_flips):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: (v / total_flips) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_axis = list(data.keys())
    y_axis = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(
        x_axis,
        y_axis,
        marker="o",
        color="skyblue",
        linestyle="-",
        linewidth=2,
        markerfacecolor="blue",
    )
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage of Cases (%)")
    plt.title("Distribution of Number of Heads in 10 Coin Flips")
    plt.xticks(range(11))
    plt.show()
