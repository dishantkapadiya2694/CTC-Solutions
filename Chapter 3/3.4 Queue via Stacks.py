"""Implement Queue using 2 Stacks"""

from Stack import stack

class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__Stack1 = stack(capacity)
        self.__Stack2 = stack(capacity)
        self.__activeStack = self.__Stack1
        self.__passiveStack = self.__Stack2

    def enqueue(self, val):
        if not self.__activeStack.spaceAvailable() and not self.__passiveStack.spaceAvailable():
            print "Queue Full"
            return

        elif not self.__activeStack.spaceAvailable():
           if self.__passiveStack.spaceAvailable():


        self.__activeStack.push(val)

    def dequeue(self):
        if len(self.__activeStack)+len(self.__passiveStack) == 0:
            print "Queue empty"
            return
