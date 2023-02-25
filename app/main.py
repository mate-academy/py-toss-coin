import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    statistic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    coin = ["heads", "tails"]
    toss = 10000
    for _ in range(toss):
        heads_from_10_toss = \
            sum(1 for i in range(10) if random.choice(coin) == "heads")
        statistic[heads_from_10_toss] += 1

    # convert number of hits to percentage
    for key, value in statistic.items():
        statistic[key] = value * 100 / toss

    return statistic


def draw_gaussian_distribution_graph(dct_stat: dict) -> None:
    heads_count = list(dct_stat.values())
    dpop_pers = list(dct_stat.keys())
    plt.plot(dpop_pers, heads_count)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian distribution")
    plt.show()
