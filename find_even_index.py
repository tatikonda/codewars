def find_even_index(arr):
    for i in range(len(arr)):
        print(i)
        print(sum(arr[:1]), sum(arr[i+1:]))
        if sum(arr[:i]) == sum(arr[i+1:]):            
            return i
    return -1

print(find_even_index([1,2,3,4,5,4,3,2,1]))
#print(find_even_index([20,10,-80,10,10,15,35]))