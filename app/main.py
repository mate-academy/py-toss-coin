import random
import matplotlib.pyplot as plt
from matplotlib import ticker


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}

    for _ in range(10000):
        head_dropped = 0

        for _ in range(10):
            if random.randint(0, 1) == 0:
                head_dropped += 1

        result[head_dropped] += 1

    stats = (
        {int(key): round((value / 10000) * 100, 2)
         for (key, value) in result.items()}
    )

    return stats


def draw_gaussian_distribution_graph(stats: dict) -> None:
    x_points = stats.keys()
    y_points = stats.values()

    plt.plot(x_points, y_points)
    plt.ylim([0, 100])
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.show()
