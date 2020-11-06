def Main():
    myList = [20, 44, 12, 43, 15]
    mini = myMin(myList)
    print(mini)


def myMin(myList):
    minimum = myList[0]
    for i in range(1, len(myList)):
        if minimum > myList[i]:
            minimum = myList[i]

    return minimum


Main()
