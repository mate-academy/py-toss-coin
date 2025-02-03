import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(trials=10000, flips=10):
    result = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        result[heads_count] += 1

    for key in result:
        result[key] = round((result[key] / trials) * 100, 2)

    x = list(result.keys())
    y = list(result.values())

    plt.plot(x, y)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 11, 1))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
