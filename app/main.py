from random import randint


def flip_coin() -> dict:
    counts = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0,
              4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0,
              8: 0.0, 9: 0.0, 10: 0.0}

    for _ in range(1000):
        head = 0
        for __ in range(10):
            head += randint(0, 1)
        counts[head] += 1 / 10

    counts = {key: round(value, 2) for key, value in counts.items()}

    return counts
