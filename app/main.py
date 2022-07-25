import random

from matplotlib import pyplot as plt


def flip_coin():
    count = []
    side = ["Heads", "Tails"]
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.choice(side) == "Heads":
                heads += 1
        count.append(heads)
    return {i: count.count(i) * 100 / 10000 for i in range(11)}


def draw_gaussian_distribution_graph(data):
    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y, c="b")
    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.show()
