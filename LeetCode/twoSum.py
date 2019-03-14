class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtn = [0, 0]
        found = False

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    Found = True
                    rtn[0] = i
                    rtn[1] = j
                    break
            if found:
                break

        return rtn

obj = Solution()
print(obj.twoSum([2,3,4], 6))
