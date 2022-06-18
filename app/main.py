import random
import matplotlib as mpl
import matplotlib.pyplot as plt

dictionary = {}
option = ["heads", "tails"]


def flip_coin():
    for case in range(0, 10000):
        for num, flip in enumerate(range(1, 11)):
            flip = random.choice(option)
            if flip == "heads":
                if dictionary[num] in dictionary.keys():
                    dictionary[num] += 1.0
                else:
                    dictionary[num] = 1

    for value in dictionary:
        dictionary[value] = (dictionary[value] / 1000) * 100
    return dictionary


def draw_gaussian_distribution_graph():
    my_dictionary = flip_coin()
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    x_axis = list(my_dictionary.keys())
    y_axis = list(my_dictionary.values())
    plt.plot(x_axis, y_axis, color='blue', linestyle='solid')
