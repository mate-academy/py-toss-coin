import random
import matplotlib.pyplot as pyplot


def flip_coin() -> dict:
    heads_dropped = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10000):
        heads_dropped_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_dropped_count += 1
        heads_dropped[heads_dropped_count] += 1
    return {key: value * 100 / 10000 for key, value in heads_dropped.items()}


def draw_gaussian_distribution_graph() -> None:
    pyplot.plot(flip_coin().items())

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.ylim(0, 100)

    pyplot.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
