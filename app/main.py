from matplotlib import pyplot

import random


def flip_coin(cases_of_flipping: int = 10_000, flip_coins: int = 10) -> dict:
    result = {}

    for _ in range(1, cases_of_flipping + 1):
        count_head = 0
        for _ in range(1, flip_coins + 1):
            head = random.randint(0, 1)
            if head == 1:
                count_head += 1
        result[count_head] = result.get(count_head, 0) + 1

    for head_count in range(flip_coins + 1):
        result[head_count] = (result[head_count] / cases_of_flipping) * 100

    return result


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
