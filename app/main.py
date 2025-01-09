import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_flip = 10
    count_round = 10000
    head_count_list = []
    for i in range(count_round):
        random_list = random.choices(range(0, 2), k=count_flip)
        head_count_list.append(random_list.count(1))
    return {i: round((head_count_list.count(i) / count_round) * 100, 2)
            for i in range(11)}


def draw_gaussian_distribution_graph(result_flip_coin: dict) -> None:
    x_points = list(result_flip_coin.keys())
    y_points = list(result_flip_coin.values())
    plt.plot(x_points, y_points)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.show()
