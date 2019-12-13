
# THIS IS STUPID.


class Solution:
    def missingNumber(self, nums):

        # nums.sort()
        # print(nums)

        # if len(nums) == 1 and nums[0] == 0:
        #     return 1

        # if len(nums) == 1 and nums[0] == 1:
        #     return 0

        # if len(nums) == 1:
        #     return nums[0]+1

        # for i in range(0, len(nums)-1):
        #     if nums[i+1]-nums[i] != 1:
        #         return nums[i]+1

        # return None
        s = sum(nums)
        print("1", s)
        real_sum = (0+len(nums))*(len(nums)+1)/2
        print("2", real_sum)
        print("3", s - real_sum)
        return s - real_sum


obj = Solution()
arr = [0]
ans = obj.missingNumber(arr)
print(ans)
