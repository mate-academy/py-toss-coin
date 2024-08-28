import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number = 10000
    spys = {i: 0 for i in range(11)}

    for _ in range(number):
        count = 0
        for i in range(10):
            result = random.choice([0, 1])
            if result == 1:
                count += 1
        spys[count] += 1

    res = {i: round(((value / number) * 100), 2)
           for i, value in spys.items()}
    return res
