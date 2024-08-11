import random
from collections import defaultdict


def flip_coin(trials: int = 10000) -> dict[int, float]:
    dict_result: defaultdict[int, int] = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))

        dict_result[heads_count] += 1

    final_result = {key: 0.0 for key in range(11)}

    for key in dict_result:
        percentage = (dict_result[key] / trials) * 100
        final_result[key] = round(percentage, 2)

    return final_result
