def buildNewList(inputList):
    list.reverse(inputList)
    newList = []
    for i in inputList:
        if (inputList.count(i) / 2 == 1.0) and (newList.count(i) == 0):
            newList.append(i)
    return newList


if __name__ == '__main__':
    print(buildNewList([1, 2, 3, 1, 2, 3, 4, 4]))
