import random


def flip_coin():
    count = []
    side = ["Heads", "Tails"]
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.choice(side) == "Heads":
                heads += 1
        count.append(heads)
    return {i: count.count(i) * 100 / 10000 for i in range(11)}
