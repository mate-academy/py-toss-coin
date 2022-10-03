import random


def flip_coin():
    dictionary = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0

        for _ in range(10):
            count += random.randint(0, 1)

        dictionary[count] += 1

    for i in range(11):
        dictionary[i] /= 100

    return dictionary
