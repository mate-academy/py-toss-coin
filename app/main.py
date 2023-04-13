import random


def flip_coin() -> dict:
    coin_dict = {}
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.random() < 0.5:
                heads += 1
        if heads in coin_dict:
            coin_dict[heads] += 1
        else:
            coin_dict[heads] = 1
    for key in coin_dict:
        coin_dict[key] = coin_dict[key] / 100
    return coin_dict

