import random


def flip_coin():

    list_of_total_cases = [
        [random.choice(["hs", "ts"]) for _ in range(10)] for _ in range(10000)
    ]

    list_of_count_heads = [case.count("hs") for case in list_of_total_cases]

    dict_count_heads = {i: list_of_count_heads.count(i) / 100
                        for i in range(11)}

    return dict_count_heads
