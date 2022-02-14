def two_sum(nums, t):
    for i, x in enumerate(nums):
        print('i>',i)
        for j, y in enumerate(nums):
            print('j>',j)
            if i != j and x + y == t:
                return [i, j]

print((two_sum([1,3,2], 4)))