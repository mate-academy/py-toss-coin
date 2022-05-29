import random


def flip_coin():
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        flips = {1: 0, 0: 0}
        for i in range(10):
            n = random.randint(0, 1)
            flips[n] += 1
        result[flips[1]] += 1

    for r in result:
        result[r] = int((result[r] / 10000) * 100)

    return result
