import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_drops = {numbers: 0 for numbers in range(11)}
    for _ in range(10_000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        heads_drops[heads] += 1
    return {
        count_heads: (drops / 10_000) * 100
        for count_heads, drops in heads_drops.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.bar(data.keys(), data.values(), color="yellow")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
