from random import randint
import matplotlib.pyplot as pyplt


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    trials_outcome = [0 for _ in range(trials)]
    for i in range(trials):
        for _ in range(flips):
            if randint(0, 1) == 1:
                trials_outcome[i] += 1

    result = {}

    for i in range(flips + 1):
        result[i] = round(trials_outcome.count(i) * 100 / trials, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    pyplt.plot(list(flip_coin().values()))

    pyplt.title("Gaussian graph")
    pyplt.xlabel("Heads count")
    pyplt.ylabel("Percentage of outcomes")

    pyplt.show()
