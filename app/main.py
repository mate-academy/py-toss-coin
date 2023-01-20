# write your code here
import random


def flip_coin():
    total_count_heads = 0
    total_dict = {}
    num = 0
    for i in range(5):
        heads_count = 0
        for k in range(10):
            heads_count += random.randint(0, 1)
        print("Head count = ", heads_count)
        total_count_heads += heads_count
        print("Total count = ", total_count_heads)
        total_dict[heads_count] = total_dict.get(heads_count, 0) + 1
    return total_dict


print(flip_coin())
