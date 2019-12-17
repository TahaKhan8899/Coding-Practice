class Solution:
    def majorityElement(self, nums):
        
        print(nums)
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
        print("Dict: ", countDict)
        
        majorityMin = int(len(nums)/2)
        print("majorityMin: ", majorityMin)

        majorityElems = [num for num in countDict if countDict[num] > majorityMin]



        print("Majority: ", majorityElems)
        

sln = Solution()
nums = [3,3,2,2,2]
sln.majorityElement(nums)