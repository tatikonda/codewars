def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    return result

b = ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"]
c = ["U", "V", "R"]
print(stock_list(b, c))