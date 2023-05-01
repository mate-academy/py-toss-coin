import random
import matplotlib as plt


def flip_coin() -> dict:
    result = {coin: 0 for coin in range(11)}
    eagle_and_tails = ["eagle", "tails"]
    for chance in range(10000):
        eagle_monet = 0
        for coin in range(10):
            if random.choice(eagle_and_tails) == "eagle":
                eagle_monet += 1
        result[eagle_monet] += 1

    for key, values in result.items():
        result[key] = values / 100 * 1

    return result


def draw_gaussian_distribution_graph(x_point: list, y_point: list) -> None:
    plt.pyplot.title("Gaussian distribution")
    plt.pyplot.xlabel("Heads count")
    plt.pyplot.ylabel("Drop percentage %")
    plt.pyplot.plot(x_point, y_point, 100, color="r")
    plt.pyplot.show()
