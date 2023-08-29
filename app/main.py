import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    drop_count = {}
    for test in range(10000):
        choices = []
        for i in range(10):
            choices.append(random.choice([0, 1]))
        head_count = choices.count(1)
        if not drop_count.get(head_count):
            drop_count[head_count] = 1
            continue
        drop_count[head_count] += 1
        del choices
    result = {idx: value / 100 for idx, value in drop_count.items()}
    return result


def draw_gaussian_distribution_graph(flip_results: dict) -> None:
    x_points = []
    y_points = []
    for i in range(11):
        x_points.append(i)
        y_points.append(flip_results[i])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_points, y_points)
    plt.show()



