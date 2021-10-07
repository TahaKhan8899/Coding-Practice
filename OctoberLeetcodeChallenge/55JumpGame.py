from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        # start at last index
        pos = len(nums) - 1

        for j in range(pos, -1, -1):
            # can I reach j from any index before it?
            for i in range(j - 1, -1, -1):
                dist = j - i
                if nums[i] >= dist:
                    if i == 0:
                        return True
                    break
                if (i == 0):
                    return False

        return True


ans = Solution().canJump([0, 0, 0, 0, 0])
print(ans)
