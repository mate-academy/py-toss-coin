import random
import matplotlib.pyplot as plp


def flip_coin_once() -> int:
    return sum(random.randint(0, 1) for _ in range(10))


def flip_coin() -> dict:
    res = {}
    for i in range(11):
        res[i] = 0

    for _ in range(10000):
        heads_counter = flip_coin_once()
        res[heads_counter] += 1

    for i in range(11):
        res[i] = round(res[i] / 10000 * 100, 2)

    return res


def draw_gaussian_distribution_graph() -> None:
    res = flip_coin()
    x_points = list(res.keys())
    y_points = list(res.values())
    fig, ax = plp.subplots()
    plp.plot(x_points, y_points, color="y")
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 10)
    plp.title("Gaussian distribution")
    plp.xlabel("Heads count")
    plp.ylabel("Drop percentage %")
    plp.show()
