import random
import matplotlib
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    numbers = [[random.randint(0, 1) for _ in range(10)]
               for _ in range(1, 10001)]
    sum_numbers = [sum(number) for number in numbers]
    dict_numbers = {"0": sum_numbers.count(0) / 10000 * 100,
                    "1": sum_numbers.count(1) / 10000 * 100,
                    "2": sum_numbers.count(2) / 10000 * 100,
                    "3": sum_numbers.count(3) / 10000 * 100,
                    "4": sum_numbers.count(4) / 10000 * 100,
                    "5": sum_numbers.count(5) / 10000 * 100,
                    "6": sum_numbers.count(6) / 10000 * 100,
                    "7": sum_numbers.count(7) / 10000 * 100,
                    "8": sum_numbers.count(8) / 10000 * 100,
                    "9": sum_numbers.count(9) / 10000 * 100,
                    "10": sum_numbers.count(10) / 10000 * 100}
    return dict_numbers


def draw_gaussian_distribution_graph(coins: dict,
                                     title: str = "Gaussian distribution",
                                     x_label: str = "Head count",
                                     y_label: str = "Drop percents %") -> None:
    x_values = list(coins.keys())
    y_values = list(coins.values())
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


coin = flip_coin()
draw_gaussian_distribution_graph(coin)
