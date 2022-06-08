from random import randint
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def flip_coin():
    n = 10  # number of trials
    t = 10000  # number of coin tosses in each trial

    trials = [sum([randint(0, 1) for i in range(n)]) for j in range(t)]
    freq = [trials.count(k) / 100 for k in range(n + 1)]

    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    plt.plot(range(n + 1), freq, color="blue")
    plt.show()


flip_coin()
