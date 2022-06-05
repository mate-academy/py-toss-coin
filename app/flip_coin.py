import random


def flip_coin():
    heads_count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    for _ in range(10000):
        heads_flip = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip:
                heads_flip += 1
        heads_count[heads_flip] += 1

    return heads_count
