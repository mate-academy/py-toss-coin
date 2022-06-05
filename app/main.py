import random


def flip_coin():
    result = {i: 0 for i in range(0, 11)}
    for _ in range(10000):
        flips = ['Heads' if x == 1 else 'Tails' for x in
                 [random.randint(0, 1) for _ in range(10)]]
        heads = flips.count('Heads')
        result[heads] += 1
    for k, v in result.items():
        result[k] = round(v / 100, 2)
    return result
