import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    # Initialize counts for each number of heads (0 to 10)
    results = {i: 0 for i in range(11)}
    trials = 10000

    for _ in range(trials):
        # Simulate 10 coin flips
        heads = sum(random.choice([0, 1]) for _ in range(10))
        # Increment count for the resulting number of heads
        results[heads] += 1

    # Convert counts to percentages
    percentages = {key: round((value / trials) * 100, 2)
                   for key, value in results.items()}
    xx = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    yy = np.array(list(percentages.values()))
    plt.plot(xx, yy)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.show()
    return percentages
