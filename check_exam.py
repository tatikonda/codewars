def check_exam(arr1,arr2):
    total = 0
    if len(arr1) != len(arr2):
        return total
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            total += 4
        elif arr2[i] == '':
            total += 0
        else:
            total -= 1
    return total if total >= 0 else 0

print(check_exam(["a", "a", "c", "b"], ["", "c", "b", "d"]))