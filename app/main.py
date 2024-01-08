import random
# from typing import Callable
#
# from matplotlib import pyplot


def flip_coin() -> dict:

    result = {}

    for case in range(15000):
        nr_of_heads_out_of_10 = 0
        for num in range(1, 11):
            heads_or_tails = random.randint(0, heads := 1)
            if heads_or_tails == heads:
                nr_of_heads_out_of_10 += 1

        if nr_of_heads_out_of_10 in result:
            result[nr_of_heads_out_of_10] += 1
        else:
            result[nr_of_heads_out_of_10] = 1

    for key in result.keys():
        result[key] /= (15000 / 100)

    return dict(sorted(result.items()))

# # EXTRA TASK
# def draw_gaussian_distribution_graph(func: Callable) -> None:
#     result_dict = func()
#     x_points = []
#     y_points = []
#
#     for key, values in result_dict.items():
#         x_points.append(key)
#         y_points.append(values)
#
#     pyplot.plot(
#         x_points,
#         y_points,
#         "h-.m",
#         ms=10,
#         mec="k",
#         mfc="#00CED1"
#     )
#
#     pyplot.title("Gaussian distribution")
#     pyplot.xlabel("Heads count")
#     pyplot.ylabel("Drop percentage %")
#     pyplot.xlim(0, 10)
#     pyplot.ylim(0, 100)
#     pyplot.show()
