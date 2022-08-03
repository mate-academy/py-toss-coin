from random import choice


def flip_coin():
    result = dict.fromkeys((number for number in range(11)), 0)

    for _ in range(10000):
        count = 0

        for _ in range(10):
            if choice(["Heads", "Tails"]) == "Heads":
                count += 1
            result[count] += 1

    for key, value in result.items():
        result[key] = value / 10000 * 100
    return result
