import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        results[heads_count] = results.get(heads_count, 0) + 1

    for key in results:
        results[key] = (results[key] / 10000) * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> plt:
    headers = list(results.keys())
    drops = list(results.values())

    mean = sum(headers[i] * drops[i] for i in range(len(headers))) / sum(drops)
    std_dev = (
        sum((headers[i] - mean) ** 2 * drops[i]
            for i in range(len(headers))) / sum(drops)
    )
    std_dev = std_dev ** 0.5

    curve_x = range(min(headers), max(headers) + 1)
    curve_y = [
        100 * (1 / (std_dev * (2 * 3.14) ** 0.5))
        * (2.71 ** -(((i - mean) / std_dev) ** 2) / 2)
        for i in curve_x
    ]

    plt.bar(headers, drops, alpha=0.7, align="center")
    plt.plot(curve_x, curve_y, color="r")

    plt.xlabel("Headers count")
    plt.ylabel("drops %")
    plt.title("Gaussian distribution")
