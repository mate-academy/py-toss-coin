import random


def flip_coin():
    dict_flip_result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for i in range(10000):
        flips = [random.randint(0, 1) for x in range(10)]
        count = sum(flips)
        dict_flip_result[count] += 1 / 100

    return {key: int(value) for key, value in dict_flip_result.items()}
