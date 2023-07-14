import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    rounds = random.randint(10000, 100000)
    cases = []

    for _ in range(0, rounds):
        round_of_flip = []
        for time in range(0, 10):
            choice_side = random.choice(["heads", "tails"])
            round_of_flip.append(choice_side)

        count_of_heads = round_of_flip.count("heads")

        cases.append(count_of_heads)

    count_of_percents = {}

    for key in range(0, 11):
        count = cases.count(key)
        percent = round(((count / len(cases)) * 100), 2)

        count_of_percents[key] = percent

    return count_of_percents


def draw_gaussian_distribution_graph(list_of_dots: dict) -> None:
    list_of_key = []
    list_of_value = []

    for key, value in list_of_dots.items():
        list_of_key.append(key)
        list_of_value.append(value)

    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.plot(list_of_key, list_of_value)
    plt.show()
