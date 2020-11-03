def Main():
    list_1 = [1, 2, 3, 4, 5]
    total = mySum(list_1)
    print(total)


def mySum(list_1):
    result = 0
    for i in range(len(list_1)):
        result = result + list_1[i]

    return result


Main()
