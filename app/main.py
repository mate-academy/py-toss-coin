import matplotlib.pyplot as plt
import random


FLIP_NUMBER = 10000


def get_cases_percent(cases: dict):
    cases_amount = sum(cases.values())
    return {
        case: round(value / cases_amount * 100, 1)
        for case, value in cases.items()
    }


def flip_coin():
    dict_of_flip_cases = {}.fromkeys(range(0, 11), 0)

    for _ in range(FLIP_NUMBER + 1):
        case = int(random.gauss(5.5, 1.5804))
        if 0 <= case <= 10:
            dict_of_flip_cases[case] += 1

    return get_cases_percent(dict_of_flip_cases)


def draw_gaussian_distribution_graph():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

    plt.axis([1, 10, 0, 100])

    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    dates = flip_coin()

    plt.plot(dates.keys(), dates.values(), linestyle="solid")

    plt.legend(loc="upper right", frameon=False)
    fig.savefig("fig.png")
