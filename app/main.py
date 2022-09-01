import matplotlib.pyplot as plt
import random as rnd


def flip_coin():
    result = {}
    for i in range(10000):
        key = sum(rnd.randint(0, 1) for _ in range(10))
        if key not in result.keys():
            result[key] = 1
        else:
            result[key] += 1
    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)
    result = dict(sorted(result.items()))
    return result


def draw_gaussian_distribution_graph():
    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.plot(flip_coin().keys(), flip_coin().values())
    plt.show()
