from LinkedListNode import linkedListNode

def intersectingNode(listHead1, listHead2):
    len1 = 0
    len2 = 0
    temp1 = listHead1
    temp2 = listHead2
    while temp1!= None:
        len1 += 1
        temp1 = temp1.next

    while temp2 != None:
        len2 += 1
        temp2 = temp2.next

    bigList = listHead1 if len1 > len2 else listHead2
    smallList = listHead2 if bigList == listHead1 else listHead1

    difference  = abs(len1 - len2)

    for i in range(difference):
        bigList = bigList.next

    while bigList != None:
        if bigList == smallList:
            return bigList
        bigList = bigList.next
        smallList = smallList.next

    return None


a = linkedListNode(1)
b = linkedListNode(2,a)
c = linkedListNode(3,b)
d = linkedListNode(4,c)
e = linkedListNode(5,d)
f = linkedListNode(6,e)

g = linkedListNode(4,c)
h = linkedListNode(5,g)

temp = intersectingNode(f, h)
if temp != None:
    print temp.data
else:
    print None

