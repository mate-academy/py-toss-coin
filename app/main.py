import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    choices = ["head", "tail"]
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            choice = random.choice(choices)
            if choice == "head":
                counter += 1
        result[counter] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.plot(data.keys(), data.values())

    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")

    plt.show()
