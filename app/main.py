import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        head_coins = 0
        for i in range(10):
            head_coins += random.randint(0, 1)
        if head_coins in result:
            result[head_coins] += 1 / 100
        else:
            result[head_coins] = 1 / 100
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    lists = sorted(data.items())
    x, y = zip(*lists)

    plt.plot(x, y)

    font = {"family": "serif"}

    plt.title("Gaussian Distribution", fontdict=font)
    plt.xlabel("Heads count", fontdict=font)
    plt.ylabel("Drop percentage %", fontdict=font)

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
