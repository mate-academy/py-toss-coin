from random import choice
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    sides = ["heads", "tails"]

    flip_stats = dict.fromkeys(list(range(11)), 0)
    for _ in range(10000):
        result = {"heads": 0, "tails": 0}
        for _ in range(10):
            result[choice(sides)] += 1
        flip_stats[result["heads"]] += 1

    flip_stats = {key: value / 100 for key, value in flip_stats.items()}

    return flip_stats


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()

    ypoints = list(points.values())
    plt.plot(ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()
