import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, int]:
    dic_py = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            counter += random.randint(0, 1)
        dic_py[counter] += 1
    for i, value in dic_py.items():
        value = value / 100
        dic_py[i] = value
    return dic_py


def draw_gaussian_distribution_graph(amount: int, interest: int) -> None:
    ex = np.array(amount)
    y_k = np.array(interest)
    plt.plot(ex, y_k)
