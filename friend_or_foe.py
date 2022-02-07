def friend(x):
    friend_list = []
    for word in x:
        if len(word) == 4:
            friend_list.append(word)
    return friend_list

print(friend(["Ryan", "Kieran", "Mark"]))
