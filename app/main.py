import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    result = {key: 0 for key in range(11)}
    for _ in range(num_trials):
        heads_count = sum(1 for _ in range(10)
                          if random.choice(["H", "T"]) == "H")
        result[heads_count] += 1
    probabilities = {key: (count / num_trials) * 100
                     for key, count in result.items()}

    return probabilities


def create_plot(probabilities: dict) -> None:
    x_axis = list(probabilities.keys())
    y_axis = list(probabilities.values())

    plt.plot(x_axis, y_axis)
    plt.title("Heads distribution")
    plt.xlabel("Heads, times")
    plt.ylabel("Probability, %")
    plt.show()
