import random


def flip_coin() -> dict:
    heads_count = {key: 0 for key in range(11)}
    for case in range(10000):
        coin_flips = {key: 0 for key in range(10)}
        for i in range(10):
            coin_flips[i] = random.randint(0, 1)
        for i in range(10):
            heads_count[list(coin_flips.values()).count(0)] += 1
    heads_percents = {
        key: round((val / sum(heads_count.values()) * 100), 2)
        for key, val in heads_count.items()
    }
    return heads_percents
