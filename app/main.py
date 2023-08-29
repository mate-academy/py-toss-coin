import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}
    for _ in range(10000):
        head_drop = 0
        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                head_drop += 1
        result[head_drop] += 1
    return {
        key: round(value * 100 / sum(result.values()), 2)
        for key, value in result.items()
    }


def draw_gaussian_distribution_graph(points: dict) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    xpoints = np.array(list(points.keys()))
    ypoints = np.array(list(points.values()))
    plt.plot(xpoints, ypoints)
    plt.show()
