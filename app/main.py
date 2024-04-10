import random

from matplotlib import pyplot


def flip_coin() -> dict:
    coins_dict = dict.fromkeys(range(11), 0)
    amount = 10000
    for _ in range(amount):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        coins_dict[heads_count] += 1

    for heads in coins_dict:
        coins_dict[heads] = (coins_dict[heads] / amount) * 100

    return coins_dict


def draw_gaussian_distribution_graph(coins_dict: dict) -> None:
    pyplot.bar(coins_dict.keys(), coins_dict.values())
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.title("Gaussian Distribution")
    pyplot.show()
