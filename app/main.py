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
    for head_count in range(11):
        result_dict[head_count] = math.ceil((array_of_heads.count(head_count) / 10000) * 100)

    return result_dict


def draw_gaussian_distribution_graph():
    result_dict = flip_coin()

    x_coordinates = list(result_dict.keys())
    y_coordinates = list(result_dict.values())

    fig, ax = plt.subplots()

    ax.plot(x_coordinates, y_coordinates, color='b', linewidth=3)
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
