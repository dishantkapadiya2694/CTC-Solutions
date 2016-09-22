"""Design a stack which, beside push and pop, also returns minimum element in O(1)"""

class stack:
    'Implements push, pop, peak and display'
    def __init__(self, limit):
        self.__stk = [None] * limit
        self.__top = -1
        self.__capacity = limit

    def push(self, val):
        if (self.__top + 1) < self.__capacity:
            if self.__top == -1:
                min = val
            else:
                top = self.topElement()
                min = val if top[1] > val else top[1]
            self.__top += 1
            self.__stk[self.__top] = [val, min]
        else:
            print "Stack Overflow"


    def pop(self):
        if (self.__top - 1) >= -1:
            self.__top -= 1
            return self.__stk[self.__top+1][0]
        else:
            print "Stack Underflow"

    def topElement(self):
        if -1 < self.__top < self.__capacity:
            return self.__stk[self.__top]
        elif self.__top <= -1:
            print "Invalid position of top"

    def peek(self):
        if -1 < self.__top < self.__capacity:
            return self.__stk[self.__top[0]]
        elif self.__top <= -1:
            print "Invalid position of top"

    def __str__(self):
        temp = []
        for i in range(self.__top + 1):
            temp.append(self.__stk[i][0])
        print temp

    def display(self):
        self.__str__()



a = stack(10)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(-1)
a.push(4)
a.push(3)
a.push(2)
print a.pop()