import random


def flip_coin():
    outcomes = dict()
    for i in range(11):
        outcomes[i] = 0

    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.randint(0, 10) & 1:
                heads += 1
        outcomes[heads] += 1

    return {key: round(value * 0.01, 2) for (key, value) in outcomes.items()}
