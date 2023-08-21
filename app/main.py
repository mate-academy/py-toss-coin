import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> None:
    outcomes = {num: 0 for num in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = 0
        for _ in range(flips_per_trial):
            if random.random() < 0.5:
                heads_count += 1

        outcomes[heads_count] += 1

    for num in outcomes:
        outcomes[num] = (outcomes[num] / trials) * 100

    return outcomes


def draw_gaussian_distribution_graph() -> None:
    flip_coin_f = flip_coin()
    xpoints = list(flip_coin_f.keys())
    ypoints = list(flip_coin_f.values())

    plt.bar(xpoints, ypoints)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Coin Flipping Distribution")
    plt.show()
