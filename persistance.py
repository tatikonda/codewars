def persistence(num):
    counter=0 # set counter to 0
    while num>9: # 
        counter+=1
        total=1
        for i in str(num):
            total=total * int(i)
        num=total
    return counter
    
print(persistence(876))