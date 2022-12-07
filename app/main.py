from random import choice
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin() -> dict:
    possible_heads = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    amount_of_heads = 0

    flip_coin_dict = dict.fromkeys(possible_heads, amount_of_heads)

    for case in range(0, 10000):
        count_heads = 0

        for toss in range(0, 10):
            if choice(["heads", "tails"]) == "heads":
                count_heads += 1
        flip_coin_dict[count_heads] += 0.01

    return flip_coin_dict


def draw_gaussian_distribution_graph() -> None:
    x = flip_coin().keys()
    y = flip_coin().values()

    fig, ax = plt.subplots()
    plt.axis([0, 10, 0, 100])
    ax.plot(x, y, color="r", linewidth=3)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    fig.set_figwidth(12)
    fig.set_figheight(8)

    plt.show()
