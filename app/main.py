import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    for case in range(10000):
        dropping_times = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                dropping_times += 1
        result[dropping_times] += 1

    for key, value in result.items():
        result[key] = value / 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_axis = list(result.keys())
    y_axis = list(result.values())

    plt.plot(x_axis, y_axis)
    plt.axis([0, 10, 0, 100])
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.tight_layout()
    plt.show()


results = flip_coin()
draw_gaussian_distribution_graph(results)
