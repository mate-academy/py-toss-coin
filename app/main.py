import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    attempts = 10000
    flips = 10
    result = dict({key: 0 for key in range(flips + 1)})
    for attempt in range(attempts):
        case = 0
        for flip in range(flips):
            if random.randint(1, 2) == 1:
                case += 1
        result[case] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color="green")
    plt.xlabel("Keys")
    plt.ylabel("Values")
    plt.title("The distribution")
    plt.grid(True)
    plt.show()
