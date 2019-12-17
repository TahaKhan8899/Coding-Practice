class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        endIndex = (m+n)-1
        n1End = m-1
        n2End = n-1
        print("nums1: ", nums1)
        print("nums2: ", nums2)

        while (n1End >= 0 and n2End >= 0):
            print("Progress: ", nums1, "n1End: ", nums1[n1End], " n2End: ", nums1[n2End], " endIndex: ", endIndex)

            if(nums1[n1End] >= nums2[n2End]):
                nums1[endIndex] = nums1[n1End]
                n1End -= 1
                endIndex -= 1
            else:
                nums1[endIndex] = nums2[n2End]
                n2End -= 1
                endIndex -= 1
        
        print(n1End)
        print(n2End)
        print(endIndex)

        while n2End > 0:
            nums1[endIndex] = nums2[n2End]
            endIndex -= 1
            n2End -= 1

        while endIndex >= 0 and n2End >= 0:
            nums1[endIndex] = nums2[n2End]
            n2End -= 1

        print("final: ", nums1)
        
        

obj = Solution()
# nums1 = [5,10,15,0,0,0,0]
# m = 3
# nums2 = [1,9,12,17]
# n = 4
nums1 = [4,8,12,0]
m = 3
nums2 = [5]
n = 1

obj.merge(nums1, m, nums2, n)