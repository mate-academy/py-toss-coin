import matplotlib.pyplot as plt

import random


def flip_coin() -> dict:
    coin_data = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for i in range(1, 10001):
        coin = 0
        for ten_times in range(1, 11):
            coin_up = random.randint(1, 2)
            if coin_up == 1:
                coin += 1
        coin_data[coin] += 1
    for key, value in coin_data.items():
        coin_data[key] = round(value * 0.01, 2)
    return coin_data


def draw_gaussian_distribution_graph(coin_data: flip_coin()) -> None:
    xpoints = []
    ypoints = []
    for key, value in coin_data.items():
        xpoints.append(int(key))
        ypoints.append(round(value * 0.01, 2))
    plt.plot(xpoints, ypoints)
    plt.show()
