import random
import matplotlib.pyplot as pl


def flip_coin():
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        result[sum([random.randint(0, 1) for n in range(10)])] += 1
    return {key: int(value / 100) for key, value in result.items()}


def draw_gaussian_distribution_graph():
    odds_dict = flip_coin()
    pl.plot(odds_dict.keys(), odds_dict.values())
    pl.xlabel("Heads count")
    pl.ylabel("Drop percentage %")
    pl.title("Gaussian distribution")
    pl.savefig("filename.png")
    pl.show()
