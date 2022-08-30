import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin():
    result_dict = {}
    count_dict = {}
    for i in range(1, 10001):
        suma = 0
        for _ in range(10):
            suma += random.randint(0, 1)
        count_dict[suma] = count_dict.get(suma, 0) + 1
    num = sum(count_dict.values())
    for k, v in count_dict.items():
        result_dict[k] = v / num * 100
    return result_dict


def draw_gaussian_distribution_graph(results: dict):
    x = []
    y = []
    for k, v in results.items():
        x.append(k)
        y.append(v)
    xpoints = np.array(x)
    ypoints = np.array(y)
    plt.plot(xpoints, ypoints, 'o')
    plt.show()
