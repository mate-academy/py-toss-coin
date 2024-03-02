import random
import matplotlib.pyplot as plt
import numpy as np

variants = ["Heads", "Tails"]


def toss_coin() -> str:
    return random.choice(["Heads", "Tails"])


def get_side_result_number(attempts: int = 10,
                           variant: str = variants[0]) -> int:
    count = 0

    for attempt in range(attempts):
        result = toss_coin()
        if result == variant:
            count += 1

    return count


def flip_coin() -> dict:
    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    for _ in range(10000):
        result = get_side_result_number()
        results[result] += 1

    for key in results.keys():
        results[key] = round(results[key] / 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    heads_count = np.array(results.keys())
    percentage = np.array(results.values())

    plt.plot(heads_count, percentage)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
