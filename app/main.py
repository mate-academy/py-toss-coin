import random
from matplotlib import pyplot as plt


def flip_coin():
    outcomes = dict()
    for i in range(11):
        outcomes[i] = 0

    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.randint(0, 1):
                heads += 1
        outcomes[heads] += 1

    return {key: round(value * 0.01, 2) for (key, value) in outcomes.items()}


def draw_gaussian_distribution_graph():
    percents = [percent for percent in flip_coin().values()]
    plt.title("Gaussian distribution")
    plt.xlabel("Drop out of 10 attempts")
    plt.ylabel("Chance of occurring")
    plt.plot(percents, color="blue", linewidth=2)
    plt.show()


draw_gaussian_distribution_graph()


