import random

import matplotlib.pyplot as plt


def flip_coin():
    output = {heads_count: 0 for heads_count in range(11)}
    for case in range(10000):
        heads = 0
        for flip in range(10):
            heads += random.randint(0, 1)
        output[heads] += 1
    for heads_count in output:
        output[heads_count] /= 100
    return output


def draw_gaussian_distribution_graph():
    plt.axis([0, 10, 0, 100])

    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    data = flip_coin()
    plt.plot(list(data.keys()), list(data.values()),
             color='blue', linestyle='solid')

    plt.show()
