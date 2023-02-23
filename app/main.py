import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    num_cases = 10000
    results = {quantity_times: 0 for quantity_times in range(11)}
    for case in range(num_cases):
        num_heads = 0
        for heads_dropped in range(10):
            if random.random() < 0.5:
                num_heads += 1
        results[num_heads] += 1
    for key in results:
        results[key] = round(results[key] / num_cases * 100, 2)
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    heads_dropped = results.keys()
    percentage = results.values()
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.plot(heads_dropped, percentage)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
