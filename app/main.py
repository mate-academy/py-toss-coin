import random
import matplotlib.pyplot as plt
import numpy


def flip_coin() -> dict:
    heads_dropped = {i: 0 for i in range(11)}

    for _ in range(10000):
        count_of_heads = [random.randint(0, 1) for _ in range(10)].count(1)
        heads_dropped[count_of_heads] += 1

    for count_of_heads in heads_dropped:
        count_in_percents = (heads_dropped[count_of_heads] / 10000) * 100
        heads_dropped[count_of_heads] = round(count_in_percents, 2)

    x_points = numpy.array(list(heads_dropped.keys()))
    y_points = numpy.array(list(heads_dropped.values()))

    plt.plot(x_points, y_points)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()

    return heads_dropped
