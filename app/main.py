import matplotlib.pyplot as plt
import random


def flip_coin() -> list[int, float]:
    coin_values = ["heads", "tails"]
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            if random.choice(coin_values) == "heads":
                counter += 1
        result[counter] += 1
    return {key: round(((result[key] / 10000) * 100), 2)
            for key in result.keys()}


def draw_gaussian_distribution_graph() -> None:
    coordinates = flip_coin()
    xpoints = [key for key in coordinates.keys()]
    ypoints = [value for value in coordinates.values()]
    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.show()
