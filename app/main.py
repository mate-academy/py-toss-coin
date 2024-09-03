import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    for key in result:
        result[key] = round((result[key] / 10000) * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:

    plt.plot(list(flip_coin().values()))

    plt.xlabel("Number of heads")
    plt.ylabel("Probability (%)")
    plt.title("Gaussian distribution of coin flips")
    plt.show()
