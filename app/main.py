from random import choice
import matplotlib.pyplot as plt


def flip_coin():

    results = dict(zip(range(0, 11), [0] * 11))

    for _ in range(10001):
        experiment = sum([choice([0, 1]) for f in range(10)])
        results[experiment] += 0.01

    return results


def draw_gaussian_distribution_graph():

    experiments = flip_coin()

    percentage = [quantity / 100 for quantity in list(experiments.values())]

    fig, ax = plt.subplots()
    ax.plot(list(experiments.keys()), percentage, color='b')
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.yticks(range(0, 101, 10))
    plt.title("Gaussian distribution")
    plt.show()
