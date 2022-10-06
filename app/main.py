import random


def flip_coin() -> dict:
    flips_rate = {number: 0 for number in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(["Head", "Tail"]) == "Head":
                count += 1

        flips_rate[count] += 1

    return {key: value / 100 for key, value in flips_rate.items()}
