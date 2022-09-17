import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin():
    coin_dict = {i: 0 for i in range(11)}
    for j in range(10000):
        count = 0
        for j in range(10):
            if random.randint(1, 2) == 1:
                count += 1
        coin_dict[count] += 1
    coin_dict = {k: v / 100 for k, v in coin_dict.items()}
    return coin_dict


def draw_gaussian_distribution_graph():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.axis([0, 10, 0, 100])

    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    new_dict = flip_coin()
    ys = [new_dict[x] for x in range(11)]
    xs = [[x] for x in range(11)]
    plt.plot(
        xs, ys, color='blue', linestyle='solid',
        label='sin(x)'
    )
    plt.legend(loc='upper right')
    fig.savefig('graph.png')
