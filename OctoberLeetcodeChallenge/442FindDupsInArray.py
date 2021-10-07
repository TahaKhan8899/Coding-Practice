from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # Kind of a trick question....
        # use the values of nums[i]-1 as an inidex number
        # since all values are from 1 to n

        res = []

        for i in range(0, len(nums)):

            numInd = abs(nums[i]) - 1

            if nums[numInd] < 0:
                res.append(abs(nums[i]))
            else:
                nums[numInd] *= -1

        return res


ans = Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])
print(ans)
