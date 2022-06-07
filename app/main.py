from random import randint


def flip_coin():
    heads_times = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                   6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += randint(0, 1)
        heads_times[heads] += 1

    return {key: (value / 100) for key, value in heads_times.items()}
