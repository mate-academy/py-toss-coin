from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_cases = 10_000
    throws_in_case = 10

    res = {i: 0 for i in range(11)}

    for _ in range(count_cases):
        heads_counter = 0

        for _ in range(throws_in_case):
            throw = randint(0, 1)
            heads_counter += throw if throw == 1 else 0
        res[heads_counter] += 1

    res = {key: round(value / sum(res.values()) * 100, 2)
           for key, value in res.items()}

    return res


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(data.keys(), data.values(), markerfacecolor="#FF0000")
    plt.yticks(list(range(0, 101, 10)))
    plt.xticks(list(range(0, 11)))
    plt.show()
