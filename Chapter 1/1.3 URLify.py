"""write a method to replace all the space characters with '%20' characters. Assume that you have enough space at the
   end and you are given length of string.

    Example:    Input = "Mr John Smith  ", 13
                Output = "Mr%20John%20Smith" """


def URLify(val, len):
    for i in range(len-1,-1,-1):
        if val[i] == ' ':
            val[i] = '%'
            val[i+1] = '2'
            val[i+2] = '0'
        else:
            val[i+2] = val[i]
    return val

print URLify("a b                 ", 3)



#refer to Java Solution