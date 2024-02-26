import random


def flip_coin() -> dict:
    dict_store = {}
    for _ in range(10000):
        heads = [random.randint(0, 1) for _ in range(10)]
        how_many_heads = len([h for h in heads if h == 1])
        dict_store[how_many_heads] = dict_store.get(how_many_heads, 0) - 1

    res = {k: (v / -10000) * 100 for k, v in dict_store.items()}
    return res
