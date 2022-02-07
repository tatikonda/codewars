def count_positives_sum_negatives(arr):
    if not arr: return []
    count = 0
    sum_list = 0
    for x in arr:
        if x > 0:
            count += 1
        if x < 0:
            sum_list += x
    return [count,sum_list]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0,0]))