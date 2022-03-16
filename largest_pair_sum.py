def largest_pair_sum(nums):
    sort_list = sorted(nums)
    return sum(sort_list[-2:])

print(largest_pair_sum([10,14,2,23,19]))