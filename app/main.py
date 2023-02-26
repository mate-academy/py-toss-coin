import random


def flip_coin() -> dict:
    flips = {i: 0 for i in range(11)}
    choices = ("heads", "tails")

    for i in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(choices) == "heads":
                count += 1
        flips[count] += 1

    return {key: value / 100 for key, value in flips.items()}
