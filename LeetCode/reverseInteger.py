class Solution:
    def reverse(self, x: int) -> int:

        if x == 0 or x > (2 ** 31) or x < (-2 ** 31):
            return 0

        temp = x
        stringFlippedInt = ""
        isNeg = x < 0

        while (temp % 10 == 0):
            temp = temp // 10

        if (isNeg):
            temp *= -1

        while(temp > 0):
            digit = temp % 10
            stringFlippedInt += str(digit)
            temp = temp // 10

        if (isNeg):
            stringFlippedInt = '-' + stringFlippedInt

        ans = int(stringFlippedInt)

        if ans > (2**31) or ans < (-2**31):
            return 0

        return int(stringFlippedInt)


obj = Solution()
print(obj.reverse(1534236469))
