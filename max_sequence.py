def max_sequence(arr):
    max = 0
    sub_max = 0
    for i in arr:
        if sub_max > 0:
            sub_max += i
            if sub_max < 0:
                sub_max = 0
            elif sub_max > max:
                max = sub_max
        elif i > 0:
            sub_max += i

    return max


print(max_sequence([-2, 1, -3, 4, -1, 2, 3, -2, -5, 4]))

