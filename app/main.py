import matplotlib.pyplot as plt
from matplotlib import ticker
from random import randint


def flip_coin() -> dict:
    result = {key: 1 for key in range(11)}
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            if randint(0, 1) == 1:
                heads_count += 1

        result[heads_count] += 1

    stats = (
        {int(key): round((value / 10000) * 100, 2)
         for (key, value) in result.items()}
    )
    return stats


def draw_gaussian_distribution_graph(stats: dict) -> None:
    x_point = stats.key()
    y_point = stats.value()

    plt.plot(x_point, y_point)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.show()
