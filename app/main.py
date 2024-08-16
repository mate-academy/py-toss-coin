from random import randint
import matplotlib.pyplot as pyplt


def flip_coin() -> dict:
    rounds_num = 10000
    round_result = [0 for _ in range(rounds_num)]
    for i in range(rounds_num):
        for _ in range(10):
            if randint(0, 1) == 1:
                round_result[i] += 1

    result = {}

    for i in range(10 + 1):
        result[i] = round(round_result.count(i) * 100 / rounds_num, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    pyplt.plot(flip_coin().values())

    pyplt.title("Gaussian distribution")
    pyplt.xlabel("Heads count")
    pyplt.ylabel("Percentage %")

    pyplt.show()
