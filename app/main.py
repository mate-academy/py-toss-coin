from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
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
    for _ in range(10000):
        number = 0
        for num in range(10):
            if randint(0, 1) == 0:
                number += 1
        result[number] += 1

    for key in result:
        result[key] = round(result[key] / 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    result_list = [result.get(i) for i in result]
    plt.plot(result_list)
