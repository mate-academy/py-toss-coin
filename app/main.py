from matplotlib import pyplot

import random


def flip_coin() -> dict:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / num_cases * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    graphic_dict = flip_coin()
    pyplot.xlabel("Number of heads")
    pyplot.ylabel("drop percentage")
    x_points = [number for number in graphic_dict]
    y_point = [number for number in graphic_dict.values()]
    pyplot.bar(x_points, y_point)
    pyplot.show()


draw_gaussian_distribution_graph()
print(flip_coin())
