def Main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num = 2
    newList = my_filter(myList, num)
    print(newList)


def my_filter(myList, num):
    updateList = []
    for i in range(len(myList)):
        if myList[i] % num != 0:
            updateList.append(myList[i])

    return updateList


Main()
