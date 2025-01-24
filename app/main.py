import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    statistics = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        count = 0

        for _ in range(10):
            if random.randint(0, 1):
                count += 1

        statistics[count] += 1

    return {num: drop / 100 for num, drop in statistics.items()}


def draw_gaussian_distribution_graph() -> None:
    percents = flip_coin()
    x, y = list(percents.keys()), list(percents.values())

    plt.plot(x, y)
    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()
