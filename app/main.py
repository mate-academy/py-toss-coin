import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}

    for _ in range(10000):
        heads = sum([
            random.randint(0, 1)
            for _ in range(10)
        ])
        if heads in result.keys():
            result[heads] += heads
        else:
            result[heads] = heads

    for i in range(0, 11):
        result[i] = round(result[i] / 100, 2)

    return dict(sorted(result.items()))


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values())

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
