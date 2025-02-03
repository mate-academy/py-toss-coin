import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    draw_gaussian_distribution_graph(results)

    return results


def draw_gaussian_distribution_graph(flip_dict: dict) -> None:
    plt.plot(list(flip_dict.keys()), list(flip_dict.values()))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.xticks(np.arange(0, 11, 1))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


if __name__ == "__main__":
    flip_coin()
