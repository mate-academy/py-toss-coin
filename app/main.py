# write your code here
import random
import matplotlib.pyplot as plt


def flip_coin() -> list:
    coin = ["head", "tail"]
    probability = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
                   8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        result = 0
        for _ in range(10):
            if random.choice(coin) == "head":
                result += 1
        probability[result] += 1
    for key in probability.keys():
        probability[key] /= 100

    return probability


def draw_gaussian_distribution_graph() -> None:
    points = []
    for key in flip_coin().values():
        points.append(key)
    plt.plot(points)
    plt.title("Gaussian distribution")
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")

    plt.show()
