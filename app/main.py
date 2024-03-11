from random import gauss, randint
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    quantity_cases = {
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
    standard_deviation = pow(10 * (1 - 0.5) * 0.5, 1 / 2)
    throws = randint(10000, 50000)
    throw = 0
    while throw != throws:
        quantity_of_coins = round(gauss(5, standard_deviation))
        if quantity_of_coins > 10:
            quantity_of_coins = 10
        if quantity_of_coins < 0:
            quantity_of_coins = 0
        quantity_cases[quantity_of_coins] += 1
        throw += 1
    return {k: v * 100 / throws for k, v in quantity_cases.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    key_list = []
    value_list = []
    for key, value in data.items():
        key_list.append(int(key))
        value_list.append(value)
    x_points = np.array(key_list)
    y_points = np.array(value_list)

    font1 = {"family": "serif", "color": "blue", "size": 20}
    font2 = {"family": "serif", "color": "darkred", "size": 15}

    plt.title("Розподілення Гауса - 10 монет", fontdict=font1)
    plt.xlabel("Кількість випавших 'орлів'", fontdict=font2)
    plt.ylabel("Вирогідність випадку", fontdict=font2)

    plt.plot(x_points, y_points)


data = flip_coin()
draw_gaussian_distribution_graph(data)
