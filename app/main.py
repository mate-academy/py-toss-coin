import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {i: i for i in range(11)}
    for number in range(10000):
        counter = 0
        for flip in range(10):
            if random.choice((1, 0)) == 1:
                counter += 1
        result_dict[counter] += 1

    for flip in result_dict:
        result_dict[flip] = result_dict[flip] * 100 / 10000
    return result_dict
