import random as r


def flip_coin() -> dict:
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
        5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for case in range(10000):
        heads = 0
        for count in range(10):
            if r.randint(0, 1) == 1:
                heads += 1
        result[heads] += 1

    for res in result:
        result[res] /= 100
    return result
