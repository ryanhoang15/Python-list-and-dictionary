def Main():
    myList = [1, 2, 4, 7]
    newList = my_lists(myList)
    print(newList)


def my_lists(myList):
    updateList = []
    for i in range(len(myList)):
        nestedList = []
        for j in range(myList[i]):
            nestedList.append(j+1)

        updateList.append(nestedList)

    return updateList


Main()
