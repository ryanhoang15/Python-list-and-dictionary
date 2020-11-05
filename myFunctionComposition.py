def Main():
    dict_1 = {'x': 24, 'y': 25}
    dict_2 = {24: 'twentyfour', 25: 'twentyfive'}
    newDict = my_function_composition(dict_1, dict_2)
    print(newDict)


def my_function_composition(dict_1, dict_2):
    updateDict = {}
    for key_1 in dict_1:
        keyValue = dict_1[key_1]
        for key_2 in dict_2:
            if keyValue == key_2:
                updateDict[key_1] = dict_2[keyValue]

    return updateDict


Main()
