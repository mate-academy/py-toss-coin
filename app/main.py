from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    head_occurrences = dict.fromkeys(range(0, 11), 0)
    occurrences = 0

    for _ in range(10_000):
        for _ in range(10):
            if choice(["head", "tail"]) == "head":
                occurrences += 1
        head_occurrences[occurrences] += 1
        occurrences = 0

    return {key: (value / 10_000) * 100
            for key, value
            in head_occurrences.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points, y_points = data.keys(), data.values()
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.xticks(list(range(0, 11)))
    plt.xlim([0, 10])
    plt.ylabel("Drop percentage %")
    plt.ylim([0, 100])
    plt.yticks(list(range(0, 101, 10)))
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin())
