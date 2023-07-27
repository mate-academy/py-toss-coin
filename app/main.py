import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counter = 0
    dict_flips = \
        {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    while counter < 10000:
        number_of_head = 0
        for flip in range(10):
            value = random.randrange(0, 2)
            if value == 1:
                number_of_head += 1
        dict_flips[number_of_head] += 1
        counter += 1
    for i in range(11):
        dict_flips[i] = (dict_flips[i] / 10000) * 100
    return dict_flips


def draw_gaussian_distribution_graph() -> None:
    dict_flips = flip_coin()
    axes_x = dict_flips.keys()
    axes_y = dict_flips.values()
    plt.plot(axes_x, axes_y)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
