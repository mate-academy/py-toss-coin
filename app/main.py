import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    res = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = sum(random.choice([0, 1]) for _ in range(10))
        res[count] += 1

    return {key: (value/10000) * 100 for key, value in res.items()}

def draw_gaussian_distribution_graph() -> None:

    res = flip_coin()

    ypoints = np.array([value for value in res.values()])

    plt.plot(ypoints, color='blue')
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()