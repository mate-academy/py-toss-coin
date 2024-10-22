import random


def flip_coin() -> dict:
    my_dict = {char: 0 for char in range(11)}
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            flip_coins = random.randint(0, 1)
            if flip_coins == 1:
                counter += 1
        my_dict[counter] += 1

    for key in my_dict:
        my_dict[key] = round((my_dict[key] / 10000) * 100, 2)
    return my_dict
