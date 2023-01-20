# write your code here
import random


def flip_coin():
    total_count_heads = 0
    total_dict = {}
    super_total_dict = {}
    for i in range(5):
        heads_count = 0
        for k in range(10):
            heads_count += random.randint(0, 1)
        total_count_heads += heads_count
        print("Total count = ", total_count_heads)
        total_dict[heads_count] = (total_dict.get(heads_count, 0) + 1)
        print(total_dict)
    for key, value in total_dict.items():
        super_total_dict[key] = round(value / total_count_heads, 3)
    return super_total_dict


print(flip_coin())