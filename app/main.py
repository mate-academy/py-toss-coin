import matplotlib.pyplot as plt

from random import randint
from matplotlib.ticker import MultipleLocator


def flip_coin(cases):
    drops_count = {key: 0 for key in range(11)}

    for _ in range(cases):
        heads_amount = sum(randint(0, 1) for _ in range(10))
        drops_count[heads_amount] += 1

    drops_statistic = {
        head: round((amount * 100) / cases, 1)
        for head, amount in drops_count.items()
    }

    draw_result(drops_statistic)

    return drops_statistic


def draw_result(data):
    y_points = list(data.values())

    fig, ax = plt.subplots()

    ax.plot(y_points, color="b")
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_minor_locator(MultipleLocator(5))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.show()

print(flip_coin(10000))
