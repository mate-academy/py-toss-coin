import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    side_coin = ["Heads", "Tails"]
    attempts = {i: 0 for i in range(0, 11)}

    for _ in range(1, 10001):
        sum_of_heads = 0
        for _ in range(10):
            if random.choice(side_coin) == "Heads":
                sum_of_heads += 1
        attempts[sum_of_heads] += 1

    for key, value in attempts.items():
        attempts[key] = value / 10000 * 100

    x = np.array(list(range(0, 11)))
    y = np.array(list(attempts.values()))

    plt.plot(x, y)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()

    return attempts
