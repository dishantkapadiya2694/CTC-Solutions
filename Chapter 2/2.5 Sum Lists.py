"""Numbers are represented in form of Linked Lists e.g. 912 = 2->1->9. You are given 2 numbers, Add them and represent answer in
   the same form. Also, repeat the same if were written like this. 912 = 9->1->2."""

# you can also do it by traversing through the list and converting the list into a number. this doesn't work if number is huge for the processor.


from LinkedListNode import linkedListNode

def sumLists(num1, num2):
    n1 = num1
    n2 = num2
    ans = None
    carry = 0
    sum = 0

    while n1!=None or n2!=None or carry != 0:
        n1d = 0 if n1 == None else n1.data
        n2d = 0 if n2 == None else n2.data
        sum = n1d+n2d+carry
        temp = linkedListNode(sum%10,None)
        ans = linkedListNode.addToTail(ans, temp)
        carry = (sum - temp.data)/10
        n1 = None if n1 == None else n1.next
        n2 = None if n2 == None else n2.next

    return ans


def sumListsReversed(num1, num2):
    n1 = num1
    n2 = num2
    ans = None
    carry = 0
    sum = 0

    while n1!=None or n2!=None or carry != 0:
        n1d = 0 if n1 == None else n1.data
        n2d = 0 if n2 == None else n2.data
        sum = n1d+n2d+carry
        temp = linkedListNode(sum%10,None)
        ans = linkedListNode.addToTail(ans, temp)
        carry = (sum - temp.data)/10
        n1 = None if n1 == None else n1.next
        n2 = None if n2 == None else n2.next

    return ans

num1 = linkedListNode.addToTail(None, linkedListNode(7, linkedListNode(1, linkedListNode(6, None))))
num2 = linkedListNode.addToTail(None, linkedListNode(5, linkedListNode(9, linkedListNode(2, None))))

ans = sumLists(num1, num2)
ans.displayFromHere()


