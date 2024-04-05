import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    num_trials = 10000
    for _ in range(num_trials):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1

    percentages = {
        key: value / num_trials * 100
        for key, value in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    point_x = list(percentages.keys())
    point_y = list(percentages.values())

    plt.plot(point_x, point_y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11, 1))
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
