import random
# import matplotlib.pyplot as plt


def simulate(num: int) -> int:
    numflips = []
    for i in range(num):
        numflips.append(random.choice(["H", "T"]))
    return numflips.count("H")


def flip_coin() -> dict:
    trial = []
    for jote in range(10000):
        temp2 = simulate(10)
        trial.append(temp2)
    distribution = {x: trial.count(x) / 100 for x in range(0, 11)}
    return distribution


# def draw_gaussian_distribution_graph():
#     xpoints = flip_coin().keys()
#     ypoints = flip_coin().values()
#     plt.plot(xpoints, ypoints)
#     plt.show()
#
#
# draw_gaussian_distribution_graph()
