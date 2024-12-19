import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    num_simulations = 10000
    results: Dict[int, float] = {i: 0 for i in range(11)}
    for _ in range(num_simulations):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / num_simulations) * 100

    return results


results = flip_coin()

number_of_heads = list(results.keys())
percentage_values = list(results.values())

plt.bar(number_of_heads, percentage_values)
plt.title("Distribution of Heads in 10 Coin Flips")
plt.xlabel("Number of Heads")
plt.ylabel("Percentage")
plt.show()
