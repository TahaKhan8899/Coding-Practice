# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1 , l2 ):
        printLL("Original 1: ", l1)
        printLL("Original 2: ", l2)
        
        ll1 = reverseLL(l1)
        ll2 = reverseLL(l2)

        printLL("Reversed 1: ", ll1)
        printLL("Reversed 2: ", ll2)

        # turn these linked lists into ints and add them

        return True

def reverseLL(head):
    next = ListNode(None)
    prev = ListNode(None)
    current = head

    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    
    return head

def printLL(msg, head):
    curr = head
    string = [msg]
    while(curr):
        string.append(curr.val)
        curr = curr.next
    print(string)

a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
sln = Solution()
sln.addTwoNumbers(a, b)