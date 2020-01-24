class Solution:
    def findNumbers(self, nums):

        newNums = []
        for num in nums:

            tmpNum = str(num)
            tmpNumArray = [digit for digit in tmpNum]

            if len(tmpNumArray) % 2 == 0:
                newNums.append(int(tmpNum))

        return len(newNums)


obj = Solution()
nums = [555, 901, 482, 1771]
ans = obj.findNumbers(nums)
print("Final: ", ans)
