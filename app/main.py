import random
import matplotlib.pyplot as plt


def flip_coin(flipping: int = 10000) -> dict:
    results = []
    for _ in range(flipping):
        head = 0
        for _ in range(10):
            result = random.choice(["heads", "tails"])
            if result == "heads":
                head += 1
        results.append(head)
    percents = {}
    for i in sorted(results):
        percents[i] = results.count(i) / 100
    return percents


def draw_gaussian_distribution_graph() -> None:
    flipping = flip_coin()
    xpoints = list(flipping.keys())
    ypoints = list(flipping.values())
    plt.plot(xpoints, ypoints)
    plt.show()
