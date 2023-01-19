import random
import matplotlib.pyplot as plt


def random_coin(num: int) -> int:
    count = 0
    for i in range(num):
        if random.choice([0, 1]) == 0:
            count += 1
    return count


def flip_coin() -> dict:
    random_list = []
    for num in range(10000):
        random_list.append(random_coin(10))
    random_dict = {
        a: random_list.count(a) / 100 for a in range(0, 11)
    }
    return random_dict


def draw_gaussian_distribution_graph() -> None:
    xpoints = flip_coin().keys()
    ypoints = flip_coin().values()
    plt.plot(xpoints, ypoints)
    plt.show()
