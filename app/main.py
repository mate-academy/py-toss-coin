import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                   6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        amount = 0
        for _ in range(10):
            heads = random.randint(0, 1)
            if heads:
                amount += 1
        if amount in result_dict:
            result_dict[amount] += 0.01
        else:
            result_dict[amount] = 0.01
    return result_dict


def draw_gaussian_distribution_graph(dict_graph: dict) -> None:
    plt.axis([0, 10, 0, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    x_axis = []
    y_axis = []
    for key, value in dict_graph.items():
        x_axis.append(key)
        y_axis.append(value)
    plt.plot(x_axis, y_axis)
    plt.show()
