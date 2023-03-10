import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip = {}
    for flips in range(11):
        flip[flips] = flips
    for repeat in range(10000):
        flip[sum(random.choices([0, 1], k=10))] += 1

    for values in flip:
        flip[values] = flip[values] / 100
    return flip


def draw_gaussian_distribution_graph(flip: [dict]) -> None:
    x_ = []
    y_ = []
    for key in flip.keys():
        x_.append(key)
    for value in flip.values():
        y_.append(value)
    plt.plot(x_, y_)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
