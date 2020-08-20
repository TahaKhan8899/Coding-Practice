import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        # exponent = math.log(num) / math.log(4)
        # print(exponent)
        # return exponent.is_integer()

        while num % 4 == 0:
            num = num / 4
        if num == 1:
            return True
        return False


obj = Solution()
print(obj.isPowerOfFour(1024))
