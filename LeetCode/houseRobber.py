
def rob(nums):

    sum1 = 0
    sum2 = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            sum1 += nums[i]
        else:
            sum2 += nums[i]

    print(sum1)
    print(sum2)

    if sum1 > sum2:
        return sum1
    else:
        return sum2


nums = [2, 7, 9, 3, 1]
ans = rob(nums)
print("answer: ", ans)
