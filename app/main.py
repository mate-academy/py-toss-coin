import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin():
    result = {i: 0 for i in range(11)}
    for i in range(1, 10001):
        heads = 0
        for j in range(1, 11):
            flipped_coin = random.randint(0, 1)
            if flipped_coin == 1:
                heads += 1
        result[heads] += 1
    result = {key: round(value / 100, 2) for key, value in result.items()}
    return result


def draw_gaussian_distribution_graph():
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    result = flip_coin()
    plt.plot(result.keys(), result.values(), color="blue")
    # Changing step on X-axis. Starts from 0 to 10, step - 1
    plt.xticks(np.arange(0, 11, 1))
    # Changing step on Y-axis. Starts from 0 to 100, step - 10
    plt.yticks(np.arange(0, 101, 10))
    plt.show()
