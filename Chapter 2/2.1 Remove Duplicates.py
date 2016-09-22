"Remove Duplicates from a given Linked List"

from LinkedListNode import linkedListNode

def removeDups(listHead):
    n1 = listHead
    while(n1!=None):
        n2 = n1
        while(n2.next!= None):
            if(n2.next.data == n1.data):
                n2.next = n2.next.next
            else:
                n2 = n2.next
        n1 = n1.next

a = linkedListNode(1)
b = linkedListNode(2,a)
c = linkedListNode(3,b)
d = linkedListNode(4,c)
e = linkedListNode(5,d)
f = linkedListNode(6,e)

removeDups(f)
f.displayFromHere()