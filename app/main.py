import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] / 10000) * 100

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    result_x = list(result.keys())
    result_y = list(result.values())
    plt.plot(result_x, result_y)
    plt.yticks(range(0, 101, 10))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
