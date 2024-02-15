import random
from matplotlib import pyplot


def flip_coin() -> dict:
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    total_trials = 10000
    num_flips = 10

    for _ in range(total_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] / total_trials) * 100

    return result


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_coordinates = []
    y_coordinates = []

    for key, value in result.items():
        x_coordinates.append(key)
        y_coordinates.append(value)

    pyplot.plot(x_coordinates, y_coordinates)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.show()
