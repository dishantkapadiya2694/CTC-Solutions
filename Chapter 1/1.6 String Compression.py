"""given a string compress it.
    Example: aaabbcccccaa = a3b2c5a2"""


def strCompression(str):
    newStr = ""
    lastChar = str[0]
    lastCharCount = 1
    for i in range(1, str.__len__()):
        if str[i] == lastChar:
            lastCharCount += 1;
        else:
            newStr += lastChar+lastCharCount.__str__()
            lastChar = str[i]
            lastCharCount = 1
    newStr += lastChar + lastCharCount.__str__()

    return newStr if str.__len__() > newStr.__len__() else str


print strCompression("aabbbcccccrrrrjjjjdddkklkjgh")