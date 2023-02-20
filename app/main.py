import random
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
    count = 0
    for _ in range(10000):
        for __ in range(10):
            rand = random.randint(1, 2)
            if rand == 1:
                count += 1
        result[count] += 1
        count = 0

    return {
        0: round(100 / (10000 / result[0]), 2),
        1: round(100 / (10000 / result[1]), 2),
        2: round(100 / (10000 / result[2]), 2),
        3: round(100 / (10000 / result[3]), 2),
        4: round(100 / (10000 / result[4]), 2),
        5: round(100 / (10000 / result[5]), 2),
        6: round(100 / (10000 / result[6]), 2),
        7: round(100 / (10000 / result[7]), 2),
        8: round(100 / (10000 / result[8]), 2),
        9: round(100 / (10000 / result[9]), 2),
        10: round(100 / (10000 / result[10]), 2),
    }


def draw_gaussian_distribution_graph(points: dict) -> None:
    points_list = list(points.values())
    plt.plot(points_list)
    plt.show()
