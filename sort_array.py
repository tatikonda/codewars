def sort_array(arr):
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in arr]

# First sort the odd numbers and sort them in reverse
# Now check for each value in the array, replace with odd number using pop()

print(sort_array([5, 3, 2, 8, 1, 4]))