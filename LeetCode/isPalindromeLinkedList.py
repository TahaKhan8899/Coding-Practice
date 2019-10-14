# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # This is an attempt at O(N) time and O(1) space
    def isPalindrome(self, head):

        # count the size of the linked list
        curr = head
        size = 0
        while(curr):
            size += 1
            print(curr.val)
            curr = curr.next

        print("size: ", size)
        half = size/2
        half = int(half)
        print("half index: ", half)

        # make a pointer to the half node
        halfPtr = head
        increment = 0
        while(increment != half):
            halfPtr = halfPtr.next
            increment += 1

        print("HalfNode: ", halfPtr.val)

        # reverse first half of linked list:
        print("Reversing First Half:")
        reversedHead = reverseHalf(head, halfPtr)

        printLL(reversedHead)
        printLL(halfPtr)

        isPal = True
        if(size % 2 == 0):
            print("Even Size")
            # Iterate the first and second half and see if they match
            halfCopy = halfPtr
            while(reversedHead != halfCopy and reversedHead != None and halfPtr != None):
                print("First Half: ", reversedHead.val)
                print("Second Half: ", halfPtr.val)
                if(reversedHead.val != halfPtr.val):
                    isPal = False
                    break
                else:
                    reversedHead = reversedHead.next
                    halfPtr = halfPtr.next
        else:
            print("Odd Size")
            # Iterate the first and second half and see if they match
            halfCopy = halfPtr
            halfPtr = halfPtr.next
            while(reversedHead.next != halfCopy and reversedHead != None and halfPtr != None):
                print("First Half: ", reversedHead.val)
                print("Second Half: ", halfPtr.val)
                if(reversedHead.val != halfPtr.val):
                    isPal = False
                    break
                else:
                    reversedHead = reversedHead.next
                    halfPtr = halfPtr.next

        return isPal


def reverseHalf(head, halfPtr):

    prev = ListNode(None)
    next = ListNode(None)
    curr = head

    while(curr and curr != halfPtr):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev

    return head


def printLL(head):
    curr = head
    while(curr):
        print(curr.val)
        curr = curr.next


n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(2)
n1.next.next.next.next = ListNode(1)

obj = Solution()
ans = obj.isPalindrome(n1)
print(ans)
