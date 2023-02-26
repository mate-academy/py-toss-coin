from random import randint
from matplotlib import pyplot


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
    pyplot.plot(data.keys(), data.values())
    pyplot.show()
