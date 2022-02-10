def bouncing_ball(h, bounce, window):
    if h != 0 and bounce > 0 and bounce < 1 and window < h:
        count = 1
        current = h*bounce
        print('before loop',current)
        while current > window:
            current *= bounce
            print(current)
            count += 2
        return count 
    else: 
         return -1 

print(bouncing_ball(30, 0.66, 1.5))