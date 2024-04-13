import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = dict.fromkeys(range(0, 11), 0)

    for _ in range(10_000):
        heads = [random.randint(0, 1) for _ in range(10)]
        result_dict[heads.count(1)] += 1

    for key, value in result_dict.items():
        result_dict[key] = round((value / 10_000) * 100, 2)

    return result_dict


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    y_ticks = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    x_ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.plot(distribution.keys(), distribution.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gussian distribution")
    plt.yticks(y_ticks)
    plt.xticks(x_ticks)
    plt.show()
