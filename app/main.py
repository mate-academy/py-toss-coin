import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        heads_count = sum([random.randint(0, 1) for _ in range(10)])
        if heads_count not in result:
            result[heads_count] = 0
        result[heads_count] += 1
    for i in result:
        result[i] = result[i] * 100 / 10000
    return dict(sorted(result.items()))


def draw_gaussian_distribution_graph() -> None:
    flip_return = flip_coin()
    plt.plot(flip_return.keys(), flip_return.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph()
