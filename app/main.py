from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(randint(0, 1) for _ in range(10))
        result[heads] += 1

    result = {key: value / cases * 100 for key, value in result.items()}
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())
    plt.plot(keys, values)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
