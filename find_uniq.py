def find_uniq(arr):
    # your code here
    arr.sort()
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        print(arr[0])
        n = arr[0]
    else:
        print(arr[0], len(arr), arr)
        n = arr[len(arr)-1]


    return n  

print(find_uniq([ 1, 1, 1, 8, 1, 1, 1, 1 ]))