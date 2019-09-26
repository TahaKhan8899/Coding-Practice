class Solution:
    def removeDuplicates(self, nums):

        dict = {}
        for i in range(0, len(nums)):
            if nums[i] in dict:
                nums = nums[0:i] + nums[i+1:]
                print(nums)
                i = i-1
            else:
                dict[nums[i]] = 1
                print(nums[i])

        # nums = nums[0:1] + nums[2:]
        # print(nums)


obj = Solution()
nums = [1, 2, 2, 1, 3, 4]
obj.removeDuplicates(nums)
