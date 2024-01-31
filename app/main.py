import random
import matplotlib.pyplot as mpl


def flip_coin() -> dict:
    cases = 10000
    times = 10
    coin = ["head", "tail"]
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
        10: 0
    }

    for case in range(cases):
        head = 0

        for flip in range(times):
            if random.choice(coin) == "head":
                head += 1

        result[head] += 1 / 100

    return result


def draw_gaussian_distribution_graph() -> None:
    percents = flip_coin()

    x_values = list(percents.keys())
    y_values = list(percents.values())

    mpl.plot(x_values, y_values)

    mpl.title("Gaussian distribution")
    mpl.xlabel("Heads count")
    mpl.ylabel("Drop percentage %")

    mpl.show()
