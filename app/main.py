import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(0, 11)}

    for i in range(10000):
        dropped = random.choices([0, 1], k=10)
        heads_count[dropped.count(1)] += 1

    return {k: round(v / 10000 * 100, 2) for k, v in heads_count.items()}


result = flip_coin()


def draw_gaussian_distribution_graph(points: dict) -> None:
    point_x = [k for k in points.keys()]
    point_y = [v for v in points.values()]

    plt.plot(point_x, point_y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph(result)
