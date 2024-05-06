import random


def flip_coin() -> dict:
    head_times = {
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
    for case in range(10_000):
        heads = 0
        for coin in range(10):
            if random.choice(("head", "tail")) == "head":
                heads += 1

        head_times[heads] += 1

    return {head_time: round(head_times[head_time] / 100, 2)
            for head_time in head_times}
