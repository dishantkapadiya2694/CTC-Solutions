"Given a linked list, delete a node which is neith head nor tail."

from LinkedListNode import linkedListNode

def deleteFromBetween(listHead):
    if listHead == None or listHead.next == None or listHead.next.next == None:
        return False

    listHead.next = listHead.next.next
    return True

a = linkedListNode(1)
b = linkedListNode(2,a)
c = linkedListNode(3,b)
d = linkedListNode(4,c)
e = linkedListNode(5,d)
f = linkedListNode(6,e)

f.displayFromHere()
print"\n\t-:AFTER DELETION:-\n"

assert deleteFromBetween(f)

f.displayFromHere()