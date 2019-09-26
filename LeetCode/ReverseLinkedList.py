# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # algo:
        # make a copy of shiftNode
        # Make original shift node point to head
        # next shift node is next of shiftNodeCopy

        # print(head.val)
        # print(head.next.val)
        if head.next == None:
            print("log")
            return

        shiftNodeOriginal = head.next
        print(shiftNodeOriginal.next.val)
        shiftNodeCopy = shiftNodeOriginal
        shiftNodeOriginal.next = head
        print(shiftNodeOriginal.val)
        head.next = shiftNodeCopy.next
        print(head.next.next.val)

        # print(head.val)
        # print(head.next.val)
        # self.reverseList(head.next)


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = None
obj = Solution()
obj.reverseList(a1)
