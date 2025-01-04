import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {ind: 0 for ind in range(11)}
    coin = ["heads", "number"]

    for _ in range(10000):
        flip_10_times = sum(
            1 for _ in range(10) if random.choice(coin) == "heads"
        )
        result[flip_10_times] += 1
    result = {key: round(value / 100, 2) for key, value in result.items()}

    return result


def draw_gaussian_distribution_graph() -> None:
    x_ax = list(flip_coin().keys())
    y_ax = list(flip_coin().values())
    plt.plot(x_ax, y_ax)
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")
    plt.show()
