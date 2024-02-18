import random


def flip_coin() -> dict:
    heads_list = [sum(random.choices([1, 0], k=10)) for _ in range(10_000)]

    heads_occurrence = {}
    for number in range(11):
        heads_occurrence[number] = heads_list.count(number) / 100

    return heads_occurrence
