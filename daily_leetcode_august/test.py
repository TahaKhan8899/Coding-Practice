def myFunction(nums):
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
    return sum


nums = [2, 2, 2, 2, 2]
answer = myFunction(nums)
print(answer)
