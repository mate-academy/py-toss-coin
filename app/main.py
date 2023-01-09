import random
# import matplotlib as plt


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
    distribution = {"0": trial.count(0) / 100,
                    "1": trial.count(1) / 100,
                    "2": trial.count(2) / 100,
                    "3": trial.count(3) / 100,
                    "4": trial.count(4) / 100,
                    "5": trial.count(5) / 100,
                    "6": trial.count(6) / 100,
                    "7": trial.count(7) / 100,
                    "8": trial.count(8) / 100,
                    "9": trial.count(9) / 100,
                    "10": trial.count(10) / 100}
    return distribution


# def draw_gaussian_distribution_graph():
#     xpoints = flip_coin().keys()
#     ypoints = flip_coin().values()
#     plt.plot(xpoints, ypoints)
#     plt.show()
