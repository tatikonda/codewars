def descending_order(num):
    num_list = sorted(str(num))[::-1]
    return int("".join(x for x in num_list))


print(descending_order(3344521132))