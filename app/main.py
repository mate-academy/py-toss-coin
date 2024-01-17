from random import randint
from matplotlib import pyplot as plt
from time import time


def flip_coin() -> dict:
    result = {i: 0 for i in range(10 + 1)}
    time1 = time()
    for _ in range(10000):
        total = sum(1 for _ in range(10) if randint(0, 1) == 0)
        result[total] += 1
    print(time() - time1)
    return {k: round(v / 100, 2) for k, v in result.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.values(),
             linestyle="dashed",
             marker="o",
             color="pink")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
