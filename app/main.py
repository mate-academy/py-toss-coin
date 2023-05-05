import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    times_of_heads = {
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

    for i in range(1, 10001):
        counter = 0
        for _ in range(1, 11):
            if random.choice(coin) == "heads":
                counter += 1

        times_of_heads[counter] += 1

    for i in times_of_heads:
        times_of_heads[i] = round(times_of_heads[i] / 10000 * 100, 2)

    return times_of_heads
