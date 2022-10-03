import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def flip_coin():
    dictionary = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0

        for _ in range(10):
            count += random.randint(0, 1)

        dictionary[count] += 1

    for i in range(11):
        dictionary[i] /= 100

    return dictionary


def draw_gaussian_distribution_graph():
    dictionary = flip_coin()

    xpoints = list(dictionary.keys())
    ypoints = list(dictionary.values())

    plt.axis([0, 10, 0, 100])

    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
