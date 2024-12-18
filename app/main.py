import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_seid = ["Head", "Tail"]
    coin_chance_flip = {}
    for game in range(10000):
        heads_dropped_count = 0
        for flip in range(10):
            if random.choice(coin_seid) == "Head":
                heads_dropped_count += 1
        if heads_dropped_count in coin_chance_flip:
            coin_chance_flip[heads_dropped_count] += 1
        else:
            coin_chance_flip[heads_dropped_count] = 1
    for key, value in coin_chance_flip.items():
        coin_chance_flip[key] = round((value / 10000) * 100, 2)
    return dict(sorted(coin_chance_flip.items()))


def draw_gaussian_distribution_graph() -> None:
    coin_result = flip_coin()
    x_points = []
    y_points = []
    for key, value in coin_result.items():
        y_points.append(int(key))
        x_points.append(value)
    plt.plot(y_points, x_points)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
    print(f"coin: {coin_result} \n y: {y_points} \n x: {x_points}")
