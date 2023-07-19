import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counter_eagle = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10_000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1):
                count += 1
        counter_eagle[count] += 1

    for key in counter_eagle:
        counter_eagle[key] = round(counter_eagle[key] / 100, 2)
    return counter_eagle


def draw_gaussian_distribution_graph(coords: dict) -> None:
    x_coord = list(coords.keys())
    y_coord = list(coords.values())
    plt.plot(x_coord, y_coord)
    y_ticks = [i * 10 for i in range(10)]
    y_labels = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    plt.yticks(ticks=y_ticks, labels=y_labels)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
