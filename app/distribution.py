import matplotlib.pyplot as plt
import numpy as np
from app.main import flip_coin


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_values = np.array([data.keys()])
    y_values = np.array([data.values()])

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


draw_gaussian_distribution_graph(flip_coin(11000))
