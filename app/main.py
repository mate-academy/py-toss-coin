import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    num_simulations: int = 10000
    simulation_results: Dict[int, float] = {i: 0.0 for i in range(11)}
    for _ in range(num_simulations):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        simulation_results[heads_count] += 1

    for key in simulation_results:
        simulation_results[key] = ((simulation_results[key] / num_simulations)
                                   * 100)

    return simulation_results


def draw_gaussian_distribution_graph(simulation_results: Dict[int, float]) -> \
        None:
    number_of_heads = list(simulation_results.keys())
    percentage_values = list(simulation_results.values())

    plt.bar(number_of_heads, percentage_values)
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.show()


simulation_results = flip_coin()
draw_gaussian_distribution_graph(simulation_results)
