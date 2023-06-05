import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {x: 0 for x in range(11)}
    for i in range(10_000):
        head = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                head += 1
        result[head] += 1

    return {i: result[i] / 100 for i in range(11)}


def draw_gaussian_distribution_graph() -> None:
    plt.plot(10, 100)
    plt.plot([x for x in flip_coin().keys()],
             [y for y in flip_coin().values()])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
