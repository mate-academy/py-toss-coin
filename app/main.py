from random import randint
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip = {i: 0 for i in range(11)}
    total_flips = 0

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            coin = randint(0, 1)
            if coin:
                heads += 1
        flip[heads] += 1
        total_flips += 1

    for key in flip:
        flip[key] = round(flip[key] / total_flips * 100, 2)

    return flip


# def draw_gaussian_distribution_graph() -> None:
#     percentages = flip_coin()
#     plt.plot(list(percentages.keys()),
#              list(percentages.values()), marker="o", linestyle="-")
#     plt.xlabel("Number of Heads")
#     plt.ylabel("Percentage")
#     plt.title("Coin Flip Distribution")
#     plt.show()
