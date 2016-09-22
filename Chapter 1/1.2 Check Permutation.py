"""Given 2 strings check if 1st string is a palindrome of another"""

def checkPermutation(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 != len2:
        return False

    hash1 = {}
    hash2 = {}
    for i in range(len1):
        if hash1.has_key(str1[i]):
            hash1[str1[i]] += 1
        else:
            hash1[str1[i]] = 1
        if hash2.has_key(str2[i]):
            hash2[str2[i]] += 1
        else:
            hash2[str2[i]] = 1

    if hash1 == hash2:
        return True
    return False



print checkPermutation("abcdabcd", "acdbacdb")