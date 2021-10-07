# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        # if head.next = None:
        #     return head
        # currentNode = head
        # while head.next != None:
        #     currentNodeCopy = currentNode
        #     currentNode.next =
        p = None
        c = head
        n = head.next

        while n != None:
            c.next = p
            p = c
            c = n
            n = n.next

        c.next = p

        return c


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = None
ans = Solution().reverseList(a1)
c = ans
while c != None:
    print(c.val)
    c = c.next
