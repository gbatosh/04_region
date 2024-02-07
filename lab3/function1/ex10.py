def unique(list):
    newlist = []
    for i in range(len(list)):
        if newlist.count(list[i]) == 0:
            newlist.append(list[i])
    for i in range(len(newlist)):
        print(newlist[i], end = ' ')
unique([11,2,3,4,2,3,4,5,4,6,5,65,4])