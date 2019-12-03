import MaxHeap
class Solution:
    def lastStoneWeight(self, stones):
        
        print("Before Heapify", stones)
        stoneHeap = MaxHeap.MaxHeap(stones)
        print("After Heapify", stoneHeap.printHeap())

        # while I have more than 2 stones
        while (len(stoneHeap.heap) > 2):
            print("Inside Loop", stoneHeap.printHeap())            
            
            # take the max elements
            s1 = stoneHeap.pop()
            s2 = stoneHeap.pop()

            # smash them together
            if s1 > s2:
                diff = s1 - s2
            elif s2 > s1:
                diff = s2 - s1
            else:
                continue

            stoneHeap.push(diff)
        
        # if there are no stones left, return 0
        if len(stoneHeap.heap) == 1:
            return 0
        # otherwise return the remaining stone
        else:
            return(stoneHeap.heap[1])


# finalWeight = Solution().lastStoneWeight([2,7,4,1,8,1])
finalWeight = Solution().lastStoneWeight([1000, 1000])
print("Final Weight = ", finalWeight)