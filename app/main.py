from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    num_of_rounds = 10000
    rounds = [0 for _ in range(num_of_rounds)]
    for i in range(num_of_rounds):
        for _ in range(10):
            if randint(0, 1) == 1:
                rounds[i] += 1

    for i in range(11):
        result[i] = round(rounds.count(i) * 100 / num_of_rounds, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    plt.plot(flip_coin().values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
