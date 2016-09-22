"Given 2 strings, check if string 2 is a rotation of string 1. You are given a function isSubstring and can be used ONLY ONCE."

def isRotation(s1, s2):
    if s1.__len__() == s2.__len__():
        s1s1 = s1+s1
        return s2 in s1s1
    return False