from random import choice
import matplotlib.pyplot as plt


def flip_coin():
    dict_result = dict.fromkeys((number for number in range(11)), 0)

    for trial in range(10000):
        count = 0

        for flip in range(10):
            if choice(["Heads", "Tails"]) == "Heads":
                count += 1
        dict_result[count] += 1

    for key, value in dict_result.items():
        dict_result[key] = value / 10000 * 100
    return dict_result


def draw_gaussian_distribution_graph(data):
    x = list(data.keys())
    y = list(data.values())
    plt.axis([0, 10, 0, 100])
    plt.plot(x, y)
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.show()
