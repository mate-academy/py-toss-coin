import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coins = ["heads", "tails"]
    distribution = {i: 0 for i in range(11)}

    for _ in range(10000):
        new_list = []
        for _ in range(10):
            new_list.append(random.choice(coins))
        num_heads = new_list.count("heads")
        distribution[num_heads] += 1

    result = {key: value / 100 for key, value in distribution.items()}

    return result


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_line = list(distribution)
    y_line = [value for value in distribution.values()]

    plt.ylim(0, 100)
    plt.plot(x_line, y_line, marker="o")
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)

    plt.show()
