import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    data = {str(i): 0 for i in range(11)}
    sides = ["head", "tail"]
    for _ in range(10000):
        number_of_heads = 0
        for _ in range(10):
            if random.choice(sides) == "head":
                number_of_heads += 1
        print(number_of_heads)
        data[str(number_of_heads)] += 1
    percentages = {
        i: round((data[str(i)] / 10000) * 100, 2)
        for i in range(11)
    }
    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    x_coords = list(percentages.keys())
    y_coords = list(percentages.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x_coords, y_coords, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(x_coords)
    plt.grid(axis="y")

    plt.show()
