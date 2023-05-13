import random


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    temp = []
    for attempt in range(10000):
        temp_result = []
        for side in range(10):
            coin = random.choice(["head", "tail"])
            temp_result.append(coin)
        temp.append(temp_result)
    for sides in temp:
        result[sides.count("head")] += 1
    for value in result:
        result[value] /= 100
    return result
