import random
import matplotlib.pyplot as plt


def heads_count(number: int = 10) -> int:
    counter = 0
    for i in range(number):
        if random.choice([0, 1]) == 0:
            counter += 1

    return counter


def flip_coin() -> dict:
    list_of_heads = []
    for num in range(10000):
        list_of_heads.append(heads_count())

    result_dict = {
        number: list_of_heads.count(number) / 100 for number in range(0, 11)
    }

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    xpoints = flip_coin().keys()
    ypoints = flip_coin().values()
    plt.plot(xpoints, ypoints)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
