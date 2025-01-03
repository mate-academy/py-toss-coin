import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads = {0: 0,
             1: 0,
             2: 0,
             3: 0,
             4: 0,
             5: 0,
             6: 0,
             7: 0,
             8: 0,
             9: 0,
             10: 0}
    for _ in range(10000):
        random_heads = [random.choice([0, 1]) for _ in range(10)]
        heads[sum(random_heads)] += 1
    for index in range(11):
        heads[index] = (heads[index] / 10000) * 100
    return heads


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values(), color="Blue")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
