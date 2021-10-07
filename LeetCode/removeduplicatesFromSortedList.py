def removeDuplicates(nums):
    uniqueIndex = 0

    if len(nums) == 0 or len(nums) == 1:
        return nums

    for i in range(1, len(nums)):
        print("list: ", nums)
        print("unique index: ", uniqueIndex)
        if nums[i] == nums[uniqueIndex]:
            continue
        else:
            temp = nums[uniqueIndex + 1]
            nums[uniqueIndex + 1] = nums[i]
            nums[i] = temp
            uniqueIndex += 1

    print("list: ", nums)
    print("unique index: ", uniqueIndex)
    return nums[0:uniqueIndex+1]


# test1 = removeDups([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5])
# print(test1)
test2 = removeDups([1, 2, 3, 3])
print(test2)
