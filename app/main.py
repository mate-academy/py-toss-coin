import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_toss_results = {i: 0 for i in range(11)}

    for _ in range(10000):
        head_counter = 0
        for number in range(10):
            if random.randint(0, 1) == 0:
                head_counter += 1

        coin_toss_results[head_counter] += 1

    coin_toss_results_in_percentage = {item: round(value / 100, 2) for
                                       item, value in
                                       coin_toss_results.items()}

    return coin_toss_results_in_percentage


def draw_gaussian_distribution_graph() -> None:
    flip_coin_data = flip_coin()
    x_points = list(flip_coin_data.keys())
    y_points = list(flip_coin_data.values())

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.plot(x_points, y_points, marker="o")

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.grid()
    plt.show()
