import random

dictionary = {
    1: 0.0,
    2: 0.0,
    3: 0.0,
    4: 0.0,
    5: 0.0,
    6: 0.0,
    7: 0.0,
    8: 0.0,
    9: 0.0,
    10: 0.0}
option = ["heads", "tails"]


def flip_coin():
    for case in range(0, 10000):
        for num, flip in enumerate(range(1, 11)):
            flip = random.choice(option)
            if flip == "heads":
                dictionary[num] += 1.0

    for value in dictionary:
        dictionary[value] = (dictionary[value] / 1000) * 100
    return dictionary
