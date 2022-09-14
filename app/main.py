import random


def flip_coin():
    dict_ = {0: 0,
             1: 0,
             2: 0,
             3: 0,
             4: 0,
             5: 0,
             6: 0,
             7: 0,
             8: 0,
             9: 0,
             10: 0,
             }
    for i in range(10000):
        count = 0
        for j in range(10):
            count += random.randint(0, 1)
        dict_[count] = round(dict_[count] + 0.01)
    return dict_
