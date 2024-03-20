import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    temper_list = []
    result_for_graph = {}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            result = random.choice(["heads", "tails"])
            if result == "heads":
                head += 1
        temper_list.append(head)
    for i in sorted(temper_list):
        result_for_graph[i] = temper_list.count(i) / 100
    return result_for_graph


def draw_gaussian_distribution_graph() -> None:
    flipping = flip_coin()
    xpoints = list(flipping.keys())
    ypoints = list(flipping.values())
    plt.plot(xpoints, ypoints)
    plt.show()
