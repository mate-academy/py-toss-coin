import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for i in range(10000):
        count_heads = 0
        for chance in range(10):
            if random.choice(["head", "tail"]) == "head":
                count_heads += 1
        heads_count[count_heads] += 1

    total_cases = 10000
    for key in heads_count:
        heads_count[key] = round(heads_count[key] / total_cases * 100, 2)
    return heads_count


def draw_gaussian_distribution_graph(heads_count: dict) -> None:
    x_point = list(heads_count.keys())
    y_point = list(heads_count.values())

    plt.plot(x_point, y_point)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


heads_distribution = flip_coin()
draw_gaussian_distribution_graph(heads_distribution)
