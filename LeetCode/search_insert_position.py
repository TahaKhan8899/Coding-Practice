class Solution:
    def containsDuplicate(self, nums):
        sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        return False
