import random
import matplotlib.pyplot as plt


def flip_coin():
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        case = 0
        for _ in range(10):
            case += random.randint(0, 1)
        result[case] = result[case] + 1

    for key, value in result.items():
        result[key] = round((value / 10000) * 100, 2)
    return result


def draw_gaussian_distribution_graph():
    result = flip_coin()
    plt.plot(result.keys(), result.values())
    plt.axis([0, 10, 0, 100])
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title('Gaussian distribution')
