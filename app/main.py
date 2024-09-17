import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int: float]:
    heads_amount = [0] * 11
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            if random.choice(["head", "tail"]) == "head":
                heads_count += 1

        heads_amount[heads_count] += 1

    return {key: value / 10000 * 100 for key, value in enumerate(heads_amount)}


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    plt.plot(distribution.keys(), distribution.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis((0, 10, 0, 100))

    plt.show()
