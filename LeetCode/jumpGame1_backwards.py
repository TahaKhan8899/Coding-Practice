class Solution:
    def canJump(self, nums):

        pos = len(nums)-1
        print(nums, "starting at pos: ", pos)

        for prevIndex in range(len(nums)-1, -1, -1):
            if prevIndex + nums[prevIndex] >= pos:
                pos = prevIndex
                print("new pos: ", pos)

        if pos == 0:
            return True

        return False


obj = Solution()
nums1 = [0, 12, 1, 0, 4]
nums2 = [2, 0]
nums3 = [2, 3, 1, 1, 4]
nums4 = [4]
nums5 = [3, 2, 1, 0, 4]
ans = obj.canJump(nums5)
print("Final: ", ans)
