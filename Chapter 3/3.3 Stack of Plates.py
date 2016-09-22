"""Implement a data structure for SetOfStacks that mimics the real life stacks. Everytime a staack is overflown, a new stack should be created. But pop() should return
   values as if it were one stack.
   FOLLOW UP: Implement a function popAt(index) which pops from a specific stack"""

from Stack import stack

class setOfStacks:

    def __init__(self, capacity):
        self.__stacks = [stack(capacity)]
        self.__capacity = capacity

    def push(self,val):
        if (len(self.__stacks) == 0) or (len(self.__stacks[-1]) == self.__capacity):
            self.__stacks.append(stack(self.__capacity))
        self.__stacks[-1].push(val)

    def pop(self):
        self.__stacks[-1].pop()
        if len(self.__stacks[-1]) == 0:
            self.__stacks.pop()

    def peek(self):
        self.__stacks[-1].peek()

    def display(self):
        temp = []
        for i in range(len(self.__stacks)):
            for j in range(len(self.__stacks[i])):
                temp.append(self.__stacks[i][j])

        print temp

    def Dispaly(self):
        for i in range(len(self.__stacks)):
            self.__stacks[i].display()



a = setOfStacks(10)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
a.push(7)
a.push(8)
a.push(9)
a.push(10)
a.push(11)
a.push(12)
a.push(13)
a.push(14)
a.push(15)
a.push(16)
a.push(17)
a.push(18)
a.push(19)
a.push(20)
#a.display()
a.Dispaly()
for i in range(20):
    a.pop()

a.push(5)
a.Dispaly()


"""Incomplete"""
