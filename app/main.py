import random
import matplotlib


def flip_coin() -> dict[int, float]:
    total_flips = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(total_flips):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: (v / total_flips) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_points = list(data.keys())
    y_points = list(data.values())

    matplotlib.pyplot.figure(figsize=(10, 6))
    matplotlib.pyplot.plot(x_points, y_points)
    matplotlib.pyplot.show()
    matplotlib.pyplot.xlabel("Number of Heads in 10 Flips")
    matplotlib.pyplot.ylabel("Percentage of Cases (%)")
    matplotlib.pyplot.title("Distribution of Number of Heads in 10 Coin Flips")
    matplotlib.pyplot.xticks(range(11))
    matplotlib.pyplot.show()
