import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin():
    main = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        cases = 0
        for _ in range(10):
            cases += random.randint(0, 1)
        main[cases] += 1
    for i in main:
        main[i] /= 100
    return main


def draw_gaussian_distribution_graph():
    main = flip_coin()
    x = []
    y = []
    for i in range(0, len(main)):
        x.append(i)
        y.append(main[i])
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1024 / dpi, 768 / dpi))
    mpl.rcParams.update({'font.size': 12})

    plt.axis([0, 10, 0, 100])

    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    plt.plot(x, y, color='blue', linestyle='solid')

    fig.savefig('Gaussian_distribution.png')
