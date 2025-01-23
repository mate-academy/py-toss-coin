import random

import matplotlib.pyplot as plt


def flip_coin_ten_times() -> int:
    coin = ["head", "tail"]
    head_counter = 0
    for i in range(10):
        choice = random.choice(coin)
        if choice == "head":
            head_counter += 1
    return head_counter


def flip_coin() -> dict:
    result = {}
    total_cases = 10000

    for i in range(total_cases):
        number = flip_coin_ten_times()
        if number not in result:
            result[number] = 1
        else:
            result[number] += 1

    for key, value in result.items():
        result[key] = round(value / total_cases * 100, 2)

    return dict(sorted(result.items()))


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    x_points = [key for key in points.keys()]
    y_points = [value for value in points.values()]

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)

    plt.show()
