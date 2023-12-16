import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {num: 0 for num in range(11)}

    for _ in range(10000):
        result = sum(random.randint(1, 2) == 2 for _ in range(10))
        result_dict[result] += 1

    for key in result_dict:
        result_dict[key] = result_dict[key] * 100 / 10000

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    # Extract keys and values from the dictionary
    x_values = list(data.keys())
    y_values = list(data.values())

    # Create a bar chart
    plt.bar(x_values, y_values, color="skyblue")

    # Add labels and a title
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.title("Gaussian distribution")

    # Show the plot
    plt.show(block=True)


flip_coin()
draw_gaussian_distribution_graph()
