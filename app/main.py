import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    stats = {}
    attempts = 10000
    flips = 10
    for attempt in range(attempts):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        stats[heads] = stats.get(heads, 0) + 1

    for head in stats:
        stats[head] = round(stats[head] / attempts * 100, 2)

    sorted_stats = dict(sorted(stats.items()))
    return sorted_stats


def draw_gaussian_distribution_graph() -> None:
    stats_dict = flip_coin()

    x_points = list(stats_dict.keys())
    y_points = list(stats_dict.values())

    plt.plot(x_points, y_points, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()


print(draw_gaussian_distribution_graph())
