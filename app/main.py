from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_cases = 10000
    throws_in_case = 10

    res = {i: 0 for i in range(10 + 1)}

    for _ in range(count_cases):
        heads_count = 0

        for _ in range(throws_in_case):
            throw = randint(1, 2)
            heads_count += throw if throw == 1 else 0
        res[heads_count] += 1

    res = {k: round(v / sum(res.values()) * 100, 2)
           for k, v in res.items()}

    return res


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(data.keys(), data.values(), markerfacecolor="#FF0000")
    plt.yticks(list(range(0, 101, 10)))
    plt.xticks(list(range(0, 11)))
    plt.show()
