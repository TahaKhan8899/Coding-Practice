# NOT DONE

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        print("hi")

        # Algo: everything before the difference is discarded, look at both indices after that
        sizeA = getSize(headA)
        sizeB = getSize(headB)

        diff = (sizeA - sizeB) * -1

        if sizeA > sizeB:
            # increment array a, diff times
            newStartNodeA = increment(headA, diff)
            # print(newStartNodeA.val)
        else:
            # increment array b, diff times
            increment(headA, diff)


def increment(node, amount):
    newNode = node
    for i in range(0, amount):
        newNode = newNode.next
        print(newNode.val)

    return newNode


def getSize(head):

    size = 0
    currentNode = head
    while(currentNode != None):
        size = size + 1
        currentNode = currentNode.next

    return size


def test():
    a1 = ListNode(4)
    a2 = ListNode(5)
    a3 = ListNode(6)
    a4 = ListNode(7)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = None

    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(7)
    b1.next = b2
    b2.next = b3
    b3.next = None

    slnObj = Solution()
    slnObj.getIntersectionNode(a1, b1)


test()
