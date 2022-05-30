import random


def flip_coin():
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        result[sum([random.randint(0, 1) for n in range(10)])] += 1
    return {key: int(value / 100) for key, value in result.items()}


print(flip_coin())
