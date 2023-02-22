import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    dict_amount_count = {}
    for i in range(0, 11):
        dict_amount_count[i] = 0

    coin = ["head", "tail"]
    for _ in range(10000):
        head_counter = 0
        for _ in range(10):
            current = random.choice(coin)
            if current == "head":
                head_counter += 1
        dict_amount_count[head_counter] += 1

    for key, value in dict_amount_count.items():
        dict_amount_count[key] = round((value / 10000) * 100, 2)
    return dict_amount_count


def draw_gaussian_distribution_graph(input_data: dict) -> None:
    xpoints = input_data.keys()
    ypoints = input_data.values()

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(xpoints, ypoints)

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(list(xpoints))
    plt.yticks(list(range(0, 101, 5)))

    plt.show()
