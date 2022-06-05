import random


def flip_coin():
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
              6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        flips = ['Heads' if x == 1 else 'Tails' for x in
                 [random.randint(0, 1) for _ in range(10)]]
        heads = flips.count('Heads')
        result[heads] += 1
    for k, v in result.items():
        result[k] = round(v / 100, 2)
    return result
