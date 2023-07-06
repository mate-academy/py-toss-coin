import random
import matplotlib.pyplot as plt


def flip_coin():
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in range(100000):
        heads = 0
        for j in range(10):
            coin = random.randint(0, 1)
            if coin == 0:
                heads += 1
        result[heads] += 1
    for key in result:
        result[key] = round(result[key] / 100, 2)
    return result


def draw_gaussian_distribution_graph():
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y)
    plt.title("Gaussian Distribution Graph")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    plt.show()


    draw_gaussian_distribution_graph()

    return {
        number: count / rang * 100
        for number, count in dict_of_probabilities.items()
                }


def draw_gaussian_distribution_graph() -> None:
    special_dict = flip_coin()
    x_points = [number for number in special_dict]
    y_points = [number for number in special_dict.values()]
    plt.plot(x_points, y_points)
    plt.show()


draw_gaussian_distribution_graph()
