import random
import numpy
from matplotlib import pyplot


def flip_coin() -> dict:
    flip_coin_head_values = {
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
        10: 0
    }

    for _ in range(100):
        random.seed(random.randint(0, 1000))
        count_head = 0
        for _ in range(10):
            flip_result = random.randint(0, 1)
            if flip_result == 1:
                count_head += 1

        flip_coin_head_values[count_head] += 1

    for key, values in flip_coin_head_values.items():
        flip_coin_head_values[key] = round(values / 100, 2)

    return flip_coin_head_values


def draw_gaussian_distribution_graph(distribution_results: dict) -> None:
    point_x = numpy.array(list(distribution_results.keys()))
    point_y = numpy.array(list(distribution_results.values()))
    pyplot.plot(point_x, point_y)
    pyplot.xlabel("Number of occurrences"
                  " of the obverse of the coin in the cycle")
    pyplot.ylabel("Number of repetitions of the loop value")
    pyplot.show()
