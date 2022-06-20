import random
import matplotlib as mpl
import matplotlib.pyplot as plt

dictionary = {i: 0 for i in range(1, 11)}
option = ["heads", "tails"]


def flip_coin():
    for case in range(0, 10000):
        heads = 0
        for _ in range(1, 11):
            flip = random.choice(option)
            if flip == "heads":
                heads += 1
        if heads in dictionary.keys():
            dictionary[heads] += 1
        else:
            dictionary[heads] = 1
    heads_total = sum(dictionary.values())
    for value in dictionary:
        dictionary[value] = round((dictionary[value] / heads_total) * 100, 1)
    return dictionary


def draw_gaussian_distribution_graph():
    my_dictionary = flip_coin()
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    x_axis = list(my_dictionary.keys())
    y_axis = list(my_dictionary.values())
    plt.plot(x_axis, y_axis, color='blue', linestyle='solid')
    fig.savefig('mate.png')
