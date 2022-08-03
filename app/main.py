from random import choice
import matplotlib.pyplot as plt


def flip_coin():
    result = dict.fromkeys((number for number in range(11)), 0)

    for _ in range(10000):
        count = 0

        for _ in range(10):
            if choice(["Heads", "Tails"]) == "Heads":
                count += 1
            result[count] += 1

    for key, value in result.items():
        result[key] = value / 10000 * 100
    return result


def draw_gaussian_distribution_graph(data):
    x = list(data.keys())
    y = list(data.values())
    plt.axis([0, 10, 0, 100])
    plt.plot(x, y)
    plt.title('Gaussian distibution')
    plt.xlable('Heads count')
    plt.ylable('Drop percentage %')
    plt.show()
