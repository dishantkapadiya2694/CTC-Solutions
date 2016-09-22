"""Implement an algorithm to check if a string has all the unique characters. Also try doing the same without using any extra Data Structure."""

def isUnique(str):
    setOfChar = set()
    strList = list(str)

    for c in strList:
        if setOfChar.__contains__(c):
            return False
        else:
            setOfChar.add(c)
    return True



def isUniqueWithoutDS(str):
    strlen = len(str)
    for i in range(strlen):
        for j in range(i+1, strlen):
            if str[i] == str[j]:
                return False
    return True


print isUniqueWithoutDS("Dishant")