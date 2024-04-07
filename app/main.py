import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(
        num_trials: int = 10000,
        num_flips: int = 10
) -> Dict[int, float]:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        num_heads = sum(random.randint(0, 1) for _ in range(num_flips))
        results[num_heads] += 1

    return {key: (value / num_trials) * 100 for key, value in results.items()}


distribution_data = flip_coin(num_trials=100000)
print(flip_coin())


def draw_gaussian_distribution_graph(
        data: Dict[int, float]
) -> None:
    plt.plot(list(data.keys()),
             list(data.values()),
             color="blue",
             linestyle="-"
             )
    plt.xlabel("Heads counts")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()


draw_gaussian_distribution_graph(distribution_data)
