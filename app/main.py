import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    possible_choices = [1, 0]
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for test_number in range(10000):
        number_of_heads = 0
        for _ in range(10):
            choice = random.choice(possible_choices)
            if choice == 1:
                number_of_heads += 1
        result[number_of_heads] += 1
    for i in result.keys():
        result[i] = (result[i] / 10000) * 100

    x = np.array(list(result.keys()))
    y = np.array(list(result.values()))

    plt.plot(x, y)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.show()

    return result

flip_coin()