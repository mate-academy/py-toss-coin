import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            heads_count += random.randint(0, 1)
        result[heads_count] += 1
    for key in result:
        result[key] /= 100
    return result
