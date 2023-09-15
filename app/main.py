import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    drop_0 = 0
    drop_1 = 0
    drop_2 = 0
    drop_3 = 0
    drop_4 = 0
    drop_5 = 0
    drop_6 = 0
    drop_7 = 0
    drop_8 = 0
    drop_9 = 0
    drop_10 = 0
    for _ in range(10000):
        orels = 0
        for _ in range(10):
            number = random.randint(1, 10)
            if number > 5:
                orels += 1
        if orels == 0:
            drop_0 += 1
        if orels == 1:
            drop_1 += 1
        if orels == 2:
            drop_2 += 1
        if orels == 3:
            drop_3 += 1
        if orels == 4:
            drop_4 += 1
        if orels == 5:
            drop_5 += 1
        if orels == 6:
            drop_6 += 1
        if orels == 7:
            drop_7 += 1
        if orels == 8:
            drop_8 += 1
        if orels == 9:
            drop_9 += 1
        if orels == 10:
            drop_10 += 1

    fin_dict = {
        0: round(drop_0 / 100, 2),
        1: round(drop_1 / 100, 2),
        2: round(drop_2 / 100, 2),
        3: round(drop_3 / 100, 2),
        4: round(drop_4 / 100, 2),
        5: round(drop_5 / 100, 2),
        6: round(drop_6 / 100, 2),
        7: round(drop_7 / 100, 2),
        8: round(drop_8 / 100, 2),
        9: round(drop_9 / 100, 2),
        10: round(drop_10 / 100, 2),
    }

    return fin_dict


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()

    xpoints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ypoints = [
        flips[0],
        flips[1],
        flips[2],
        flips[3],
        flips[4],
        flips[5],
        flips[6],
        flips[7],
        flips[8],
        flips[9],
        flips[10],
    ]
    plt.figure(figsize=(100, 10))
    plt.plot(xpoints, ypoints)
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")
    plt.show()
