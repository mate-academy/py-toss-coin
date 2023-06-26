import random
import math
import matplotlib.pyplot as plt
import numpy as np


def flip_coin():
    counts = {i: 0 for i in range(11)}
    for i in range(100000):
        heads = 0
        for j in range(10):
            r = random.random()
            if r < 0.5:
                heads += 1
        counts[heads] += 1
    percentages = {k: math.ceil(v / 1000) / 100 for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph():
    data = np.random.normal(0, 1, 1000)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.show()


draw_gaussian_distribution_graph()
print(flip_coin())

