import random
from matplotlib import pyplot


def flip_coin():
    coin = [True, False]
    results = {}
    for i in range(11):
        count = sum(
            1 for _ in range(10000)
            if sum(1 for _ in range(10) if random.choice(coin)) == i
        )
        results[i] = count / 100
    return results


def draw_gaussian_distribution_graph():
    x = [key for key in flip_coin().keys()]
    y = [value for value in flip_coin().values()]
    pyplot.plot(x, y, "r")
    pyplot.ylim(0, 100)
    pyplot.xlim(0, 10)
    pyplot.title("Gaussian distribution", fontsize=20)
    pyplot.xlabel("Heads count", fontsize=16)
    pyplot.ylabel("Drop percentage %", fontsize=16)
    pyplot.show()
