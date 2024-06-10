from random import randint


def flip_coin() -> dict:
    result = {}
    for i in range(0, 11):
        result[i] = 0

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if randint(0, 1):
                count += 1
        result[count] += 1

    attempts = 10000
    for key in result:
        result[key] = (result[key] / attempts) * 100

    return result
