import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def create_dictionary():
    dict_of_occurrences = {k: 0 for k in range(11)}
    for iteration in range(10000):
        flips = [random.randrange(0, 2, 1) for i in range(10)]
        dict_of_occurrences[flips.count(1)] += 1
    return dict_of_occurrences


def draw_gauss_curve():
    try:
        list_of_occurrences = [key for key, value in
                               create_dictionary().items()
                               for _ in range(value)]
        fig, ax = plt.subplots(1, 1)

        ax.scatter(create_dictionary().keys(), create_dictionary().values())
        plt.xlabel('Key', fontsize=10, color="green")
        plt.ylabel('Count of occurrences', fontsize=10, color="blue")

        mu = np.mean(list_of_occurrences)
        sigma = np.std(list_of_occurrences)

        u = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
        ax2 = ax.twinx()
        ax2.plot(u, stats.norm.pdf(u, mu, sigma), color='crimson')
        ax2.set_ylabel('normal curve')

        plt.show()
    except KeyboardInterrupt:
        print("Goodbye!")


draw_gauss_curve()
