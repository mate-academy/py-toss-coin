import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_dict = {}
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.random() < 0.5:
                heads += 1
        if heads in coin_dict:
            coin_dict[heads] += 1
        else:
            coin_dict[heads] = 1
    for key in coin_dict:
        coin_dict[key] = coin_dict[key] / 100
    return coin_dict


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_axis = list(result.keys())
    y_axis = list(result.values())

    plt.plot(x_axis, y_axis)
    plt.axis([0, 10, 0, 100])
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.tight_layout()
    plt.show()


results = flip_coin()
draw_gaussian_distribution_graph(results)
