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
            print("Last index was: ", location, "with value: ", nums[location])
            return True
        else:
            didJump = False
            if nums[jumpedIndex] > 0:
                # result = jumpNext(nums, jumpedIndex)
                didJump = True
                stk.append(location)
                nums[location] -= 1
                location = jumpedIndex
                numJumps = nums[jumpedIndex]
                print("item: ", nums[location], "location: ", location)
            if not didJump:
                numJumps -= 1
                nums[location] -= 1

            # if numJumps == 0, go back on the stack and try again
            if stk and numJumps == 0:
                print("out of jumps... ")
                print("STACK: ", stk)
                location = stk[len(stk)-1]
                stk.pop()
                numJumps = nums[location]
                print("NUMS: ", nums, "NEW LOCATION: ", location)

    return False


obj = Solution()
nums1 = [0, 12, 1, 0, 4]
nums2 = [2, 3]
nums3 = [2, 3, 1, 1, 4]
nums4 = [4]
nums5 = [3, 2, 1, 0, 4]
ans = obj.canJump(nums5)
print("Final: ", ans)
