"""given a binary tree, design an algorithm wbich creates a linked list of all nodes at each depth."""

from Nodes import BinaryTreeNode
#from LinkedListNode import linkedListNode


"""Basic class for Linked List"""

class linkedListNode:
    "Basic class for Linked List"
    def __init__(self, data, next=None):
        self.data = data
        self. next = next

    def displayFromHere(self):
        temp = self
        while(temp != None):
            print str(temp.data)
            temp = temp.next

    @staticmethod
    def addToTail(list, node):
        if list == None:
            list = linkedListNode(node.data, node.next)
        else:
            temp = list
            while (temp.next != None):
                temp = temp.next
            temp.next = node
        return list

    @staticmethod
    def addToHead(list, node):
        if list == None:
            list = linkedListNode(node.data, node.next)
            return list
        else:
            node.next = list
            return node

    def __len__(self):
        length = 1
        while self.next:
            length += 1
            self = self.next
        return length

    def nodeAtIndex(self, index):
        assert len(self) > index
        temp = self
        for i in range(index):
            temp = temp.next
        return temp

class llnode:
    def __init__(self, height):
        self.__list = []
        self.__height = height

    def __str__(self):
        return "Height: " + str(self.__height) + "\n" + str(self.__list) + "\n"

    def addItem(self, item):
        self.__list.append(item)

def minimalTree(arr):

    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return BinaryTreeNode(arr[0])

    ind = len(arr)/2

    temp = BinaryTreeNode(arr[ind])
    arr.remove(arr[ind])

    templ = minimalTree(arr[:ind])
    if templ:
        temp.setLeftChild(templ)

    tempr = minimalTree(arr[ind:])
    if tempr:
        temp.setRightChild(tempr)
    return temp





def listOfDepths(node, height, list):
    if node:
        listOfDepths(node.leftChildrens(), height + 1, list)
        currentLen = len(list)
        if height >= currentLen:
            for i in range(height - currentLen + 1):
                linkedListNode.addToTail(list, linkedListNode(llnode(currentLen + i)))
        item = list.nodeAtIndex(height).data
        item.addItem(node.data())
        listOfDepths(node.rightChildrens(), height + 1, list)



tree = minimalTree([1,2,3,4,5,5,5,6,7,8,9])
temp = linkedListNode(llnode(0))
listOfDepths(tree, 0, temp)



while temp:
    print str(temp.data)
    temp = temp.next