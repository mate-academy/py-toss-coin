import random


def flip() -> str:
    return random.choice(["Heads", "Tails"])


def count_heads() -> int:
    heads_total = 0
    for number in range(10):
        if flip() == "Heads":
            heads_total += 1
    return heads_total


def flip_coin() -> dict:
    count_flips = {0: 0,
                   1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0,
                   7: 0,
                   8: 0,
                   9: 0,
                   10: 0}
    for number in range(10000):
        count_flips[count_heads()] += 1

    percentage_count_flips = {}
    for number in range(11):
        percentage_count_flips[number] = (
            round((count_flips[number] / 10000 * 100), 2))
    return percentage_count_flips
