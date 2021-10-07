# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# from _typeshed import FileDescriptor


def isBadVersion(version):
    return 1


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n

        while l < r:
            mid = (l - r) // 2 + l

            if (isBadVersion(mid)):
                r = mid
            else:
                l = mid + 1

        return l


obj = Solution()
ans = obj.firstBadVersion(10)
print(ans)
