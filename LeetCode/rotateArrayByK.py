class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        save the first len(nums)-k elements into tmp
        replace the beginning of nums with the last k elements
        """
        tmp = nums[:len(nums)-k]
        nums[:k] = nums[len(nums)-k:]
        nums[k:] = tmp

obj = Solution()
nums = [1,2,3,4,5,6]
obj.rotate(nums, 2)
print(nums)
