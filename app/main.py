import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    data = {}
    total_count = 0
    for _ in range(10000):
        sequence = [random.choice(["head", "not_head"]) for _ in range(10)]
        data[sequence.count("head")] = data.get(sequence.count("head"), 0) + 1
        total_count += 1
    for key in data:
        data[key] = round((data[key] / 10000) * 100, 2)

    return data


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values)

    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.title("Grap based on dict")

    plt.show()
