def digitSquareSum(n):
    sum = 0
    nums = str(n)
    for char in nums:
        sum += int(char)*int(char)

    return sum


def isHappy(n):
    slow = n
    fast = n

    slow = digitSquareSum(slow)
    print("slowSum: ", slow)
    fast = digitSquareSum(fast)
    print("fastSum: ", fast)
    fast = digitSquareSum(fast)
    print("fastSum: ", fast)
    while(slow != fast):
        slow = digitSquareSum(slow)
        print("inside slowSum: ", slow)
        fast = digitSquareSum(fast)
        print("fastSum: ", fast)
        fast = digitSquareSum(fast)
        print("fastSum: ", fast)

    if (slow == 1):
        return 1
    else:
        return 0


print(isHappy(20))
# print(digitSquareSum(19))
