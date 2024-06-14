import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin():
    result_dict = {i: i for i in range(11)}
    for number in range(10000):
        counter = 0
        for flip in range(10):
            if random.choice((1, 0)) == 1:
                counter += 1
        result_dict[counter] += 1

    for flip in result_dict:
        result_dict[flip] = result_dict[flip] * 100 / 10000
    return result_dict


def draw_gaussian_distribution_graph(points_dict):
    x = np.array([0, 0])
    y = np.array([10, 100])
    plt.plot(x, y, 'o')
    xpoints = np.array([i for i in points_dict])
    print(xpoints)
    ypoints = np.array([points_dict[i] for i in points_dict])
    print(ypoints)
    plt.plot(xpoints, ypoints)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
