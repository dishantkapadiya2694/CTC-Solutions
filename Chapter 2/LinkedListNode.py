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
        for i in self.next:
            length += 1
        return length

    def nodeAtIndex(self, index):
        assert len(self) >= index
        temp = self
        for i in range(index):
            temp = temp.next
        return temp