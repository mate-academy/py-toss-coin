import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    result_dict: Dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(10000):
        times = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                times += 1

        result_dict[times] += 1

    probability_dict: Dict[int, float]\
        = {key: round(value / 10000, 3)
           for key, value in result_dict.items()}

    return probability_dict


print(flip_coin())
