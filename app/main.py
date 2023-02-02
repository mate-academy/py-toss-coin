import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    statistic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        result = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                result += 1
        statistic[result] += 1

    for key in statistic:
        statistic[key] /= 100

    return statistic


def draw_gaussian_distribution_graph() -> None:
    statistic = flip_coin()

    x_points = []
    y_points = []
    for key in statistic:
        x_points.append(key)
        y_points.append(statistic[key] / 100)

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
