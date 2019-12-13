class Solution(object):
    def twoSum(self, nums, target):

        for i in range(0, len(nums)):
            complement = target - nums[i]
            print("Checking if:", complement, " in ", nums[i+1:])
            if complement in nums[i+1:]:
                nums[i] = None
                print(nums)
                return [i, nums.index(complement)]

        return []

        # BRUTE FORCE:

        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             Found = True
        #             rtn[0] = i
        #             rtn[1] = j
        #             break
        #     if found:
        #         break

        # return rtn


obj = Solution()
print(obj.twoSum([3, 2, 4], 6))
