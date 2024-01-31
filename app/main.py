import random

from matplotlib import pyplot


def flip_coin(num_flips: int = 10000, num_coin_tosses: int = 10) -> dict:
    results = {}

    for _ in range(num_flips):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_coin_tosses))
        results[num_heads] = results.get(num_heads, 0) + 1

    return {key: (value / num_flips) * 100 for key, value in results.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys, values = zip(*sorted(data.items()))

    pyplot.bar(keys, values, align="center")
    pyplot.title("Coin Toss Distribution")
    pyplot.xlabel("Number of Heads")
    pyplot.ylabel("Percentage")
    pyplot.show()
