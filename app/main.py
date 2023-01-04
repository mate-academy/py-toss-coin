import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {}
    for i in range(11):
        result_dict[i] = 0

    for i in range(10000):
        count = 0
        for _ in range(10):
            number = random.randint(0, 1)
            if number == 1:
                count += 1
        if count in result_dict.keys():
            result_dict[count] += 1

    for key, value in result_dict.items():
        result_dict[key] = round(((value / 10000) * 100), 2)

    return result_dict


xpoints = flip_coin().keys()
ypoints = flip_coin().values()


def draw_gaussian_distribution_graph() -> plt:
    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.show()
