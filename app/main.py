import random
import math

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin():
    array_of_heads = [
        sum([random.randint(0, 1) for _ in range(10)])
        for _ in range(10000)
    ]

    result_dict = {}
    for x in range(11):
        result_dict[x] = math.ceil((array_of_heads.count(x) / 10000) * 100)

    return result_dict


def draw_gaussian_distribution_graph():
    result_dict = flip_coin()

    x = list(result_dict.keys())
    y = list(result_dict.values())

    fig, ax = plt.subplots()

    ax.plot(x, y, color='b', linewidth=3)
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    plt.axis([0, 10, 0, 100])

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    fig.set_figwidth(12)
    fig.set_figheight(8)

    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
