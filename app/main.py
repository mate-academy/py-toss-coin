import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {}
    all_heads = 0
    for case in range(10000):
        head = 0
        for _ in range(10):
            coin = random.choice(["head", "tail"])
            if coin == "head":
                head += 1
        all_heads += head
        if head in result:
            result[head] += 1
        else:
            result[head] = head
    result = dict(sorted(result.items()))
    print(result)
    for key in result:
        result[key] = (result[key] / 10000) * 100
    return result


def draw_gaussian_distribution_graph() -> None:
    coins = flip_coin()
    x_points = np.array([key for key in coins])
    y_points = np.array([coins[key] for key in coins])
    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
