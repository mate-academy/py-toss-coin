import random

import matplotlib.pyplot as plt

from app import validation


def flip_coin(flips: int = 10000, coins: int = 10) -> dict:
    results = {i: 0 for i in range(coins + 1)}
    for _ in range(flips):
        random_list_results = [random.randint(0, 1) for _ in range(coins)]
        heads = random_list_results.count(1)
        results[heads] += 1

    for key in results:
        results[key] = round((results[key] / flips) * 100, 3)

    return results


def main() -> dict:
    """
    Main function to run the coin flipping simulation.
    """

    flips, amount = validation.input_data()

    data_dict = flip_coin(flips, amount)
    return data_dict


if __name__ == "__main__":
    data_main = main()
    x_axis = list(data_main.keys())
    y_axis = list(data_main.values())

    # Plotting the graph
    plt.figure(figsize=(7, 5))
    plt.plot(x_axis, y_axis, label="Sine Curve", marker=".")
    # plt.plot(x, y2, label='Cosine Curve')

    # Setting the X,Y-axis limit from 0 to 100
    plt.ylim(0, 100)
    plt.xlim(0, max(x_axis))

    # Setting the x-axis ticks to display all integers from 0 to max(x)
    plt.xticks(range(0, max(x_axis) + 1))
    # Y-axis from 0 to 100 with a step of 10
    plt.yticks(range(0, 101, 10))

    # Adding labels
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Coin Flip Simulation Results")
    plt.show()

# for full version cod(with input interface)
# def flip_coin(flips: int, coins: int) -> dict:
