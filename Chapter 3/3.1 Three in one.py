""" Implement 3 stacks by using only one array."""

class multiStack:

    def __init__(self, numberOfStacks):
        self.__stack = [None] * 10 * numberOfStacks
        self.__overallSize = len(self.__stack)
        self.__indices = [i for i in range(numberOfStacks)]

    def push(self, val, stack):
        stack -= 1
        assert self.__indices[len(self.__indices)- 1] < self.__overallSize - 1
        assert -1 < stack < len(self.__indices)
        if self.__stack[self.__indices[stack]] == None:
            self.__stack[self.__indices[stack]] = val
            return
        # move one place ahead
        a = range(self.__indices[len(self.__indices) - 1], self.__indices[stack], -1)
        for i in range(self.__indices[len(self.__indices) - 1], self.__indices[stack], -1):
            self.__stack[i+1] = self.__stack[i]
        for i in range(len(self.__indices) - 1, stack, -1):
            self.__indices[i] += 1
        self.__indices[stack] += 1
        self.__stack[self.__indices[stack]] = val

    def display(self, stack):
        stack -= 1
        assert -1 < stack < len(self.__indices)
        temp = []
        start = 0 if stack == 0 else self.__indices[stack - 1] + 1
        end = self.__indices[stack] + 1
        for i in range(start, end):
            temp.append(self.__stack[i])

        print temp



a = multiStack(3)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(1,1)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(2,2)
a.push(3,3)
a.push(3,3)
a.push(3,3)
a.push(3,3)
a.push(5,1)
a.push(5,2)
a.push(5,3)
a.push(5,3)
a.display(1)
a.display(2)
a.display(3)
