import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flipping_coin_cases = [
        [random.randint(0, 1) for _ in range(10)]
        for _ in range(10001)
    ]

    flipping_coin = [case.count(0) for case in flipping_coin_cases]

    return {
        num: (flipping_coin.count(num) / 10000) * 100
        for num in range(0, 11)
    }


def draw_gaussian_distribution_graph() -> None:
    flipping_cases_probability = flip_coin()
    probability = flipping_cases_probability.values()
    amount = flipping_cases_probability.keys()
    plt.plot(amount, probability)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.ylim(0, 100)
    plt.show()


print(flip_coin())
print(sum(flip_coin().values()))
