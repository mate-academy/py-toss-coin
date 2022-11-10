import matplotlib
import random


def flip_coin():
    coins = {}
    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.choice(["head", "tails"]) == "head":
                count += 1
        if count in coins:
            coins[count] += 1
        else:
            coins[count] = 1

    for key in coins:
        coins[key] = round((coins[key] / 10000) * 100, 2)
    return coins

