"Return the Kth element from last"

from LinkedListNode import linkedListNode

def kthFromLast(listHead, k):
    n = listHead
    count = 0
    while(n != None):
        count += 1
        n = n.next

    kthFromLastIndex = count - k
    assert kthFromLastIndex >= 0
    n = listHead
    for i in range(kthFromLastIndex):
        n = n.next
    return n.data


a = linkedListNode(1)
b = linkedListNode(2,a)
c = linkedListNode(3,b)
d = linkedListNode(4,c)
e = linkedListNode(5,d)
f = linkedListNode(6,e)

print kthFromLast(f, 4)