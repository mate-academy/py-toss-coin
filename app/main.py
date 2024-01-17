import random


def flip_coin() -> dict:
    head_roll = {}
    for _ in range(10000):
        heads = sum(random.choices([0, 1], k=10))
        if heads in head_roll:
            head_roll[heads] += 1
        else:
            head_roll[heads] = 1
    result = {key: (value / 100) for key, value in head_roll.items()}
    return result
