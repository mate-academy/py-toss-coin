import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dct = {i: 0 for i in range(11)}
    for flips in range(10000):
        ten_flips = []
        for i in range(10):
            ten_flips.append(random.randint(0, 1))
        dct[sum(ten_flips)] += 1
    for key, value in dct.items():
        dct[key] = value / 100
    return dct


def draw_gaussian_distribution_graph(list_of_coord: list) -> plt:
    y_points = list_of_coord

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.yticks(range(0, 101, 10))
    plt.yticks(range(5, 101, 10), minor=True)
    plt.xticks(range(0, 11, 1))
    plt.plot(y_points)
    plt.show()


if __name__ == "__main__":
    list_of_coord = [value for value in flip_coin().values()]
    draw_gaussian_distribution_graph(list_of_coord)
