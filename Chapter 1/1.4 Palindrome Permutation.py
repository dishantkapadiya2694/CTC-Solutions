"Find if the given string is a permutation of a plaindrome"

def generateHash(str):
    str = str.lower()
    str = str.replace(" ","")
    str = list(str)
    a = []
    for i in range(26):
        a.append(0)
    for x in str:
        a[ord(x) - ord('a')] += 1

    return a


def check(hash):
    foundOdd = False
    for x in hash:
        if x%2 == 1:
            if foundOdd == True:
                return False
            foundOdd = True
    return True

print check(generateHash("aaaabb"))