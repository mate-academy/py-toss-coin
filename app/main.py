import random


def flip_coin():
    count = 11
    final_dict = {i: 0 for i in range(11)}
    list_ = ["heads", "tails"]
    for i in range(10000):
        if count == 0:
            final_dict[0] += 1
        if count == 1:
            final_dict[1] += 1
        if count == 2:
            final_dict[2] += 1
        if count == 3:
            final_dict[3] += 1
        if count == 4:
            final_dict[4] += 1
        if count == 5:
            final_dict[5] += 1
        if count == 6:
            final_dict[6] += 1
        if count == 7:
            final_dict[7] += 1
        if count == 8:
            final_dict[8] += 1
        if count == 9:
            final_dict[9] += 1
        if count == 10:
            final_dict[10] += 1
        count = 0
        for i in range(10):
            item = random.choice(list_)
            if item == "heads":
                count += 1
    return final_dict

