import random
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flips_data = {i: 0 for i in range(11)}
    coin = ("heads", "tails")
    for i in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                count += 1
        flips_data[count] += 1

    result = {key: value / 100 for key, value in flips_data.items()}
    return result


def draw_gaussian_distribution_graph():
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    fig, ax = plt.subplots()
    ax.plot(x, y, color="b", linewidth=2)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    ax.set_ylim(0, 100)
    ax.set_xlim(0, 10)
    ax.set_title("Gaussian distribution")
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")

    plt.show()
