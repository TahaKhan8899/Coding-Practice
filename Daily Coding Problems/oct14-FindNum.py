class Solution(object):
    def findSingle(self, nums):
        # Fill this in.
        a = sorted(nums)
        print(a)

        single = None

        for i in range(0, len(a)):
            if i % 2 == 0:
                if i == len(a)-1:
                    single = a[i]
                    break
                if a[i] != a[i+1]:
                    single = a[i]
                    break

        return single


nums = [1, 1]
print(Solution().findSingle(nums))
# 3
