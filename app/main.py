import random
import matplotlib.pyplot as plt


def flip_coin():
    dict_coin_result = {i: 0 for i in range(11)}

    for i in range(10000):
        flips = [random.randint(0, 1) for _ in range(10)]
        count = sum(flips)
        dict_coin_result[count] += 1 / 100

    return {key: int(value) for key, value in dict_coin_result.items()}


def draw_gaussian_distribution_graph():
    plt.xlabel("x")
    plt.ylabel("y")

    plt.plot(*zip(*flip_coin().items()))

    plt.xlim([0, 10])
    plt.ylim([0, 100])

    plt.xticks([i for i in range(0, 11)])
    plt.yticks([i * 10 for i in range(0, 11)])
    plt.minorticks_on()

    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %", fontsize=12)
    plt.xlabel("Heads count", fontsize=12)

    plt.show()
