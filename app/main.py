import random


def flip_coin() -> dict:
    results = []
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results.append(heads)

    probabilities = {}
    for heads in range(10 + 1):
        count = results.count(heads)
        probability = (count / 10000) * 100
        probabilities[heads] = round(probability, 2)

    return probabilities

# import matplotlib.pyplot as plt
# def draw_gaussian_distribution_graph() -> None:
#     xpoints = flip_coin().keys()
#     ypoints = flip_coin().values()
#
#     plt.plot(xpoints, ypoints)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.show()
