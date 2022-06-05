from app.flip_coin import flip_coin

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def draw_gaussian_distribution_graph():
    heads_count = flip_coin()

    fig, ax = plt.subplots()

    plt.axis([0, 10, 0, 100])

    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    xs = []
    count = []

    for key, value in heads_count.items():
        value = value / 100
        xs.append(key)
        count.append(value)

    plt.plot(xs, count, color='blue', linestyle='solid',
             label='Flip distribution')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    plt.legend(loc='upper right')
    fig.savefig('Gaussian distribution.png')
