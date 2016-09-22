
class stack:
    'Implements push, pop, peak and display'
    def __init__(self, limit):
        self.__stk = [None] * limit
        self.__top = -1
        self.capacity = limit

    def push(self, val):
        if (self.__top + 1) < self.__capacity:
            self.__top += 1
            self.__stk[self.__top] = val
        else:
            print "Stack Overflow"


    def pop(self):
        if (self.__top - 1) >= -1:
            self.__top -= 1
            return self.__stk[self.__top+1]
        else:
            print "Stack Underflow"

    def peek(self):
        if -1 < self.__top < self.__capacity:
            return self.__stk[self.__top]
        elif self.__top <= -1:
            print "Invalid position of top"

    def spaceAvailable(self):
        return True if self.top < self.__capacity - 1 else False

    def isEmpty(self):
        return True if self.__top == -1 else False

    def __reversed__(self):
        temp = self.__stk
        return temp.reverse()

    def __str__(self):
        temp = []
        for i in range(self.__top + 1):
            temp.append(self.__stk[i])
        print temp

    def __len__(self):
        return (self.__top+1)

    def display(self):
        self.__str__()