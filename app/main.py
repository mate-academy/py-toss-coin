from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    d = {i: 0 for i in range(11)}
    for _ in range(10_000):
        heads = 0
        for _ in range(10):
            number = randint(0, 1)
            if number == 1:
                heads += 1
        d[heads] += 1
    for i in d:
        d[i] = round(d[i] / 10_000 * 100, 2)
    return d


def draw_gaussian_distribution_graph(d: dict) -> None:
    plt.figure(figsize=(10, 8))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.plot(d.keys(), d.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
