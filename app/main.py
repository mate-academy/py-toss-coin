import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    result_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1
        result_dict[heads] += 1
    total_cases = sum(result_dict.values())
    return {
        key: round((value / total_cases) * 100, 2)
        for key, value in result_dict.items()
    }


def draw_gaussian_distribution_graph() -> None:

    dpi = 90
    fig = plt.figure(dpi=dpi, figsize=(800 / dpi, 500 / dpi))

    dict_of_results = flip_coin()
    x_coord = []
    y_coord = []
    for key, value in dict_of_results.items():
        x_coord.append(key)
        y_coord.append(value)

    plt.plot(x_coord, y_coord, "o-g", label="first", lw=3)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.grid(True)
    fig.savefig("gaussian.png")
