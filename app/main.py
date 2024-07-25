from random import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
              8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        temp = 0
        for _ in range(10):
            flip = random()
            if flip > 0.500000000:
                temp += 1
        result[temp] += 1
    for key, value in result.items():
        result[key] = value / 100
    return result
