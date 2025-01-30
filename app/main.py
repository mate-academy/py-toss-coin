import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    trials = 10000
    result = {i: 0.0 for i in range(0, 11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    for key in result:
        result[key] = round((result[key] / trials) * 100, 2)

    return result

    xpoints = np.array(result.keys())
    ypoints = np.array(result.values())

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
