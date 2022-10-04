import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def flip_coin() -> dict:
    sample = [
        [random.randint(0, 1) for _ in range(10)].count(1)
        for _ in range(10000)
    ]
    return {
        i: round(sample.count(i) * 0.01, 2)
        for i in range(0, 11)
    }


def draw_gaussian_distribution_graph() -> None:
    graf = flip_coin()
    fig, ax = plt.subplots()

    ax.axis([0, 10, 0, 100])
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.title('Gaussian distribution')

    plt.plot(graf.keys(), graf.values())

    plt.show()
