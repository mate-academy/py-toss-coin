import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_flip_coin = {}
    for number_heads in range(11):
        result_head = 0
        for _ in range(10000):
            count = 0
            for _ in range(10):
                if random.randint(0, 1) == 1:
                    count += 1
            if number_heads == count:
                result_head += 1
        result_flip_coin[number_heads] = result_head / 10000 * 100
    return result_flip_coin


def draw_gaussian_distribution_graf(dict_x_key_y_value: dict) -> None:
    point_x = []
    point_y = []
    for index in range(11):
        point_x.append(index)
        point_y.append(dict_x_key_y_value[index])
    plt.plot(point_x, point_y)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentege %")

    plt.show()
