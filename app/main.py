import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    # Initialize dictionary to store results
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        num_heads = sum(random.choice([0, 1]) for _ in
                        range(10))  # Simulate flipping a coin 10 times
        results[num_heads] += 1

    # Calculate percentages
    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)

    return results


def draw_gaussian_distribution_graph(dict_of_chances: dict) -> None:
    plt.bar(dict_of_chances.keys(), dict_of_chances.values(), color="blue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips (10 times)")
    plt.show()
