import matplotlib.pyplot

from random import randint


def flip_coin() -> dict:
    results = {}
    head = 0

    for _ in range(10000):
        for _ in range(10):
            drop = randint(0, 1)
            if drop == 0:
                head += 1
        if head not in results:
            results[head] = 1
        else:
            results[head] += 1
        head = 0

    results = dict(sorted(results.items(), key=lambda item: item[0]))

    for key, value in results.items():
        results[key] = value / 100

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_axis = list(data.keys())
    y_axis = list(data.values())
    matplotlib.pyplot.plot(x_axis, y_axis)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop percentage %")
    matplotlib.pyplot.title("Gaussian distribution")
    matplotlib.pyplot.show()
