from random import randint


def flip_coin():

    flips_result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for i in range(10000):
        heads = [randint(0, 1) for _ in range(10)].count(1)
        flips_result[heads] += 1 / 100

    flips_result_rounded = {key: int(flips_result[key]) for key in flips_result}

    return flips_result_rounded


print(flip_coin())
