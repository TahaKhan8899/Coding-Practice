# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):

        l3 = ListNode(0)
        head = l3

        while (l1 and l2):
            print("Comparing: ", l1.val, l2.val)

            if (l2.val >= l1.val):
                print("1: ", l2.val, ">=", l1.val)
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            elif (l1.val > l2.val):
                print("1: ", l1.val, ">=", l2.val)
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
            
            print("l3 so far:")
            lll = head
            while (lll.next):
                print(lll.val)
                lll = lll.next
        
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2

        return head.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

obj = Solution()
ans = obj.mergeTwoLists(l1, l2)
tmp = ans
print("final answer")
while(tmp.next):
    print(tmp.val)
    tmp = tmp.next
print(tmp.val)



        


        