def data_reverse(data):
    temp = []
    res = []
    for i in range(len(data)//8):
        temp.append(data[i*8:(i+1)*8])

    for item in temp[::-1]:
        res += item
    return res
    
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
print(data_reverse(data1))