from random import choice

import matplotlib.pyplot as plt


def is_head_equal(number: int) -> bool:
    result = 0
    coin = ["head", "tail"]
    for _ in range(10):
        if choice(coin) == "head":
            result += 1
    return True if result == number else False


def flip_coin() -> dict:
    number = 0
    count = 0
    result = {}
    while number <= 10:
        for _ in range(10000):
            if is_head_equal(number):
                count += 1
        result[number] = round(count / 10000 * 100, 2)
        number += 1
        count = 0
    return result


def draw_gaussian_distribution_graph() -> None:
    coordinates = flip_coin()
    point_x = [key for key in coordinates.keys()]
    point_y = [value for value in coordinates.values()]

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

    plt.axis([0, 10, 0, 100])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")

    plt.plot(
        point_x,
        point_y,
        "o-b",
        alpha=0.7,
        label="first",
        lw=5,
        mec="r",
        mew=1,
        ms=10
    )
    plt.legend()
    plt.grid(True)
    fig.savefig("gaussian_distribution.png")
