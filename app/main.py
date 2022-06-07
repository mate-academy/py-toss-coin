import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random


def flip_coin():
    dicts_of_flips = []
    for _ in range(10000):
        dicts_of_flips.append([random.randint(0, 1) for _ in range(10)])

    counts = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for turn in dicts_of_flips:
        counts[turn.count(1)] += 1

    return counts


def draw_gaussian_distribution_graph():
    x_plot = list(flip_coin())
    y_plot_help = list(flip_coin().values())
    y_plot = [i * 100 / 10000 for i in y_plot_help]
    y_ticks = [y for y in range(101) if y % 10 == 0]
    plt.ylim(None, 100)
    plt.title(
        "Gaussian distribution",
        fontsize=14,
        color="black"
    )
    plt.xlabel(
        "Heads count",
        fontsize=12,
        color="black"
    )
    plt.ylabel(
        "Drop percentage %",
        fontsize=12,
        color="black"
    )
    plt.plot(x_plot, y_plot, color="blue")
    plt.xticks(x_plot)
    plt.yticks(y_ticks)
    ax = plt.subplot()
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
