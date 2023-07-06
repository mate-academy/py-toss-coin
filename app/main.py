import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
              8: 0, 9: 0, 10: 0}
    rang = 100000
    for event in range(rang):
        heads = 0
        for quantity in range(10):
            coin = random.randint(0, 1)
            if coin == 0:
                heads += 1
        result[heads] += 1
    return {
        number: count / rang * 100
        for number, count in result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    var_x = list(data.keys())
    var_y = list(data.values())
    plt.plot(var_x, var_y)
    plt.title("Gaussian Distribution Graph")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    plt.show()


draw_gaussian_distribution_graph()


def draw_gaussian_distribution_graph_1() -> None:
    special_dict = flip_coin()
    x_points = [number for number in special_dict]
    y_points = [number for number in special_dict.values()]
    plt.plot(x_points, y_points)
    plt.show()


draw_gaussian_distribution_graph_1()
