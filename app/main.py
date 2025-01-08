import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    number_of_heads = list(data.keys())
    percentage_of_occurrences = list(data.values())

    plt.plot(number_of_heads,
             percentage_of_occurrences,
             color="blue",
             label="Distribution of the number of eagles")
    plt.title("Normal distribution")
    plt.xlabel("Number of eagles")
    plt.ylabel("Percentage of cases")
    plt.grid(True)
    plt.show()
