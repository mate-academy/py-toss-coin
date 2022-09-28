import random

import matplotlib.pyplot as plt


def flip_coin():
    count = 0
    d_result = {
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
    for _ in range(10000):
        for _ in range(0, 11):
            if random.choice([0, 1]) == 1:
                count += 1
        for i in range(11):
            if i == count:
                d_result[i] += 1
        count = 0
    for i in range(11):
        d_result[i] /= 10000
        d_result[i] *= 100
        d_result[i] = round(d_result[i], 2)
    print(d_result)
    return d_result


def draw_gaussian_distribution_graph(data: dict):
    y = []
    x = range(11)
    for i in data.values():
        y.append(i)
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

    plt.axis([0, 10, 0, 100])
    plt.plot(x, y, "v-.g", label="Coin Flip")
    plt.legend(loc='upper right')
    plt.grid(True)
    fig.savefig('coinflip.png')


draw_gaussian_distribution_graph(flip_coin())
