def delete_nth(order,max_e):
    res = []
    for o in order:
        if res.count(o) < max_e: res.append(o)
    return res

print(delete_nth([1,1,3,3,7,2,2,2,2], 3))