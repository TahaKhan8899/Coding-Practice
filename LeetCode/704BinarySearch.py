from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        start = 0
        mid = len(nums) // 2
        end = len(nums) - 1

        if (nums[mid] == target):
            return mid

        if end == mid:
            if nums[mid-1] == target:
                return mid-1
            else:
                return -1

        while (target != nums[mid] and start < mid and mid < end):
            print("Indices: ", start, mid, end)
            print("values: ", nums[start], nums[mid], nums[end])
            if target > nums[mid]:
                start = mid
                mid = ((end - start) // 2) + start
                if start == mid:
                    if nums[mid+1] == target:
                        return mid+1
                    else:
                        return -1
            else:
                end = mid
                mid = (end - start) // 2 + start
                print("Indices: ", start, mid, end)
                print("values: ", nums[start], nums[mid], nums[end])

        if (target == nums[mid]):
            return mid
        else:
            return -1
