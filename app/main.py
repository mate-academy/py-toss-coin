import random
import matplotlib.pyplot as plt


def flip_coin():
    head_or_tail_list = [[random.choice(["h", "t"]) for
                          _ in range(10)] for _ in range(0, 10000)]
    list_of_count = [head.count("h") for head in head_or_tail_list]
    dict_of_count = {i: list_of_count.count(i) / 100 for i in range(11)}
    return dict_of_count


def draw_gaussian_distribution_graph():
    data = flip_coin()
    plt.axis([0, 10, 0, 80])
    plt.title('Gaussian Distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drope percentage %')
    plt.plot(data.keys(), data.values())
    plt.show()
