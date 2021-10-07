class Solution:
    def maxProduct(self, nums):
        maxProduct = nums[0]
        for i in range(0, len(nums)):
            subArr = [nums[i]]
            print("sub arr: ", subArr)
            currentProd = listProd(subArr)
            if currentProd > maxProduct:
                maxProduct = currentProd
            for j in range(i+1, len(nums)):
                subArr.append(nums[j])
                print("sub arr: ", subArr)
                print("Max: ", maxProduct)
                print("j: ", nums[j])
                currentProd = listProd(subArr)
                if currentProd > maxProduct:
                    maxProduct = currentProd

        return maxProduct


def listProd(lst):
    prod = 1
    for x in lst:
        prod *= x
    return prod


ans = Solution().maxProduct([-2, 3, -4])
print("Final:", ans)
