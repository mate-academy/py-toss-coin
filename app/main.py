import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin():
    res = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for i in range(10000):
        count_or = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                count_or += 1
        res[count_or] += 1
    for key, val in res.items():
        val = val / 100
        res[key] = val
    return res


def draw_gaussian_distribution_graph():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    res = flip_coin()

    xs = []
    perc_vals = []
    for key, val in res.items():
        xs.append(key)
        perc_vals.append(val)

    plt.plot(xs, perc_vals, color='blue', linestyle='solid')
    fig.savefig('trigan.png')
    pass


draw_gaussian_distribution_graph()
