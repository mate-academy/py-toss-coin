import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {
        i: 0.0 for i in range(11)
    }
    for _ in range(10000):
        flips = (
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1)
        )
        occurrences = flips.count(1)
        result_dict[occurrences] += 1
    for key in result_dict:
        value = result_dict[key]
        result_dict[key] = round((value / 100), 2)
    return result_dict


if __name__ == "__main__":
    result = flip_coin()
    x_asics = [num for num in range(0, 11)]
    print(x_asics)
    y_asics = [num for num in range(0, 110, 10)]
    occurrences = [num for num in result.values()]
    fig, ax = plt.subplots()

    ax.plot(x_asics, occurrences, "-o", label="Occurrences")
    ax.set_ylim(0, 100)
    ax.set_yticks([num for num in range(0, 101, 10)])


    plt.plot(x_asics, occurrences)
    plt.xlabel("Frequency of Occurrences")
    plt.ylabel("Count of Occurrences")
    plt.title(f"Flip Coin")
    plt.show()
