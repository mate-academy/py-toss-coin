import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(0, 10))
        result[heads_count] += heads_count

    total = sum(value for value in result.values())
    for key, value in result.items():
        result[key] = (value / total) * 100

    return result

print(flip_coin())

