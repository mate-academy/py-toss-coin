import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin() -> dict:
    res = {x: 0 for x in range(11)}
    coins = ("heads", "tail")
    for _ in range(10_000):
        count = 0
        for _ in range(10):
            if random.choice(coins) == "heads":
                count += 1
        res[count] += 1
    res1 = {x: v/100 for x, v in res.items()}
    return res1


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    fig, ax = plt.subplots()
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    x = list(data.keys())
    y = list(data.values())
    ax.plot(x, y, color='r', linewidth=3)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)
    plt.show()
