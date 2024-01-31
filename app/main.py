import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = []
    for i in range(10000):
        random_list = [random.choice([0, 1]) for _ in range(10)]
        results.append(sum(random_list))
    probs = {num: results.count(num) / len(results) * 100
             for num in set(results)}
    return probs


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.plot(
        list(data.keys()),
        list(data.values()),
        "ro-",
        label="Flip coin"
    )
    plt.yticks(np.arange(0, 101, 10))
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.legend()
    plt.show()
