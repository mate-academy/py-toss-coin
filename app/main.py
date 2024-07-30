import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["head", "non-head"]
    datas = []

    for index in range(10000):
        num_head = 0
        for i in range(10):
            result = random.choice(coin)
            if result == "head":
                num_head += 1
        datas.append(num_head)

    return {
        n: round((datas.count(n) / 10000) * 100, 2) for n in range(11)
    }


def draw_gaussian_distribution_graph() -> None:
    xpoint = [i for i in range(11)]
    ypoint = list(flip_coin().values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(xpoint, ypoint, "b")
    plt.ylim(0, 100)
    plt.xticks([num for num in range(0, 11)])
    plt.yticks([num * 10 for num in range(0, 11)])

    plt.minorticks_on()
    plt.show()


if __name__ == "__main__":
    flip_coin()
    draw_gaussian_distribution_graph()
