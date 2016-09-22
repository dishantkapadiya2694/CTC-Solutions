"check if given list is a Plaindrome"

from LinkedListNode import linkedListNode

def palindrome(listHead):
    n = listHead
    reversedList = None
    while n!= None:
        reversedList = linkedListNode.addToHead(reversedList, linkedListNode(n.data))
        n = n.next

    # now compare both lists
    while listHead!= None:
        if listHead.data != reversedList.data:
            return False
        listHead = listHead.next
        reversedList = reversedList.next

    return True



a = linkedListNode(1)
b = linkedListNode(2,a)
c = linkedListNode(3,b)
d = linkedListNode(3,c)
e = linkedListNode(2,d)
f = linkedListNode(1,e)

print palindrome(f)


