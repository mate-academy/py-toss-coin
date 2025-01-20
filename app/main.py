import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            side_of_coin = random.randint(0, 1)
            if side_of_coin == 1:
                heads += 1
        result[heads] += 1

    for heads in result:
        result[heads] = (result[heads] / 10000) * 100

    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_coor = list(data.keys())
    y_coor = list(data.values())

    plt.bar(x_coor, y_coor, color="skyblue")
    plt.title("Coin Flip Distribution (10 Flips, 10000 Trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Occurrences")
    plt.xticks(x_coor)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()


result = flip_coin()
draw_gaussian_distribution_graph(result)


print(flip_coin())
