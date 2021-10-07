class Solution:
    def numberOfSubarrays(self, nums, k):
        nice = 0
        for i in range(0, len(nums)):
            for j in range(i + k - 1, len(nums)):
                sub = nums[i:j + 1]
                print(sub)
                oddNums = len(list(filter(lambda x: (x % 2 != 0), sub)))
                if oddNums > k:
                    break
                if oddNums == k:
                    nice += 1
                print(nice)

        return nice


test = Solution().numberOfSubarrays([1, 1, 2, 1, 1, 1, 3], 3)
print(test)
