def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    x = len(min(a1, key=len))
    y = len(max(a2, key=len))
    result1 = abs(x-y)
    x = len(max(a1, key=len))
    y = len(min(a2, key=len))
    result2 = abs(y-x)
    return result1 if result1 >= result2 else result2

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(a1,a2))