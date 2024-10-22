import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = {i: 0 for i in range(11)}
    trials = 10000

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for i in range(10))
        cases[heads] += 1

    percents_ = {k: (v / trials) * 100 for k, v in cases.items()}
    return percents_


result = flip_coin()
print(flip_coin)


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    plt.plot(results.keys(), results.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()


draw_gaussian_distribution_graph(result)
