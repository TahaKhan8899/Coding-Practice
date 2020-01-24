class Solution:
    def canJump(self, nums):

        if len(nums) == 1:
            return True

        canJump = jumpNext(nums, 0)

        return canJump


def jumpNext(nums, location):
    print("item: ", nums[location], "location: ", location)

    stk = []
    numJumps = nums[location]

    while numJumps > 0:
        jumpedIndex = location + numJumps
        if jumpedIndex > len(nums)-1:
            numJumps -= 1
        elif jumpedIndex == len(nums)-1:
            print("Went from ", nums[location], " to ", numJumps)
            return True
        else:
            if nums[jumpedIndex] > 0:
                result = jumpNext(nums, jumpedIndex)
                if result:
                    return True
            numJumps -= 1

    return False


obj = Solution()
nums = [0, 12, 1, 0, 4]
nums2 = [2, 3]
nums3 = [2, 3, 1, 1, 4]
nums4 = [4]
nums5 = [3, 2, 1, 0, 4]
ans = obj.canJump(nums5)
print("Final: ", ans)
