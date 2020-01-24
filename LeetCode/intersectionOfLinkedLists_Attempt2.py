# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
    
        p1 = headA
        p2 = headB
        
        if p1 == None or p2 == None:
            return None

        if p1 == p2:
            return p1
        
        if p1.next == p2:
            return p2
        if p2.next == p1:
            return p1

        listA_Size = getSize(headA)
        listB_Size = getSize(headB)

        # print(listA_Size)
        # print(listB_Size)

        if listA_Size > listB_Size:
            diff = listA_Size - listB_Size
            numTimesStepped = 0
            print("Diff: ", diff)
            while numTimesStepped != diff:
                print("p1: ", p1.val, "p2: ", p2.val)
                if p1 != p2:
                    p1 = p1.next
                    numTimesStepped += 1
                elif p1 == p2:
                    return p1
        elif listB_Size > listA_Size:
            diff = listB_Size - listA_Size
            numTimesStepped = 0
            while numTimesStepped != diff:
                if p2 != p1:
                    p2 = p2.next
                    numTimesStepped += 1
                elif p2 == p1:
                    return p1

        while p2 != None and p1 != None:
            print("inside")
            print("p1: ", p1.val, "p2: ", p2.val)
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next

        return None


def getSize(head):
    count = 0
    ptr = head
    while(ptr is not None):
        count += 1
        ptr = ptr.next
    return count


def test1():
    # 3 -> 4 -> 5 -> 6 -> 7
    a0 = ListNode(3)
    a1 = ListNode(4)
    a2 = ListNode(5)
    a3 = ListNode(6)
    a4 = ListNode(7)
    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = None

    # 1 -> 5
    b1 = ListNode(1)
    b2 = a2
    b1.next = b2

    slnObj = Solution()
    ans = slnObj.getIntersectionNode(a0, b1)
    print(ans.val)


def test2():
    # 5 -> 6 -> 7
    a0 = ListNode(5)
    a1 = ListNode(6)
    a2 = ListNode(7)
    a0.next = a1
    a1.next = a2
    a2.next = None

    # 1 -> 5
    b1 = ListNode(1)
    b2 = a0
    b1.next = b2

    slnObj = Solution()
    ans = slnObj.getIntersectionNode(a0, b1)
    print(ans.val)


def test3():
    # 5 -> 6 -> 7
    a0 = ListNode(5)
    a1 = ListNode(6)
    a2 = ListNode(7)
    a0.next = a1
    a1.next = a2
    a2.next = None

    # 1 -> 5
    b1 = ListNode(1)
    b2 = a0
    b1.next = b2

    slnObj = Solution()
    ans = slnObj.getIntersectionNode(a0, b1)
    print(ans.val)


test1()
test2()
