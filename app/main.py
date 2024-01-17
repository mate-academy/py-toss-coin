import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    head_roll = {}
    for _ in range(10000):
        heads = sum(random.choices([0, 1], k=10))
        if heads in head_roll:
            head_roll[heads] += 1
        else:
            head_roll[heads] = 1
    result = {key: (value / 100) for key, value in head_roll.items()}
    return result


def plot_histogram(data: dict) -> None:
    sorted_data = dict(sorted(data.items()))
    keys = list(sorted_data.keys())
    values = list(sorted_data.values())

    plt.plot(keys, values)
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability in %")
    plt.title("Coin Flip Simulation")
    plt.show()
