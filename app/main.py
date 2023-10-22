import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        head = 0
        for time in range(10):
            choice = random.choice(["head", "tails"])
            if choice == "head":
                head += 1
        result[head] += 1
    return {key: value / 100 for key, value in result.items()}

