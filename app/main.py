import random
import matplotlib.pyplot as mp
import numpy as np


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}
    for case in range(10000):
        count = 0
        for flip in range(10):
            if random.randrange(2) == 1:
                count += 1
        result[count] += 1
    for num_heads, percentage in result.items():
        result[num_heads] = percentage / 100
    return result


ypoints = np.array(list(flip_coin().values()))
mp.plot(ypoints)
mp.xlabel("Heads count")
mp.ylabel("Drop percentage %")
