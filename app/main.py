import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin():
    side = ("heads", "tails")
    keys = [i for i in range(11)]
    heads_dict = dict.fromkeys(keys, 0)
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.choice(side) == "heads":
                heads += 1
        heads_dict[heads] += 1
    for key in heads_dict:
        heads_dict[key] = heads_dict[key] / 100
    return heads_dict


def draw_gaussian_distribution_graph():
    dpi = 100
    fig = plt.figure(dpi=dpi, figsize=(768 / dpi, 476 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 10, 0, 100])

    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    point_dict = flip_coin()
    xs = list(point_dict.keys())
    gauss_values = list(point_dict.values())

    plt.plot(xs, gauss_values)

    fig.savefig('Gaussian_distribution.png')
