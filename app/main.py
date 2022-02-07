import random


def flip_coin():
    chance_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                   5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        num = random.randint(0, 10)
        chance_dict[num] += 1

    return chance_dict
