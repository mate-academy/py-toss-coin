import random


def flip_coin():
    dict_of_causes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                      5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        count_of_head = 0

        for i in range(10):
            if random.randint(1, 2) == 1:
                count_of_head += 1

        dict_of_causes[count_of_head] += 1

    return {key: value / 100 for key, value in dict_of_causes.items()}


print(flip_coin())
