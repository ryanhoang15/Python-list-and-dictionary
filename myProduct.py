def Main():
    myList = [1, 2, 3, 4, 5]
    total = myProduct(myList)
    print(total)


def myProduct(myList):
    result = 1
    for i in range(len(myList)):
        result = result * myList[i]
    return result


Main()
