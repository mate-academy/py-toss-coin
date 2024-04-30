import matplotlib.pyplot
import random


def flip_coin() -> dict:
    result = dict.fromkeys([x for x in range(0, 11)], 0)

    for _ in range(10000):
        count = 0
        for _ in range(1, 11):
            count += random.randint(0, 1)
        result[count] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result


def draw_gaussian_distribution_graph() -> None:
    matplotlib.pyplot.plot(range(0, 11), flip_coin().values())
    matplotlib.pyplot.title("Gaussian distribution")
    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")
    matplotlib.pyplot.show()
