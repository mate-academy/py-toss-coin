import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Convert counts to percentages
    for heads_count in results:
        results[heads_count] = (results[heads_count] / num_trials) * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    # Extracting keys and values from the results dictionary
    heads_counts = list(results.keys())
    percentages = list(results.values())

    plt.figure(figsize=(8, 6))
    plt.plot(heads_counts, percentages, marker="o", linestyle="-", color="b")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
