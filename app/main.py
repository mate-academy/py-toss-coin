import random


def flip_coin() -> dict:
    coin = ["head", "tail"]
    result = {i: 0 for i in range(0, 11)}
    for i in range(1, 10001):
        heads = 0
        for time in range(1, 11):
            if random.choice(coin) == "head":
                heads += 1
        result[heads] += 1
    result = dict(sorted(result.items()))
    for key, value in result.items():
        result[key] = value / 100
    return result
