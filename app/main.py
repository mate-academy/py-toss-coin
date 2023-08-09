import numpy as np
import matplotlib.pyplot as plt
import random


def flip_coin() -> None:
    yyy0 = yyy1 = yyy2 = yyy3 = yyy4 = 0
    yyy5 = yyy6 = yyy7 = yyy8 = yyy9 = yyy10 = 0
    for ii in range(10000):
        ii += 1
        yy = 0
        ee = 0
        for rr in range(10):
            rr += 1
            flip = random.randrange(2)
            if flip == 0:
                yy += 1
            elif flip == 1:
                ee += 1
        if ee == 10:
            yyy0 += 1
        elif yy == 1:
            yyy1 += 1
        elif yy == 2:
            yyy2 += 1
        elif yy == 3:
            yyy3 += 1
        elif yy == 4:
            yyy4 += 1
        elif yy == 5:
            yyy5 += 1
        elif yy == 6:
            yyy6 += 1
        elif yy == 7:
            yyy7 += 1
        elif yy == 8:
            yyy8 += 1
        elif yy == 9:
            yyy9 += 1
        elif yy == 10:
            yyy10 += 1
    percent0 = (yyy0 / 100)
    percent1 = (yyy1 / 100)
    percent2 = (yyy2 / 100)
    percent3 = (yyy3 / 100)
    percent4 = (yyy4 / 100)
    percent5 = (yyy5 / 100)
    percent6 = (yyy6 / 100)
    percent7 = (yyy7 / 100)
    percent8 = (yyy8 / 100)
    percent9 = (yyy9 / 100)
    percent10 = (yyy10 / 100)
    dict_oll = (
        ({0: percent0, 1: percent1, 2: percent2, 3: percent3,
          4: percent4, 5: percent5, 6: percent6, 7: percent7,
            8: percent8, 9: percent9, 10: percent10})
    )
    return dict_oll

    xx = np.array(list(dict_oll.keys()))
    yy = np.array(list(dict_oll.values()))
    plt.plot(xx, yy)
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")
    plt.show()
