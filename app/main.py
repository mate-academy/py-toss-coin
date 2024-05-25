import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    throws = []
    result = {}
    for i in range(10000):
        throw = {"heads": 0, "tails": 0}
        for _ in range(10):
            throw[random.choice(coin)] += 1
        throws.append(throw)
    for i in range(11):
        result[i] = round(len([t for t in throws if t["heads"] == i]) / len(throws) * 100, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    coin_data = flip_coin()
    heads_count = list(coin_data.keys())
    drop_percent = list(coin_data.values())
    plt.plot(heads_count, drop_percent)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
