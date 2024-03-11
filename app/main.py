import random
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> None:
    outcomes = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        outcomes[num_heads] += 1

    percentages = {key: (value / num_cases) * 100
                   for key, value in outcomes.items()}
    return percentages


def draw_gaussian_distribution_graph(percentages: int) -> None:
    plt.bar(percentages.keys(), percentages.values(), color="blue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()


# Test the functions
if __name__ == "__main__":
    percentages = flip_coin()
    print(percentages)
    draw_gaussian_distribution_graph(percentages)
