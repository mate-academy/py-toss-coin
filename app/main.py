import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flips = 10
    rounds = 10000
    coin = ["H", "T"]
    results = {key: 0 for key in range(flips + 1)}
    for _ in range(rounds):
        count = sum(int(random.choice(coin) == "H") for _ in range(flips))
        results[count] += 1

    return {k: (v / 100) for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    plt.ylim(0, 100)
    plt.plot(list(range(11)), flip_coin().values())
    plt.title("Gaussian Distribution")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of times %")
    plt.show()
