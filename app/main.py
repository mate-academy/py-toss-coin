import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coins = {}
    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.choice(["head", "tails"]) == "head":
                count += 1
        if count in coins:
            coins[count] += 1
        else:
            coins[count] = 1

    for key in coins:
        coins[key] = round((coins[key] / 10000) * 100, 2)
    return coins


def draw_gaussian_distribution_graph():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.axis([0, 10, 0, 100])

    x = []
    y = []

    for key, value in sorted(flip_coin().items()):
        x.append(key)
        y.append(value)

    plt.plot(x, y, color="red")
    fig.savefig("graph.png")
