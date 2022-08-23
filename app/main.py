import random
import matplotlib


def cointoss():
    return random.choice(["Heads", "Tails"])


def flip_coin():
    result = []
    for f in range(10000):
        list = []
        for i in range(10):
            list.append(cointoss())
        result.append(list.count("Heads"))
    dict = {}
    for t in range(11):
        dict.update({t: result.count(t) / 100})
    return dict


def draw_gaussian_distribution_graph():
    dict = flip_coin()
    x = [key for key in dict.keys()]
    y = [values for values in dict.values()]
    matplotlib.plt.plot(x, y)
    matplotlib.plt.show()
