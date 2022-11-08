import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin() -> dict:
    coins = {}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            coin = random.choice(["head", "emblem"])
            if coin == "head":
                count += 1
        if count in coins:
            coins[count] += 1
        else:
            coins[count] = 1

    for coin_percent in coins:
        coins[coin_percent] = round((coins[coin_percent] / 10000) * 100, 2)
    return coins


def draw_gaussian_distribution_graph() -> plt:
    drop_percentage = []
    head_count = []

    for key, value in sorted(flip_coin().items()):
        drop_percentage.append(key)
        head_count.append(value)

    fig, ax = plt.subplots()

    ax.plot(drop_percentage, head_count, color="b", linewidth=2)

    plt.axis([0, 10, 0, 100])

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage, %")

    plt.show()
