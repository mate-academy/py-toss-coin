import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_chance = {key: 0 for key in range(11)}
    for i in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                count_heads += 1
        dict_chance[count_heads] += 1
    dict_percent = {
        key: (value / 10000) * 100 for key, value in dict_chance.items()
    }
    return dict_percent


def draw_gaussian_distribution_graph(points: dict) -> None:
    xpoints = []
    ypoints = []
    for key, value in points.items():
        xpoints.append(key)
        ypoints.append(value)
    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()
