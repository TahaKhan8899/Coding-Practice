class Solution:
    def findDuplicates(self, nums):

        numDict = {}
        dupList = []

        for num in nums:
            if num in numDict:
                dupList.append(num)
            else:
                numDict[num] = 1
        print(dupList)
        print(nums)

        return nums


obj = Solution()
print(obj.findDuplicates([1, 5, 2, 3, 4, 2]))
