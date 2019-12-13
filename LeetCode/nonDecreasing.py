import random
class Solution:
    def checkPossibility(self, nums):
        
        beenChanged = False
        isNonDecreasing = True
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                if not beenChanged:
                    changeResult = tryChangeNumber(nums, i)
                    if not changeResult[1]:
                        isNonDecreasing = False
                        break
                    else:
                        beenChanged = True
                        nums = changeResult[0]
                else:
                    isNonDecreasing = False
                    break

        return isNonDecreasing

def tryChangeNumber(nums, index):

    lower = nums[index-1]
    upper = nums[index+1]

    if upper - lower > 1:
        changeNum = random.randint(lower+1, upper-1)
        print("Upper: ", upper, "Lower: ", lower, "ChangeNum = ", changeNum)
        nums[index] = changeNum
    else:
        return (nums, False)

    return (nums, True)


obj = Solution()
nums1 = [1,7,2,10,8]
nums2 = [4,3,2]
ans = obj.checkPossibility(nums2)
print("Answer: ", ans)